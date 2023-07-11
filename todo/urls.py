from django.urls import path
from todo.views import TodoAPIView

urlpatterns = [
    path("todo/", TodoAPIView.as_view()),
    path("todo/<int:pk>/", TodoAPIView.as_view()),
]

