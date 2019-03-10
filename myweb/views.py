from django.shortcuts import render

def my_web_home_page(request):
    return render(request, 'home.html')
