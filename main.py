# Import the necessary module
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()


def main():
    configure()
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')

    # Example usage
    print(f'SECRET_KEY: {SECRET_KEY}')
    print(f'DATABASE_URL: {DATABASE_URL}')