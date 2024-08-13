from textwrap import dedent
from crewai import Task


class GameTasks:
    def code_task(self, agent, game):
        return Task(
            description=dedent(f"""\
                You will create a game using Python, these are the instructions:

                Instructions
                ------------
                {game}

                Your final answer must be the full Python code, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Complete and functional Python code for the game as per the instructions provided."
        )

    def review_task(self, agent, game):
        return Task(
            description=dedent(f"""\
                You are helping create a game using Python, these are the instructions:

                Instructions
                ------------
                {game}

                Using the code you received, check for errors. Check for logic errors,
                syntax errors, missing imports, variable declarations, mismatched brackets,
                and security vulnerabilities.

                Your final answer must be the corrected Python code, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Corrected and error-free Python code that adheres to the provided game instructions."
        )

    def evaluate_task(self, agent, game):
        return Task(
            description=dedent(f"""\
                You are helping create a game using Python, these are the instructions:

                Instructions
                ------------
                {game}

                You will review the code to ensure that it is complete and
                performs the intended functions as described.

                Your final answer must be the verified Python code, only the Python code and nothing else.
            """),
            agent=agent,
            expected_output="Verified and fully functional Python code that fulfills the game's intended purpose."
        )
