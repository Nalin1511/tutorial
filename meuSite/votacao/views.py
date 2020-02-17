from django.http import HttpResponse


def index(request):
    return HttpResponse("oiiieee")

def resultados (request):
    return HttpResponse("resultados")
