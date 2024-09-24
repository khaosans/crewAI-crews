import subprocess

class Deployment:
    def __init__(self, environment):
        self.environment = environment

    def package_app(self):
        subprocess.run(["pip", "install", "-r", "requirements.txt"])
        subprocess.run(["streamlit", "run", "app.py"])

    def deploy_to_cloud(self):
        # Example: Deploy to Heroku
        subprocess.run(["git", "init"])
        subprocess.run(["heroku", "create"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Deploy to Heroku"])
        subprocess.run(["git", "push", "heroku", "master"])