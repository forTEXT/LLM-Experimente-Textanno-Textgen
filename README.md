# LLM-Experimente-Textanno-Textgen

# Literaturwissenschaftlich Arbeiten mit großen Sprachmodellen?
## Zwei Experimentreihen zur Textgenerierung mit Künstlicher Intelligenz

Autorinnen: 
- Mari Akazawa, Technische Universität Darmstadt, Institut für Sprach- und Literaturwissenschaft, Darmstadt (Hessen), Deutschland, ORCID: 0009-0007-2653-6275
- Evelyn Gius, Technische Universität Darmstadt, Institut für Sprach- und Literaturwissenschaft, Darmstadt (Hessen), Deutschland, ORCID: 0000-0001-8888-8419

Dieses Repositorium beinhaltet alle von uns ausgeführten Experimente, Daten und Codes.

### Zusammenfassung
In diesem Beitrag untersuchen wir die Nützlichkeit von Künstlicher Intelligenz für die literaturwissenschaftliche Forschung anhand von zwei dafür typischen Tätigkeiten. In zwei Experimentreihen mit großen Sprachmodellen wurden einerseits Annotationen für einem literarischen Text erstellt und andererseits drei Abschnitte dieses Beitrags generiert. Die Gestaltung der Experimente berücksichtigt die technischen Voraussetzungen, die Literaturwissenschaftler*innen typischerweise mitbringen. Damit wollen wir eine Nutzerperspektive beleuchten, die bislang in der Entwicklung und Bewertung von großen Sprachmodellen wenig beachtet wird. Die Experimente zum Schreiben der Abschnitte wurden mit ChatGPT umgesetzt, sodass sie direkt im Browserfenster und ohne technische Vorkenntnisse oder besondere Rechnerkapazitäten umgesetzt werden konnten. Für die Experimentreihe zur Generierung der Textannotationen haben wir einige technische Kenntnisse angenommen, die in der Literaturwissenschaft zwar nicht ganz selbstverständlich, aber in einigen Fällen doch vorhanden sind: Wir haben das generative Sprachmodell Llama 3.1 mit einer Anwendung lokal auf einem Rechner genutzt. Dafür sind neben durchschnittlichen Rechnenkapazitäten auch zumindest grundlegende Programmierkompetenzen erforderlich nötig gewesen. Beide Experimentreihen waren zwar teilweise erfolgreich, insgesamt scheint der aktuelle Stand dieser genutzten großen Sprachmodelleder Technologie allerdings nicht geeignet, um mit begrenzten Möglichkeiten in vertretbarer Zeit zufriedenstellende Ergebnisse zu erreichen. 


### Zwei Experimentreihen

#### Experimentreihe 1: Textannotation mit Llama 3.1

In unserer ersten Experimentreihe untersuchen wir, ob LLMs literaturwissenschaftliche Annotationen erzeugen können. 
Wir nutzen für die Experimente Daten aus dem Projekt heureCLÉA. Die Experimente werden mit Llama 3.1 durchgeführt. Konkret nutzen wir auf einem MacBook Air mit M1-Chip und mit 16 GB Arbeitsspeicher über die Anwendung LM Studio das Modell Meta-Llama-3.1-8B-Instruct-IQ4_XS.gguf.
Das Sprachmodell erhält, neben der Anweisung zur Annotation, den Teil der Annotationsrichtlinie (Gius und Jacke 2016), der sich auf das Phänomen ,Ordnungʻ bezieht, den Text „Auch ich war in Arkadien“ (Joseph von Eichendorff, 1834) aus dem Korpus des heureCLÉA-Projektes (Gius et al. 2017) und zum Teil Beispiele aus den Annotationen (Gius et al. 2017). Um die generierten Annotationen zu evaluieren, vergleichen wir sie mit den manuellen Annotationen aus dem heureCLÉA-Projekt. 


#### Experimentreihe 1: Textannotation mit Llama 3.1

Die zweite literaturwissenschaftliche Tätigkeit, für die wir mit entsprechenden Experimenten den Einsatz von LLMs prüfen, ist das Schreiben von wissenschaftlichen Beiträgen. Dafür generieren wir Texte zur Darstellung der Forschungsfrage, -methoden und -ergebnisse der in diesem Beitrag durchgeführten Annotationsexperimente. Für die Textgenerierung greifen wir auf ChatGPT (Version „chatgpt-4o-latest“ vom 03. September 2024)

Die Nutzung von ChatGPT für die Textgeneration in diesem Beitrag ist mit folgenden drei Zielen verbunden: 
- Ausformulieren einer Argumentationsstruktur 
- Erstellen von Textzusammenfassungen
- Schreiben von Analysen anhand übergebener Daten



### Ordnerstruktur
- generate_article_text:
  - analysis
  - experiment_setting
  - SotA_LLMs-Literary_studies
  - SotA_LLMs_Literary_Studies v2

- preprocess_annotations: (Pre)processing der Annotationen; Standoff Annotationen ohne Text in XML zu Inline-Annotationen (XML) sowie JSON-Dateien
  - annotationstotxt.py
  - catmapy.py
  - spielwiese.py
  - findindex.py

- annotationtask
  - oneshot_eg.py
  - oneshot.py
  - order_fullshot_results.md

- data:
  - results: Markdowns/TXTs mit Dokumentation der Prompt-Versuche
  - annotation: Enthält Ergebnisse von "preprocess_annotations", also Inline-Annotationen, JSONs und alles gefiltert nach ORDER/FREQ/DUR
  - tags: Tags and ID Infos on Frequency/Duration/Order
  - guidelines
  - raw
  - tags_guidelines_json.py
  - strategien.txt
  - guidelinesv2.txt
  - create_tag_json.py




## Python-Dateien
- oneshot.ipynb - One Shot Tests
- zeroshot.ipynb - Zero Shot Tests
- lmstudio.ipynb



