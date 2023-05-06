# aliens if-else version #1

alien_color = 'zielony'
points = 0

if alien_color == 'zielony':
    points += 5
    print(f'Gracz zarobił {points} za zastrzelenie zielonego obcego.')
else:
    points += 10
print(f'Gracz zarobił w sumie {points} za zastrzelenie obcych.')

# aliens if-else version #2
alien_color = 'czerwony'
alien_points = 0

if alien_color == 'zielony':
    alien_points += 5
    print(f'Gracz zarobił {alien_points} za zastrzelenie zielonego obcego.')
else:
    alien_points += 10
    print(f'Gracz zarobił {alien_points} za zastrzelenie innego obcego.')
print(f'Gracz zarobił w sumie {alien_points} za zastrzelenie obcych.')
