from ast import List
from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv(dotenv_path=".env.test")

uri = os.getenv("MONGODB_URI") 

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.sample_mflix
collection = db.movies

embeddings = AzureOpenAIEmbeddings(
    azure_deployment="td2",
    model="text-embedding-ada-002",
    disallowed_special=(),
)

def generate_embedding(text):
    return embeddings.embed_query(text)

@app.get("/")
async def root():
    # Your code here
    try:
        client.admin.command('ping')
        print("MongoDB is connected!")
    except Exception as e:
        print(e)
    return {"msg": "I am ready!"}

@app.get("/search")
async def search(query: str):
    # Your code here
    results = []
    try:
        vectorSearch = {
                '$vectorSearch': {
                    'index': 'vector_index', 
                    'path': 'plot_embedding_azureopenai', 
                    'queryVector': generate_embedding(query),
                    'numCandidates': 150, 
                    'limit': 10
                }
        }
        project = {
                '$project': {
                    '_id': 0,
                    'title': 1, 
                    'plot': 1, 
                    'year': 1, 
                    'poster':1,
                    'score': {
                        '$meta': 'vectorSearchScore'
                    }
                }
            }
        pipeline = [vectorSearch, project]
        docs = collection.aggregate(pipeline)
        for document in docs:
            results.append(document)
        
    except Exception as e:
        print(e)
    return {"results": results}

@app.get("/init")
async def init_embedding():
    # Use LangChain and Azure Open AI for Atlas Search
    for doc in collection.find({'plot':{"$exists": True}, 'plot_embedding_azureopenai':{"$exists": False}}):
        doc['plot_embedding_azureopenai'] = generate_embedding(doc['plot'])
        collection.replace_one({'_id': doc['_id']}, doc)
    # Your code here
    print("Embedding generated!")
    return {"msg": "generated!"}