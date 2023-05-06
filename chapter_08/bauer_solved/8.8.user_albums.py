def make_album(band_name, album_title, no_tracks=None):
    """Zwraca słownik z nazwą zespołu/artysty i nazwą albumu"""
    response = {'band': band_name, 'album': album_title}
    if no_tracks:
        response['number_of_tracks']  = no_tracks
    return response

active = True
while active:
    user_band = input(f"Podaj nazwę zespołu/artysty: ")
    user_album = input(f"Podaj nazwę albumu {user_band}: ")
    user_data = make_album(user_band, user_album)
    print(user_data)
    active = False
