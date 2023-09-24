from django.urls import path
from booking import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('cricket',views.cricket,name='cricket'),
    path('football',views.football,name='football'),
]