from django.http import HttpResponse
import datetime

# A cada funcion se le denomina vista, asi que esta es nuetsra primera vista


def saludo(request):
    mensaje = "Hola esta es el primer response"
    return HttpResponse(mensaje)

# Esta seria nuestra segunda vista.


def despedida(request):
    return HttpResponse("Hasta luego bros!")

# Esta es la tercer vista:


def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    mensaje = "fecha y hora actuales: " + str(fecha_actual)

    return HttpResponse(mensaje)


def calculaEdad(request, edad, anio):
    periodo = anio-2021
    edadFutura = edad + periodo
    mensaje = "En el año %s tendras %s años" % (anio, edadFutura)

    return HttpResponse(mensaje)


def mensajeUsuario(request, mensaje):
        if mensaje == 'brandon':
            output = "Ingreso"
        else:
            output = "Incorrecto"    
        return HttpResponse(output)
