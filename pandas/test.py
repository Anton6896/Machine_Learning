# """
# SF Salaries Exercise
# Welcome to a quick exercise for you to practice your pandas
# skills! We will be using the [SF Salaries Dataset]
# (https://www.kaggle.com/kaggle/sf-salaries) from
# Kaggle! Just follow along and complete the tasks outlined
# in bold below. The tasks will get harder and harder as you
# go along.
# """

import pathlib
import pandas as pd


def test():
    file_name = str(pathlib.Path(
        __file__).parent.parent.absolute()) + '/pandas/Salaries.csv'

    # sal = pd.read_csv(file_name)
    sal = pd.read_csv(file_name)
    print(
        f" sal head : \n {sal.head()}\n" +
        f" sal info : \n {sal.info()}\n"
    )

if __name__ == "__main__":
    test()
