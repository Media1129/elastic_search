from datetime import datetime
from elasticsearch import Elasticsearch
from pprint import pprint



es = Elasticsearch()

doc  = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
doc2 = {
    'author': 'jeffery',
    'text': 'new add doc',
    'timestamp': datetime.now()
}


res = es.index(index="test-index", id=1, body=doc)
print("\n\n-----------------------------------------------------------------------")
print(res['result'])  # updated


res = es.get(index="test-index", id=1)
# print(res['_source'])
# {
#     '_id': '1',
#     '_index': 'test-index',
#     '_primary_term': 1,
#     '_seq_no': 8,
#     '_source': {'author': 'kimchy',
#                 'text': 'Elasticsearch: cool. bonsai cool.',
#                 'timestamp': '2021-08-02T10:53:57.357138'},
#     '_type': '_doc',
#     '_version': 9,
#     'found': True
# }



res = es.indices.refresh(index="test-index")


res = es.search(index="test-index", body={"query": {"match_all": {}}})
# pprint(res)
# {
#     '_shards': {'failed': 0, 'skipped': 0, 'successful': 1, 'total': 1},
#     'hits': {'hits': [{'_id': '1',
#                         '_index': 'test-index',
#                         '_score': 1.0,
#                         '_source': {'author': 'kimchy',
#                                     'text': 'Elasticsearch: cool. bonsai cool.',
#                                     'timestamp': '2021-08-02T11:02:12.514909'},
#                         '_type': '_doc'}],
#             'max_score': 1.0,
#             'total': {'relation': 'eq', 'value': 1}},
#     'timed_out': False,
#     'took': 1
# }



print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
