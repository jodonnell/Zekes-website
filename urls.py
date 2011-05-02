from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
                           (r'^$', 'zeke.zeke_site.views.index'),
                           (r'^work/$', 'zeke.zeke_site.views.work'),
                           (r'^play/$', 'zeke.zeke_site.views.play'),
                           (r'^contact/$', 'zeke.zeke_site.views.contact'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

                           (r'^admin/', include(admin.site.urls)),
)
