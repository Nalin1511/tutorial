from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('votacao/', include ('votacao.urls')),
    path('docedeleite/', include ('docedeleite.urls')),
]
