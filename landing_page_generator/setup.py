import os

def create_env_file():
    """Create a .env file for Supabase configuration."""
    env_content = """# Supabase Configuration
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
"""
    with open('.env', 'w') as env_file:
        env_file.write(env_content)
    print(".env file created. Please fill in your Supabase credentials.")

def create_readme():
    """Create a README file with setup instructions."""
    readme_content = """# Project Setup Instructions

## Prerequisites
- Python 3.x
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```

## Environment Variables
1. Create a `.env` file in the root directory of the project.
2. Fill in your Supabase credentials in the `.env` file:
   - `SUPABASE_URL`: Your Supabase project URL.
   - `SUPABASE_KEY`: Your Supabase API key.

## Setting Up Supabase
1. **Create a Supabase Project**:
   - Go to [Supabase](https://supabase.io/) and sign up or log in.
   - Create a new project and note the `SUPABASE_URL` and `SUPABASE_KEY`.

2. **Database Setup**:
   - Use the Supabase dashboard to create tables and manage your database.
   - You can run SQL commands directly in the SQL editor provided by Supabase.

3. **Connecting to Supabase**:
   - Ensure your application is configured to connect to Supabase using the credentials in your `.env` file.
   - Use the Supabase client library in your back-end code to interact with the database.

## Running the Application
To run the application, execute the following command: