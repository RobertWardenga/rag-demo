from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import BasePromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def get_llm() -> BaseLanguageModel:
	return ChatOpenAI(model="gpt-4o-mini")


def get_prompt() -> BasePromptTemplate:
	prompt = ChatPromptTemplate.from_messages([
		("system", "Du bist ein hilfsbereiter Assistent für Frage-Antwort Aufgaben."
		           " Nutze den gegebenen Kontext um die Frage best möglich zu "
		           "beantworten. Wenn du die Antwort nicht kennst antworte einfach"
		           " das du die Antwort nicht kennst und sie nicht aus den "
		           "Informationen hervorgeht. Nutzte maximal drei Sätze und Halte"
		           " die Antwort einfach und konzise.\n\nKontext: {context}"),
		("user", "Frage: {question}")
	])
	return prompt
