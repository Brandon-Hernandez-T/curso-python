tema_curso = "== Condiciones =="
print(tema_curso)

#Condicional IF - ELSE
numeroIngresado = int(input("Introduce un numero: "))
if numeroIngresado >= 10 :
    print("El numero es mayor o igual a 10")
else :
    print("El numero es menor a 10")
print("Fin")

#Condicional elif
calificacionQuimica = int(input("Ingresa calificacion de Quimica: "))
calificacionMatematicas = int(input("Ingresa calificacion de Matematicas: "))
calificacionEspaniol = int(input("Ingresa calificacion de Espaniol: "))
promedio = (calificacionQuimica + calificacionMatematicas + calificacionEspaniol) / 3
if promedio == 10 :
    print("Tu calificaciones es: ", promedio, ' Felicidades eres "EXCELENTE"')
elif promedio >= 7 and promedio <= 9 :
    print("Tu calificaciones es: ", promedio, ' Felicidades eres "REGULAR"')
else :
    print("Tu calificaciones es: ", promedio, ' Ups! estas "REPROBADO"')
print("Fin")
