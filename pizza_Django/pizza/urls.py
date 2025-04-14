from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('', include('pizzashop.urls')),
    path('menu/', include('pizzashop.urls')),
]
