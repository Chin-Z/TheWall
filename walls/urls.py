from django.conf.urls import patterns, include, url
from django.contrib import admin
from walls import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'walls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'webwalls.views.index'),
    url(r'^add', 'webwalls.views.add'),
)

