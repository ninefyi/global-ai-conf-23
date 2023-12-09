from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch

app = FastAPI()

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
    try:
        docs = collection.find({"plot_embedding_azureopenai":{"$exists": "true"}}).limit(50)
        print(docs)
        # vector_search = MongoDBAtlasVectorSearch.from_documents(
        #     docs,
        #     embeddings,
        #     index_name="vector_plot_embedding_azureopenai"  
        # )
        # vector_search = MongoDBAtlasVectorSearch.from_connection_string(
        #     uri,
        #     f"mflix.movies",
        #     embeddings,
        #     index_name="vector_plot_embedding_azureopenai"
        # )
        # results = vector_search.similarity_search_with_score(query=query, k=5)
        # print(results)
        for document in docs:
            print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
        
    except Exception as e:
        print(e)
    return {"results": []}

@app.get("/init")
async def init_embedding():
    # Use LangChain and Azure Open AI for Atlas Search
    for doc in collection.find({'plot':{"$exists": True}, 'plot_embedding_azureopenai':{"$exists": False}}):
        doc['plot_embedding_azureopenai'] = generate_embedding(doc['plot'])
        collection.replace_one({'_id': doc['_id']}, doc)
    # Your code here
    print("Embedding generated!")
    return {"msg": "generated!"}