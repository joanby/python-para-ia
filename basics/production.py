## Resto del script 

import os 

api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_NAME", "default.db")
database

if 'API_KEY' in os.environ:
    api_key = os.environ["API_KEY"]
else: 
    print("Clave API no encontrada")


from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get('API_KEY')
api_key

debug = os.environ.get('DEBUG')
debug