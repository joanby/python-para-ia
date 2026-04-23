age = 18

if age >=18: 
    print("Puedes votar")
    print("Puedes conducir")
    print("Eres adult@")

temperature = 35
if temperature > 30:
    print("Hace calor aquí...")
else:
    print("La temperatura es ideal")


score = 35
if score >=90:
    print("A - Excelente")
elif score >=80:
    print("B - Notable")
elif score >=50:
    print("C - Bien")
else: #estoy por debajo de 50
    print("F - Necesitas mejorar")


age = 25
has_license = True

if age >= 18 and has_license:
    print("Puedes conducir")

weekend = True
holiday = False
if weekend or holiday:
    print("yujuuu! hoy no curro!!!")

raining = False
if not raining:
    print("Vamos de paseo!!")

has_tickets = False
age = 18
if has_tickets:
    if age >= 18:
        print("Disfruta de la película")
    else:
        print("Necesitas la supervisión de un adulto...")
else:
    print("Compra un ticket para entrar")