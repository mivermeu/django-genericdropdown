from django.conf.urls import url

urlpatterns = [
    url(r'^updatecombo/(?P<id>\d+)?$', 'genericdropdown.views.updateCombo', name='updatecombo'),
]
