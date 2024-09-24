import logging

from dotenv import load_dotenv

load_dotenv()

from agents import ChatbotAgents
from crewai import Crew
from tasks import ChatbotTasks


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='app_logs.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


# Initialize tasks and agents
tasks = ChatbotTasks()
agents = ChatbotAgents()


if __name__ == "__main__":
    logging.info("Starting the application building Crew Application")

    print("## Welcome to the Chatbot Crew")
    print('-------------------------------')
    # this part should be input from the application
    chatbot_description = input(
        "Describe the chatbot you would like to build. What will be its main functionalities?"
    )

    logging.info('Chatbot description received: {}', chatbot_description)

    # Create Agents and save them
    chatbot_developer_agent = agents.chatbot_developer_agent()
    qa_engineer_agent = agents.qa_engineer_agent()
    product_manager_agent = agents.product_manager_agent()

    # Create Tasks and save them
    implement_chatbot = tasks.implement_task(chatbot_developer_agent, chatbot_description)
    test_chatbot = tasks.test_task(qa_engineer_agent, chatbot_description)
    review_chatbot = tasks.review_task(product_manager_agent, chatbot_description)
    tasks.save_task(product_manager_agent, chatbot_description, '/Users/Sour/agent-code-folder')

    # Create Crew responsible for Chatbot
    crew = Crew(
        agents=[chatbot_developer_agent, qa_engineer_agent, product_manager_agent],
        tasks=[implement_chatbot, test_chatbot, review_chatbot],
        verbose=True,
    )

    logging.info("Kicking off the Crew")
    chatbot = crew.kickoff()
    logging.info("Crew kickoff completed")

    # Save final task results

    # Print results
    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print("Final code for the chatbot:")
    print(chatbot)

