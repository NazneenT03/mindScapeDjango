
from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from mindscape_app.views import UserRegistrationViewSet

# router = DefaultRouter()
# router.register(r'register', UserRegistrationViewSet, basename='register')

urlpatterns = [
    path('', include('mindscape_app.urls')),
    path('admin/', admin.site.urls),
    # Other URL patterns...
]
