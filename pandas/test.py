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
    sal = pd.read_csv(file_name)

    print(
        f" sal head : \n {sal.head()}\n" +
        f" sal info : \n {sal.info()}\n"
    )

    print(
        f"What is the average BasePay ? \n" +
        f"\t{sal['BasePay'].mean() }\n"
    )

    print(
        '\nWhat is the highest amount of OvertimePay in the dataset ? \n' +
        f"\t{sal['OvertimePay'].max()} "
    )

    job_title = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
    print(
        "\nWhat is the job title of JOSEPH DRISCOLL ?" +
        "Note: Use all caps, otherwise you may get an\n" +
        "answer that doesn't match up (there is also" +
        "a lowercase Joseph Driscoll) : \n" +
        f"\t{job_title.values[0]} "
    )

    amount = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
    print(
        '\nHow much does JOSEPH DRISCOLL make (including benefits)? \n' +
        # return Series.values -> list
        f"\t{amount.values[0]} "
    )

    name = sal[sal['TotalPayBenefits'] ==
               sal['TotalPayBenefits'].max()].transpose()
    print(
        '\nWhat is the name of highest paid person (including benefits)? \n' +
        f"\t{name} "
    )

    name = sal[sal['TotalPayBenefits'] ==
               sal['TotalPayBenefits'].min()].transpose()
    print(
        #  she is in debt
        '\nWhat is the name of lowest paid person (including benefits)? \n' +
        f"\t{name} "
    )

    amount = sal[
        (sal['Year'] >= 2011) & (sal['Year'] <= 2014)
    ].groupby('Year').mean()['BasePay']
    df = pd.DataFrame(amount)
    print(
        #  she is in debt
        '\nWhat was the average (mean) BasePay of all employees per year? (2011-2014) ? \n' +
        f"\t{df} "
    )


    amount = sal['JobTitle'].unique()
    print(
        #  she is in debt
        '\nHow many unique job titles are there? \n' +
        f"\t{amount} "
    )

    # print(sal.info())


if __name__ == "__main__":
    test()
