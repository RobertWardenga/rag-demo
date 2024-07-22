from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, Runnable
from langchain_core.retrievers import BaseRetriever
from langchain_core.prompts import BasePromptTemplate
from langchain_core.language_models import BaseLanguageModel

def get_chain(
		retriever: BaseRetriever,
		prompt: BasePromptTemplate,
		llm: BaseLanguageModel,
) -> Runnable:
	def join_docs(docs):
		print("Quellen:")
		for doc in docs:
			print(f"{doc.metadata['file_path']} Seite {doc.metadata['page']}")
		return "\n\n".join(doc.page_content for doc in docs)

	chain = (
	    {"context": retriever | join_docs, "question": RunnablePassthrough()}
	    | prompt
	    | llm
	    | StrOutputParser()
	)

	return chain