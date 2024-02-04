import matplotlib.pyplot as plt
import numpy as np
import time

def main():
    record_time = np.empty((100,))
    temp = []
    for i in range(100):
        tic = time.time()
        temp.append(i)
        toc = time.time()
        record_time[i] = toc-tic
        
    plt.plot(record_time)
    plt.show()

if __name__ == "__main__":
    main()

