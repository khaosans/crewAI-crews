import streamlit as st
from agents import ChatbotAgents

st.title("Chatbot System")

agents = ChatbotAgents()

agent_options = {
    "Chatbot Developer": agents.chatbot_developer_agent,
    "QA Engineer": agents.qa_engineer_agent,
    "Product Manager": agents.product_manager_agent,
    "Data Engineer": agents.data_engineer_agent,
    "Deployment Engineer": agents.deployment_engineer_agent,
    "Integration Tester": agents.integration_tester_agent,
    "Database Engineer": agents.database_engineer_agent
}

agent_choice = st.selectbox("Choose an agent", list(agent_options.keys()))

if st.button("Create Agent"):
    agent = agent_options[agent_choice]()
    st.write(f"Created {agent.role} Agent")
    st.write(f"Goal: {agent.goal}")
    st.write(f"Backstory: {agent.backstory}")