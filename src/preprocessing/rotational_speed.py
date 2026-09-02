import numpy as np
def rotational_speed(tachometer):
    n = len(tachometer)
    speed = np.zeros((n))
    current_speed = 0
    last = 0
    prev = 0
    samplerate = 50000
    for i, v in zip(range(n), tachometer):
        if v > 2 and prev < 2:
            current_speed = samplerate/(i - last)
            last = i
        speed[i] = current_speed
        prev = v
    return speed
