from importlib import resources
from os import getenv

"""
Environment variables have highest priorities.
Then `local.env` definitions.
"""

try:
    from dotenv import load_dotenv

    with resources.path("envs", "local.env") as p:
        print(f"Settings file `local.env` is read: {load_dotenv(p)}")
except (FileNotFoundError, ModuleNotFoundError):
    pass

USER = getenv("POSTGRES_USER")
PASSWORD = getenv("POSTGRES_PASSWORD")
HOST = getenv("DB_HOST")
PORT = 5432
DATABASE = getenv("POSTGRES_DB")
