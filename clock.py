import time

def timer():
    for i in range(60):
        print('\r{:2d} seconds'.format(i), end='')
        time.sleep(1)

timer()
