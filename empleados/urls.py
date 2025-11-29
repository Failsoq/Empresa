from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.listado, name='empleados' ), # type: ignore
]
    