from django.shortcuts import render

# Create your views here.
from dolls.models import Doll


def index(request):
    dolls = Doll.objects.only('price', 'name').get()
    return render(request, 'index.html', context={'dolls': dolls})
