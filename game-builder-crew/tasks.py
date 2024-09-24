from textwrap import dedent
from crewai import Task
import requests

class ChatbotTasks:
    def implement_task(self, agent, description):
        return Task(
            description=dedent(f"""\
                You will create a chatbot, these are the instructions:

                Instructions
                ------------
                {description}

                Your final answer must be the full Python code for the chatbot, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Complete and functional Python code for the chatbot as per the instructions provided."
        )

    def test_task(self, agent, description):
        return Task(
            description=dedent(f"""\
                You are helping create a chatbot, these are the instructions:

                Instructions
                ------------
                {description}

                Using the code you received, check for errors. Check for logic errors,
                syntax errors, missing imports, variable declarations, mismatched brackets,
                and security vulnerabilities.

                Your final answer must be the corrected Python code for the chatbot, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Corrected and error-free Python code for the chatbot that adheres to the provided instructions."
        )

    def review_task(self, agent, description):
        return Task(
            description=dedent(f"""\
                You are helping create a chatbot, these are the instructions:

                Instructions
                ------------
                {description}

                You will review the code to ensure that it is complete and
                performs the intended functions as described.

                Your final answer must be the verified Python code for the chatbot, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Verified and fully functional Python code for the chatbot that fulfills the intended purpose."
        )

    def save_task(self, agent, code, directory):
        return Task(
            description=dedent(f"""\
                You will save the following Python code to a specified directory:

                Code
                ----
                {code}

                Directory
                ---------
                {directory}

                Your final answer must be a confirmation message indicating that the code has been successfully saved to the directory.
            """),
            agent=agent,
            expected_output="Confirmation message indicating successful saving of the code to the specified directory."
        )