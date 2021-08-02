import json
import time

from elasticsearch import Elasticsearch


def get_connection():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if not es.ping():
        raise ConnectionError("Cannot connect to local elasticsearch server")
    
    return es


if __name__ == "__main__":
    es = get_connection()

    query = {
        "query": {
            "bool": {
                "must": {
                    "terms": {
                        "ingredients": [
                            "chocolate",
                            "milk"
                        ]
                    }
                },
                "must_not": {
                    "terms": {
                        "ingredients": [
                            "eggs",
                            "egg"
                        ]
                    }
                },
                "should": [
                    {
                        "match": {
                            "title": "white chocolate"
                        }
                    },
                    {
                        "match": {
                            "title": "birthday"
                        }
                    },
                    {
                        "term": {
                            "title": "cake"
                        }
                    }
                ]
            }
        }
    }

    start = time.time()
    result = es.search(index='recipes', body=query, size=5)
    end = time.time()

    print(json.dumps(result, indent=2))
    print(f"Search took {end-start} seconds")
