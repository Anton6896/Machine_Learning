import pandas as pd
import numpy as np
from numpy.random import randn


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


def data_frames():
    # working with data frames this is the main of pandas
    # pd.DataFrame()
    # df.drop(axis=1, inplace=True)
    # df.loc , df.iloc
    # df.reset_index
    # df.set_index

    np.random.seed(101)
    print("---------- selection from df\n")
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

    # drop column axis=1, inplace=True
    df.drop('c', axis=1, inplace=True)
    print(f"drop column c: \n{df}")
    # drop column
    df.drop('e', inplace=True)
    print(f"drop row e : \n{df}")

    # select rows in df
    print(
        f"loc['a'] will return series of row a :\n{df.loc['a']}\n " +
        f"iloc[0] select by index , same series :\n{df.iloc[0]}\n"
    )

    # select the stack of data
    print(
        f"get the xyz from b : \n{df.loc['b', ['x','y','z']]}\n" +
        f"or same with iloc : \n{df.iloc[1, 1:]} \n"
    )

    # conditional selection and multi selection
    print('\n------------- complex selection from df \n')
    df = pd.DataFrame(
        randn(5, 4),  # data
        ['a', 'b', 'c', 'd', 'e'],  # rows
        ['w', 'x', 'y', 'z']  # column
    )

    bool_df = df > 0
    print(bool_df)

    # look for the data that greater then 0 else nan
    print(
        'look for the data that greater then 0 else nan :  \n' +
        f"{df[bool_df]}\n" +
        f"look for the data from column w where w < 0 : " +
        f"\n{ df[df['w'] < 0]['w'] } \n "
    )
    print(
        " get value that at column b that < -0.30" +
        f"\n {df[df['w'] < 0]['w'][df[df['w'] < 0]['w'] < -0.30][0]} \n"
    )
    print(
        # must use and = & , or = | (C leng notation)
        "multiple conditions w<0 & x>1 and show w,x" +
        f"\n{df[(df['w'] < 0) & (df['x'] > 1)][['w','x']]}\n "
    )

    # must commit to make it in place
    df.reset_index(inplace=True)
    print(df)
    df['states'] = 'ca ny wy or co'.split()  # split return list
    print(df)
    # put state as index at the df and delete the index column
    df.set_index('states', inplace=True)
    df.drop('index', axis=1, inplace=True)
    print(df)

    print('\n -----------   multi index :\n ')

    outside = 'g1 g1 g1 g2 g2 g2'.split()
    inside = [1, 2, 3, 1, 2, 3]
    hier_index = list(zip(outside, inside))
    hier_index = pd.MultiIndex.from_tuples(hier_index)
    df = pd.DataFrame(
        randn(6, 2),  # data
        hier_index,  # multi index rows
        ['A', 'B']  # columns
    )
    df.index.names = ['groups', 'num']
    print(df)
    print(
        # don't forget to use loc and iloc
        f"grabing data from multi index from g2 -> 2B: \n{df.loc['g2'].loc[2,'B']}\n"
    )

    # cross section (XS) allow to use multi selection from fiferent groups
    print(
        f"multi selection in groups : \n{df.xs(1,level='num')}\n"
    )


def missing_data():
    # dropna
    # fillna

    print('================= working with nan value ')
    d = {
        'a': [1, 2, np.nan],
        'b': [5, np.nan, np.nan],
        'c': [1, 2, 3]
    }

    df = pd.DataFrame(d)
    print(df)
    # can drop the data with the nan value by df.dropna(axis= 0/1)
    # need to chose the axis rows = 0 , columns = 1
    print(df.dropna(axis=0))
    # argument df.dropna(trash=2)  -> trash is define the number of
    # nan value at data ( at least 2 for drop condition )

    # df.fillna() , for do must select inplace
    print(
        f"fill data to na \n {df.fillna('value!')}\n"
    )

    df['a'].fillna(value=df['a'].mean(), inplace=True)
    print(
        "also good to fill the value from the data it self : \n" +
        f" {df}\n"
    )


def groupby_df():
    # agregation func
    # groupby()
    # describe()
    # transpose()

    data = {
        'company': 'goog goog mfst mfst fb fb'.split(),
        'person': 'sam charly amy canessa carl sarrah'.split(),
        'sales': [200, 120, 340, 124, 350, 124]
    }
    df = pd.DataFrame(data)
    print(df)

    print(
        # groupby return the agregate object so you need to use it for calculation
        "group by company and get mean for sales: \n " +
        f" { df.groupby('company').mean()  } \n "
    )

    print(
        f"great method describe : \n {df.groupby('company').describe()} \n"
    )


if __name__ == "__main__":
    # series()
    # data_frames()
    # missing_data()
    groupby_df()
