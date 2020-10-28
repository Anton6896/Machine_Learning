import pandas as pd
import numpy as np
from numpy.random import randn, randint


def series():
    # basic of pandas series

    labels = ['a', 'b', 'c']
    my_data = [10, 20, 30]
    arr = np.array(my_data)
    d = {
        'a': 10, 'b': 20, 'c': 30
    }
    print(f'pandas basic series : \n{pd.Series(my_data)}\n')
    print(
        # you dont need to specify the data and index
        # pd.Series(my_data, labels)
        f'pandas series vs labels : \n{pd.Series(data=my_data, index=labels)}\n')

    print(f'pandas series vs dict  : \n{pd.Series(d)}\n')

    ser1 = pd.Series(
        data=np.random.randint(10, 100, 4),
        index=['usa', 'germany', 'ussr', 'chaina']
    )
    ser2 = pd.Series(
        data=np.random.randint(10, 100, 4),
        index=['usa', 'germany', 'Italy', 'chaina']
    )
    print(
        f'will try to join 2 series :\n{ser1}\n{ser2}\n{ser1+ser2}'
    )


# working with data frames this is the main of pandas
def data_frames():
    np.random.seed(101)

    df = pd.DataFrame(
        randn(5, 4),  # data
        ['a', 'b', 'c', 'd', 'e'],  # rows
        ['w', 'x', 'y', 'z']  # column
    )
    print(
        f' data frame is : \n{df}, \n' +
        f"data series from this data frame \n{df['w']}\n" +
        f"can see that the df['w'] is type pf : {type(df['w'])}\n" +
        f"list of columns : \n {df[['w', 'x']]}\n"
    )

    df['c'] = df['w'] + df['x']
    print(
        f" crete new column c by w+x columns  \n{df}"
    )

    # drop column axis = 1
    df.drop('c')
    print(df)


if __name__ == "__main__":
    # series()
    data_frames()
