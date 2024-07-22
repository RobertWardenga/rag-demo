# Retrieval Augmented Generation Demo
`python rag-demo` startet die Anwendung
## installation
`conda env create -f requirements.yml`

## Kommentare zur Implementation
- Ich habe auf weiteres Splitting der PDFs verzichtet da der Inhalt sehr kurz ist
- ich habe versucht mit pdf2html parsern eine besser Unterteilung in Abschnitte zu erhalten allerdings sind die Implementationen der PDF-Parser/Loader dafür nicht ausreichend. Als nächsten schritt, würde ich einen custom PDF parser/loader implementieren der Auf mit `PyMuPDF` html dateien aus den Seiten gewinnt (siehe [sample.html](data/sample.html)) und Chunks von diesen Seiten auf Basis von Formatierungen erstellt
- im Deployment würde ich einen kommerziellen Parser verwenden (z.B. Azure AI oder Neoo4j) um genauere Quellenangaben machen zu können (Splitting auf Section-level oder feiner)


## Skalierung
Der implementierte Ansatz lässt sich auf große Datenmengen erweitern. Die VectorDB is skalierbar und für sehr große Datenmengen existieren hoch performante DB. Ebenso sieht es beim Retrieval durch semantische Suche aus. Eines der Hauptprobleme besteht darin Fragen zu beantworten, die einen großen Kontext benötigen so wie superlative Fragen oder solche nach allen Jede etc. Um solche Fragen zu beantworten würde ich die gegebenen Dokumente in einen Wissensgraph parsen (z.B. RDF-Graph oder Property Graph). Anschließen können Graphqueries für diese Fragen erstellt werden, die gegen den Graphen evaluieert werden um einen geeigneten kontext zu erhalten. Würde man die bezeichnungen in den Dokumenten in den Relationen des Graphen verwenden erhält man Fakten in der from (XBO 1000 W/HSC OFR, hat_Nennstrom, 50 A). Die Frage 'Gebe mir alle Leuchtmittel mit mindestens 1500W und einer Lebensdauer von mehr als 3000 Stunden?' kann dann durch Folgendes SPARQL-Query beantwortet und als context von einem LLM verbalisiert werden. 
````
SELECT DISTINCT ?leuchte 
WHERE{
    ?leuchte hat_Nennleistung ?leistung,
             hat_Lebensdauer ?Lebensdauer.
    FILTER(?lebensdauer>3000 && ?Leistung>1500W)
}
````
(in Langchain gibt es mehrere Chains für diese Anwendung)

## Verifizierung
Eine Möglichkeit die Generationen von RAG systemen zu bewerten ist die Nutzung von AI Feedback oder die generierung von Test Datensätzen (durch starke LLMs). Zur erzeugung von RAG Testdatensätzen kann ein LLM aus einem gegebenen Dokument oder Abschnitt in the Datenbasis Fragen und dazugehörige Antworten generieren. Um das RAG System zu evaluieren werden die Fragen aus dem Testdatensatz übergeben, anschließend die gegebenen Antworten mit der Referenzantwort verglichen (z.B. mit BERTScore oder BARTScore) sowie die Retrieval-Accuracy berechnet. Die gegebenen Antworten direkt durch ein LLM zu bewerten wurde z.B. in [RAGAS](https://docs.ragas.io/en/stable/index.html) ([Artikel](https://arxiv.org/pdf/2309.15217)) implementiert. Ein LLM wird dabei geprompted verschiedene Aspekte von RAG-Antworten und Kontext-Retrieval zu bewerten - z.B. Faktenbasiertheit, Relevanz etc. RAGAS hat eine Integration in Langchain und ließe sich auf Deutsch (oder andere Sprachen) verallgemeinern.

Wenn es um konkrete Zahlen geht, sieht die Evaluierung schwieriger aus, wenn die generierte Antwort nicht lediglich die gesuchte Zahl ist. Mithilfe von QueryLanguages und strukturieten Daten (extrahiert aus den PDFS) lassen sich genaue Antworten erzeugen hier hängt die Qualität der Antwort von der Erstellung der DB aus PDFs ab, welche auch Fehleranfällig ist. Zudem ist die generierung der Queries (noch) ein fehleranfälliger Prozess. Ich würde mich über weitere Einblicke in der Verifizierung sehr freuen.
