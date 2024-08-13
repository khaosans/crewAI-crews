import sqlite3
import json

class Persistence:
    def __init__(self, db_path='game_app.db'):
        self.connection = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS agents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role TEXT NOT NULL,
                    backstory TEXT,
                    allow_delegation BOOLEAN,
                    verbose BOOLEAN
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    game_id INTEGER,
                    agent_id INTEGER,
                    description TEXT NOT NULL,
                    expected_output TEXT,
                    result TEXT,
                    FOREIGN KEY(game_id) REFERENCES games(id),
                    FOREIGN KEY(agent_id) REFERENCES agents(id)
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id INTEGER,
                    log TEXT,
                    FOREIGN KEY(task_id) REFERENCES tasks(id)
                )
            ''')

    def save_game(self, description):
        with self.connection:
            cursor = self.connection.execute(
                'INSERT INTO games (description) VALUES (?)',
                (description,)
            )
            return cursor.lastrowid

    def save_agent(self, role, backstory, allow_delegation, verbose):
        with self.connection:
            cursor = self.connection.execute(
                '''INSERT INTO agents (role, backstory, allow_delegation, verbose) 
                VALUES (?, ?, ?, ?)''',
                (role, backstory, allow_delegation, verbose)
            )
            return cursor.lastrowid

    def save_task(self, game_id, agent_id, description, expected_output):
        with self.connection:
            cursor = self.connection.execute(
                '''INSERT INTO tasks (game_id, agent_id, description, expected_output) 
                VALUES (?, ?, ?, ?)''',
                (game_id, agent_id, description, expected_output)
            )
            return cursor.lastrowid

    def save_task_result(self, task_id, result):
        # Serialize the result (CrewOutput object) to a JSON string
        result_serialized = json.dumps(result, default=str)

        with self.connection:
            self.connection.execute(
                'UPDATE tasks SET result = ? WHERE id = ?',
                (result_serialized, task_id)
            )

    def save_log(self, task_id, log):
        with self.connection:
            self.connection.execute(
                'INSERT INTO logs (task_id, log) VALUES (?, ?)',
                (task_id, log)
            )

    def close(self):
        self.connection.close()
