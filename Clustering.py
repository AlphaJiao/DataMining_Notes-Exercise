from sklearn.cluster import KMeans
import numpy as np
import csv
import Orange
import pandas as pd


dataset = pd.read_csv('data.csv')
X = dataset.iloc[:,[1,25]].values
Name = dataset.iloc[:,0]
X1= np.array(X)

'''
for i in range(30):
    X1[i] = X1[i] / np.linalg.norm(X1[i],ord=2)
    
'''  
kmeans = KMeans(init='random', n_clusters=8, max_iter=300, n_init=10,tol=0.0001).fit(X) #Q1 change parameter; Q4 change X->X1
print kmeans.labels_ 
print kmeans.inertia_ #Q1,SSE


for k in range(8): #Q3
    a = []
    for i in range(30):
        if kmeans.labels_[i] == k:
            a.append(Name[i])
    print "cluster",k + 1,":" ,
    print a
