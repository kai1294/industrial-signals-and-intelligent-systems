import os
import pathlib
import numpy as np
from preprocessing.rotational_speed import rotational_speed
def main():
    os.chdir(pathlib.Path(__file__).parent.parent.resolve())
    print(os.getcwd())
    file = 'normal/12.288.csv'
    analyze(file)

def analyze(file):
    data = np.loadtxt(f'data/raw/fault-induction-motor-dataset/{file}',delimiter=',', dtype=float)
    tachometer = data[:, 0]
    underhang_a = data[:, 1]
    underhang_r = data[:, 2]
    underhang_t = data[:, 3]
    overhang_a = data[:, 4]
    overhang_r = data[:, 5]
    overhang_t = data[:, 6]
    microphone = data[:, 7]
    print(rotational_speed(tachometer))

if __name__ == '__main__':
    main()
