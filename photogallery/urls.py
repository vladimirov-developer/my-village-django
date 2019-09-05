from django.conf.urls import url
from .views import AlbumListView, PhotoListView


urlpatterns = [
    url(r'^$', AlbumListView.as_view(), name="photogallery_album_list"),
    url(r'^(?P<album_id>\d+)/$', PhotoListView.as_view(), name='photogallery_photo_list'),
]
