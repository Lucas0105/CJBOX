from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('kakao/', views.kakao),
    path('naver/<str:token>/', views.naver),
    path('google/', views.google),
    path('userStatus/', views.userStatus),
    path('follow/', views.follow),
    path('myList/', views.myList),
    path('myList/<str:nickname>/<int:page>/', views.myListShow),
    path('myList/<str:nickname>/', views.myListAll),
    path('reviews/<str:nickname>/<int:page>/', views.review),
    path('<str:nickname>/', views.my_profile),
    path('<str:nickname>/followings/<int:page>/', views.followings),
    path('<str:nickname>/followers/<int:page>/', views.followers),
]
