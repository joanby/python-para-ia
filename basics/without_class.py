name = "OpenAI"
model = "gpt-4o-mini"

def generate_response(prompt):
    #procesamos el prompt
    response = "Aquí iria la respuesta del modelo"
    return response

# ... 

class OpenAIClient: 
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def generate_response(self, prompt):
        #Procesamos el prompt
        response = "Aquí iria la respuesta del modelo"
        return response


api_key = "sk-......"
prompt = "Explicación de qué es Python"
response = make_api_call(api_key, prompt)
print(response)


## api_utils.py
def setup_api(api_key):
    return {
        "api_key": api_key, 
        "base_url": "https://api.openai.com"
    }

def generate_response(api_config, prompt):
    # Hacer la llamada a la API
    return response

## main.py
from api_utils import setup_api, generate_response 
api_config = setup_api("sk-xxx")


# client.py

class OpenAIClient: 
    def __init__(self, api_key):
        self.name = "OpenAI"
        self.model = "gpt-4o-mini"
        self.api_key = api_key
        self.base_url = "https://api.openai.com"

    def generate_response(self, prompt):
        #Procesamos el prompt
        response = "Aquí iria la respuesta del modelo"
        return response

# main.py
from client import OpenAIClient
client = OpenAIClient("sk-xxxx")
reponse = client.generate_response("Explícame qué es Python")