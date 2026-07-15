from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
def store_embeddings(chunks):
    embedding_model = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )

    if os.path.exists("db"):
        print("Loading existing DB...")
        vectordb = Chroma(
            persist_directory="db",
            embedding_function=embedding_model
        )
    else:
        print("Creating new DB...")
        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory="db"
        )
        vectordb.persist()

    return vectordb
