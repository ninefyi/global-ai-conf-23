# Build Semantic Search Application with Azure OpenAI service and MongoDB Atlas Search

* Global AI Conference 2023
* Stack: Azure App Service, Azure OpenAI, Python, LangChain, MongoDB Atlas Search (Vector Search Feature)

* Reference 1: https://medium.com/microsoftazure/azure-openai-and-langchain-eba69f18f050
* Reference 2: https://techcommunity.microsoft.com/t5/startups-at-microsoft/build-a-chatbot-to-query-your-documentation-using-langchain-and/ba-p/3833134
* Reference 3: https://www.mongodb.com/developer/products/atlas/semantic-search-mongodb-atlas-vector-search/

* Create Atlas Vector Search Index
```js
{
  "name": "vector_plot_embedding_azureopenai",
  "type": "vectorSearch",
  "fields": [
    {
      "type": "vector",
      "path": "plot_embedding_azureopenai",
      "numDimensions": 1536,
      "similarity": "euclidean"
    }
  ]
}
```

* Local/Codespace development

`uvicorn main:app --host 0.0.0.0 --port 8000 --reload`