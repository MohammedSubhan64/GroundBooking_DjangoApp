from django.urls import path
from booking import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
]