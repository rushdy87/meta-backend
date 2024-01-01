from django.shortcuts import render

# Create your views here.


def index(requist):
    return render(requist, 'index.html', {})
