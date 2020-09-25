from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('add_course', views.add_course, name="add_course"),
    path('login_view', views.login_view, name="login_view"),
    path('logout_view', views.logout_view, name="logoutview"),
    path('cancel_course', views.cancel_course, name="cancel_course"),
    path('welcome', views.welcome, name="welcome"),


]