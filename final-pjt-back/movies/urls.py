from django.urls import path
from . import views

urlpatterns = [
    path('popular/', views.popular),
    path('newMovie/<int:page>/', views.newMovie),
    path('search/<str:title>/', views.search),
    path('detail/<int:id>/', views.detail),
    path('recommend/', views.recommend),
    path('<str:genre>/<int:page>/', views.genre),
]
