from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_framework.routers import DefaultRouter

from customers.views import CustomerViewSet
from events.views import EventViewSet
from contracts.views import ContractViewSet


router = DefaultRouter()

router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'events', EventViewSet, basename='events')
router.register(r'contracts', ContractViewSet, basename='contracts')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path("login/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]
