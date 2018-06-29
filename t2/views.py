from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 't2/index.html')
def p5(request):
    return render(request, 't2/p5.html')
def p1(request):
    return render(request, 't2/p1.html')
def p2(request):
    return render(request, 't2/p2.html')
def p3(request):
    return render(request, 't2/p3.html')
def p4(request):
    return render(request, 't2/p4.html')