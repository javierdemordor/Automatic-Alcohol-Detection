import json
import os
import pandas as pd
import numpy as np

path = '/home/javier/Documents/Aalto/ASR/Project/ALC'


def extractLabel(data):
    if 'levels' in data:
        if len(data['levels'][0]['items']) == 0:
            return -1
        else:
            for item in data['levels'][0]['items'][0]['labels']:
                if item['name'] == 'alc':
                    return item['value']
    else:
        return None


labelsData = []
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith("json"):
            with open(dirpath + '/' + filename) as f:
                data = json.load(f)
            label = extractLabel(data)
            if label is not None:
                labelsData.append([filename, extractLabel(data)])

df = pd.DataFrame(np.array(labelsData))
df.to_csv('labels.csv')
