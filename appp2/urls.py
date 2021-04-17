from django.urls import path
from . import views

urlpatterns = [
    path('fa1/', views.cans1 , name='fa1'),
]
