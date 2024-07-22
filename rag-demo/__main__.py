import click

from data_store import get_datastore
from retrieval import get_retriever
from llm import get_llm, get_prompt
from chain import get_chain
from dotenv import load_dotenv

@click.command()
def rag_demo():
	load_dotenv(".env")

	vectorstore = get_datastore(persist_dir="data/vectorstore")
	retriever = get_retriever(vectorstore=vectorstore)
	llm = get_llm()
	prompt = get_prompt()
	chain = get_chain(retriever=retriever, llm=llm, prompt=prompt)

	click.echo("Stelle eine Frage:")
	while True:
		question = click.prompt('>', type=str)
		click.echo(question)
		for chunk in chain.stream(question):  # "Wofür kann XBO 1000 W/HSC OFR genutzt werden?"
			print(chunk, end="", flush=True)


if __name__ == "__main__":
	rag_demo()