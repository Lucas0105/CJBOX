from django.urls import path
from . import views

urlpatterns = [
    path('', views.review),
    path('comment/', views.commentCreate),
    path('comment/delete/', views.commentDelete),
    path('<int:review_id>/', views.detail),
    path('<int:review_id>/comment/<int:page>/', views.commentRead),
    path('<int:movie_id>/review/<int:page>/', views.reviewRead),
]
