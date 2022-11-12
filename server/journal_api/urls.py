from django.urls import path
from .views.test_view import getRoutes

urlpatterns = [
    path('', getRoutes),
    ]