from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from team import views


urlpatterns = [
    url('team/$', views.TeamList.as_view(), name='team-create'),
    url('team/(?P<pk>[0-9]+)/$', views.TeamDetails.as_view(), name='team-details')
   ]