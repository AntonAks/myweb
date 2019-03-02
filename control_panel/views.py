from django.shortcuts import render

from . models import ControlPanel

def control_panel(request):
    return render(request, 'control_panel/control_page.html')
