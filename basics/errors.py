if x > 5:
    print("Número grande")

result = 10/0

print(score)

"hello" + 5

try:
    with open("data.txt", 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("El fichero data.txt no se encuentra disponible")
    content = "Valor por defecto en caso de que el fichero no exista"
print("Finalizado")

try:
    age = int(input("Introduce tu edad: "))
    print(f"En 10 años tu edad será {age + 10}")
except ValueError:
    print("Por favor, introduce un número entero")

try:
    with open("number.txt",'r') as f:
        text = f.read()
    number = int(text)
    result = 100/number
except FileNotFoundError:
    print("El fichero number.txt no existe")
except ValueError:
    print("El fichero no contiene un número que sea válido")
except ZeroDivisionError:
    print("No se puede dividir por cero")
else: 
    print(f"El resultado es {result}")


try: 
    file = open("data.txt", 'r')
    data = file.open()
except FileNotFoundError:
    print("El fichero no existe")
finally:
    if "file" in locals() and not file.closed:
        file.close()
    print("Limpieza finalizada")