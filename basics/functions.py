def greet():
    print("Hola, mundo!!")
    print("Bienvenidos a Python")

greet()

def nombre_de_la_funcion():
    # El código de la función aparece aquí
    # El código se debe indentar correctamente
    pass

def calculate_total():
    pass

def send_email():
    pass

def validate_password():
    pass

def say_goodbye():
    print("Adioooos!!!")
    print("Nos vemos en otra ocasión!!!")
    pass

say_goodbye()
say_goodbye()
say_goodbye()


def check_weather():
    temperature = 25
    if temperature > 25:
        print("Hace calor aquí!!")
    else:
        print("Hace un tiempo magnífico!")

check_weather()


def calculate_price():
    price = 100
    tax = price * 0.21
    print(f"Total: {price + tax} €")

calculate_price()

discount_rate = 0.15 #Variable global

def apply_discount(price):
    discount = price * discount_rate
    return price - discount

result = apply_discount(100)
print(result)


counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)

total = 0

def add_to_total(amount):
    global total
    total += amount

add_to_total(50)
print(total) 

def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)


def greet_juan():
    print("Hola Juan!!!")

greet_juan()

def greet(name):
    print(f"Hola {name}!!!")

greet("Juan")
greet("Alicia")
greet("Charlie")


def introduce(name, age):
    print(f"Mi nombre es {name}")
    print(f"Y tengo {age} años")

introduce("Juan", 37)
introduce("Alicia", 25)

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: {final_price} €")

calculate_total(100, 0.21, 15)

def greet(name, greeting = "Hola"):
    print(f"{greeting}, {name}")

greet("Juan")
greet("Alicia", "Qué pasa")
greet("Mario", "Uy, cuanto tiempo")

def create_profile(name, age, city):
    print(f"{name} tiene {age} años y vive en {city}")

create_profile("Juan Gabriel", 37, "Palma de Mallorca")

create_profile(city="Nueva York", age = 30, name = "Alicia")
create_profile(name="Javi", city="Londres", age = 25)


def add_print(a, b):
    print(a+b)

add_print(4,6)

def add_return(a, b):
    return a+b

result = add_return(4,6)
print(f"El resultado de la operación es {result}")

def calculate_area(width, height):
    area = width * height
    return area

room_area = calculate_area(8, 4)
print(f"El área del salón es de {room_area} metros cuadrados")

def double(number):
    return number * 2

result = double(4)

total = double(5) + double (3)

print(double(4))

if double(6)>10:
    print("Número enorme!!!")

def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([4,7,2,8,1,9])
print(f"Mín: {minimum}, Max: {maximum}")

result = get_min_max([4,7,2,8,1,9])
print(result)

def get_greeting_print(name):
    print(f"Hola, {name}!!!") 

def get_greeting_return(name):
    return f"Hola, {name}!!!"

message = get_greeting_print("Juan Gabriel")
print(message)


message = get_greeting_return("Juan Gabriel")
print(message)