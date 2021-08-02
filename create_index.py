import json
from elasticsearch import Elasticsearch, helpers
from tqdm import tqdm

# RECIPE1M_FILE = "layer1.json"
RECIPE1M_FILE = "../recipes_with_nutritional_info.json"



def get_connection():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if not es.ping():
        raise ConnectionError("Cannot connect to local elasticsearch server")
    
    return es


if __name__ == "__main__":
    es = get_connection()

    body = {
        "settings": {
            "index": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            }
        },
        "mappings": { # mapping 相當於資料表的結構
            "properties": {
                "id": {
                    "type": "text"
                },
                "title": {
                    "type": "text"
                },
                "ingredients": {
                    "type": "text"
                },
                "instructions": {
                    "type": "text"
                }
            }
        }
    }

    # index 相當於資料庫
    if not es.indices.exists(index="recipes"): 
        result = es.indices.create(index='recipes', ignore=400, body=body)
        print(result)
    
    with open(RECIPE1M_FILE) as jsonfile:
        data = json.load(jsonfile)
    
    actions = []
    for entry in tqdm(data):
        doc = {
            "id": entry["id"],
            "title": entry["title"],
            "ingredients": [ing["text"] for ing in entry["ingredients"]],
            "instructions": [ing["text"] for ing in entry["instructions"]]
        }
        actions.append({
            "_index": "recipes",
            "_op_type": "index",
            "_source": doc
        })
    helpers.bulk(es, actions)
