from django.contrib import admin
from django.urls import path, include

from ClassRooms import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('iod/', include('iod.urls')),
]
