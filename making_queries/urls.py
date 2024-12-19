from django.urls import path

from making_queries import views, json_views


urlpatterns = [
    # path('blogs/', views.blogs_queryset, name='blogs')
    # path('blogs/', views.filter_referencing_fields, name='blogs')
    # path('blogs/', views.filter_using_outer_ref_and_sub_query, name='blogs')
    path('blogs/', json_views.using_kt, name='blogs')
]