import pandas as pd
import os
path= '/home/huzaifa/Code/TensorCodeProblemSet/house_price' # dir path
train = os.path.join(path,'Test_Set.csv')

Testx = os.path.join(path,'X_testset.csv')
Testy = os.path.join(path,'Y_testset.csv')

target = 'target'

data = pd.read_csv(train,index_col=0)
x,y = data.drop(columns=[target]),data[target]

x.to_csv(Testx,index=False)
y.to_csv(Testy,index=False)
