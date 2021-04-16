from django.urls import path
from . import views

urlpatterns = [
    path('pa1/', views.funs1 , name='pa1'),
    path('pa2/', views.funs2 , name='pa1'),
    path('pa3/', views.funs3 , name='pa1'),
]
