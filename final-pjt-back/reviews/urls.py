from django.urls import path
from . import views

urlpatterns = [
    path('', views.review),
    path('<int:movie_id>/review/<int:page>/', views.reviewRead),
]
