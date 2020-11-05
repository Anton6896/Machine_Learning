from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pathlib
import os 


def main():
    # get_data
    pathtofile = str(os.path.abspath(os.getcwd())) + '/course_data/11-Linear-Regression/USA_Housing.csv'
    df = pd.read_csv(pathtofile)
    print(df.info())
    sns.displot(df['Price'], kde=True)

    

if __name__ == "__main__":
    main()
    plt.tight_layout()  # visual
    plt.show()  # print
