# 8.7. Альбом
def make_album(author: str, album: str, album_tracks=None):
    album_info = {'author': author, 'album': album}

    if album_tracks is not None:
        album_info['album_tracks'] = album_tracks

    return album_info


print(make_album('автор', 'альбом', 3))
