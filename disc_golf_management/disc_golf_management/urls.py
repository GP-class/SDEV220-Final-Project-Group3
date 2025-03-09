from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('games/', include('games.urls')),
    path('scores/', include('scores.urls')),
]