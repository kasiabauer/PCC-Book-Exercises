devices = ['Lenovo', 'MacBook Pro', 'Nintendo Switch', 'PS4', 'iPhone']

print(devices)
devices[0] = 'Oculus Quest'
print(devices)
devices.append('Lenovo')
print(devices)

devices.insert(0, 'Sony WH-1000XM3')
print(devices)
del devices[0]
print(devices)
devices.pop()
print(devices)
removed_device = devices.pop()
print(f'From Devices list removed: {removed_device}\nNow devices list: \n {devices}')


devices.pop(1)
print(devices)

print('=====')
borrowed_device = 'Oculus Quest'
devices.remove(borrowed_device)
print(borrowed_device)
print(devices)

devices.append(borrowed_device)
devices.append('MacBook Pro')
devices.append('iPhone')
devices.append('Sony WH-1000XM3')
print(devices)


devices.sort()
print(devices)
print(sorted(devices, reverse=True))
devices.reverse()
print(devices)
print(len(devices))


