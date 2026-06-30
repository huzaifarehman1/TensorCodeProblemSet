import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# -----------------------
# Load data
# -----------------------
path = ''
data = pd.read_csv(path)

# -----------------------
# Visualization
# -----------------------
sns.scatterplot(data=data, x='Hours_Charged', y='target')
plt.title("Hours Charged vs Battery Gained")
plt.show()

# -----------------------
# Find saturation point
# -----------------------
maximum_battery = data['target'].max()

max_charge = data[
    data['target'] == maximum_battery
    ]['Hours_Charged'].min()

# -----------------------
# Remove saturation region 
# -----------------------
data['Hours_Charged'] = np.clip(data[['Hours_Charged']],a_min=0,a_max=max_charge)

sns.scatterplot(data=data, x='Hours_Charged', y='target')
plt.title("Hours Charged vs Battery Gained")
plt.show()


# -----------------------
# Linear Regression
# -----------------------
X = data[['Hours_Charged']]
y = data['target']


model = LinearRegression()
model.fit(X, y)

def predict(xx):
    
    xx = np.clip(xx[['Hours_Charged']],a_min=0,a_max=max_charge)
    return model.predict(xx)    

# make prediction and save


test_path = ''
path_to_save_submission = ''

testX = pd.read_csv(test_path)
x = testX[['Hours_Charged']]


guess = predict(x)

dataframe = pd.DataFrame({'target':guess})
dataframe.to_csv(path_to_save_submission)