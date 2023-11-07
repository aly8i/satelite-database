
from django.urls import path, include
from django.contrib import admin

from .views import AccountViewset,UserViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('accounts',AccountViewset,basename='accounts')
router.register('users',UserViewset)
urlpatterns = [
    path('api/', include(router.urls)),
    ]
