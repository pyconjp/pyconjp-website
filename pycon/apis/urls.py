from django.conf.urls import patterns, url

from .views import api_schedule_list

urlpatterns = patterns("pycon.apis.views",
                       url(r"^([\w\-]+)/list/$", "api_schedule_list"),
                       url(r"^presentation/(\d+)/$", "api_presentation_detail"),

                       #    url(r'^proposals/(?P<proposal_id>[\d]+)/$', views.proposal_detail,
                       #        name='proposal_detail',
                       #    ),
                       #    url(r'^proposals/(?P<proposal_id>[\d]+)/logs/$', views.proposal_irc_logs,
                       #        name='proposal_irc_logs',
                       #    ),
                       )
