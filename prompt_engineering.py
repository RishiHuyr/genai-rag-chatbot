"""
Prompt Engineering for RAG Chatbot
"""

def build_prompt(query, context):
    """
    Build a prompt for the LLM using the user query and retrieved context.
    Args:
        query (str): User query.
        context (str): Retrieved context (string or list of strings).
    Returns:
        str: Prompt for LLM.
    """
    if isinstance(context, list):
        context = "\n".join(context)
    prompt = f"""You are an AI assistant. Use the following context to answer the user's question.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"""
    return prompt 