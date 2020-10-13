def suma(v1,v2):
	resultado = int(v1) + int(v2)
	return resultado

def resta(v1,v2):
	resultado = int(v1) - int(v2)
	return resultado
def multiplicacion(v1,v2):
	resultado = int(v1) * int(v2)
	return resultado
def division(v1,v2):
	resultado = int(v1) / int(v2)
	return resultado

while True:	
	v1 = input("Ingrese valor 1: ")
	v2 = input("Ingrese valor 2: ")
	operacion = input("Seleccione operacion(suma/resta/multiplicacion): ")

	if operacion == "suma":	
		print(suma(v1,v2))
	elif operacion == "resta":
		print(resta(v1,v2))
	elif operacion == "multiplicacion":
		print(multiplicacion(v1,v2))
	seguir = input("Desea realizar otra operacion(y/n): ")
	if seguir == "y":
		pass
	else:
		break
