class ProductManager:
    def __init__(self):
        self.project_info = {
            "name": "Chatbot Project",
            "description": "A project to develop a chatbot using Streamlit.",
            "timeline": "3 months",
            "team": ["Developer", "QA Engineer", "Data Engineer", "Deployment Engineer", "Integration Tester", "Database Engineer"]
        }

    def get_project_info(self):
        return self.project_info