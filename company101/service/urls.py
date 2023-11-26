from django.urls import path, re_path
 
from .views import *
 
urlpatterns = [
    path('', index),
    path('service/<int:service_id>/', service),
    # path('about/', about),
    # path('cats/<slug:cat>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]
