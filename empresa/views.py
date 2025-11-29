from django.shortcuts import render
from typing import Dict

def inicio(request):

    datos: Dict[str,str] = {
    'titulo': 'Pagina de inicio',
    'encabezado': 'Bienvenidos'
    }
    
    return render(request, 'empresa/home.html', datos)