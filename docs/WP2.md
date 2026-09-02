# WP2 Documentation

## Preprocessing
### Rotational speed
The tachometer measures the rotation of the shaft and creates a pulse once per rotation. The start of each pulse can be detected by the signal going from <2 to >2 between consecutive samples. By computing the time between the start of consecutive pulses rotational speed can be computed. (See docs/Tachometer Signal.png)
Note: Rotational speed is undefined until the first pulse is detected, and might be inaccurate until the second pulse depending on the initial phase of the signal.
