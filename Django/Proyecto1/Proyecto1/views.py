from django.http import HttpResponse

# A cada funcion se le denomina vista, asi que esta es nuetsra primera vista
def saludo(request) :
    return HttpResponse("Hola esta es el primer response")

# Esta seria nuestra segunda vista.
def despedida(request):
    return HttpResponse("Hasta luego bros!")