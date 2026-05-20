import pandas as pd
import numpy as np
import sys
from scripts.utils import stdgen, stdfilter
from scipy import stats
import warnings

warnings.filterwarnings("ignore")
def load_data(path = 'data/train.csv'):
    data = pd.read_csv(path)
    X = data.drop(['index', 'IC50, mM', 'CC50, mM', 'SI'], axis=1)

    y_0 = pd.DataFrame(data['IC50, mM'])
    y_1 = pd.DataFrame(data['CC50, mM'])
    return X, (y_0, y_1)


def find_consts(X: pd.DataFrame):
    for x in X:
        std = X[x].std()
        if std == np.float64(0.0):
            yield x

def find_noise(X: pd.DataFrame, y_0, y_1):
    for x in X.columns.tolist():
        r1 = abs(stats.spearmanr(X[x], y_0)[0])
        r2 = abs(stats.spearmanr(X[x], y_1)[0])
        if max(r1, r2) < 0.05:
            yield x

def cleaner():
    X, y = load_data()
    noises = stdgen(find_noise(X, y[0], y[1]))
    consts = stdgen(find_consts(X))
    return X.drop(stdfilter(noises + consts), axis=1)


