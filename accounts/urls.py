from django.urls import path
from . import views
urlpatterns = [
    path('login',views.loginPage,name='login'),
    path('register',views.registerPage,name='register'),
    path('user',views.user,name='user'),
    path('logout',views.logoutpage,name='logout')
]