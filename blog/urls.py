from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'), #we're assigning a view called post_list, if someone enters 127.0.0.1:8000 then go to this view 
]