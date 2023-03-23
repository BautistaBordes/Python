from random import choice, randrange
from datetime import datetime 


operators = ["+", "-", "*", "/"]

times = 5 

init_time = datetime.now()

aciertos = 0
errores = 0

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)

    print(f"\nCuanto es {number_1} {operator} {number_2}")

    if not((number_2 == 0)and(operator == "/")):
        user_result = float(input("Resultado: "))
        if operator == "+":
            result = number_1 + number_2 
        elif operator == "-":
            result = number_1 - number_2
        elif operator == "*":
            result = number_1 * number_2
        else:
            result = number_1 / number_2
        if user_result == result:
            print("Correcto")
            aciertos += 1
        else:
            print("Incorrecto")
            errores += 1
    else:
        print("No se puede dividir por 0")

end_time = datetime.now()
total_time = end_time - init_time

print(f"\nTardaste {total_time.seconds} segundos.")
print("Respuesta correctas: " + str(aciertos))
print("Respuesta incorrectas: " + str(errores))