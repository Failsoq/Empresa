from django.shortcuts import render
from typing import Dict, Tuple, Any


# Create your views here.
# Crea una tupla de empleados
def listado(request):
    empleados: Tuple[str, ...] = ( # La ', ...' para crear una tupla con varios valores
    'Manuel lopez',
    'Martha Correa',
    'Marcos Peña',
    'Yamileth Rodriguez',
    'Carlos Flores',
)
    datos: Dict[str, Any] = {
    'titulo': 'Empleados',
    'encabezado': 'Listado de empleados',
    'empleados': empleados
    }
    
    return render(request, 'empleados/listado.html', datos)