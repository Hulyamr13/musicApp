from django.urls import path, include

from musics import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/', include([
        path('create/', views.create_album, name='create_album'),
        path('details/<int:id>/', views.details_album, name='details_album'),
        path('edit/<int:id>/', views.edit_album, name='edit_album'),
        path('delete/<int:id>/', views.delete_album, name='delete_album'),
    ])),
    path('song/', include([
        path('create/', views.create_song, name='create_song'),
        path('play/<int:album_id>/<int:song_id>/', views.play_song, name='play_song'),
        path('serve/<int:album_id>/<int:song_id>/', views.serve_song, name='serve_song'),
    ])),
]
