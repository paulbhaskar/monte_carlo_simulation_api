import os
from dotenv import load_dotenv

# reads environment variables from a .env file; please place this file in root directory for autodiscovery
load_dotenv()

MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'monte_carlo_simulation')
MONGO_DB_HOST = os.environ.get('MONGO_DB_HOST', '127.0.0.1')
MONGO_DB_PORT = int(os.environ.get('MONGO_DB_PORT', 27017))
