from dotenv import load_dotenv

load_dotenv()

from tasks import DevTasks

from crewai import Crew

from agents import ApplicationAgents
from file_io import save_python

print("## Welcome to the Game Crew")
print('-------------------------------')
app = input("What is the game you would like to build? What will be the mechanics?\n")

# Initialize agents
agents = ApplicationAgents()

# Create the crew with the senior roles
# Create the crew with the senior roles
backend_agent = agents.senior_backend_engineer_agent()
front_end_agent = agents.senior_front_end_developer_agent()
qa_engineer_agent_ = agents.senior_qa_engineer_agent1()
qa_engineer_agent = agents.additional_senior_qa_engineer_agent1()
cheif_qa_engineer = agents.chief_senior_qa_engineer_agent()

tasks = DevTasks()

# create a task for each task in DevTasks

back_end_task = tasks.code_back_end_task(backend_agent, app)
front_end_task = tasks.code_front_end_task(front_end_agent, app)
qa_review_task = tasks.review_task(qa_engineer_agent_, app)
qa_review_task_another = tasks.review_task(qa_engineer_agent, app)
evaluate_task = tasks.evaluate_task(cheif_qa_engineer, app, save_python)

crew = Crew(
    name="Application Development Crew",
    agents=[
        backend_agent,
        front_end_agent,
        qa_engineer_agent_,
        qa_engineer_agent,
        cheif_qa_engineer,
    ],
    tasks=[
        back_end_task,
        front_end_task,
        qa_review_task,
        qa_review_task_another,
        evaluate_task,
    ],
)

game = crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code for the game:")
print(app)
