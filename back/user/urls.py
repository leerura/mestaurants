from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]