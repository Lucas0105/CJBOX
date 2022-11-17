from django.urls import path
from . import views

urlpatterns = [
    path('popular/', views.popular)
]
