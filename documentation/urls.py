
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('making_queries.urls')),
    path('', include('aggregation.urls'))
]
