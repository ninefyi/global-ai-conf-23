from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from bson import json_util

# # Connect to MongoDB
uri='mongodb://localhost:27017'
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.sample_mflix
collection = db.movies

movies = collection.find({},{'title':1, 'plot':1, 'poster':1, 'year':1, 'plot_embedding_azureopenai':1}).limit(1000)

# Export movies to JSON file
with open("movies.json", "w") as file:
    for movie in movies:
        file.write(json.dumps(movie, default=json_util.default))
        file.write("\n")

print("Successfully exported movies to JSON file")