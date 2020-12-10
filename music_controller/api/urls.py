from django.urls import path
from .views import main, RoomView

urlpatterns = [
    path('main', main),
    path('roomview', RoomView.as_view()),
]