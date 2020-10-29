from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows/new', views.new_show),
    path('shows/show', views.create),
    path('shows/view/<tvid>', views.view),
    path('delete/<tvid>', views.deleteshow),
    path('edit/<tvid>', views.editshow),
    path('update/<tvid>', views.updateshow),
]
