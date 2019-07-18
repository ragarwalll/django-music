from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),
    # /music/{album_id}
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    re_path(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('logout/', views.UserLogout, name='logout'),

]