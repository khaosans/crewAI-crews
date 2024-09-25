import json
import os
import shutil
from textwrap import dedent

from crewai import Agent, Crew, Task
from langchain.agents.agent_toolkits import FileManagementToolkit
from langchain.llms import Ollama  # {{ edit_1 }} - Importing Ollama LLM
from tasks import TaskPrompts

from tools.browser_tools import BrowserTools
from tools.file_tools import FileTools
from tools.search_tools import SearchTools
from tools.template_tools import TemplateTools  # Import the new tool

from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool  # Ensure this import is present

class TaskBoardCrew():  # Updated class name
    def __init__(self, idea):
        self.agents_config = json.loads(open("config/agents.json", "r").read())
        self.idea = idea
        self.templates = TemplateTools.read_templates('./templates')  # Read all taskboard templates
        self.__create_agents()

    def run(self):
        expanded_idea = self.__expand_idea()
        components = self.__choose_template(expanded_idea)
        self.__update_components(components, expanded_idea)

    def __expand_idea(self):
        task_prompts = TaskPrompts()  # Create an instance of TaskPrompts
        create_stories = Task(
            description=task_prompts.expand().format(idea=self.idea),  # Use the instance to call expand
            agent=self.product_manager  # Updated to product manager
        )
        break_down_tasks = Task(
            description=task_prompts.create_user_stories(),  # Use the instance to call create_user_stories
            agent=self.back_end_developer  # Updated to back-end developer
        )
        crew = Crew(
            agents=[self.product_manager, self.back_end_developer],  # Updated to product manager
            tasks=[create_stories, break_down_tasks],
            verbose=True
        )
        expanded_idea = crew.kickoff()
        return expanded_idea

    def __choose_template(self, expanded_idea=None):
        task_prompts = TaskPrompts()  # Create an instance of TaskPrompts
        choose_template_task = Task(
            description=task_prompts.refine_templates().format(idea=self.idea),  # Use the instance to call choose_template
            agent=self.front_end_engineer  # Updated to front_end_engineer
        )
        update_page = Task(
            description=task_prompts.update_board().format(idea=self.idea),  # Use the instance to call update_page
            agent=self.front_end_engineer  # Updated to front_end_engineer
        )
        crew = Crew(
            agents=[self.front_end_engineer],
            tasks=[choose_template_task, update_page],
            verbose=True
        )
        components = crew.kickoff()
        return components

    def __update_components(self, components, expanded_idea):
        components = components.replace("\n", "").replace(" ", "").replace("```", "")
        components = json.loads(components)
        for component in components:
            # Use the read_file tool instead of directly opening the file
            file_content = FileTools.read_file(f"./workdir/{component.split('./')[-1]}")  # {{ edit_1 }}
            create_content = Task(
                description=TaskPrompts.component_content().format(
                    expanded_idea=expanded_idea,
                    file_content=file_content,
                    component=component
                ),
                agent=self.qa_engineer  # Updated to qa_engineer
            )
            update_component = Task(
                description=TaskPrompts.update_component().format(
                    component=component,
                    file_content=file_content
                ),
                agent=self.front_end_engineer  # Updated to front_end_engineer
            )
            qa_component = Task(
                description=TaskPrompts.qa_component().format(
                    component=component
                ),
                agent=self.qa_engineer  # Updated to qa_engineer
            )
            crew = Crew(
                agents=[self.qa_engineer, self.front_end_engineer],
                tasks=[create_content, update_component, qa_component],
                verbose=True
            )
            crew.kickoff()

    def __create_agents(self):
        product_manager_config = self.agents_config["product_manager"]  # Updated to product_manager
        back_end_developer_config = self.agents_config["back_end_developer"]  # Updated to back_end_developer
        developer_config = self.agents_config["front_end_engineer"]  # Updated to front_end_engineer
        qa_engineer_config = self.agents_config["qa_engineer"]  # Updated to qa_engineer

        toolkit = FileManagementToolkit(
            root_dir='workdir',
            selected_tools=["read_file", "list_directory"]
        )

        ollama = Ollama(model="llama3.1")  # {{ edit_1 }}
        self.product_manager = Agent(  # Updated to product_manager
            **product_manager_config,
            function_calling_llm=ollama,  # {{ edit_1 }}
            verbose=True,
            tools=[
                SearchTools.search_internet,
                TemplateTools.learn_taskboard_options,  # Updated to taskboard options
                BrowserTools.scrape_and_summarize_website
            ]
        )

        self.back_end_developer = Agent(  # Updated to back_end_developer
            **back_end_developer_config,
            llm=ollama,  # Use the same LLM
            verbose=True,
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                FileTools.write_file  # Tool to write SQL commands
            ]
        )

        self.front_end_engineer = Agent(  # Updated to front_end_engineer
            **developer_config,
            llm=ollama,  # {{ edit_3 }}
            verbose=True,
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                TemplateTools.learn_taskboard_options,  # Updated to taskboard options
                TemplateTools.copy_taskboard_template_to_project_folder,  # Updated to taskboard template
                FileTools.write_file
            ] + toolkit.get_tools()
        )

        self.qa_engineer = Agent(  # Updated to qa_engineer
            **qa_engineer_config,
            llm=ollama,  # {{ edit_4 }}
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ]
        )

    def copy_template(self, taskboard_template):  # Updated parameter name
        """Copy the specified taskboard template to the project folder."""  # Updated comment
        result = TemplateTools.copy_taskboard_template_to_project_folder(taskboard_template)  # Updated method call
        print(result)


if __name__ == "__main__":
    print("Welcome to Idea Generator")
    print(dedent("""
    ! YOU MUST FORK THIS BEFORE USING IT !
    """))

    print(dedent("""
        Disclaimer: This will use gpt-4 unless you changed it 
        not to, and by doing so it will cost you money (~2-9 USD).
        The full run might take around ~10-45m. Enjoy your time back.\n\n
    """))
    idea = "taskboard like jira, supabase backend, tailwind frontend"
    
    if not os.path.exists("./workdir"):
        os.mkdir("./workdir")

    if len(os.listdir("./templates")) == 0:
        print(
            dedent("""
            !!! NO TEMPLATES FOUND !!!
            ! YOU MUST FORK THIS BEFORE USING IT !
            
            Taskboard templates are not included as they are Tailwind templates. 
            Place Tailwind individual template folders in `./templates`, 
            if you have a license you can download them at
            https://tailwindui.com/templates, their references are at
            `config/templates.json`.
            
            This was not tested with other templates, 
            prompts in `tasks.py` might require some changes 
            for that to work.
            
            !!! STOPPING EXECUTION !!!
            """)
        )
        exit()

    crew = TaskBoardCrew(idea)  # Updated class name
    crew.run()
    zip_file = "workdir"
    shutil.make_archive(zip_file, 'zip', 'workdir')
    shutil.rmtree('workdir')
    print("\n\n")
    print("==========================================")
    print("DONE!")
    print(f"You can download the project at ./{zip_file}.zip")
    print("==========================================")

