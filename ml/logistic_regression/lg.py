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

    train_ds = pd.read_csv(
        str(pathlib.Path(__file__).parent.parent.parent.absolute()) +
        "/course_data/13-Logistic-Regression/titanic_train.csv"
    )

    main_ds = pd.read_csv(
        str(pathlib.Path(__file__).parent.parent.parent.absolute()) +
        "/course_data/13-Logistic-Regression/titanic_test.csv"
    )

    print(train_ds.head())

    sns.heatmap(
        train_ds.isnull(),
        yticklabels=False,
        cbar=False,
        cmap="viridis"
    )

    


if __name__ == "__main__":

    titanic_ds()
    plt.show()
