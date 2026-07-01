import  pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import seaborn as sns
import matplotlib.pyplot as plt


path_train = r''
path_test = r''

target = 'target'

# load data
training_data = pd.read_csv(path_train) 
testing_data = pd.read_csv(path_test)

# split into X and Y
Xtrain = training_data.drop(columns=[target,'date'])
Ytrain = training_data[target]

# to check wether a feature is usefull or not
sns.heatmap(training_data.drop(columns=['date']).corr(method='spearman'))
plt.show()

# making lag features and rolling mean and rolling standerd deviations as features
col = Xtrain.columns
window = [1,2,3,4,5,6,7,14]
longest = window[-1]
def make_lag_rolling_features(data,window):
    col = data.columns
    for i in col:
        for j in window:
            if j != 1:
                temp = i + '_' + str(j) + '_' + 'mean'        
                data[temp] = data[i].rolling(j).mean()
                
                temp = i + '_' + str(j) + '_' + 'std'        
                data[temp] = data[i].rolling(j).std()
            
            temp =  i + '_' + str(j) + '_' + 'log'
            data[temp] = data[i].shift(j)
    return data

Xtrain = make_lag_rolling_features(Xtrain,window)        
                
Xtrain_new = Xtrain.dropna() # removing nan caused by lag feature creation 
total_trainSample = len(Xtrain_new)
total = len(training_data)

Ytrain = Ytrain.iloc[total-total_trainSample:]# removing nan caused by lag feature creation

Xtrain['date'] = pd.to_datetime(training_data['date'])# including date object

# adding time features as months days etc
for df in [Xtrain]:

    
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["dayofweek"] = df["date"].dt.dayofweek      # Monday=0
    df["dayofyear"] = df["date"].dt.dayofyear
    df["quarter"] = df["date"].dt.quarter
    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12) # periodic year feature
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)# periodic year feature
    df["day_sin"] = np.sin(2*np.pi*df["dayofyear"]/365)#periodic month feature
    df["day_cos"] = np.cos(2*np.pi*df["dayofyear"]/365)#periodic month feature

Xtrain = Xtrain.drop(columns=['date']) # removing the date object

pre = ColumnTransformer([('pre',StandardScaler(),list(Xtrain_new.columns))])
model = Pipeline([('preprocessor',pre),('model',GradientBoostingRegressor(loss='squared_error',
                                                                          learning_rate=0.01,
                                                                          n_estimators=600,
                                                                          verbose=100,
                                                                          n_iter_no_change=3,
                                                                          validation_fraction=0.1,
                                                                          tol=0.001))])

model.fit(Xtrain_new,Ytrain)


#predict
#make features in test data
# combining past features to make lag and rolling features for test data
combined = pd.DataFrame(np.vstack([training_data.drop(columns=[target,'date']).iloc[-longest:],testing_data.drop(columns=['date'])]),columns=col)


combined = make_lag_rolling_features(combined,window)
combined = combined.dropna()# this remove the originally added past features


combined['date'] = pd.to_datetime(testing_data['date'])
for df in [combined]:

    
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["dayofweek"] = df["date"].dt.dayofweek      # Monday=0
    df["dayofyear"] = df["date"].dt.dayofyear
    df["quarter"] = df["date"].dt.quarter
    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)
    df["day_sin"] = np.sin(2*np.pi*df["dayofyear"]/365)
    df["day_cos"] = np.cos(2*np.pi*df["dayofyear"]/365)


prediction = model.predict(combined)

pd.DataFrame({
    "target": prediction
}).to_csv("submission.csv", index=False)



