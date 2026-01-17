from django.shortcuts import render
from typing import Dict

# Create your views here.
def listado(request):
    datos: Dict[str, str] = {
        'titulo': 'Página de  pedidos',
        'encabezado': 'Listado ordenado de pedidos',
    }

    return render(request, 'pedidos/listado.html', datos) # <-----  Repasar este codigo #
    
    
    
    
    #Se crea un diccionario para darle valor a las variables de 'listado.html'
