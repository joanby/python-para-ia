#Listas
from typing import Any


my_list = []

#         0          1          2
fruits = ["Manzana", "Plátano", "Naranja"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Hola", 5, True, 3.1415]

print(fruits[0])
print(fruits[1])
print(fruits[6])
print(fruits[-1])
print(fruits[-2])
print(fruits[0:2])
print(fruits[1:])
print(fruits[:2])

fruits = ["Manzana", "Plátano", "Naranja"]
fruits[0] = "Mango"
print(fruits)

fruits.append("Uvas")
fruits.append("Kiwi")
print(fruits)
print(len(fruits))

fruits.remove("Naranja")
print(fruits)

del fruits[1]
print(fruits)

last_fruit = fruits.pop()
print(fruits)
last_fruit

numbers = [3,2,6,1,5,1]
print(len(numbers))
print(numbers.count(1))
print(numbers.index(6))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers_copy = numbers.copy() 
numbers_copy

fruits = ["Manzana", "Plátano", "Naranja"]

if "Manzana" in fruits:
    print("Manzana encontrada!")

if fruits: #si la lista está vacía
    print("La lista tiene elementos")
else:
    print("La lista está vacía")

for fruit in fruits: 
    print(f"Me encanta el/la {fruit}")

#Diccionarios
my_dict = {}

people = {
    "name": "Juan Gabriel",
    "age": 37, 
    "city": "Palma de Mallorca"
}

scores = dict[str, int](maths = 97, english = 85, science = 74)

print(people["name"])
print(scores["maths"])

print(scores["history"])

print(people.get("job"))
print(people.get("job", "Desconocido"))

person = {
    "name": "Juan Gabriel",
    "age" : 37
}

person["email"] = "juangabriel@frogames.es"
person["age"] = 38

print(person)

del person["email"]
print(person)
age = person.pop("age")
print(person)
print(age)
person.clear()
person

people
print(people.keys())
print(people.values())
print(people.items())

if "name" in people:
    print("El usuario tiene nombre")

people.update({"age": 38, "job": "Mathematician"})
print(people)

students = {
    "alicia": {"age": 22, "grade": 89},
    "mario": {"age": 23, "grade": 72},
    "juan": {"age": 25, "grade": 98}
}
students["alicia"]["grade"]

for student in students:
    print(f"{student.lower()} tiene de nota {students[student]['grade']}")

#Tuplas
empty_tuple = ()
point = (3,5)
colors = ("rojo", "verde", "azul")

single = (42, )
tuplee = (42)

coordinates = 10, 15, 20

point
print(point[0])
print(colors[-1])
print(colors[0:2])

point
x, y = point


a, b, c = 1, 2, 3

x, y = y, x

#Conjuntos
empty_set = set[Any]()
numbers = {1,2,3,4,5,5,4,3}
fruits = set[str](["manzana", "manzana", "plátano", "pera"])

scores = [85, 90, 95, 90, 85, 80]
unique_scores = set[int](scores)

colors = {"rojo", "azul"}
colors.add("verde")
print(colors)

colors.remove("green")
print(colors)
colors.discard("amarillo")

if "rojo" in colors:
    print("El rojo está disponble")

for color in colors:
    print(color)

list(colors)

names = ["Alicia", "Juan", "Alicia", "Roberto", "Jose", "Juan"]
unique_name = list(set(names))
unique_name

allowed_users = {"Alicia", "Juan", "Roberto"}
new_user = "Jose"
if new_user in allowed_users:
    print("Acceso concedido!")
