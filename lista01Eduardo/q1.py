import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('class01.csv',)
train_dataset, validation_dataset, *_ = np.split(df, [350])
