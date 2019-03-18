from django.shortcuts import render

def wordcounter(request):
    return render(request, 'wordcounter/wordcounter.html')
