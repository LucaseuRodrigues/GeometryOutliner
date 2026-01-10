from django.shortcuts import render
from .forms import CoordinatesModelForm


def index(request):
    form = CoordinatesModelForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)
