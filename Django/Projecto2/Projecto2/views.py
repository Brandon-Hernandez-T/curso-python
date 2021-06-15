from django.http import HttpResponse
import datetime

# A cada funcion se le denomina vista, asi que esta es nuetsra primera vista
def saludo(request) :
    mensaje = "Hola esta es el primer response"
    return HttpResponse(mensaje)

# Esta seria nuestra segunda vista.
def despedida(request):
    return HttpResponse("Hasta luego bros!")

#Esta es la tercer vista: 
def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    mensaje = "fecha y hora actuales: " + str(fecha_actual)

    return HttpResponse(mensaje)

def calculaEdad(request, anio):
    edadActual = 18
    periodo = anio-2021
    edadFutura = edadActual + periodo
    mensaje = "En el año " + str(anio) + " tendras " + str(edadFutura) + " años"
    
    return HttpResponse(mensaje)