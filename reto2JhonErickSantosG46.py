#Jhon Erick Santos Gonzalez
#Misiontic 2022 G46 
#Reto 2 Semana 3
#programa de descuentos sobre matricula
#entradas nombre y apellidos, edad en años, puntaje de examen,salario 
#procesos calcular el valor del descuento con base en los criterios
#salidas nombre y apellido,valor del descuento por edad,descuento por ingresos, puntaje y valor total descuento

alumnos = []
name = input("Ingrese su nombre completo: ") 
alumnos.append(name) # los nombres de los benificiarios se agregan a la lista "alumnos"
age = int(input("Ingrese su edad: "))
salary = float(input("Ingrese el valor mensual de ingresos familiares: "))
puntaje = int(input("Ingrese el puntaje obtenido: "))
salary_base = 908526

if age > 0  :  # se mira el rango de edades para elegir el valor porcentual del descuento
    if age >= 15 and age <= 18:
        des_age = 0.25
    elif age >= 19 and age <= 21 :
        des_age = 0.15
    elif age >=22 and age <= 25 :
        des_age = 0.10
    else:
        des_age = 0
if salary  >= 0 : # se mira el salario ingresado en comparacion al salario minimo establecido 
    if salary <= salary_base :
        des_salary = 0.30
    elif salary > salary_base and salary <= salary_base * 2 :
        des_salary = 0.20
    elif salary > salary_base * 2  and salary <= salary_base * 3 :
        des_salary = 0.10
    elif salary > salary_base * 3 and salary <= salary_base * 4 :
        des_salary = 0.05
    else:
        des_salary = 0
if puntaje <= 100 :   # se mira el puntaje para elegir el valor porcentual del descuento
    if puntaje >= 80 and puntaje < 86 :
        des_punt = 0.30
    elif puntaje >= 86 and puntaje < 91 :
        des_punt = 0.35
    elif puntaje >= 91 and puntaje < 96 :
        des_punt = 0.40
    elif puntaje >= 96 :
        des_punt = 0.45
    else:
        des_punt = 0

print(str("Beneficiario:"),alumnos[0].upper()) # se pide imprimir el primer nombre de la lista
print(str("Descuento por edad del "), int(des_age * 100), str("%"))
print(str("Descuento por ingresos familiares del "), int(des_salary * 100), str("%"))
print(str("Descuento por puntaje en su examen del "), int(des_punt * 100), str("%"))

des_total = int((des_punt * 100) + (des_age * 100) + (des_salary * 100))
print(str("Descuento total en el valor su matricula del "), des_total, "%")
