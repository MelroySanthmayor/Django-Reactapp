"""shopapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path,include
from rest_framework import routers
from shop_api.views import ListViewSet,UserViewSet,RatingViewSet

router = routers.DefaultRouter()
router.register(r'list',ListViewSet, base_name="list")
router.register(r'user',UserViewSet,base_name="user")
router.register(r'rating'RatingViewSet,base_name="rating")
urlpatterns = [
    re_path(r'api/', include(router.urls)),
    re_path(r'admin/', admin.site.urls),
]
