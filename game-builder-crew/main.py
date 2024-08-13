import logging
from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from tasks import GameTasks
from agents import GameAgents
from persistence import Persistence

# Configure logging
logging.basicConfig(level=logging.INFO, filename='app_logs.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Initialize Persistence
persistence = Persistence()

# Initialize tasks and agents
tasks = GameTasks()
agents = GameAgents()

logging.info("Starting the application building Crew Application")

print("## Welcome to the Game Crew")
print('-------------------------------')
game_description = input("What is the game you would like to build? What will be the mechanics?\n")
logging.info(f"Game description received: {game_description}")

# Save game description
game_id = persistence.save_game(game_description)
logging.info(f"Game saved with ID: {game_id}")

# Create Agents and save them
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

senior_engineer_agent_id = persistence.save_agent(
    senior_engineer_agent.role, senior_engineer_agent.backstory,
    senior_engineer_agent.allow_delegation, senior_engineer_agent.verbose
)
logging.info(f"Senior Engineer Agent saved with ID: {senior_engineer_agent_id}")

qa_engineer_agent_id = persistence.save_agent(
    qa_engineer_agent.role, qa_engineer_agent.backstory,
    qa_engineer_agent.allow_delegation, qa_engineer_agent.verbose
)
logging.info(f"QA Engineer Agent saved with ID: {qa_engineer_agent_id}")

chief_qa_engineer_agent_id = persistence.save_agent(
    chief_qa_engineer_agent.role, chief_qa_engineer_agent.backstory,
    chief_qa_engineer_agent.allow_delegation, chief_qa_engineer_agent.verbose
)
logging.info(f"Chief QA Engineer Agent saved with ID: {chief_qa_engineer_agent_id}")

# Create Tasks and save them
code_game = tasks.code_task(senior_engineer_agent, game_description)
review_game = tasks.review_task(qa_engineer_agent, game_description)
approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game_description)

code_game_id = persistence.save_task(game_id, senior_engineer_agent_id, code_game.description, code_game.expected_output)
logging.info(f"Code Task created and saved with ID: {code_game_id}")

review_game_id = persistence.save_task(game_id, qa_engineer_agent_id, review_game.description, review_game.expected_output)
logging.info(f"Review Task created and saved with ID: {review_game_id}")

approve_game_id = persistence.save_task(game_id, chief_qa_engineer_agent_id, approve_game.description, approve_game.expected_output)
logging.info(f"Approval Task created and saved with ID: {approve_game_id}")

# Create Crew responsible for Copy
crew = Crew(
    agents=[
        senior_engineer_agent,
        qa_engineer_agent,
        chief_qa_engineer_agent
    ],
    tasks=[
        code_game,
        review_game,
        approve_game
    ],
    verbose=True
)

logging.info("Kicking off the Crew")
game = crew.kickoff()
logging.info("Crew kickoff completed")

# Save final task results
persistence.save_task_result(code_game_id, game)
logging.info(f"Final game result saved for Code Task ID: {code_game_id}")

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code for the game:")
print(game)

# Close persistence connection
persistence.close()
logging.info("Persistence connection closed. Application finished.")
