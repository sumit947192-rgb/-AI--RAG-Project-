from src.ingest import load_documents
from src.chunking import chunk_documents
from src.embed_store import store_embeddings
from src.retrieve import get_retrievers
from src.generate import generate_answers

def run():
    docs = load_documents("data/Lifespan_Development.pdf")
    chunks = chunk_documents(docs)
    embedding = store_embeddings(chunks)
    retriever = get_retrievers(embedding)

    query = input("Ask a question:")
    retrieved_docs = retriever.invoke(query)
    answer = generate_answers(query, retrieved_docs)
    print(answer)

if __name__=="__main__":
    run()