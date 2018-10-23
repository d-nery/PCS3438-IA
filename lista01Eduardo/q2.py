import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import operator

from scipy.spatial.distance import cdist

KFOLD = 10


def euclideanDistance(row1, row2):
    # Ignore target column (last)
    return np.sqrt(np.sum((row1[:-1] - row2[:-1])**2))


def getNeighbors(training_set, instance, k):
    ts = training_set.copy()

    # Calcula a distancia euclidiana entre a instancia e todos
    # os pontos do treino e os ordena, retornando as K menores
    # distancias
    ts['distance'] = np.linalg.norm(ts.sub(instance), axis=1)
    ts = ts.sort_values(by=['distance'])
    return ts[:k].copy()


def getResponse(neighbors):
    # Retorna a classe majoritária da vizinhança
    return neighbors['target'].value_counts().index[0]


def main():
    df = pd.read_csv('class02.csv')

    step = len(df)//KFOLD
    accuracies = []

    for current in np.arange(0, len(df), step):
        validation_dataset = df[current:current+step].copy()
        train_dataset = pd.concat([df[0:current], df[current+step:]])

        errors = 0
        for _, row in validation_dataset.iterrows():
            neighbors = getNeighbors(train_dataset, row, 10)
            response = getResponse(neighbors)
            if (response != row['target']):
                errors += 1

        accuracy = (1 - errors/len(validation_dataset)) * 100
        accuracies.append(accuracy)

        print("Errors:", errors)
        print("Accuracy: {:.2f}%".format(accuracy))

    print("Average Accuracy: {:.2f}%".format(np.mean(accuracies)))

if __name__ == "__main__":
    main()
