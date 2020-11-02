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
    # plt.xlabel('x label')
    # plt.ylabel('y label')
    # plt.title('my title')
    #
    # plt.subplot(1, 2, 1)
    # # plt.plot(x, y, 'r')
    # plt.subplot(1, 2, 2)
    # plt.plot(y, x, 'b')

    # oop method
    # fig = plt.figure()
    # # size of fig [0.1, 0.1, 0.8, 0.8]
    # axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    # # .plot() will fill the fig
    # # axes.plot(x, y)
    # axes.set_xlabel('x label')
    # axes.set_ylabel('y label')
    # axes.set_title('title my ')

    # subplot
    fig = plt.figure()
    axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes2 = fig.add_axes([0.57, 0.15, 0.3, 0.2])
    axes1.plot(x, y)
    axes2.plot(y, x)


def adv_1():
    # fig, axes = plt.subplots(nrows=1, ncols=2)
    # fig.savefig('my_fig.png', dpi=200)

    # ax[0].set_title('fig 0')
    # ax[0].set_xlabel('lab x', label='some label')
    # ax[0].set_ylabel('lab y')
    # ax.legend()

    x = np.linspace(0, 5, 11)
    y = x ** 2

    # fig, axes = plt.subplots(nrows=1, ncols=2)
    # for axe in axes:  # axes is an list ( axes[0], axes[1] etc)
    #     axe.plot(x, y)

    # axes[0].set_title('plot 1')
    # axes[1].set_xlabel('x label here')
    # axes[1].set_ylabel('y label here')

    #  ==================    figure size and dpi
    # fig = plt.figure(figsize=(8, 2))
    # ax = fig.add_axes([0, 0, 1, 1])
    # ax.plot(x, y)

    # fig, ax = plt.subplots(figsize=(8, 4), nrows=2, ncols=1)

    # ax[0].plot(x, y)
    # ax[0].set_title('fig 0')
    # ax[0].set_xlabel('lab x')
    # ax[0].set_ylabel('lab y')

    # ax[1].plot(y, x)
    # ax[1].set_title('fig 1')

    # save as file
    # fig.savefig('my_fig.png', dpi=200)

    # add legend
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.plot(x, x**2, label='x**2')
    ax.plot(x, x**3, label='x**3')
    # loc=0 for best location
    ax.legend(loc=0)


def adv_2():
    x = np.linspace(0, 5, 11)
    y = x ** 2

    # customization of the plot (visual)
    


if __name__ == '__main__':
    # base()
    # adv_1()
    adv_2()

    plt.tight_layout()  # visual
    plt.show()  # print
