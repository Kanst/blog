from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.conf import settings
from registration.forms import RegistrationFormUniqueEmail
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),
    url(r'^contact/$', 'blog.views.contact', name='contact'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^blog/[^/]+/$', 'article.views.home', name='home'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markitup/', include('markitup.urls')),
    url(r'^tags/$', 'blog.views.tags'),
    url(r'^tag/(?P<tag>[-_A-Za-z0-9]+)/$','article.views.with_tag'),
    (r'^comments/post/', 'blog.redir.post_comment'),
    (r"^comments/", include("django.contrib.comments.urls")),
    url(r'^register/$', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
    (r'^accounts/', include('registration.urls')),
    #url(r'^tag/(?P<tag>[-_A-Za-z0-9]+)/page/(?P<token>[-\w]+)/$', 'blog.views.with_tag' ),
)

if settings.DEBUG:
	urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
        )