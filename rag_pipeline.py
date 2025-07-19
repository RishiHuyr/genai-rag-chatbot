"""
RAG Pipeline: Chunking, Embedding, Retrieval, Generation
"""

from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ARIZE_API_KEY = os.getenv('ARIZE_API_KEY')

import glob
from sentence_transformers import SentenceTransformer
import numpy as np
from vector_db import VectorDB
import requests
from prompt_engineering import build_prompt

def load_documents(data_dir="data"):
    """
    Load all .txt files from the data directory.
    Returns:
        list of str: List of document texts.
    """
    documents = []
    for file_path in glob.glob(os.path.join(data_dir, "*.txt")):
        with open(file_path, "r", encoding="utf-8") as f:
            documents.append(f.read())
    return documents

def chunk_documents(documents, chunk_size=500, overlap=100):
    """
    Split documents into overlapping chunks.
    Args:
        documents (list of str): List of documents.
        chunk_size (int): Number of characters per chunk.
        overlap (int): Number of overlapping characters between chunks.
    Returns:
        list of str: Chunks.
    """
    chunks = []
    for doc in documents:
        start = 0
        while start < len(doc):
            end = min(start + chunk_size, len(doc))
            chunks.append(doc[start:end])
            if end == len(doc):
                break
            start += chunk_size - overlap
    return chunks

def embed_chunks(chunks, embedding_model):
    """
    Embed each chunk using the provided embedding model.
    Args:
        chunks (list of str): Text chunks.
        embedding_model: Embedding model instance.
    Returns:
        np.ndarray: Embeddings.
    """
    return np.array(embedding_model.encode(chunks, show_progress_bar=True))

def build_vector_db(chunks, embedding_model):
    """
    Build and return a VectorDB instance populated with chunk embeddings.
    Args:
        chunks (list of str): Text chunks.
        embedding_model: Embedding model instance.
    Returns:
        VectorDB: Populated vector database.
    """
    embeddings = embed_chunks(chunks, embedding_model)
    vector_db = VectorDB(embeddings.shape[1])
    vector_db.add(embeddings, chunks)
    return vector_db

def retrieve_relevant_chunks(query, vector_db, embedding_model, top_k=3):
    """
    Retrieve top-k relevant chunks from the vector database for a query.
    Args:
        query (str): User query.
        vector_db: Vector database instance.
        embedding_model: Embedding model instance.
        top_k (int): Number of chunks to retrieve.
    Returns:
        list of str: Relevant chunks.
    """
    query_embedding = np.array(embedding_model.encode([query]))
    return vector_db.search(query_embedding, top_k=top_k)

def call_groq_llama3(prompt, api_key, model="llama3-8b-8192"):
    """
    Call Groq API for Llama 3 completion.
    Args:
        prompt (str): Prompt for the LLM.
        api_key (str): Groq API key.
        model (str): Model name.
    Returns:
        str: LLM response.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 512,
        "temperature": 0.2
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def generate_answer(query, context, llm=None):
    """
    Generate an answer using the LLM, given the query and retrieved context.
    Args:
        query (str): User query.
        context (str): Retrieved context.
        llm: Not used (for compatibility).
    Returns:
        str: Generated answer.
    """
    prompt = build_prompt(query, context)
    return call_groq_llama3(prompt, GROQ_API_KEY) 