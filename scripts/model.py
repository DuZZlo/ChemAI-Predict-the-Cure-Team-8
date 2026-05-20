import catboost
import warnings
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error 
from scripts.data_prepr import cleaner, load_data
import pandas as pd
from dataclasses import dataclasses
from scripts.feature import hypothesis_1_adme, hypothesis_2_topology, hypothesis_3_electronic
warnings.filterwarnings('ignore')

@dataclasses
class Finetune:
    iterations: list[int]
    depth: list[int]
    lr: list[float]
    models: list
    Xt: pd.DataFrame
    yt: pd.DataFrame
    Xp: pd.DataFrame
    yp: pd.DataFrame
    metric = root_mean_squared_error


    def fit(self):
        for m in self.models:
            
            model = m(self.iterations, self.depth, self.lr)
            model.fit(self.Xt, self.yt)

 
model = catboost.CatBoostRegressor()
X = cleaner()
y_0 = load_data()[1][0]
Xt, Xp, y_0t, y_0p = train_test_split(X, y_0)
model.fit(Xt, y_0t)
preds = model.predict(Xp)
