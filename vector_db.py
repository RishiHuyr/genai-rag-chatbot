"""
Vector Database Management using FAISS
"""
import faiss
import numpy as np

class VectorDB:
    def __init__(self, embedding_dim):
        """
        Initialize FAISS index.
        Args:
            embedding_dim (int): Dimension of embeddings.
        """
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.chunks = []

    def add(self, embeddings, chunks):
        """
        Add embeddings and corresponding chunks to the index.
        Args:
            embeddings (np.ndarray): Embeddings to add.
            chunks (list of str): Corresponding text chunks.
        """
        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding, top_k=3):
        """
        Search for top-k similar chunks.
        Args:
            query_embedding (np.ndarray): Query embedding.
            top_k (int): Number of results to return.
        Returns:
            list of str: Top-k similar chunks.
        """
        D, I = self.index.search(query_embedding, top_k)
        return [self.chunks[i] for i in I[0]] 