import catboost
import warnings
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error 
from data_prepr import cleaner, load_data
import numpy as np
warnings.filterwarnings('ignore')


 
model = catboost.CatBoostRegressor()
X = cleaner()
y_0 = load_data()[1][0]
Xt, Xp, y_0t, y_0p = train_test_split(X, y_0)
model.fit(Xt, y_0t)
preds = model.predict(Xp)
print(root_mean_squared_error(y_0p,preds))