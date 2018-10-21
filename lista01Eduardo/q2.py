import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import operator

def euclideanDistance(row1, row2):
    # Ignore target
    return np.linalg.norm(row1[:-1] - row2[:-1])


def getNeighbors(trainingSet, instance, k):
    ts = trainingSet.copy()
    ts['distance'] = np.inf

    for i in range(len(trainingSet)):
        ts.loc[i, 'distance'] = euclideanDistance(instance, trainingSet.iloc[i])

    ts = ts.sort_values(by=['distance'])
    return ts.iloc[:k,:]

def getResponse(neighbors):
    return neighbors['target'].value_counts().index[0]

KFOLD = 10

df = pd.read_csv('class02.csv')

step = len(df)//KFOLD

train_dataset = df.iloc[0:step, :]
validation_dataset = df.iloc[step:, :]

errors = 0
for index, row in validation_dataset.iterrows():
    neighbors = getNeighbors(train_dataset, row, 10)
    response = getResponse(neighbors)
    if (response != row['target']):
        print('Erro! {} | {}'.format(response, row['target']))
        errors += 1

print("Errors:", errors)
print("Accuracy: {:.2f}%".format((1 - errors/len(validation_dataset)) * 100))
