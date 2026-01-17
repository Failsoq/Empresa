from django.shortcuts import render
from typing import Dict, List, Any # Siempre pendiente de importar typing en views
# Create your views here.

def listado(request):
    productos: List[str] = [
        'Cloro',
        'Jabon liquido',
        'Lavaplatos',
        'Desinfectante',
        'Detergente',

    ]

    datos: Dict[str, Any] = {
        'titulo': 'Página de productos',
        'encabezado' : 'Listado ordenado de productos',
        'productos': productos

    }
    
    return render(request, 'productos/listado.html', datos)