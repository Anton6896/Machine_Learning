# https://plotly.com/python/
# https://github.com/santosjorge/cufflinks

# plotly version is : 4.12.0

import pandas as pd
import numpy as np

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf


def func():
    cf.go_offline()

    df = pd.DataFrame(
        np.random.randn(100, 4),
        columns='A B C D'.split()
    )

    print(df.head())


if __name__ == "__main__":
    func()
