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
sns.scatterplot(data=data, x='Hours_Charged', y='Battery_Gained')
plt.title("Hours Charged vs Battery Gained")
plt.show()

# -----------------------
# Find saturation point
# -----------------------
maximum_battery = data['Battery_Gained'].max()

max_charge = data[
    data['Battery_Gained'] == maximum_battery
    ]['Hours_Charged'].min()

# -----------------------
# Remove saturation region 
# -----------------------
#data['Hours_Charged'] = np.clip(data[['Hours_Charged']],a_min=0,a_max=max_charge)

sns.scatterplot(data=data, x='Hours_Charged', y='Battery_Gained')
plt.title("Hours Charged vs Battery Gained")
plt.show()


# -----------------------
# Linear Regression
# -----------------------
X = data[['Hours_Charged']]
y = data['Battery_Gained']


model = LinearRegression()
model.fit(X, y)

def predict(xx):
    
    #xx = np.clip(xx[['Hours_Charged']],a_min=0,a_max=max_charge)
    return model.predict(xx)    
x = pd.read_csv('/home/huzaifa/Code/tensorcode/ProblemSet/laptop_battery/Test_Set.csv')
xx = x[['Hours_Charged']]
yy = x['Battery_Gained']

g = predict(xx)
print(r2_score(yy,g))