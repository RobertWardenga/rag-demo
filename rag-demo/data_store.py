import os.path
from langchain_core.vectorstores import VectorStore
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
def get_datastore(persist_dir: str, recompute_embeddings: bool = False) -> VectorStore:
	if recompute_embeddings or not os.path.exists(os.path.join(persist_dir, "chroma.sqlite3")):
		vectorstore = Chroma.from_documents(documents=pages, embedding=OpenAIEmbeddings(), persist_directory=persist_dir)
	else:
		vectorstore = Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings())
	return vectorstore
