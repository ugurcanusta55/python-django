from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    # /home/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/home/<album_id>
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    #/home/album/add/
    url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),

    #/home/album/2/
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),

    #/home/album/add/
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),


]
