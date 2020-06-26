from django.contrib import admin
from django.urls import path, include
from chart import views                                     # !!!

urlpatterns = [
    path('', views.titanic_dual_axes, name='titanic_dual_axes'),
    path('ticket-class/1/',
         views.ticket_class_view_1, name='ticket_class_view_1'),
    path('ticket-class/2/',
         views.ticket_class_view_2, name='ticket_class_view_2'),
    path('ticket-class/3/',
         views.ticket_class_view_3, name='ticket_class_view_3'),
    path('world-population/',
         views.world_population, name='world_population'),
    path('json-example/', views.json_example, name='json_example'),
    path('json-example/data/', views.chart_data, name='chart_data'),

    path('covid19_deaths/',
         views.covid19_deaths, name='covid19_deaths'),
    path('admin/', admin.site.urls),
]