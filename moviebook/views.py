from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "moviebook/index.html", dict(nazov_filmu="Strážci Galaxie", zanr="Fantasy", hodnotenie="11/10"))
