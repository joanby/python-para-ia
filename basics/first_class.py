class Dog: #sintaxis del PascalCase
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Fluffy", "Golden Retriever")
dog2 = Dog("Max", "Poodle")
dog3 = Dog(name = "Snoopy", breed = "Beagle")


print(dog1.name)
print(dog2.breed)


class APIConfig: 

    version = "1.0" # la misma para todas las instancias
    max_retries = 5 # la misma para todas las instancias

    def __init__(self, api_key, model = "gpt-3.5-turbo", max_tokens = 100):
        self.api_key = api_key
        self.model = model 
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"
        self.request_count = 0

dev_config = APIConfig("sk-dev-key-xxxx", max_tokens=50)

prod_config = APIConfig("sk-prod-key", "gpt-4o-mini", max_tokens=1000)

print(dev_config.model)
print(prod_config.model)
print(prod_config.max_tokens)

dev_config.max_tokens = 300
print(dev_config.max_tokens)
print(prod_config.max_tokens)



class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Email inválido: {email}")
            return False 
        return True

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Edad inválida: {age}")
            return False
        return True

    def get_errors(self):
        return self.errors

validator = DataValidator()
validator.validate_email(email = "juangabriel-frogames.es")
validator.validate_age(age = 245)

validator.validate_email("juangabriel@frogames.es")
validator.validate_age(37)

validator.get_errors()




class Animal:
    def __init__(self, name):
        self.name = name
        self.is_pet = True

    def eat(self):
        return f"{self.name} está comiendo"
    
    def sleep(self):
        return f"{self.name} está durmiendo"

class Dog(Animal): ##herencia Dog hereda de Animal 
    def __init__(self, name, breed):
        super().__init__(name) ## clase hijo llama al constructor de la clase padre
        self.breed = breed

    def bark(self):
        return f"{self.name} está ladrando!!!"

    def describe(self):
        return f"{self.name} es de la raza {self.breed}"


my_dog = Dog("Snoopy")
my_dog2 = Dog(name = "Lassy")

print(my_dog.eat())
print(my_dog.sleep())
print(my_dog.bark())