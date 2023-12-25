from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name="Routes"),
    path("dashboard/", views.get_dashboard_info),
    path("login/", views.UserLogin.as_view()),
]