"""
URL configuration for testproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("python",views.python,name="PYTHON"),
    path("c",views.c,name="C"),
    path("javascript",views.javascript,name="JAVASCRIPT"),
    path("java",views.java,name="JAVA"),
    path("cpp",views.cpp,name="CPP"),
    path("react",views.react,name="REACT"),
    path("node",views.node,name="NODE"),
    path("php",views.php,name="PHP"),
    path("kotlin",views.kotlin,name="KOTLIN"),
    path("flutter",views.flutter,name="FLUTTER"),
    path("forgot-password",views.forgot,name="forgot-password"),
    path("change-password",views.change_password,name="change"),
    path("delete",views.delete,name="delete"),
    path("edit",views.edit,name="edit"),
    path("change_detail",views.change_detail,name="change_detail")
 
]
