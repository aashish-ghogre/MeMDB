from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from games import views


urlpatterns = [
    url('games/$', views.GameList.as_view(), name='game-list'),
    url('games/(?P<pk>[0-9]+)/$',views.GameDetails.as_view(),name='game-details')
   ]