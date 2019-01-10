
'''studio URL Configuration

The  list routes URLs to views. For more information please see:
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
'''
from django.conf.urls import include,url

from django.conf import settings

from django.contrib.auth import views as auth_views

from carfinderapp import views as app_views
from carfinderapp.views import api_views as api_views

urlpatterns = [
    # Home
    url(r'^$',           app_views.main, name='home'),

    # Swagger UI
    url(r'^swaggerui/$', app_views.schema_view),

    # REST API
    url(r'^api/snoops/$',                             api_views.SnoopList.as_view(),      name='snoops'),
    url(r'^api/snoops/(?P<pk>[0-9]+)/$',              api_views.SnoopDetail.as_view(),         name='snoop'),


    url(r'^api/cars/$',                             api_views.CarList.as_view(),           name='cars'),
    url(r'^api/cars/(?P<pk>[0-9]+)/$',              api_views.CarDetail.as_view(),         name='car'),

     #url(r'^api/order_items/$',                        app_views.OrderItemList.as_view(),   name='order_items'),


]
