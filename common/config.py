from dotenv import load_dotenv
import os

load_dotenv()

class AppConfig:

    API_KEY = os.getenv("API_KEY")
    CITY="Warsaw"
    FILENAME="pogoda_2026.csv"
