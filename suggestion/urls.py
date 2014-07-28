from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'suggestion.views.biotools'),
	url(r'^get/(?P<tool_id>\d+)/$', 'suggestion.views.biotool'),
	url(r'^add_biotool/$', 'suggestion.views.add_biotool'),
	url(r'^user_query/$', 'suggestion.views.user_query'),
	url(r'^suggestion/$', 'suggestion.views.suggestion'),
	
)
