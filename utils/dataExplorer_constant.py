from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('BBDD_MONGO_URI')
DATABASE_DB = os.getenv('BBDD_MONGO_DB')
