from pymongo import MongoClient

# Conexão com o MongoDB
mongo_client = MongoClient("mongodb://mongodb:27017")
db = mongo_client["content_db"]
collection = db["contents"]

def get_content_details(content_id: str):
    # Busca o documento no MongoDB
    content = collection.find_one({"_id": content_id})
    if content:
        return {
            "title": content.get("title", ""),
            "details": content.get("details", ""),
            "tags": content.get("tags", []),
            "author": content.get("author", "")
        }
    return {}

