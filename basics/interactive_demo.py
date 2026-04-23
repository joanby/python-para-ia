# Números
from re import S


age = 25
score = -10

price = 19.99
temperature = -5.5
pi = 3.141592

total = 10+7
change = 20 - 7

area = 6 * 4
half = 11/2

squared = 5**2
cubed = 5**3

result = 10/3
result = 10//3

# Strings
name = "Juan Gabriel"
message = "Hola mundo!"

lenguage = 'Python'
lenguage = "Python"

paragraph = """Esto es
un párrafo
multilínea 
en Python"""

first = "Juan"
second = "Gabriel"

full_name = first + " " + second
print(full_name)

stars = "*" * 5
print(stars)

message = "Hola, ¿cómo estás?"
print(len(message))

empty = ""
print(len(empty))

age = 37
message = "Tengo " + str(age) + " años"
print(message)

# Booleanas
is_logged_in = True
is_admin = False
has_permission = True

age = 37
can_vote = (age >= 18) # >, >=, == , <=, <, !=

print(age != 37)

first = 5
second = 2
print(first != second)


# Operaciones
print(10**3)
result = (2+3)*4

age = 18
print(age <= 18)


age = 25 
has_license = True

can_drive = (age >= 18) and has_license

day = "Sábado"
is_weekend = (day == "Sábado" or day == "Domingo")

is_adult = age >= 18
is_child = not is_adult

#AND ambas deben ser ciertas
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#OR siempre que una es cierta
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#NOT
print(not True)
print(not False)

score = 0
score = score + 10
score += 10

x = 10
x += 5
x *= 2