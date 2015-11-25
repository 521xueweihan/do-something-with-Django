#coding:utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'test_web_app.views.index', name='index'),
    url(r'^home$', 'test_web_app.views.home', name='home'),
    url(r'^add/$', 'test_web_app.views.add', name='add'),
    url(r'^add/(\d+)/(\d+)/$', 'test_web_app.views.add2', name='add2'),
    url(r'^add3/$', 'test_web_app.views.add3', name='add3'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
