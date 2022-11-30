from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),    
    path("busqueda/", views.busqueda, name="busqueda"),
    path("validar/", views.validar_certificado, name="validar"),
    path('estadisticas/<int:id_sondeo>/', views.estadisticas, name="estadisticas"),
    path('estadisticasTema/<int:id_tema>/', views.estadisticasTema, name="estadisticasTema"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)