# seaborn library
import seaborn as sns


def basic():
    tips = sns.load_dataset('tips')
    print(tips.head())  # pandas dataFrame


if __name__ == '__main__':
    basic()
