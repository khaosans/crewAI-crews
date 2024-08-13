import os
import requests
from langchain.tools import tool
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from pydantic import ConfigDict
from sec_api import QueryApi
from unstructured.partition.html import partition_html

class SECTools:
    user_agent = os.getenv('USER_AGENT', 'YourAppName/1.0 (contact@example.com)')
    model_config = ConfigDict(
        populate_by_name=True  # Use the new key name
    )
    headers = {
        'User-Agent': os.getenv('USER_AGENT', 'YourAppName/1.0 (contact@example.com)'),
    }

    @tool("Search 10-Q form")
    def search_10q(ticker, query):
        """
        Search for the 10-Q form for a given stock ticker.

        Args:
            ticker (str): The stock ticker.
            query (str): The query to search within the 10-Q form.

        Returns:
            dict: The JSON data from the SEC.
        """
        url = f'https://data.sec.gov/submissions/CIK{ticker}.json'

        # Make the request with the User-Agent header
        response = requests.get(url, headers=SECTools.headers)

        if response.status_code == 200:
            data = response.json()
            # Process your data as needed
            return data
        else:
            raise Exception(f"Error fetching data from SEC: {response.status_code}")

    @tool("Search 10-K form")
    def search_10k(data):
        """
        Search for the latest 10-K form for a given stock.

        Args:
            data (str): A pipe (|) separated text of length two, representing the stock ticker and the question.

        Returns:
            dict: The JSON data from the SEC.
        """
        stock, ask = data.split("|")
        queryApi = QueryApi(api_key=os.environ['SEC_API_API_KEY'])
        query = {
            "query": {
                "query_string": {
                    "query": f"ticker:{stock} AND formType:\"10-K\""
                }
            },
            "from": "0",
            "size": "1",
            "sort": [{"filedAt": {"order": "desc"}}]
        }

        # Make the request with the User-Agent header
        response = requests.get(queryApi.get_filings(query), headers=SECTools.headers)

        if response.status_code == 200:
            data = response.json()
            # Process your data as needed
            return data
        else:
            raise Exception(f"Error fetching data from SEC: {response.status_code}")

    @staticmethod
    def __embedding_search(url, ask):
        text = SECTools.__download_form_html(url)
        elements = partition_html(text=text)
        content = "\n".join([str(el) for el in elements])
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=150,
            length_function=len,
            is_separator_regex=False,
        )
        docs = text_splitter.create_documents([content])
        retriever = FAISS.from_documents(
            docs, OpenAIEmbeddings()
        ).as_retriever()
        answers = retriever.get_relevant_documents(ask, top_k=4)
        answers = "\n\n".join([a.page_content for a in answers])
        return answers

    @staticmethod
    def __download_form_html(url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
            'Cache-Control': 'max-age=0',
            'Dnt': '1',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        return response.text