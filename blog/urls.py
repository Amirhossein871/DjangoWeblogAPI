from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListCreateGenericAPIView.as_view(), name='post_list_create_api'),
    path('<int:pk>/', views.PostDetailGenericAPIView.as_view(), name='post_detail_api'),
]