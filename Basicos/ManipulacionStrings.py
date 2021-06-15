tema_curso = "== Manipulacion de Strings =="
print(tema_curso)

#Asignacion de variables
mensaje = "Hola"
mensaje += " "
mensaje += "Brandon"
print(mensaje)

#Concatenacion
mensaje = "Hola"
espacio = " "
nombre = "Brandon"
print(mensaje + espacio + nombre)

#Numero a String
numero_uno = 4
numero_dos = 6
suma = numero_uno + numero_dos
suma = str(suma)
print("El resultado de la suma es: " + suma)

#Busqueda
mensaje = "Prueba de busqueda"
buscar_subcadena = mensaje.find("busqueda")
print(buscar_subcadena)

#Extraccion
mensaje_extraccion = "Este es el mensaje de Extraccion"
buscar_extraccion = mensaje_extraccion.find("Extraccion")
extraer_subcadena = mensaje_extraccion[0:buscar_extraccion]
print(extraer_subcadena)

#Comparacion
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)