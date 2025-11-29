from django.shortcuts import render
from typing import Dict

# Create your views here.
def listado(request):
    datos: Dict[str,str] = {
    'titulo': 'Empleados',
    'encabezado': 'Listado de empleados'
    }
    
    return render(request, 'empleados/listado.html', datos)