from django.urls import path

from making_queries import views


urlpatterns = [
    # path('blogs/', views.blogs_queryset, name='blogs')
    # path('blogs/', views.filter_referencing_fields, name='blogs')
    path('blogs/', views.filter_using_outer_ref_and_sub_query, name='blogs')
]