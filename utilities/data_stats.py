import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
path = r'/home/huzaifa/Code/TensorCodeProblemSet/MNIST_classifier/Training_Set.csv'

data = pd.read_csv(path)['target']




def stat(data):
    
    print(data.columns)
    
    print(data.info())
    print(data.describe())

def unique(data):
    print(np.unique(data.values))

def info(data):
        print(data.info())
        print(data.describe())

def count(data):
    temp = np.unique(data.values)
    for i in temp:
        count_ = np.count_nonzero([data.values == i])
        print(f'{i} => total {count_} times')
    
count(data)    