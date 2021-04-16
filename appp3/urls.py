from django.urls import path
from . import views

urlpatterns = [
    path('sa1/', views.tans1 , name='sa1'),
    path('sa2/', views.tans2 , name='sa2'),
    path('sa3/', views.tans3 , name='sa3'),
]
