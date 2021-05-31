import pandas as pd
import numpy as np

#data = np.loadtxt("train_glove300.csv",delimiter=",",unpack=True)
data_train_glove300_read = pd.read_csv('train_glove300.csv', sep=',')
#print(data_train_glove300)
x_train_glove300_raw = data_train_glove300_read['tweet']
x_train_glove300_raw = np.array(x_train_glove300_raw)
#print(x_train_glove300_raw[1])
x_train_glove300 = []
for i in x_train_glove300_raw:
    x_train_glove300.append(np.array(i).item().split(' '))
print(x_train_glove300)