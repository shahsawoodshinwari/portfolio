from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Message

# Create your views here.
def index(request):
    context = {"title": "Index"}
    return render(request, "myportfolio/index.djt", context)


def portfolio_detail(request):
    context = {"title": "PortFolio Details"}
    return render(request, "myportfolio/portfolio-details.djt", context)


def message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        body = request.POST.get('message')

        if name and email and subject and message:
            Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=body
                )
        return HttpResponseRedirect(reverse('portfolio:index'))
    else:
        return HttpResponseRedirect(reverse('portfolio:index'))
