from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^updatecombo/(?P<id>\d+)?$', 'genericdropdown.views.updateCombo', name='updatecombo'),
)
