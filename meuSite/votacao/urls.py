from django.urls import path
from votacao.views import index, resultados

urlpatterns = [
    path('votar/', index),
    path('resultados/', resultados),
]
