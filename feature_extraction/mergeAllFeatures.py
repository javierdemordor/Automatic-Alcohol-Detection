import os
import pandas as pd

# one time script that merges all feature vectors (separated files) into one single csv

path = '/home/javier/Documents/Aalto/ASR/Project/Features'

listOfDf = []
counter = 0
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.csv'):
            df = pd.read_csv(path + '/' + filename)
            df['name'] = filename
            listOfDf.append(df)
            if counter % 100 == 0:
                print(counter)
                mix = pd.concat(listOfDf)
                listOfDf.clear()
                listOfDf.append(mix)
                mix.to_csv('temp.csv')
            counter += 1
df = pd.concat(listOfDf)
df.to_csv('final.csv')