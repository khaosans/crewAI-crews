from textwrap import dedent
from crewai import Task

class GameTasks:
    def code_task(self, agent, app):
        return Task(
            description=dedent(f"""\
                You will create an application using Python, these are the instructions:

                Instructions
                ------------
                {app}

                Your final answer must be the full Python code, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Complete and functional Python code for the application as per the instructions provided."
        )

    def review_task(self, agent, application):
        return Task(
            description=dedent(f"""\
                You are helping create an application using Python, these are the instructions:

                Instructions
                ------------
                {application}

                Using the code you received, check for errors. Check for logic errors,
                syntax errors, missing imports, variable declarations, mismatched brackets,
                and security vulnerabilities.

                Your final answer must be the corrected Python code, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Corrected and error-free Python code that adheres to the provided application instructions."
        )

    def evaluate_task(self, agent, application):
        return Task(
            description=dedent(f"""\
                You are helping create an application using Python, these are the instructions:

                Instructions
                ------------
                {application}

                You will review the code to ensure that it is complete and
                performs the intended functions as described.

                Your final answer must be the verified Python code, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Verified and fully functional Python code that fulfills the application's intended purpose."
        )
