from django.urls import path, include
from  . import views
from api.views import *


urlpatterns = [
    #gestion site
    path('', views.home, name='home'),
    path('employee', views.employee, name='employee'),
    path('statistique', views.statistique, name='statistique'),
]
