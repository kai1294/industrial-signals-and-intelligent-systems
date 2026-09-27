import matplotlib.pyplot as plt
import numpy as np

def plot(tachometer, underhang_a, underhang_r, underhang_t, overhang_a, overhang_r, overhang_t, microphone, start, end, title):
    fig, ax = plt.subplots(2,4, layout='constrained')
    ax[0, 0].plot(underhang_a[start:end]); ax[0, 0].set_title("Underhang Axial")
    ax[0, 1].plot(underhang_r[start:end]); ax[0, 1].set_title("Underhang Radial")
    ax[0, 2].plot(underhang_t[start:end]); ax[0, 2].set_title("Underhang Tangential")
    ax[0, 3].plot(tachometer[start:end]); ax[0, 3].set_title("Tachometer")
    ax[1, 0].plot(overhang_a[start:end]); ax[1, 0].set_title("Overhang Axial")
    ax[1, 1].plot(overhang_r[start:end]); ax[1, 1].set_title("Overhang Radial")
    ax[1, 2].plot(overhang_t[start:end]); ax[1, 2].set_title("Overhang Tangential")
    ax[1, 3].plot(microphone[start:end]); ax[1, 3].set_title("Microphone")
    fig.suptitle(title)

    plt.show(block=False)
