import pandas as pd
def get_data(pred,y):
    data = pd.read_csv(pred)['target']
    y = pd.read_csv(y)['target']
    return data,y

def evaluation_score(metric, min_score, max_score, pred, y):
    from sklearn import metrics

    metric_fn = getattr(metrics, metric)

    score = metric_fn(y, pred)   # y_true first, predictions second
    score2 = (score - min_score) / (max_score - min_score)

    return round(score, 4), (round(score2, 4))*100
path_guess = '/home/huzaifa/Code/TensorCodeProblemSet/submission.csv'
path_y = '/home/huzaifa/Code/TensorCodeProblemSet/Space_balls_2/Y_testset.csv'
data,y = get_data(path_guess,path_y)
metric = 'adjusted_rand_score'
min = 0
max = 1
print(evaluation_score(metric,max_score=max,min_score=min,pred=data,y=y))

