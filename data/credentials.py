import os

from dotenv import load_dotenv

load_dotenv()


class Credentials:

    if os.environ["STAGE"] == "qa":
        LOGIN = os.getenv("LOGIN")
        PASSWORD = os.getenv("PASSWORD")
    elif os.environ["STAGE"] == "preprod":
        LOGIN = os.getenv("LOGIN")
        PASSWORD = os.getenv("PASSWORD")
