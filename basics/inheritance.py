class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False

    def load(self):
        print(f"Cargando el modelo {self.model_name}")
        self.is_loaded = True

class TextModel(BaseModel):
    def __init__(self, model_name, max_length = 1000):
        super().__init__(model_name)
        self.max_length = max_length

    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        #el modelo aquí ya está cargado 
        if len(text) > self.max_length:
            text = text[:self.max_length]
        return f"Texto procesado: {text}"


model = TextModel(model_name="gpt-3.5-turbo", max_length=100)
result = model.process_text(text = "Hola mundo, soy Juan Gabriel Gomila y este es un ejemplo más largo de lo habitual para ver si en este caso nos corta el texto nuestro método que hemos creado para procesar y limpiar el texto de forma adecuada.")
print(result)


# Programación funcional 

def clean_text(text):
    return text.strip().lower()

def remove_puntuation(text):
    return text.replace(".", "").replace(",", "")

result = remove_puntuation(clean_text("    Hola, Mundo.     "))
print(result)

# Programación orientada a objectos
class TextProcessor:
    def __init__(self, text):
        self.text = text
    
    def clean_text(self):
        self.text = self.text.strip().lower()
        return self

    def remove_puntuation(self):
        self.text = self.text.replace(".", "").replace(",", "")
        return self

processor = TextProcessor(text = "     Hola, Mundo.      ")
result = processor.clean_text().remove_puntuation().text
print(result)

# Fin de la clase