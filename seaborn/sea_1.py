# seaborn library
# https://github.com/mwaskom/seaborn
# https://seaborn.pydata.org/

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pathlib


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
    print(tips.head())

    # g = sns.PairGrid(iris)
    # g.map_diag(sns.displot)
    # g.map_upper(plt.scatter)
    # g.map_lower(sns.kdeplot)

    g = sns.FacetGrid(
        data=tips,
        col='time',
        row='smoker'
    )
    # g.map(
    #     sns.distplot,
    #     'total_bill')

    g.map(
        sns.scatterplot,
        'total_bill',
        'tip',
    )


def regression():
    # print(tips.head())
    # sns.lmplot(
    #     x='total_bill',
    #     y='tip',
    #     data=tips,
    #     hue='sex',
    #     markers=['^', 'v']
    # ).fig.suptitle('.lmplot ')

    f = sns.lmplot(
        x='total_bill',
        y='tip',
        data=tips,
        col='sex'
    )
    f.fig.suptitle('.lmplot ')

    # create and save the plot data as file
    pathtofile = str(pathlib.Path(
        __file__).parent.absolute()) + "/images/"
    f.savefig(pathtofile + "myfig3.png")

    


if __name__ == '__main__':
    basic()
    # categorical_plots()
    # matrix_plot()
    # grids()
    # regression()

    plt.tight_layout()  # visual
    plt.show()  # print
