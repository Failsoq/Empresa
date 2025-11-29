from django.shortcuts import render
from typing import Dict

# Create your views here.
def listado(request):
    # Crear diccionario llamado datos
    datos: Dict[str, str] = {
        'titulo': 'Lista de clientes',
        'encabezado': 'Lista ordenado de clientes'
    }
    return render(request, 'clientes/listado.html', datos)