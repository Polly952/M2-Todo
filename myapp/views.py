from django.shortcuts import render
from .models import TodoappModel

# Create your views here.
def indexview(request):
    task = TodoappModel.objects.all()
    contex = {
        'task': task
    }
    return render(request, 'index.html',contex)
