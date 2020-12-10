from django.urls import path
from .question4 import question2, question3, question4

urlpatterns = [
    path('2', question2),
    path('3', question3),
    path('4', question4),
]