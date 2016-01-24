from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<contact_id>[0-9]+)/$', views.contact, name='contact'),
    url(r'^$', views.all_contacts, name='all'),
    ]

