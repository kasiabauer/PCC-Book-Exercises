print(f'\n# Example 1')
alien_0 = {'color': 'zielony', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

print(f'\n# Example 2')
new_points = alien_0['points']
print(f'Zdobyłeś {new_points} punktów.')

print(f'\n# Example 3')
alien_0 = {'color': 'zielony', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print(f'\n# Example 4')
alien_1 = {}
alien_1['color'] = 'zielony'
alien_1['points'] = 5
print(alien_1)

print(f'\n# Example 5')
alien_2 = {'color': 'zielony'}
print(f"Obcy ma kolor {alien_2['color']}.")

alien_2['color'] = 'żółty'
print(f"Obcy ma kolor {alien_2['color']}.")

print(f'\n# Example 6')
alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'średnio'}
print(f"Początkowa wartość x-position: {alien_3['x_position']}")

if alien_3['speed'] == 'wolno':
    x_increment = 1
elif alien_3['speed'] == 'średnio':
    x_increment = 2
else:
    x_increment = 3
alien_3['x_position'] = alien_3['x_position'] + x_increment
print(f"Nowa wartość x-position: {alien_3['x_position']}")

alien_3['speed'] = 'szybko'
if alien_3['speed'] == 'wolno':
    x_increment = 1
elif alien_3['speed'] == 'średnio':
    x_increment = 2
else:
    x_increment = 3
alien_3['x_position'] = alien_3['x_position'] + x_increment
print(f"Nowa wartość x-position: {alien_3['x_position']}")

print(f'\n# Example 7')
alien_4 = {'color': 'zielony', 'points': 5}
print(alien_4)
del alien_4['points']
print(alien_4)
