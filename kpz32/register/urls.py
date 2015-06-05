from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.comp, name='comp'),
    url(r'^update/$', views.update, name='update'),
]
