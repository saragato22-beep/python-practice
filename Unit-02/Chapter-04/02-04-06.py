light_state = input()

if light_state == 'green':
    print('proceed')
elif light_state == 'yellow':
    print('prepare to stop')
elif light_state == 'red':
    print('stop')
else:
    print('proceed with caution')
