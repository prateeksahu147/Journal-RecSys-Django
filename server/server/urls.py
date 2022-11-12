from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('journal-api/', include('journal_api.urls')),
    path('journal/', include('journal_app.urls')),
]
