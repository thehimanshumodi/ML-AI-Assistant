from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from rank_bm25 import BM25Okapi
import pickle
import numpy as np
import os

# ✅ Load embedding model (must match ingest.py)
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

# ✅ Load FAISS index
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# ✅ Load raw chunks
with open("chunks.pkl", "rb") as f:
    documents = pickle.load(f)

# ✅ Create BM25 index
tokenized_corpus = [doc.page_content.split() for doc in documents]
bm25 = BM25Okapi(tokenized_corpus)


def retrieve_documents(query, k=5):

    # 🔹 Vector Search
    vector_docs = vectorstore.similarity_search(query, k=k)

    # 🔹 BM25 Search
    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)
    top_indices = np.argsort(bm25_scores)[::-1][:k]
    keyword_docs = [documents[i] for i in top_indices]

    # 🔹 Merge & Remove Duplicates
    combined = vector_docs + keyword_docs
    unique_docs = list({doc.page_content: doc for doc in combined}.values())

    return unique_docs[:k]