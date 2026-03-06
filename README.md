# Small RAG app

PDF → split into chunks → create embeddings → store in FAISS → retrieve relevant chunks → send them to an LLM → answer with sources. 

LangChain’s RAG docs describe this pattern, FAISS is for vector similarity search, and Sentence Transformers provide local embedding models.


# Beginner stack

- pypdf or LangChain PDF loader

- sentence-transformers

- faiss-cpu

- langchain

- streamlit for UI

Streamlit’s file uploader supports PDF upload, with a default per-file limit of 200 MB unless reconfigured.


# Install, bash:
```
pip install langchain langchain-community sentence-transformers faiss-cpu pypdf streamlit
```

For a fully local MVP, keep embeddings local with all-MiniLM-L6-v2 and use any local or hosted chat model. Sentence Transformers documents that loading a pretrained model is straightforward with SentenceTransformer(...).


# Release notes
v0.1 - already proves the main idea: upload PDF, index it, retrieve relevant chunks. 
The final step is replacing the displayed prompt with a real LLM call. 
LangChain’s RAG guides use retrieval plus generation as the standard pattern.
