from django.shortcuts import render

# Create your views here.

from . import nas_modul


def kalkulacka(request):
    error_msg = None
    vysledok = None
    if request.method == "POST":
            try:
                float(request.POST["a"])
                float(request.POST["b"])
            except:
                error_msg = "A nebo B není číslo!"
                return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledok=vysledok))

            if (float(request.POST["b"]) == 0 and request.POST["operator"] == "/"):
                    error_msg = "Chyba dělení nulou"
                    return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledok=vysledok))
            if (request.POST["operator"] == "+"):
                vysledok = nas_modul.secti(request.POST["a"], request.POST["b"])
            elif (request.POST["operator"] == "-"):
                vysledok = nas_modul.odecti(request.POST["a"], request.POST["b"])
            elif (request.POST["operator"] == "/"):
                vysledok = nas_modul.podil(request.POST["a"], request.POST["b"])
            elif (request.POST["operator"] == "*"):
                vysledok = nas_modul.soucin(request.POST["a"], request.POST["b"])
            else:
                error_msg = "Něco se pokazilo :("
                return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledok=vysledok))
    return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledok=vysledok))
