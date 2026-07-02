import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression

path_train = ''
path_test = ''

data_ = pd.read_csv(path_train)
data = data_.drop(columns = ['target'])
target = data_['target']

model = LogisticRegression(l1_ratio=1,class_weight='balanced',solver='saga',max_iter=1000)
model.fit(data,target)

test = pd.read_csv(path_test)
guess = model.predict_proba(test)[:,1]

pd.DataFrame({'target':guess}).to_csv('submission.csv')



