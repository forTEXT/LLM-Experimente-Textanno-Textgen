Dieses Github-Repositorium enthält alle Textdaten, Codes, Prompts, Links zu Chatverläufen mit ChatGPT-4o und Ergebnisse zu den im Beitrag "Literaturwissenschaftlich Arbeiten mit großen Sprachmodellen?" ausgeführten und vorgestellten Experimentreihen. 


# Literaturwissenschaftlich Arbeiten mit großen Sprachmodellen?
## Zwei Experimentreihen zur Textgenerierung mit Künstlicher Intelligenz

Autorinnen: 
- Mari Akazawa, Technische Universität Darmstadt, Institut für Sprach- und Literaturwissenschaft, Darmstadt (Hessen), Deutschland, ORCID: 0009-0007-2653-6275
- Evelyn Gius, Technische Universität Darmstadt, Institut für Sprach- und Literaturwissenschaft, Darmstadt (Hessen), Deutschland, ORCID: 0000-0001-8888-8419

Dieses Repositorium beinhaltet alle von uns ausgeführten Experimente, Daten und Codes.

### Zusammenfassung
In diesem Beitrag untersuchen wir die Nützlichkeit von Künstlicher Intelligenz für die literaturwissenschaftliche Forschung anhand von zwei dafür typischen Tätigkeiten. In zwei Experimentreihen mit großen Sprachmodellen wurden einerseits Annotationen für einen literarischen Text erstellt und andererseits der Text von drei Abschnitten dieses Beitrags generiert. Im ersten Abschnitt wurden Zusammenfassungen wissenschaftlicher Artikel zu LLMs in der Literaturwissenschaft generiert. Im zweiten Abschnitt ließen wir ChatGPT anhand einer vorgegebenen Struktur eine Beschreibung unserer Experimentreihe zur Annotation ausformulieren, während im dritten Abschnitt die Ergebnisse der Annotationsexperimentreihe für eine ausformulierte Analyse an ChatGPT übergeben wurden. 
Die Gestaltung der Experimentreihen berücksichtigt die typischen technischen Kenntnisse von Literaturwissenschaftler*innen. Die Experimente zum Schreiben wurden mit ChatGPT über das Chat-Interface im Browser umgesetzt, während für die Annotationen Llama 3.1 lokal verwendet wurde, was zumindest grundlegende Programmierkenntnisse erfordert. Trotz einzelner Erfolge scheint der aktuelle Stand dieser Sprachmodelle nicht geeignet, um mit begrenzten Möglichkeiten in angemessener Zeit zufriedenstellende Ergebnisse zu erreichen. 



### Zwei Experimentreihen

#### Experimentreihe 1: Textannotation mit Llama 3.1

In unserer ersten Experimentreihe untersuchen wir, ob LLMs literaturwissenschaftliche Annotationen erzeugen können. 
Wir nutzen für die Experimente Daten aus dem Projekt heureCLÉA. Die Experimente werden mit Llama 3.1 durchgeführt. Konkret nutzen wir auf einem MacBook Air mit M1-Chip und mit 16 GB Arbeitsspeicher über die Anwendung LM Studio das Modell Meta-Llama-3.1-8B-Instruct-IQ4_XS.gguf.
Das Sprachmodell erhält, neben der Anweisung zur Annotation, den Teil der Annotationsrichtlinie (Gius und Jacke 2016), der sich auf das Phänomen ,Ordnungʻ bezieht, den Text „Auch ich war in Arkadien“ (Joseph von Eichendorff, 1834) aus dem Korpus des heureCLÉA-Projektes (Gius et al. 2017) und zum Teil Beispiele aus den Annotationen (Gius et al. 2017). Um die generierten Annotationen zu evaluieren, vergleichen wir sie mit den manuellen Annotationen aus dem heureCLÉA-Projekt. 


#### Experimentreihe 1: Textannotation mit Llama 3.1

Die zweite literaturwissenschaftliche Tätigkeit, für die wir mit entsprechenden Experimenten den Einsatz von LLMs prüfen, ist das Schreiben von wissenschaftlichen Beiträgen. Dafür generieren wir Texte zur Darstellung der Forschungsfrage, -methoden und -ergebnisse der in diesem Beitrag durchgeführten Annotationsexperimente. Für die Textgenerierung nutzen wir ChatGPT (Version „chatgpt-4o-latest“ vom 03. September 2024).

Die Nutzung von ChatGPT für die Textgeneration in diesem Beitrag ist mit folgenden drei Zielen verbunden: 
- Ausformulieren einer Argumentationsstruktur 
- Erstellen von Textzusammenfassungen
- Schreiben von Analysen anhand übergebener Daten



### Ordnerstruktur

```
├── anno_task
│   ├── additional_chatgpt_annotask
│   ├── code
│   ├── data
│   │   ├── guidelines
│   │   ├── heureclea_annotations
│   │   ├── raw_data
│   │   └── tags
│   └── results
│       └── annotation_formatted
└── text_generation_task
    ├── SotA_LLMs_Literary_Studies
    ├── SotA_LLMs_Literary_Studies_v2
    ├── analysis
    └── experiment_setting
```

