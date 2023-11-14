import fileinput

period, duration = map(int, fileinput.input().readline().split(' '))

initial_rotation = 180 / period * duration

degrees = initial_rotation - (initial_rotation // 360) * 360

up = (degrees >= 0 and degrees < 90) or (degrees > 270 and degrees <= 360)

print('up' if up else 'down')
