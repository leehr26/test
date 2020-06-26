# hChart.urls.py
from django.contrib import admin
from django.urls import path, include
from chart import views                                     # !!!

urlpatterns = [
    path('', include('chart.urls')),
    path('world-population/',
         views.world_population, name='world_population'),  # !!!
    path('admin/', admin.site.urls),
    path('covid19_deaths/',
         views.covid19_deaths, name='covid19_deaths'),
    path('accounts/', include('accounts.urls')),
]