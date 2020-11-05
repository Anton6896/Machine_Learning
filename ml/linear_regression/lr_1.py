from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os 


def main():
    # get_data
    pathtofile = str(os.path.abspath(os.getcwd())) + '/course_data/11-Linear-Regression/USA_Housing.csv'
    df = pd.read_csv(pathtofile)
    print(df.info())
    # sns.displot(df['Price'], kde=True)

    # get all columns 
    X = df[df.columns]
    # target variable (want to predict the price)
    y = df['Price']

    # splite data for training train_test_split , alocate 40% fortest size 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)  


    # create and train the model 
    lm = LinearRegression()
    lm.fit(X_train, y_train)


    

if __name__ == "__main__":
    main()
    # plt.tight_layout()  # visual
    # plt.show()  # print
