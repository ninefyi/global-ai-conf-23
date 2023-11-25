from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    # Your code here
    return {"message": "Hello World"}

@app.get("/search")
async def search(query: str):
    # Use LangChain and Azure Open AI for Atlas Search
    # Your code here
    return {"results": []}

