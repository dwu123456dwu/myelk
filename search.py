from elasticsearch import Elasticsearch
import json

#connect to ES cluster
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
ars = es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})

#print(ar)
records=ars['hits']['hits']

for r in records :
    print(r['_source']['name'])
    print(r['_source']['gender'])
    print(r['_source']['height'])

ars = es.search(index="sw", body={"query": {"prefix": {"name": "lu"}}})

records=ars['hits']['hits']

for r in records :
    print(r['_source']['name'])
    print(r['_source']['gender'])
    print(r['_source']['height'])

print('another....')
ars=es.search(index="sw", body={"query": {"match_phrase_prefix": {"name" : "lu"}}})

records=ars['hits']['hits']

for r in records :
    print(r['_source']['name'])
    print(r['_source']['gender'])
    print(r['_source']['height'])

#print('fuzzy search.....')
print(ars)
