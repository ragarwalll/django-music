from django.urls import path, re_path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/{album_id}
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]