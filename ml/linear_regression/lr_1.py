from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import os
if not os.path.exists("ml/linear_regression/images"):
    os.mkdir("ml/linear_regression/images")


def main():
    df = pd.read_csv(
        '/mnt/d/Documents/Code/Mashine_Learning/course_data/11-Linear-Regression/USA_Housing.csv')
    print(df.head())


if __name__ == "__main__":
    main()
    plt.tight_layout()  # visual
    plt.show()  # print
