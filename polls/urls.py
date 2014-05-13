from django.conf.urls import patterns, url
from polls.pollActions import index, detail, createPoll, createChoice, upVote

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^(?P<poll_id>\d+)/$', detail, name='detail'),
    url(r'^createPoll/$', createPoll, name='createPoll'),
    url(r'^createChoice/(?P<poll_id>\d+)/$', createChoice, name='createChoice'),
    url(r'^upVote/(?P<poll_id>\d+)/(?P<choice_id>\d+)/$', upVote, name='upVote'),
)