# """
# Ecommerce Purchases Exercise
# In this Exercise you will be given some Fake Data about
#  some purchases done through Amazon! Just go ahead and
#  follow the directions and try your best to answer the
#  questions and complete the tasks. Feel free to reference
# the solutions. Most of the tasks can be solved in different ways.
# For the most part, the questions get progressively harder.
# Please excuse anything that doesn't make "Real-World" sense
#  in the dataframe, all the data is fake and made-up.
# Also note that all of these questions can be answered with one
# line of code.
#  """

from os import truncate
import pandas as pd
import pathlib

file_name = str(pathlib.Path(
    __file__).parent.parent.absolute()) + '/course_data/04-Pandas-Exercises/Ecommerce_Purchases'
ecom = pd.read_csv(file_name)
ecom.fillna(0, inplace=True)


def my_main():
    print(
        ecom.info()
    )

    amount = ecom['Purchase Price'].mean()
    print(
        '\nWhat is the average Purchase Price? \n' +
        f"{amount} "
    )

    high = ecom['Purchase Price'].max()
    low = ecom['Purchase Price'].min()
    print(
        '\nWhat were the highest and lowest purchase prices? \n' +
        f"lowest : {low} \t highest  : {high}"
    )

    amount = len(ecom[ecom['Language'] == 'en'])
    print(
        "\nHow many people have English 'en' as their Language of choice on the website? \n" +
        f"{amount} "
    )

    amount = len(ecom[ecom['Job'] == 'Lawyer'])
    print(
        "\nHow many people have the job title of Lawyer ? \n" +
        f"{amount} "
    )

    am = len(ecom[ecom['AM or PM'] == 'AM'])
    pm = len(ecom[ecom['AM or PM'] == 'PM'])
    print(
        "\nHow many people made the purchase during the AM and how many people made the purchase during PM ? \n" +
        f"am : {am} \t pm : {pm}"
    )

    amount = ecom['Job'].value_counts()[:5]
    print(
        "\nWhat are the 5 most common Job Titles? \n" +
        f"{amount} "
    )

    amount = ecom[ecom['Lot'] == '90 WT']['Purchase Price']
    print(
        "\nSomeone made a purchase that came from Lot: '90 WT' , what was the Purchase Price for this transaction? \n" +
        f"{amount.values[0]} "
    )

    amount = ecom[ecom['Credit Card'] == 4926535242672853]['Email']
    print(
        "\nWhat is the email of the person with the following Credit Card Number: 4926535242672853 \n" +
        f"{amount.values[0]} "
    )

    amount = len(
        ecom[
            (ecom['CC Provider'] == 'American Express') &
            (ecom['Purchase Price'] > 95)
        ]
    )
    print(
        "\nHow many people have American Express as their Credit Card Provider and made a purchase above $95 ? \n" +
        f"{amount} "
    )

    def year_checker(date):
        """
        check the Exp Date is after or equal 2025 = 25
        """
        d = date.split('/')[1]
        if int(d) >= 25:
            return True
        return False

    amount = len(ecom[ecom['CC Exp Date'].apply(lambda x: year_checker(x))])
    print(
        # ! check the answear !
        "\nHow many people have a credit card that expires in 2025? \n" +
        f"{amount} "
    )

    ecom['provider_'] = ecom['Email'].apply(lambda x: x.split('@')[1])
    top = ecom['provider_'].value_counts()[:5]
    print(

        "\nWhat are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) \n" +
        f"{top} "
    )


if __name__ == "__main__":
    my_main()
