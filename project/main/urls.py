from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='my_view'),
    path('ask/', views.ask, name='ask'),
]
