from elasticsearch import Elasticsearch
import json

#connect to ES cluster
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
anum = 45

q = {
     "query": {
        "match": {
            "account_number": 0
        }
     }
}

q["query"]["match"]["account_number"] = anum


ars = es.search(index="bank",doc_type="account", body=q)

#print(ar)
records=ars['hits']['hits']

for r in records :
    print(r['_source']['account_number'])
    print(r['_source']['balance'])




#es.delete_by_query(body=q, doc_type='account', index='bank')