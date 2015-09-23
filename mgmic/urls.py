__author__ = 'mstacy'
from django.conf.urls import patterns, url
from django.contrib import admin
#from queue.views import Run, Queue, UserTasks, UserResult,FileUploadView
from rest_framework.urlpatterns import format_suffix_patterns
from views import CheckMapFile
# q = QueueTask()
#tasks_url = []

#for task in q.list()['available_tasks']:
#    tasks_url.append(url(r'%s/$' % task, Run.as_view(), name="%s-run" % (task)))
#    #tasks_url.append(url(r'%s/.(api|json|jsonp|xml|yaml)$' % task, Run.as_view(), name="%s-run-format" % (task)))

admin.autodiscover()

urlpatterns = patterns('',
                       #url(r'run/', include(tasks_url)),
                       #url(r'run/$',Run.as_view(),name='run-main'),
                       url(r'check-mapfile/', CheckMapFile.as_view(), name='cmap-main'),
		       #url(r'file-upload/', FileUploadView.as_view(), name='file-upload'),
		       #url(r'file-upload/(?P<filename>[-\w.]+)', FileUploadView.as_view(), name='file-upload'),
                       #url(r'task/(?P<task_id>[-\w]+)/$', UserResult.as_view(), name='queue-task-result'),
                       #url(r'usertasks/$', UserTasks.as_view(), name='queue-user-tasks'),
                       #url(r'^$', Queue.as_view(), name="queue-main"),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'jsonp', 'xml', 'yaml'])
