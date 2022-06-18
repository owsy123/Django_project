
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('test123.urls')),
    path('admin/', admin.site.urls),
]
