import time
while True:
    t = time.localtime()
    print('\r%02d:%02d:%02d' % (t.tm_hour, t.tm_min, t.tm_sec), end='')
    time.sleep(1)