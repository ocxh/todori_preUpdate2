from django.urls import path
from .views import RegisterView, LoginView

#추가
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', RegisterView.as_view()), #회원가입
    path('login/', LoginView.as_view()), #로그인
    
]