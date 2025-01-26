from django.urls import re_path
from .views import updateCombo

urlpatterns = [
    re_path(r'^updatecombo/(?P<id>\d+)?$', updateCombo, name='updatecombo'),
]
