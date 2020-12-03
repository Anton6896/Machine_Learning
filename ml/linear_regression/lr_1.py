import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

import pathlib
import os

os.chdir(pathlib.Path(
    __file__).parent.absolute())

# create folder for plots
if not os.path.exists('plots'):
    os.makedirs('plots')


def cre():
    df = pd.read_csv(
        str(pathlib.Path(__file__).parent.parent.parent.absolute()) +
        "/course_data/11-Linear-Regression/USA_Housing.csv")

    # print(df.info())
    # sns.displot(df['Price'], kde=True)
    # sns.heatmap(df.corr(), annot=True)

    # see all data
    print(df.columns)

    # prepear data for calculation
    X = df[
        ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
         'Avg. Area Number of Bedrooms', 'Area Population']
    ]

    y = df['Price']

    # train
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=101)

    lm = LinearRegression()
    lm.fit(X_train, y_train)

    cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])
    print(cdf)

    predictions = lm.predict(X_test)

    path_to_plots = str(pathlib.Path(__file__).parent.absolute()) + "/plots/"

    plt.scatter(y_test, predictions)
    plt.savefig(path_to_plots + "USA_Housing_scatter_plot.png")

    sns_plot = sns.displot(y_test-predictions, kde=True)
    sns_plot.savefig(path_to_plots + "USA_Housing_disploy.png")
    # this is sine fo good choice od data
    # y_test is actual data and  - my_prediction  look the same data so we can see gaues bell
    # requerments 

    print(metrics.mean_absolute_error(y_test, predictions))
    print(metrics.mean_squared_error(y_test, predictions))
    print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))


if __name__ == "__main__":
    cre()
    # plt.show()
    
