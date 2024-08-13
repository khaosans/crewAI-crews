import logging
import os

from flask import Flask, request, jsonify, render_template, send_from_directory
from persistence import Persistence

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='app_logs.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

persistence = Persistence()


@app.route('/projects', methods=['GET'])
def list_projects():
    projects = persistence.get_all_projects()  # Method to get all projects
    return jsonify(projects)


@app.route('/download/<int:project_id>', methods=['GET'])
def download_code(project_id):
    file_path = persistence.get_code_file_path(project_id)  # Method to get code file path
    if os.path.exists(file_path):
        return send_from_directory(directory=os.path.dirname(file_path), path=os.path.basename(file_path),
                                   as_attachment=True)
    return jsonify({"error": "File not found"}), 404


@app.route('/')
def index():
    app.logger.info('Rendering index page')
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        data = request.form['data']
        app.logger.info(f"Received data: {data}")
        # Process and save the data here
        return jsonify({'status': 'success', 'message': 'Data processed successfully'})
    except Exception as e:
        app.logger.error(f"Error processing data: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        feedback = request.form['feedback']
        app.logger.info(f"Received feedback: {feedback}")
        # Save feedback or process it here
        return jsonify({'status': 'success', 'message': 'Thank you for your feedback!'})
    except Exception as e:
        app.logger.error(f"Error receiving feedback: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/submit', methods=['POST'])
def submit_project():
    data = request.json
    app_description = data.get('appDescription')

    if not app_description:
        return jsonify({"error": "Missing appDescription"}), 400

    # Save the game and get the game_id
    game_id = persistence.save_game(app_description)

    # Return project ID
    return jsonify({"project_id": game_id}), 200


@app.route('/projects', methods=['GET'])
def get_projects():
    # Example logic to get projects
    projects = persistence.get_all_projects()
    return jsonify(projects)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
