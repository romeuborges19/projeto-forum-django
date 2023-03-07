from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.

def register(request):
    form = RegisterForm()

    context = {'form': form}
    return render(request, 'authors/pages/register_page.html', context)

