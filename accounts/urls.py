from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/api/', views.RegisterAPIView.as_view(), name='register_api_view'),
    path('login/api/', TokenObtainPairView.as_view(), name='login_access_api_view'),
    path('login/api/refresh-token/', TokenRefreshView.as_view(), name='')
]
