from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm
# Create your views here.

def home(request):
    return render(request, 'main/pages/main.html')

def ask(request):
    form = QuestionForm()
    return render(request, 'main/pages/asking_page.html', context={'form': form})
