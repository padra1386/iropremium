from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('base.urls')),
    path('accounts/', include('allauth.urls')),
]