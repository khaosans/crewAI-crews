import os
import logging
import time
from textwrap import dedent
from urllib import request

from dotenv import load_dotenv
from langchain_community.llms.ollama import Ollama
from pydantic import ConfigDict

load_dotenv()

from crewai import Crew
from stock_analysis_agents import StockAnalysisAgents
from stock_analysis_tasks import StockAnalysisTasks
from openai import APIError

logging.basicConfig(level=logging.INFO, filename='app_logs.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

defalut_llm = Ollama(model="Llama3.1")

# Check if USER_AGENT environment variable is set
user_agent = os.getenv('USER_AGENT')
if not user_agent:
    logging.warning("USER_AGENT environment variable not set, consider setting it to identify your requests.")
    user_agent = 'YourAppName/1.0 (contact@example.com)'

headers = {
    'User-Agent': user_agent,
}
class FinancialCrew:
    model_config = ConfigDict(
        populate_by_name=True  # Use the new key name
    )

    def __init__(self, company):
        self.company = company

    def run(self):
        agents = StockAnalysisAgents()
        tasks = StockAnalysisTasks()

        research_analyst_agent = agents.research_analyst()
        financial_analyst_agent = agents.financial_analyst()
        investment_advisor_agent = agents.investment_advisor()

        research_task = tasks.research(research_analyst_agent, self.company)
        financial_task = tasks.financial_analysis(financial_analyst_agent)
        filings_task = tasks.filings_analysis(financial_analyst_agent)
        recommend_task = tasks.recommend(investment_advisor_agent)

        crew = Crew(
            agents=[
                research_analyst_agent,
                financial_analyst_agent,
                investment_advisor_agent
            ],
            tasks=[
                research_task,
                financial_task,
                filings_task,
                recommend_task
            ],
            verbose=True
        )

        try:
            result = crew.kickoff()
        except APIError as e:
            logging.error(f"APIError: {e}")
            result = "An error occurred while processing your request. Please try again later."

        return result

if __name__ == "__main__":
    print("## Welcome to Financial Analysis Crew")
    print('-------------------------------')
    company = input(
        dedent("""
            What is the company you want to analyze?
        """))

    financial_crew = FinancialCrew(company)
    result = financial_crew.run()
    print("\n\n########################")
    print("## Here is the Report")
    print("########################\n")
    print(result)