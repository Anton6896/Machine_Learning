import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix


# create folder and path at current dir ====================
import pathlib
import os

os.chdir(pathlib.Path(
    __file__).parent.absolute())

# create folder for plots
if not os.path.exists('plots'):
    os.makedirs('plots')

path_to_plots = str(pathlib.Path(
    __file__).parent.absolute()) + "/plots/"

# ==========================================================

"""
solving classification problems (yes / no)
"""


def titanic_ds():

    # * exploring data =================================================
    train_ds = pd.read_csv(
        str(pathlib.Path(__file__).parent.parent.parent.absolute()) +
        "/course_data/13-Logistic-Regression/titanic_train.csv"
    )

    print(
        f"\nbefore addin : -------------------------------------------------------- \n{train_ds.head()} ")

    main_ds = pd.read_csv(
        str(pathlib.Path(__file__).parent.parent.parent.absolute()) +
        "/course_data/13-Logistic-Regression/titanic_test.csv"
    )

    # print(train_ds.info())

    # sns_plot = sns.heatmap(
    #     train_ds.isnull(),  # search visual for NaN
    #     yticklabels=False,
    #     cbar=False,
    #     cmap="viridis"
    # )
    # fig = sns_plot.get_figure()
    # fig.savefig(path_to_plots + "heatmap.png")

    # sns.countplot(
    #     x='Survived',
    #     data=train_ds,
    #     hue='Pclass'
    # )

    # sns.displot(train_ds['Age'].dropna(), bins=30, kde=True)

    # sns.displot(train_ds['Fare'], bins=40, kde=True)

    # * cleaning data (prepare for calculations) ===================================
    """
    original data set have missing data at age and caabin number
    -> fill age with mean value for None values in ds 
    -> to match data lose in Cabin column -> drop data 
    """

    mean_1 = int(train_ds[train_ds['Pclass'] == 1]['Age'].mean())
    mean_2 = int(train_ds[train_ds['Pclass'] == 2]['Age'].mean())
    mean_3 = int(train_ds[train_ds['Pclass'] == 3]['Age'].mean())

    def impute_age(col):
        # replace all age that NaN by Pclass with mean of Age in it .
        Age = col[0]
        Pclass = col[1]

        if pd.isnull(Age):
            if Pclass == 1:
                return mean_1
            elif Pclass == 2:
                return mean_2
            elif Pclass == 3:
                return mean_3
        else:
            return Age

    train_ds['Age'] = train_ds[['Age', 'Pclass']].apply(impute_age, axis=1)

    # # crete dummies variable (male=0, female=1)  etc for the calculation use
    sex = pd.get_dummies(train_ds['Sex'], drop_first=True)
    embark = pd.get_dummies(train_ds['Embarked'], drop_first=True)
    p_class = pd.get_dummies(train_ds['Pclass'], drop_first=True, prefix='pcl')

    # axis=1 is ==> add by columns
    train_ds = pd.concat([train_ds, sex, embark, p_class], axis=1)

    train_ds.drop(
        # delete unused columns
        ['Sex', 'Embarked', 'Name', 'Ticket', 'Cabin', 'PassengerId', 'Pclass'],
        axis=1,
        inplace=True
    )
    train_ds.dropna(inplace=True)

    # prepare data for use ( all data is numerical and ready to use in algo )
    print("\nafter data manage : --------------------------------------------------------  \n   ")
    print(train_ds.info())
    print(train_ds.head())

    # sns_plot = sns.heatmap(
    #     train_ds.isnull(),  # see if have an null value ?
    #     yticklabels=False,
    #     cbar=False,
    #     cmap="viridis"
    # )

    # * building logic regression model ===================================

    print('\ntotal data ---------------------------------------------------------- \n')

    # training data set
    X_train, X_test, y_train, y_test = train_test_split(
        train_ds.drop('Survived', axis=1),
        train_ds['Survived'],
        test_size=0.30,
        random_state=101
    )

    lg_model = LogisticRegression(max_iter=1000)
    lg_model.fit(X_train, y_train)
    predict_my = lg_model.predict(X_test)

    # evaluating data  --> https://en.wikipedia.org/wiki/F-score
    print(
        f"classification report : \n{classification_report(y_test, predict_my)}")
    print(f"confusion matrix : \n{confusion_matrix(y_test, predict_my)}")


if __name__ == "__main__":

    titanic_ds()
    plt.show()
