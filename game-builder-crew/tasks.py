from textwrap import dedent
from crewai import Task
import requests

class ChatbotTasks:
    def implement_task(self, agent, description):
        return Task(
            description=dedent(f"""\
                You will create a chatbot using Streamlit, these are the instructions:

                Instructions
                ------------
                {description}

                Your final answer must be the full Python code for the Streamlit chatbot, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Complete and functional Python code for the Streamlit chatbot as per the instructions provided."
        )

    def test_task(self, agent, description):
        return Task(
            description=dedent(f"""\
                You are helping create a chatbot using Streamlit, these are the instructions:

                Instructions
                ------------
                {description}

                Using the code you received, check for errors. Check for logic errors,
                syntax errors, missing imports, variable declarations, mismatched brackets,
                and security vulnerabilities.

                Your final answer must be the corrected Python code for the Streamlit chatbot, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Corrected and error-free Python code for the Streamlit chatbot that adheres to the provided instructions."
        )

    def review_task(self, agent, description):
        return Task(
            description=dedent(f"""\
                You are helping create a chatbot using Streamlit, these are the instructions:

                Instructions
                ------------
                {description}

                You will review the code to ensure that it is complete and
                performs the intended functions as described.

                Your final answer must be the verified Python code for the Streamlit chatbot, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Verified and fully functional Python code for the Streamlit chatbot that fulfills the intended purpose."
        )

    def integration_test_task(self, agent, description):
        return Task(
            description=dedent(f"""\
                You will run the Streamlit app and verify its functionality, these are the instructions:

                Instructions
                ------------
                {description}

                Your final answer must be a report on the functionality of the Streamlit app, including any issues found.
            """),
            agent=agent,
            expected_output="Report on the functionality of the Streamlit app, including any issues found."
        )

    def setup_database_task(self, agent, description):
        return Task(
            description=dedent(f"""\
                You will set up and manage the database for the chatbot project, these are the instructions:

                Instructions
                ------------
                {description}

                Your final answer must be a report on the database setup and management, including any issues found.
            """),
            agent=agent,
            expected_output="Report on the database setup and management, including any issues found."
        )

    def search_github(self, query):
        url = f"https://api.github.com/search/repositories?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            repositories = [
                {"name": repo["name"], "description": repo["description"]}
                for repo in data["items"]
            ]
            return repositories
        else:
            return f"Error: {response.status_code} - {response.text}"
