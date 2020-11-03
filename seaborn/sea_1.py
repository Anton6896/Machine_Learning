# seaborn library
# https://github.com/mwaskom/seaborn
# https://seaborn.pydata.org/

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# if creating the plots in same place
# they will stick to ech other in picture

# pandas dataFrame (as learning data)
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')


def basic():
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
    print(tips.head())
    print(flights.head())

    # get matrix of data
    tips_corr = tips.corr()
    fli_p = flights.pivot_table(
        index='month',
        columns='year',
        values='passengers'
    )

    print(tips_corr)
    # sns.heatmap(
    #     tips_corr,
    #     annot=True,
    #     cmap='coolwarm'
    #
    # ).set_title('.heatmap')

    print(fli_p)
    # sns.heatmap(
    #     fli_p
    # ).set_title('.heatmap')

    sns.clustermap(
        fli_p,
        cmap='coolwarm',
        standard_scale=1
    ).fig.suptitle('.clustermap ')


def grids():
    print(iris.head())




if __name__ == '__main__':
    # basic()
    # categorical_plots()
    # matrix_plot()
    grids()

    plt.tight_layout()  # visual
    plt.show()  # print
