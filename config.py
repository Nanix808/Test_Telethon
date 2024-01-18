import os
from dotenv import load_dotenv, find_dotenv
from fastapi.templating import Jinja2Templates

load_dotenv(find_dotenv())

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BASE_URL = "http://127.0.0.1:8000/"


templates = Jinja2Templates(directory="templates")
