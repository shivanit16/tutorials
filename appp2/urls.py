from django.urls import path
from . import views

urlpatterns = [
    path('fa1/', views.cans1 , name='fa1'),
    path('fa2/', views.cans2 , name='fa2'),
    path('fa3/', views.cans3 , name='fa3'),
]
