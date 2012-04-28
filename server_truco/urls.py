from django.conf.urls.defaults import patterns, include, url
import os
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server_truco.views.home', name='home'),
    # url(r'^server_truco/', include('server_truco.foo.urls')),
    (r'^carga_categorias/$','server_truco.app.views.cargar_categorias'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enasble the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.APPDIR, 'media')}),
)
