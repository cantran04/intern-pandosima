from django.urls import path 
from . import views 
urlpatterns = [ 
    path('', views.current_datetime),
    path('detail/', views.detail),
    path('day/', views.current_datetime),
]