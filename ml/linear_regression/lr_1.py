'''
predicting the house price from the USA_Housing.csv data source 
would like to see what is be  ->  'Price' with this data 

['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
 'Avg. Area Number of Bedrooms', 'Area Population']

and what is "Root Mean Squared Error" , how far my prediction from test 
'''


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


class LinearPrediction:

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

        # the actually test data minus prediction
        # to see how far the prediction from the actual data
        plt.scatter(y_test, predictions)
        plt.savefig(path_to_plots + "USA_Housing_scatter_plot.png")

        sns_plot = sns.displot(y_test-predictions, kde=True)
        sns_plot.savefig(path_to_plots + "USA_Housing_disploy.png")

        print('\nstat data :')
        print(
            f'Mean absolute error :: {metrics.mean_absolute_error(y_test, predictions)}')
        print(
            f"Mean squared error ::  {metrics.mean_squared_error(y_test, predictions)}")
        print(
            f"Root Mean squared error :: {np.sqrt(metrics.mean_squared_error(y_test, predictions))}")

    def try1(self):
        print('\n Boston data set : ')
        from sklearn.datasets import load_boston

        boston = load_boston()
        # print(boston['DESCR'])
        print(boston.keys())

        print('\nboston df :')
        data = pd.DataFrame(boston['data'], columns=boston['feature_names'])
        print(data.head())

    def try2(self):
        """
        The company is trying to decide whether to focus their 
        efforts on their mobile app experience or their website
        """
        df = pd.read_csv(
            str(pathlib.Path(__file__).parent.parent.parent.absolute()) +
            "/course_data/11-Linear-Regression/Ecommerce_Customers"
        )
        # print(df.head())
        print(f'data frame info :\n{df.info()}')
        # print(f'\ncolumns : {df.columns}')

        X = df[
            [
                'Time on App',
                'Time on Website',
                'Length of Membership'
            ]
        ]

        y = df['Avg. Session Length']

        # create plot and save plot
        sns.jointplot(
            data=df,
            x='Time on Website',
            y='Yearly Amount Spent',
            kind="reg"
        ).savefig(path_to_plots + "time_web_vs_spend.png")

        sns.jointplot(
            data=df,
            x='Time on App',
            y='Yearly Amount Spent',
            kind="reg"
        ).savefig(path_to_plots + "time_app_vs_spend.png")

        sns.jointplot(
            data=df,
            x='Time on App',
            y='Length of Membership',
            kind="hex"
        ).savefig(path_to_plots + "time_app_vs_membership.png")

        data_pairplot = sns.pairplot(
            data=df,
            size=2.5
        ).savefig(path_to_plots + "data_pairplot.png")

        


if __name__ == "__main__":
    l = LinearPrediction()
    # l.cre()
    l.try2()

    # plt.show()
