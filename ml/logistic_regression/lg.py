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

    # cleaning data (prepare for calculations) ===================================
    """
    original data set have missing data at age and caabin number
    -> fill age with mean value for None values in ds 
    -> to match data lose in Cabin column -> drop data 
    """
    def impute_age(col):

        Age = col[0]
        Pclass = col[1]

        mean_1 = int(train_ds[train_ds['Pclass'] == 1]['Age'].mean())
        mean_2 = int(train_ds[train_ds['Pclass'] == 2]['Age'].mean())
        mean_3 = int(train_ds[train_ds['Pclass'] == 3]['Age'].mean())

        if pd.isnull(Age):
            if Pclass == 1:
                return mean_1
            elif Pclass == 2:
                return mean_2
            else:
                return mean_3
        else:
            return Age

    train_ds['Age'] = train_ds[['Age', 'Pclass']].apply(impute_age, axis=1)

    train_ds.drop('Cabin', axis=1, inplace=True)
    # any na value will be dropt (one left after all)
    train_ds.dropna(inplace=True)

    # sns_plot = sns.heatmap(
    #     train_ds.isnull(),
    #     yticklabels=False,
    #     cbar=False,
    #     cmap="viridis"
    # )

    # crete dammy variable (male=0, female=1)
    sex = pd.get_dummies(train_ds['Sex'], drop_first=True)
    embarked = pd.get_dummies(train_ds['Embarked'], drop_first=True)

    train_ds = pd.concat([train_ds, sex, embarked])
    train_ds.drop([
        'Sex', 'Embarked', 'Name', 'Ticket'
    ])

    print(train_ds.info())


    # cleaning data ===================================
if __name__ == "__main__":

    titanic_ds()
    plt.show()
