import logging
import os
import requests
from langchain.tools import tool
from langchain_ollama import OllamaEmbeddings

from langchain_community.vectorstores.faiss import FAISS
from langchain_text_splitters import CharacterTextSplitter
from sec_api import QueryApi
from unstructured.partition.html import partition_html

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SECTools():

  @tool("Search 10-Q form")
  def search_10q(data):
    logging.info("Searching 10-Q form for data: %s", data)
    stock, ask = data.split("|")
    queryApi = QueryApi(api_key=os.environ['SEC_API_API_KEY'])
    query = {
      "query": {
        "query_string": {
          "query": f"ticker:{stock} AND formType:\"10-Q\""
        }
      },
      "from": "0",
      "size": "1",
      "sort": [{"filedAt": {"order": "desc"}}]
    }

    fillings = queryApi.get_filings(query)['filings']
    if len(fillings) == 0:
      logging.error("No filings found for stock: %s", stock)
      return "Sorry, I couldn't find any filling for this stock, check if the ticker is correct."
    link = fillings[0]['linkToFilingDetails']
    answer = SECTools.__embedding_search(link, ask)
    return answer

  @tool("Search 10-K form")
  def search_10k(data):
    logging.info("Searching 10-K form for data: %s", data)
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

    fillings = queryApi.get_filings(query)['filings']
    if len(fillings) == 0:
      logging.error("No filings found for stock: %s", stock)
      return "Sorry, I couldn't find any filling for this stock, check if the ticker is correct."
    link = fillings[0]['linkToFilingDetails']
    answer = SECTools.__embedding_search(link, ask)
    return answer

  def __embedding_search(url, ask):
    logging.info("Performing embedding search for URL: %s with question: %s", url, ask)
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
      docs, OllamaEmbeddings()
    ).as_retriever()
    answers = retriever.get_relevant_documents(ask, top_k=4)
    answers = "\n\n".join([a.page_content for a in answers])
    return answers

  def __download_form_html(url):
    logging.info("Downloading form HTML from URL: %s", url)
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
    if response.status_code != 200:
      logging.error("Failed to download form HTML from URL: %s with status code: %d", url, response.status_code)
    return response.text