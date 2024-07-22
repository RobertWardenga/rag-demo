from langchain_core.vectorstores import VectorStore
from langchain_core.retrievers import BaseRetriever

def get_retriever(vectorstore: VectorStore) -> BaseRetriever:
	return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})