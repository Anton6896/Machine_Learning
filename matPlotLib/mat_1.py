import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib

'''
https://matplotlib.org/   documentation 
 
'''


def base():
    # function method
    x = np.linspace(0, 5, 11)
    y = x ** 2

    print(
        f"this is x : {x} \nthis is y : {y}"
    )
    # plt.plot(x, y)
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title('my title')

    plt.subplot(1, 2, 1)
    # plt.plot(x, y, 'r')
    plt.subplot(1, 2, 2)
    # plt.plot(y, x, 'b')

    # oop method
    fig = plt.figure()
    # size of fig [0.1, 0.1, 0.8, 0.8]
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    # ,plot() will fill the fig
    axes.plot(x, y)
    axes.set_xlabel('x label')
    axes.set_ylabel('y label')
    axes.set_title('title my ')


if __name__ == '__main__':
    path = str(pathlib.Path(
        __file__).parent.parent.absolute())

    print(f" thi file path :  {path}/matPlotLib/mat_1.py")
    base()
    plt.show()
