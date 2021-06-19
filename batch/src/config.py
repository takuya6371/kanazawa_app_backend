from dotenv import load_dotenv
load_dotenv()

import os
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASS = os.getenv('POSTGRES_PASS')
print(POSTGRES_PASS)