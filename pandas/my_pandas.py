from os import write
import pandas as pd
import numpy as np
from numpy.random import randn

import pathlib


def series():
    # basic of pandas series

    labels = ['a', 'b', 'c']
    my_data = [10, 20, 30]
    arr = np.array(my_data)
    d = {
        'a': 10, 'b': 20, 'c': 30
    }
    print(f'pandas basic series : \n{pd.Series(my_data)}')
    print(type(my_data))
    print(
        # you dont need to specify the data and index
        # pd.Series(my_data, labels)
        f'\npandas series vs labels : \n{pd.Series(data=my_data, index=labels)}\n')

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


def group_by_df():
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


def merge_join_df():
    # pd.concat([df1, df2])
    # pd.merge(left, right, how='inner', on='key')
    # left.join(right, how='outer')

    df1 = pd.DataFrame(
        {
            'A': ['A0', 'A1', 'A2', 'A3'],
            'B': ['B0', 'B1', 'B2', 'B3'],
            'C': ['C0', 'C1', 'C2', 'C3'],
            'D': ['D0', 'D1', 'D2', 'D3']
        },
        index=[0, 1, 2, 3]
    )
    df2 = pd.DataFrame(
        {'A': ['A4', 'A5', 'A6', 'A7'],
         'B': ['B4', 'B5', 'B6', 'B7'],
         'C': ['C4', 'C5', 'C6', 'C7'],
         'D': ['D4', 'D5', 'D6', 'D7']
         },
        index=[4, 5, 6, 7]
    )

    print(pd.concat([df1, df2]))

    # will concat all values via looking for the columns
    print(
        f"concat vs axis 1 : \n {pd.concat([df1, df2], axis=1)} \n "
    )

    left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})

    right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})

    print(
        # can put multiple keys if exist on=['key1', 'key2']
        "merge left and right data on key is same as (join using key) " +
        f" \n {pd.merge(left, right, how='inner', on='key')} \n "
    )

    left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                         'B': ['B0', 'B1', 'B2']},
                        index=['K0', 'K1', 'K2'])

    right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                          'D': ['D0', 'D2', 'D3']},
                         index=['K0', 'K2', 'K3'])

    print(
        # k3 data loss ( didn't exist at left table )
        f"join two different tables : \n {left.join(right)} \n" +
        f" or you can specify the how='outher' (for saving all data mussing=nan): \n{ left.join(right, how='outer')}\n "

    )


def operations():
    # df.head()
    # .unique()
    # .value_counts()
    # .apply()
    # .columns
    # .sort_values(by='col2')
    # .isnull()
    # .pivot_table(values='D', index=['A','B'], columns=['C'])

    df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [
                      444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})

    print(df.head())

    # unicue value
    print(
        f"find unique value :  {df['col2'].unique()} \n" +
        f"how many unique values :  {df['col2'].nunique()} \n" +
        f"how many values apears :  \n{df['col2'].value_counts()} \n "
    )

    df['col4'] = df['col1'].apply(lambda x: x*2)
    print(
        f"apply func : \n{df}"
    )

    print(
        f"{df.columns} \n{df.index}"
    )

    data = {'A': ['north', 'north', 'north', 'west', 'west', 'west'],
            'B': ['ncb', 'ncb', 'teva', 'teva', 'ncb', 'ncb'],
            'C': ['x', 'y', 'x', 'y', 'x', 'y'],
            'D': [12, 31, 22, 35, 45, 11]}

    df = pd.DataFrame(data)
    print(df)
    print(
        # amaziiiinggg
        "pivot data frame , combine new df from existing data that have same values" +
        f"\n {df.pivot_table(values='D', index=['A', 'B'], columns=['C'])} \n"
    )


def file_open(file_name):
    # return list with lists of file data
    # for csv files
    try:
        with open(file_name) as f:
            fdata = f.read().split()
            l = []
            for i in fdata:
                l.append(i.split(','))
            return l

    except FileNotFoundError:
        print('no file found')


def data_io():
    # pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')
    # df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')
    # pd.read_csv(example)
    # df.to_csv(folder + 'file.csv', index=False)

    # file directories
    folder = str(pathlib.Path(
        __file__).parent.parent.absolute()) + '/my_files/'
    example = '/mnt/d/Documents/Code/Mashine_Learning/course_data/03-Python-for-Data-Analysis-Pandas/example'
    Excel_Sample = '/mnt/d/Documents/Code/Mashine_Learning/course_data/03-Python-for-Data-Analysis-Pandas/Excel_Sample.xlsx'
    multi_index_example = '/mnt/d/Documents/Code/Mashine_Learning/course_data/03-Python-for-Data-Analysis-Pandas/multi_index_example'
    html_link = 'http://www.fdic.gov/bank/individual/failed/banklist.html'

    # open csv file add 'e' column and save to another path
    # df = pd.read_csv(example)
    # df['e'] = df['b'].apply(lambda x: x+1)
    # df.to_csv(folder + 'file.csv', index=False)

    # open excel
    # df = pd.read_excel(Excel_Sample, sheet_name='Sheet1')
    # print(df)
    # # wright to exel
    # with pd.ExcelWriter(folder + 'my_excel.xlsx') as writer:
    #     df.to_excel(writer, sheet_name='Sheet1')

    # html reading
    df = pd.read_html(html_link)
    # using the df[0] place of the table ad the data from html source
    print(
        df[0].head()
    )
    # with pd.ExcelWriter(folder + 'htmltoexcel.xlsx') as target:
    #     df[0].to_excel(target, sheet_name='Sheet1')


if __name__ == "__main__":
    series()
    # data_frames()
    # missing_data()
    # group_by_df()
    # merge_join_df()
    # operations()
    # data_io()
