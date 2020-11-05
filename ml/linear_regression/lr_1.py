from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os 
from datetime import datetime



def main():
    start_time = datetime.now()

    # get_data
    pathtofile = str(os.path.abspath(os.getcwd())) + '/course_data/11-Linear-Regression/USA_Housing.csv'
    df = pd.read_csv(pathtofile)
    print(df.info())
    # sns.displot(df['Price'], kde=True)

    # get all columns ( without address )
    X = df[
        ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']
    ]
    # target variable (want to predict the price)
    y = df['Price']

    # splite data for training train_test_split , alocate 40% fortest size 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)  


    # create and train the model 
    lm = LinearRegression()
    lm.fit(X_train, y_train)

    cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])
    print(cdf)
    
    # todo repeat the proces with the real data 
    #  the real data set for testing from boston #################
    # boston = load_boston()
    # # print(boston.keys())
    # boston_df = pd.DataFrame(boston['data'], columns=boston['feature_names'])
    # print(boston_df.head())


    predictions = lm.predict(X_test)

    plt.scatter(y_test, predictions)
   


    end_time = datetime.now()
    print(f'\n\n===================== Duration: {end_time - start_time} ====================')



    


    

if __name__ == "__main__":
    main()
    plt.tight_layout()  # visual
    plt.show()  # print
