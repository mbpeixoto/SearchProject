from elasticsearch import AsyncElasticsearch

es = AsyncElasticsearch(hosts=["http://elasticsearch:9200"])

async def search_content(query: str):
    response = await es.search(
        index="contents",
        body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "summary", "tags", "author"]
                }
            }
        }
    )
    hits = response["hits"]["hits"]
    results = [{"id": hit["_id"], **hit["_source"]} for hit in hits]
    return results
