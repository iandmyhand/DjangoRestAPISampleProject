from django.conf.urls import url

from ping.views import IndexViewSet, ExceptionViewSet


urlpatterns = [
    url(regex=r'^$', view=IndexViewSet.as_view(), name='index'),
    url(regex=r'^exception/$', view=ExceptionViewSet.as_view(), name='exception'),
]
