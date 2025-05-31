from django.shortcuts import render
from main.models import Prestation

def index(request):
    prestations = Prestation.objects.all()

    return render(request, 'main/index.html', context={"prestations": prestations})
