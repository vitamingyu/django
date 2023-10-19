"""
URL configuration for djpro02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from myapp import views

# 라우팅이란 ? 화면과 데이터를 요청에 맞게 넘겨주는 컨트롤러 역할을 함.
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index),
    path('hello',views.helloFunc), 
    path('world',views.worldFunc) 
]
