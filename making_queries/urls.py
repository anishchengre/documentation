from django.urls import path

from making_queries import views


urlpatterns = [
    path('blogs/', views.blogs_queryset, name='blogs')
]