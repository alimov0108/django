from django.shortcuts import render

def sabzavotlar(request):
    return render(request, 'index.html')

def mevalar(request):
    return render(request, 'kartoshka.html')

def pistalar(request):
    return render(request, 'kartoshka.html')
