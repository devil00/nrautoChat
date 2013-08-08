from django.conf.urls import patterns, include, url
from nrAutoChat import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nrAutoChat.views.home', name='home'),
    # url(r'^nrAutoChat/', include('nrAutoChat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$',views.index),
    url(r'^searching$',views.process_message),
)
