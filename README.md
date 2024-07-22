# Retrieval Augmented Generation Demo
`python rag-demo` startet die Anwendung
## installation
`conda env create -f requirements.yml`

## Kommentare zur Implementation
- Ich habe auf weiteres Splitting der PDF verzichtet da der Inhalt sehr kurz ist
- in production würde ich vermutlich einen kommerziellen Parser verwenden (z.B. Azure AI oder Neoo4j) um genauere Quellenangaben machen zu können (Splitting auf Section-level oder feiner)


## Skalierung
Der implementierte Ansatz lässt sich auf große Datenmengen erweitern. Die VectorDB is skalierbar und für sehr große Datenmengen existieren hoch performante DB. Ebenso sieht es beim Retrieval durch semantische Suche aus. Eines der Hauptprobleme besteht darin Fragen zu beantworten, die einen großen Kontext benötigen so wie superlative Fragen oder solche nach allen Jede etc. Um solche Fragen zu beantworten würde ich die gegebenen Dokumente in einen Wissensgraph parsen (z.B. RDF-Graph oder Property Graph). Anschließen können Graphqueries für diese Fragen erstellt werden, die gegen den Graphen evaluieert werden um einen geeigneten kontext zu erhalten. Würde man die bezeichnungen in den Dokumenten in den Relationen des Graphen verwenden erhält man Fakten in der from (XBO 1000 W/HSC OFR, hat_Nennstrom, 50 A). Die Frage 'Gebe mir alle Leuchtmittel mit mindestens 1500W und einer Lebensdauer von mehr als 3000 Stunden?' kann dann durch Folgendes SPARQL-query beantwortet werden 
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
