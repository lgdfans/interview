from django.urls import path

from index import views

urlpatterns = [
    path('createClient/', views.createClient),
    path('setScore/', views.setScore),
    path('getRankList/', views.getRankList),
    path('login/', views.login),
    path('index/', views.index),
    path('logout/', views.logout),
]