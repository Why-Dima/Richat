from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('create-session/<pk>/', views.CeckoutSessionView.as_view(), name='create-session'),   
]