from django.urls import path
from . import views

urlpatterns = [
    path('pa1/', views.funs1 , name='pa1'),
]
