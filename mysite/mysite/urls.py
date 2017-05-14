# -*- coding: utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from learn import views as learn_views
from polls import views as polls_views
# from learn import views
from django.conf import settings
from filebrowser.sites import site
import xadmin
# xadmin.autodiscover()
# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = [
    url(r'^$', learn_views.home, name='home'),
    url(r'^add/$', learn_views.add, name='add'),
    url(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name="add2"),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', xadmin.site.urls),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'xadmin/', include(xadmin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
        )
