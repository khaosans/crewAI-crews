# AI Crew for Project Management Dashboard
## Introduction
This project is an example using the CrewAI framework to automate the process of managing projects through a comprehensive dashboard. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

*Disclaimer: Templates are not included as they are Tailwind templates. Place Tailwind individual template folders in `./templates`. If you have a license, you can download them at (https://tailwindui.com/templates). Their references are at `config/templates.json`. This was not tested with other templates; prompts in `tasks.py` might require some changes for that to work.*

By [@joaomdmoura](https://x.com/joaomdmoura)

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Using GPT 3.5](#using-gpt-35)
- [Using Local Models with Ollama](#using-local-models-with-ollama)
- [Contributing](#contributing)
- [Support and Contact](#support-and-contact)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to provide insights and management capabilities through a project management dashboard, allowing users to track project progress, team activities, and upcoming deadlines.

## Running the Script
It uses GPT-4 by default, so you should have access to that to run it.

***Disclaimer:** This will use gpt-4 unless you change it not to, and by doing so it will cost you money (~2-9 USD). The full run might take around ~10-45m. Enjoy your time back*

- **Configure Environment**: Copy `.env.example` and set up the environment variables for [Browseless](https://www.browserless.io/), [Serper](https://serper.dev/), and [OpenAI](https://platform.openai.com/api-keys).
- **Install Dependencies**: Run `poetry install --no-root`.
- **Add Tailwind Templates**: Place Tailwind individual template folders in `./templates`. If you have a license, you can download them at (https://tailwindui.com/templates). Their references are at `config/templates.json`. I haven't tested this with other templates; prompts in `tasks.py` might require some changes for that to work.
- **Execute the Script**: Run `poetry run python main.py` and input your project details.

## Details & Explanation
- **Running the Script**: Execute `python main.py` and input your project details when prompted. The script will leverage the CrewAI framework to process the information and generate a project management dashboard.
- **Output**: The generated dashboard will be available for user interaction, providing insights into project status and team activities.
- **Key Components**:
  - `./main.py`: Main script file.
  - `./tasks.py`: Main file with the tasks prompts.
  - `./tools`: Contains tool classes used by the agents.
  - `./config`: Configuration files for agents.
  - `./templates`: Directory to store Tailwind templates (not included).

## Using GPT 3.5
CrewAI allow you to pass an llm argument to the agent construtor, that will be it's brain, so changing the agent to use GPT-3.5 instead of GPT-4 is as simple as passing that argument on the agent you want to use that LLM (in `main.py`).
```python
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model='gpt-3.5') # Loading GPT-3.5

self.idea_analyst = Agent(
    **idea_analyst_config,
    verbose=True,
    llm=llm, # <----- passing our llm reference here
    tools=[
        SearchTools.search_internet,
        BrowserTools.scrape_and_summarize_kwebsite
    ]
)
```

## Using Local Models with Ollama
The CrewAI framework supports integration with local models, such as Ollama, for enhanced flexibility and customization. This allows you to utilize your own models, which can be particularly useful for specialized tasks or data privacy concerns.

### Setting Up Ollama
- **Install Ollama**: Ensure that Ollama is properly installed in your environment. Follow the installation guide provided by Ollama for detailed instructions.
- **Configure Ollama**: Set up Ollama to work with your local model. You will probably need to [tweak the model using a Modelfile](https://github.com/jmorganca/ollama/blob/main/docs/modelfile.md), I'd recommend adding `Observation` as a stop word and playing with `top_p` and `temperature`.

### Integrating Ollama with CrewAI
- Instantiate Ollama Model: Create an instance of the Ollama model. You can specify the model and the base URL during instantiation. For example:

```python
from langchain.llms import Ollama
ollama_openhermes = Ollama(model="agent")
# Pass Ollama Model to Agents: When creating your agents within the CrewAI framework, you can pass the Ollama model as an argument to the Agent constructor. For instance:

self.idea_analyst = Agent(
    **idea_analyst_config,
    verbose=True,
    llm=ollama_openhermes, # Ollama model passed here
    tools=[
        SearchTools.search_internet,
        BrowserTools.scrape_and_summarize_website
    ]
)
```

### Advantages of Using Local Models
- **Privacy**: Local models allow processing of data within your own infrastructure, ensuring data privacy.
- **Customization**: You can customize the model to better suit the specific needs of your tasks.
- **Performance**: Depending on your setup, local models can offer performance benefits, especially in terms of latency.

## License
This project is released under the MIT License.
