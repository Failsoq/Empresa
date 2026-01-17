from django.shortcuts import render
from typing import Dict, List, Any

# Create your views here.
def listado(request):
    clientes: List [str] = [
        'ARsistema',
        'Ferreteria HH',
        'Autoperiquitos JJ',
        'Paveca',
        'Autorepuestos RR',
        'Tecno Digital',
    ]
    # Crear diccionario llamado datos
    datos: Dict[str, Any] = {
        'titulo': 'Lista de clientes',
        'encabezado': 'Lista ordenado de clientes',
        'clientes': clientes,
    }
    return render(request, 'clientes/listado.html', datos)