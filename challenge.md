# Coding Challenge:
Diese Aufgabe gibt uns die Möglichkeit, deine technischen Fähigkeiten und Problemlösungskompetenzen besser einzuschätzen. Hier sind die Details:

## Ziel:
Entwicklung einer Suchlösung auf Basis von PDF-Dokumenten unter Verwendung eines Language Model (LLM).

## Teil 1: Semantische Suche
PDF-Dokumente: Dir werden PDF-Dokumente mit definiertem Inhalt bereitgestellt.
Such-Tool Entwicklung: Erstelle ein Stück Software, in dem du Suchanfragen von Nutzern eingeben kannst. Es reicht dabei, wenn das im Code direkt passiert, es muss keine UI o.ä. entwickelt werden. Es ist ebenfalls kein Interface für das Hochladen oder Auswählen der PDFs nötig, auf diese kann einfach per Dateisystem an fixer Stelle zugegriffen werden.
Semantische Suche: Identifiziere relevante Abschnitte in den PDF-Dokumenten basierend auf den Benutzeranfragen mittels semantischer Suche. Es reicht dabei, wenn die produzierten Daten nur flüchtig vorgehalten werden, es muss nicht zwingend persistiert werden.
Antwort-Generierung: Generiere und präsentiere die Antworten mit Hilfe der Ergebnisse der semantischen Suche und des LLM. Es reicht auch hierbei ein einfacher Output auf stdout o.ä..

## Teil 2: Skalierung
Funktioniert deine Lösung auch für 500 PDFs? Was gibt es bei so vielen PDFs zu beachten? Wo sind bottlenecks oder etwaige Probleme zu erwarten?
Wie würde man es lösen, wenn der Nutzer fragt: ‘Gebe mir alle Leuchtmittel mit mindestens 1500W und einer Lebensdauer von mehr als 3000 Stunden’?

## Teil 3: Verifizierung
Welche Möglichkeiten gibt das Ergebnis zu evaluieren / bewerten, ohne dass das zwangsweise von einem Menschen passiert? Welche Metriken / Möglichkeiten existieren, um die Ausgabe mit der Eingabe zu vergleichen und sicherzustellen, dass die Antwort zur Eingabe passt (Gerade bei konkreten Werten, wie Lebensdauer von mehr als 3000 Stunden...)?

## Abgabe etc
Reiche deine Lösung bitte als .zip oder öffentlichem Link zu einem Github-Repo ein.
Abgabezeitpunkt: Es wäre schön, wenn wir spätestens Ende der kommenden Woche das Ergebnis anschauen könnten. Falls das nicht klappt, schreib bitte kurz, bis wann es für dich möglich wäre.

Wir sollten im gemeinsamen Review in der Lage sein, zusammen auf den Code zu schauen und verschiedene Suchbegriffe durchtesten zu können. Bevor wir einen Termin für ein weiteres Gespräch vereinbaren, würden wir deine gewählte Lösung zunächst prüfen.
Insgesamt sollte die Lösung dazu taugen, dass sie in einer chat-artigen Umgebung eingesetzt werden könnte. Die Antwortzeit sollte also maximal im niedrigen Minutenbereich liegen.

Bitte versuche, nicht mehr als 4 Stunden zu investieren. Wenn du in dieser Zeit nicht fertig geworden bist, würden wir dann in einem Gespräch einfach über deine unternommenen Lösungsversuche reden.

Komme bei weiteren Fragen gerne auf uns zu. Wir sind schon gespannt auf deine Lösung!

Die Quell-PDFs findest du hier: https://drive.google.com/drive/folders/1z2gqtLxgnFzFkGNpURnOMbgdezLQ-KoD?usp=share_link