from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from customers.views import CustomerViewSet


router = DefaultRouter()

router.register(r'customers', CustomerViewSet, basename='customers')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path("login/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]
