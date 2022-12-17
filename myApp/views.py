from django.shortcuts import render
from .models import Sitting


def index(request):
    sitting_objects = Sitting.objects.all()
    context = {'sitting_objects': sitting_objects}
    return render(request, 'index.html', context)
