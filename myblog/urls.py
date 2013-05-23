from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/' ,views.current_datetime),
    url(r'^myblog/', include('blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
urlpatterns += patterns((''),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': '/home/zsz/myblog/static'}),
)