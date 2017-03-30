from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'base',views.base),
    url(r'inbox',views.inbox),
    url(r'new', views.new, name='new'),
    url(r'show', views.show, name='show')
]
