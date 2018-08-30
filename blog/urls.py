from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^post/(?P<post_id>[0-9]+)/', views.post_view, name='post')
]