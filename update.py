from elasticsearch import Elasticsearch
import json

#connect to ES cluster
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
ars = es.search(index="bank",doc_type="account", body={"query": {"match": {'account_number':25}}})

#print(ar)
records=ars['hits']['hits']

for r in records :
    print(r['_source']['account_number'])
    print(r['_source']['balance'])


q = {
     "script": {
        "inline": "ctx._source.balance=660;ctx._source.age=42",
        "lang": "painless"
     },
     "query": {
        "match": {
            "account_number": 25
        }
     }
}

es.update_by_query(body=q, doc_type='account', index='bank')