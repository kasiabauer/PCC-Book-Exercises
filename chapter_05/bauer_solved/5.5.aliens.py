# aliens if-else version #2
alien_color = 'żółty'
points = 0

if alien_color == 'zielony':
    points += 5
    print(f'Gracz zarobił {points} za zastrzelenie zielonego obcego.')
elif alien_color == 'żółty':
    points += 10
    print(f'Gracz zarobił {points} za zastrzelenie żółtego obcego.')
elif alien_color == 'czerwony':
    points += 15
    print(f'Gracz zarobił {points} za zastrzelenie czerwonego obcego.')

print(f'Gracz zarobił w sumie {points} za zastrzelenie obcych.')
