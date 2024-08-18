from textwrap import dedent
from crewai import Task


class DevTasks():
    def code_back_end_task(self, agent, application):
        return Task(description=dedent(f"""\
            You will create an application using Python. These are the instructions:

            There might be HTML code for the front end you will also need to modify if needed.  Always pass front end along.
            Instructions
            ------------
            {application}

            Your final answer must be the full Python code, only the Python code and some HTML and nothing else.
            """),
                    agent=agent
                    )

    def code_front_end_task(self, agent, application):
        return Task(description=dedent(f"""\
				You will create an application using Python. These are the instructions:
				
				Always make sure to pass along the back end code with the front end code.  
	
				Instructions
				------------
				{application}
	
            Your final answer must be the full Python code, only the Python code and some HTML and nothing else.
				"""),
                    agent=agent
                    )

    def review_task(self, agent, application):
        return Task(description=dedent(f"""\
            You are helping create an application using Python. These are the instructions:

            Instructions
            ------------
            {application}

            Using the code you got, check for errors. Check for logic errors,
            syntax errors, missing imports, variable declarations, mismatched brackets,
            and security vulnerabilities.
            HTML is okay for front-end code.


            Your final answer must be the full Python code, only the Python code and some HTML and nothing else.
            """),
                    agent=agent
                    )

    def evaluate_task(self, agent, application,callback_function):
        return Task(description=dedent(f"""\
            You are helping create an application using Python. These are the instructions:

            Instructions
            ------------
            {application}

            You will look over the code to ensure that it is complete and
            does the job that it is supposed to do.
            HTML is okay for front-end code.

            Your final answer must be the full Python code, only the Python code and some HTML and nothing else.
            """),
                    agent=agent,
                    callback=callback_function
                    )

    def unit_test_task(self, agent, application):
        return Task(description=dedent(f"""\
            You will write unit tests for the application to ensure its correctness and stability. These are the instructions:

            Instructions
            ------------
            {application}

            Write tests to cover:
            - Functionality of all individual components
            - Edge cases and error handling
            - Performance and efficiency where applicable

            Your final answer must be the full Python test code, only the test code and nothing else.
            """),
                    agent=agent

                    )
