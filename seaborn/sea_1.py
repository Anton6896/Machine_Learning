# seaborn library
# https://github.com/mwaskom/seaborn
# https://seaborn.pydata.org/

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# if creating the plots in same place
# they will stick to ech other in picture

def basic():
    # pandas dataFrame (as learning data)
    tips = sns.load_dataset('tips')
    print(tips.head())

    sns.distplot(
        tips['total_bill'],
        kde=True,
    ).set_title('.distplot')

    sns.jointplot(
        x='total_bill',
        y='tip',
        data=tips,
        # kind='hex'
    ).fig.suptitle('.jointplot ')

    sns.pairplot(
        tips,
        hue='sex',
        palette='coolwarm'
    ).fig.suptitle('.pairplot')

    sns.rugplot(
        data=tips
    )


def categorical_plots():
    # pandas dataFrame (as learning data)
    tips = sns.load_dataset('tips')
    print(tips.head())

    # sns.barplot(
    #     x='sex',
    #     y='total_bill',
    #     data=tips,
    #     estimator=np.std
    # ).set_title('.barplot')

    # sns.countplot(
    #     x='sex',
    #     data=tips
    # ).set_title('.countplots')

    # sns.boxplot(
    #     x='day',
    #     y='total_bill',
    #     data=tips,
    #     # hue='sex'
    # ).set_title('.boxplot')

    # sns.violinplot(
    #     x='day',
    #     y='total_bill',
    #     data=tips,
    #     hue='sex',
    #     split=True
    # ).set_title('.violinplot')

    # sns.stripplot(
    #     x='day',
    #     y='total_bill',
    #     data=tips,
    #     jitter=True,
    #     hue='sex'
    # ).set_title('.stripplot')

    # sns.swarmplot(
    #     x='day',
    #     y='total_bill',
    #     data=tips,
    #     hue='sex'
    # ).set_title('.swarmplot')

    # this is actually the best way , you just enter kind !
    # this is the general method
    sns.factorplot(
        x='day',
        y='total_bill',
        data=tips,
        kind='bar'
    ).fig.suptitle('.factorplot ')


def matrix_plot():
    # pandas dataFrame (as learning data)
    tips = sns.load_dataset('tips')
    print(tips.head())




if __name__ == '__main__':
    # basic()
    # categorical_plots()
    matrix_plot()
    plt.tight_layout()  # visual
    plt.show()  # print
