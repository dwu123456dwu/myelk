import requests
from elasticsearch import Elasticsearch
import json

#connect to ES cluster
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


r = requests.get('http://localhost:9200')
i = 18
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/' + str(i))
    #create and add records to sw index
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i = i + 1
    print(i)

#get id=5
sw5=es.get(index='sw', doc_type='people', id=5)
print(sw5)