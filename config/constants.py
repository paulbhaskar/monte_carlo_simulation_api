import os
from dotenv import load_dotenv

# reads environment variables from a .env file; please place this file in root directory for autodiscovery
load_dotenv()

MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'monte_carlo_simulation')
MONGO_DB_HOST = os.environ.get('MONGO_DB_HOST', '127.0.0.1')
MONGO_DB_PORT = int(os.environ.get('MONGO_DB_PORT', 27017))

CELERY_BROKER = os.environ.get("CELERY_BROKER", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0")

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

TIME_ZONE = os.environ.get('TIME_ZONE', 'EST')

TASK_BATCH_SIZE = int(os.environ.get('TASK_BATCH_SIZE'))
