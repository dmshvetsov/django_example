from django.conf.urls import url
from . import views

app_name = 'contactform'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^messages$', views.create, name = 'messages')
]
