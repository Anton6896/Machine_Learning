# """
# SF Salaries Exercise
# Welcome to a quick exercise for you to practice your pandas
# skills! We will be using the [SF Salaries Dataset]
# (https://www.kaggle.com/kaggle/sf-salaries) from
# Kaggle! Just follow along and complete the tasks outlined
# in bold below. The tasks will get harder and harder as you
# go along.
# """

from os import truncate
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

    amount = len(
        sal['JobTitle'].unique()
    )
    print(
        #  she is in debt
        '\nHow many unique job titles are there? \n' +
        f"\t{amount} "
    )

    top_jobs = sal['JobTitle'].value_counts()[:5]
    print(
        '\nWhat are the top 5 most common jobs? \n' +
        f"{top_jobs} "
    )

    amount = len(
        sal[(sal['Year'] == 2013)][['Year', 'JobTitle']].value_counts()[
            sal[(sal['Year'] == 2013)][['Year', 'JobTitle']].value_counts() == 1
        ]
    )
    print(

        "\nHow many Job Titles were represented by only one person in 2013?\n" +
        "(e.g. Job Titles with only one occurence in 2013?) \n" +
        f"\t{amount} "
    )

    def name_check(name):
        # return true if name have Chief in it
        substring = "Chief"
        if substring in name:
            return True
        return False

    amount = len(sal[list(map(name_check, sal['JobTitle'].values))])
    print(
        # ! check this answear
        "\nHow many people have the word Chief in their job title?\n" +
        f"\t{amount}"
    )

    sal['title_len'] = sal['JobTitle'].apply(lambda x: float(len(x)))
    sal['TotalPayBenefits'] = sal['TotalPayBenefits'].apply(lambda x: float(x))
    sal.fillna(int(0))
    corelation = sal[['title_len', 'TotalPayBenefits']]
    print(

        "\nIs there a correlation between length of the Job Title string and Salary?\n" +
        f"\t{corelation.corr(method ='pearson')}"
    )


if __name__ == "__main__":
    test()
