from django.urls import path
from . import views

urlpatterns = [
    path('', views.review),
    path('comment/', views.commentCreate),
    path('<int:review_id>/', views.detail),
    path('<int:movie_id>/review/<int:page>/', views.reviewRead),
]
