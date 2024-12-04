from pathlib import Path


# MYSQL_HOST = 'db'
MYSQL_HOST = "localhost"
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'root'
DATABASE_NAME = "sqli_training"

SERVER_ROOT = Path(__file__).parent
PROJECT_ROOT = SERVER_ROOT.parent
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 5000