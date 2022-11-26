from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('usuario/<str:username>/', views.usuario, name="usuario"), 
    path('usuario/<str:username>/sondeo/', views.usuario_sondeo, name="usuario_sondeo"),
    path('usuario/<str:username>/pregunta/', views.usuario_pregunta , name="usuario_pregunta"),
    path('usuario/<str:username>/contestados/', views.sondeos_contestados , name="sondeos_contestados"),
             
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)