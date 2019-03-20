from django.shortcuts import render

def allblogs(request):
    print(request.__str__())

    return render(request, 'sandbox/2_2_basic_typography.html')

