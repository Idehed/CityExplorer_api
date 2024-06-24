from django.urls import path
from guides import views

urlpatterns = [
    path('guides/', views.GuideList.as_view()),
    path('guides/<int:pk>/', views.GuideDetail.as_view()),
]