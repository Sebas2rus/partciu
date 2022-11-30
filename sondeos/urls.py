
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('tema/<int:id_pregunta>/', views.tema, name="tema"), 
    path('contestado/', views.contestado, name="contestado"),
    path('sondeos/', views.sondeos, name="sondeos"),
    path('temas/', views.temas, name="temas"),
    path('sondeo/<int:id_sondeo>/', views.contestar_sondeo, name="contestar_sondeo"),
]
