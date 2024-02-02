#Request: Realizar peticiones
#HTTPResponse: Enviar respuesta por el protocolo HTTP
from django.http import HttpResponse

#Vista
def bienvenida(Request): #Pasar un objetivo tipo Request como primer argumento
    return HttpResponse("Bienvenido")

def bienvenidaRojo(Request): #Pasar un objetivo tipo Request como primer argumento
    return HttpResponse("<p style='color: red;'>Bienvenido</p>")