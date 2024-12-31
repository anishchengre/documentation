from django.urls import path

from aggregation import views


urlpatterns = [
    path('cheatsheet/', views.cheat_sheet, name='cheatsheet'),
]