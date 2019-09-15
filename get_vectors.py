# File taken, with permission, from https://github.com/skyranakis/HophacksNLP

import json
import requests
import pandas as pd

from config import *

def create_query_line(queries):
    line = '{"queries": ["'
    for i, query in enumerate(queries[:-1]):
        line += query
        line += '", "'
    line += queries[-1]
    line += '"]}'
    return line


train = pd.read_csv(TRAIN_QUERIES_FILE_PATH, sep='\t', header=None)
dev = pd.read_csv(DEV_QUERIES_FILE_PATH, sep='\t', header=None)
eval = pd.read_csv(EVAL_QUERIES_FILE_PATH, sep='\t', header=None)
total = pd.concat([train, dev, eval], axis=0)

total.columns = ['unknown', 'query']
total = total['query']

counter = 0
max_index = total.shape[0]
dataframe = pd.DataFrame()
while counter < max_index:
    if counter % 1000 == 0:
        print('Currently at {} of {}'.format(counter, max_index))
    queries = total.iloc[counter:(counter + 100)].values.tolist()
    counter += 100

    url = "https://api.msturing.org/gen/encode"
    apikey = GEN_ENCODER_API_KEY 
    headers = {'Ocp-Apim-Subscription-Key':apikey}
    params = {'queries':queries}

    r = requests.post(url = url, json = params, headers = headers)
    try:
        data = json.loads(r.json())
        temp = pd.DataFrame(data)
        dataframe = dataframe.append(temp)
    except:
        pass

print('Currently at {} of {}, saving'.format(counter, max_index))

# dataframe['query'] = dataframe['query'].apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x]))
dataframe.to_csv(EMBEDDINGS_CSV_DATA, index=False)