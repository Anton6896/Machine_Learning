import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


if __name__ == "__main__":
    df = pd.read_csv(
        # mac path
        '/Users/ant/Documents/python/ml/course_data/11-Linear-Regression/USA_Housing.csv')
    print(df.info())

    # sns.displot(df['Price'], kde=True)
    # sns.heatmap(df.corr(), annot=True)

    print(df.columns)
    plt.show()  # show picture
