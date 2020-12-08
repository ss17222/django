from django.contrib import admin
from django.urls import path
from mild.views import *
from . import views
urlpatterns = [
    path("", SignUp.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("activate/<int:uid>", Activate.as_view(), name="activate"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("delete/<int:uid>", Delete.as_view(), name="delete"),
    path("edit/<int:uid>", Edit.as_view(), name="edit"),
    path("logout/",Logout.as_view(), name="logout"),
    path("forgot/",views.forgot, name="forgot"),
    path("forgoten/<int:uid>",Forgoten.as_view(), name="forgoten"),


]
