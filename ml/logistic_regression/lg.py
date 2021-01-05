from scipy.sparse import data
import sklearn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# create folder and path at current dir ====================
import pathlib
import os

os.chdir(pathlib.Path(
    __file__).parent.absolute())

# create folder for plots
if not os.path.exists('plots'):
    os.makedirs('plots')

path_to_plots = str(pathlib.Path(
    __file__).parent.absolute()) + "/plots/"

# ==========================================================
"""
solving classification problems (yes / no)
"""


def titanic_ds():

    # exploring data ===================================
    train_ds = pd.read_csv(
        str(pathlib.Path(__file__).parent.parent.parent.absolute()) +
        "/course_data/13-Logistic-Regression/titanic_train.csv"
    )

    main_ds = pd.read_csv(
        str(pathlib.Path(__file__).parent.parent.parent.absolute()) +
        "/course_data/13-Logistic-Regression/titanic_test.csv"
    )

    print(train_ds.info())

    # sns_plot = sns.heatmap(
    #     train_ds.isnull(),
    #     yticklabels=False,
    #     cbar=False,
    #     cmap="viridis"
    # )
    # fig = sns_plot.get_figure()
    # fig.savefig(path_to_plots + "heatmap.png")

    # sns.countplot(
    #     x='Survived',
    #     data=train_ds,
    #     hue='Pclass'
    # )

    # sns.displot(train_ds['Age'].dropna(), bins=30, kde=True)

    # sns.displot(train_ds['Fare'], bins=40, kde=True)

    # cleaning data ===================================
    """
    original data set have missing data at age and caabin number
    -> fill age with mean value 
    ->
    """
    def impute_age(col):

        Age = col[0]
        Pclass = col[1]

        mean_1 = 0

        print(mean_1)

        if pd.isnull(Age):
            if Pclass == 1:
                return 37
            elif Pclass == 2:
                return 29
            else:
                return 25
        else:
            return Age

    train_ds['Age'] = train_ds[['Age', 'Pclass']].apply(impute_age, axis=1)

    # sns_plot = sns.heatmap(
    #     train_ds.isnull(),
    #     yticklabels=False,
    #     cbar=False,
    #     cmap="viridis"
    # )


if __name__ == "__main__":

    titanic_ds()
    plt.show()
