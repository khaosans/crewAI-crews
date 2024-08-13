import logging
from persistence import Persistence

# Configure logging for testing purposes
logging.basicConfig(level=logging.INFO, filename='test_db.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_db_writing():
    # Initialize the persistence layer
    persistence = Persistence()

    # Mock data for testing
    game_description = "Test Game: A simple test to check DB write functionality."
    agent_data = {
        "role": "Test Agent",
        "backstory": "This is a mock agent used for testing the database persistence.",
        "allow_delegation": False,
        "verbose": True
    }
    task_description = "Test Task: A task to test writing to the database."
    expected_output = "This is the expected output for the test task."

    # Save game description to the database
    game_id = persistence.save_game(game_description)
    logging.info(f"Game description saved with ID: {game_id}")

    # Save agent to the database
    agent_id = persistence.save_agent(
        agent_data["role"],
        agent_data["backstory"],
        agent_data["allow_delegation"],
        agent_data["verbose"]
    )
    logging.info(f"Agent saved with ID: {agent_id}")

    # Save task to the database
    task_id = persistence.save_task(game_id, agent_id, task_description, expected_output)
    logging.info(f"Task saved with ID: {task_id}")

    # Mock result data (replace with actual CrewOutput object if available)
    result = {
        "result": "Test result data - this simulates the CrewOutput.",
        "details": "This includes any details relevant to the task outcome."
    }

    # Save task result to the database
    persistence.save_task_result(task_id, result)
    logging.info(f"Task result saved for Task ID: {task_id}")

    # Close the persistence connection
    persistence.close()
    logging.info("Test completed and database connection closed.")

if __name__ == '__main__':
    test_db_writing()
    print("Test completed. Check the 'test_db.log' file for details.")
