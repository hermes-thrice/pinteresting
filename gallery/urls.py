from django.conf.urls import url
from . import views

app_name = 'gallery'
urlpatterns=[
    url('',views.welcome,name='welcome'),
]
