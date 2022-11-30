from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('body/', views.body, name="body"),
    path('signup/', views.signup, name="signup"),       
    path('login/', LoginView.as_view(template_name='login.html') , name="login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),    
    path('datos_personales/', views.datos_personales, name="datos_personales"),
]  