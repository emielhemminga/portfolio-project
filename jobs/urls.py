from django.urls import path

import .views

urlpatterns = [
    path('', views.alljobs, name='alljobs'),
]
