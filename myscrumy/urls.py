
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('samuelscrumy/', include('samuelscrumy.urls',namespace="samuelscrumy"))
]
