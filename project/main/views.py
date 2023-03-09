from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm
from .models import Question
# Create your views here.

app_name = 'main'

def home(request):
    questions = Question.objects.all().order_by('-id')

    return render(request, 'main/pages/main.html', context={
        'questions':questions
    })

def ask(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'main/pages/asking_page.html', context={'form': form})
