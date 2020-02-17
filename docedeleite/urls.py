from django.urls import path
from docedeleite.views import docedeleite, novodoce, leitecomgoiaba, aindatemdoce, equipe

urlpatterns = [
    path ('', docedeleite)
    path('novo-doce/', novodoce ),
    path('leite-com-goiaba/', leitecomgoiaba),
    path('ainda-tem-doce/', aindatemdoce),
    path('equipe/', equipe),
]
