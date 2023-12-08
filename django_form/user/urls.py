from django.urls import path 
from . import views 
urlpatterns = [ 
    path('', views.formName),
    path('your-name', views.get_name),
    path('thanks', views.thanks),
    path('form-email', views.formMail),
    path('send-email', views.sendMail),
]