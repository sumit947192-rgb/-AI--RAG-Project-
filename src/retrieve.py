def get_retrievers(vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k":5})
    return retriever
