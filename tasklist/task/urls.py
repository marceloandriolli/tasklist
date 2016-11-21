from django.conf.urls import include, url
#from . import views

urlpatterns = [
    url(r'^$', 'tasklist.task.views.list', name='list'),
    url(r'^criar/$', 'tasklist.task.views.create', name='create'),
    url(r'^editar/(?P<id>\w+)/$', 'tasklist.task.views.edit', name='edit'),
    url(r'^excluir/(?P<id>\w+)/$', 'tasklist.task.views.delete', name='delete'),

]