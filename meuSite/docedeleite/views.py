from django.http import HttpResponse


def docedeleite (request):
    return HttpResponse("Doce de leite")

def novodoce (request):
    return HttpResponse("Novo doce")


def leitecomgoiaba (request):
    return HttpResponse("Leite com goiaba")


def aindatemdoce (request):
    return HttpResponse("Ainda tem Doce")


def equipe (request):
    return HttpResponse("Nalin <br> Italo")
