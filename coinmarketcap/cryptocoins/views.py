from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cryptocoins.models import Cryptocurrency


def index(request):
    coins = Cryptocurrency.objects.all().order_by('rank')
    return render(request, 'index.html', {
        'coins': coins
    })
