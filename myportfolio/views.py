from django.shortcuts import render

# Create your views here.
def index(request):
    langs = [
        "C Programmer",
        "C++ Programmer",
        "Django Developer",
        "Python Developer",
        "SQL User",
    ]
    context = {"title": "Index", "langs": langs}
    return render(request, "myportfolio/index.djt", context)


def portfolio_detail(request):
    context = {"title": "PortFolio Details"}
    return render(request, "myportfolio/portfolio-details.djt", context)
