def make_album(band_name, album_title, no_tracks=None):
    """Zwraca słownik z nazwą zespołu/artysty i nazwą albumu"""
    response = {'band': band_name, 'album': album_title}
    if no_tracks:
        response['number_of_tracks']  = no_tracks
    return response

band_album = make_album('Pink Floyd', 'Immortal')
print(band_album)
band_album = make_album('Britney Spears', 'Toxic')
print(band_album)
band_album = make_album('Metallica', 'Master of Puppets')
print(band_album)
band_album = make_album("Guns n' Roses ", 'Use Your Illusion I', 16)
print(band_album)
