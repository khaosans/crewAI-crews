import json
import shutil
from pathlib import Path

from langchain.tools import tool


class TemplateTools():

  @tool("Learn about taskboard templates")
  def learn_taskboard_options(self, input):
    """Learn the templates at your disposal for taskboards."""
    templates = json.load(open("config/templates.json"))
    return json.dumps(templates, indent=2)

  @tool("Copy taskboard template to project folder")
  def copy_taskboard_template_to_project_folder(self, taskboard_template):
    """Copy a taskboard template to your project 
    folder so you can start modifying it, it expects 
    a taskboard template folder as input."""
    source_path = Path(f"templates/{taskboard_template}")
    destination_path = Path(f"workdir/{taskboard_template}")
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_path, destination_path)
    return f"Taskboard template copied to {taskboard_template} and ready to be modified. Main files should be under ./{taskboard_template}/src/components; you should focus on those."

  @tool("Read taskboard templates")
  def read_templates(self, taskboard_template):
    """Read all taskboard templates from the specified directory."""
    source_path = Path(f"templates/{taskboard_template}")
    # Read all files in the directory
    files = [str(file) for file in source_path.rglob("*")]
    return json.dumps(files, indent=2)