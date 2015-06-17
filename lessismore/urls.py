from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.db import router
from rest_framework import routers
from api import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'injuries', views.InjuryViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lessismore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
