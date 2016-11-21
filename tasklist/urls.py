from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'tasklist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^', include('tasklist.core.urls', namespace='core')),
    url(r'^', include('tasklist.task.urls', namespace='task')),
    url(r'^admin/', include(admin.site.urls)),
]
