from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.home, name='home'),
    path('ask/', views.ask, name='ask'),
    path('question/<int:id>', views.question, name='question')
]
