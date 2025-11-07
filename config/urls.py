from django.contrib import admin
from django.urls import path, include

urlpatter =[
    path('admin/', admin.site.urls),
    path('api/', include('estufa.urls')),
]