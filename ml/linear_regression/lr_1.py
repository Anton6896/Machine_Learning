'''
predicting the house price from the USA_Housing.csv data source 
would like to see what is be  ->  'Price' with this data 
['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
 'Avg. Area Number of Bedrooms', 'Area Population', 'Address']





'''


import sklearn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# create folder at current dir
import pathlib
import os

os.chdir(pathlib.Path(
    __file__).parent.absolute())

# create folder for plots
if not os.path.exists('plots'):
    os.makedirs('plots')

path_to_plots = str(pathlib.Path(
    __file__).parent.absolute()) + "/plots/"


class LinearRegMy:

    # function to predict price
    def cre(self):

        df = pd.read_csv(
            str(pathlib.Path(__file__).parent.parent.parent.absolute()) +
            "/course_data/11-Linear-Regression/USA_Housing.csv"
        )

        # print(df.info())
        # sns.displot(df['Price'], kde=True)
        # sns.heatmap(df.corr(), annot=True)

        # see all data
        # print(f'data frame describe :\n{df.describe()}')
        print(f'data frame describe :\n{df.head()}')
        print(f'\ncolumns : {df.columns}')

        # prepear data for calculation
        X = df[
            ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
             'Avg. Area Number of Bedrooms', 'Area Population']
        ]

        y = df['Price']

        # good to look for the object that trying to predict before starting
        # to see that he have normal form
        price_plot = sns.displot(df['Price'], kde=True)
        price_plot.savefig(path_to_plots + "price_plot.png")

        # train
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.4, random_state=101)

        lm = LinearRegression()
        lm.fit(X_train, y_train)

        # with train data
        cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])
        print(f'\nthe coefficient of data : \n{cdf}')
        print(f"interception : {lm.intercept_}")

        # prediction from train data
        predictions = lm.predict(X_test)

        plt.scatter(y_test, predictions)
        plt.savefig(path_to_plots + "USA_Housing_scatter_plot.png")

        sns_plot = sns.displot(y_test-predictions, kde=True)
        sns_plot.savefig(path_to_plots + "USA_Housing_disploy.png")

        print('\nstat data :')
        print(metrics.mean_absolute_error(y_test, predictions))
        print(metrics.mean_squared_error(y_test, predictions))
        print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))

    def my_lin_try(self):
        print('\n Boston data set : ')
        from sklearn.datasets import load_boston

        boston = load_boston()
        # print(boston['DESCR'])
        print(boston.keys())

        data = pd.DataFrame(boston['data'], columns=boston['feature_names'])
        print(data.head())


        


if __name__ == "__main__":
    l = LinearRegMy()

    # l.cre()
    l.my_lin_try()

    # plt.show()
