from django.shortcuts import render

def sandbox_page(request):
    if request.path == '/sandbox/':
        return render(request, 'sandbox/base_sandbox.html', {'Page_Title':'Bootstrap Bandbox'})
    else:
        page_name = request.path[1:]
        return render(request, page_name, {'Page_Title':str(page_name).replace('.html', '').replace('sandbox/','')})
