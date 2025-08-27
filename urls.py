from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path("login/", views.login_view, name="login_view"),
    path("Logout/", views.logout, name="logout"),
    path('Sign/', views.Signin, name="Signin"),
    path("home/", views.home, name="home"),
    path("Employ_table/", views.Employee_table, name="Employee_table"),
    path('update/<int:id>/', views.Update, name='Update'),
    path("update_details/", views.update_details, name="update_details"),
    path("Delete/<int:id>/", views.Delete, name="Delete"),  
]
