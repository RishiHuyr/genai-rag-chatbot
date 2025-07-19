import streamlit as st
from rag_pipeline import load_documents, chunk_documents, build_vector_db, retrieve_relevant_chunks, generate_answer
from sentence_transformers import SentenceTransformer

st.title("GenAI RAG Chatbot")

@st.cache_resource
def get_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_resource
def get_vector_db():
    documents = load_documents()
    chunks = chunk_documents(documents)
    embedding_model = get_embedding_model()
    return build_vector_db(chunks, embedding_model)

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("You:")

if user_input:
    st.session_state['chat_history'].append(("user", user_input))
    embedding_model = get_embedding_model()
    vector_db = get_vector_db()
    relevant_chunks = retrieve_relevant_chunks(user_input, vector_db, embedding_model)
    answer = generate_answer(user_input, relevant_chunks)
    st.session_state['chat_history'].append(("bot", answer))

for sender, message in st.session_state['chat_history']:
    if sender == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}") 