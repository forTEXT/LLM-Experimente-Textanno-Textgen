# Tests für die Generierung des Textteils über die Experimente

## **ChatGPT**
### Experiment 1
Prompt (und Upload der beiden im Prompt genannten Dateien):
Schreibe einen Abschnitt eines wissenschaftlichen Artikels über den Einsatz von LLMs für literaturwissenschaftliche Textanalysen. Es geht in diesem Abschnitt um acht One Shot- und Two Shot-Experimente. Die angehängte Datei order_oneshot_results_annotation.md enthält die Beschreibung von diesen acht Experimenten, bestehend aus dem Prompt und dem Output des LLMs. In der Datei Auch_ich_war_in_Arkadien_order_Annotator1.json sind die manuell erstellten korrekten Annotationen (Goldstandard). Beschreibe zuerst die generelle Ausrichtung dieser Experimente. Diskutiere danach Ähnlichkeiten und Unterschiede in der Qualität der Ergebnisse der einzelnen Experimente in Bezug auf den Goldstandard, die auffallend sind.

Ergänzung a:
schreibe den Teil erneut und wende strengere Kriterien für die Beurteilung an

Ergänzung b: 
Schreibe den Abschnitt noch einmal und ergänze konkrete Beispiele aus den Prompts, dem Goldstandard oder dem Output für alle Punkte, die diskutiert werden.

Ergänzung c:
ergänze neben den Stellenangaben im Text auch den Text, um den es in den genannten Beispielen geht.

Alle prompts + Outputs: https://chatgpt.com/share/671252b8-3528-8004-bec2-c5b95578f010 (18.10.2024, ChatGPT-4o)

### Experiment 2:
Prompt (und Upload der beiden im Prompt genannten Dateien):
Schreibe einen Abschnitt eines wissenschaftlichen Artikels über den Einsatz von LLMs für literaturwissenschaftliche Textanalysen. Es geht in diesem Abschnitt um 31 Zero Shot-, One Shot-, Two Shot- und Three-Shot-Experimente. Die angehängte Datei all_prompts_results.md enthält eine Übersicht zu diesen 31 Experimenten. Diese sind in der Markdowndatei nummeriert. Die Nummerierung ist der jeweiligen Überschrift zu entnehmen. Unter jeder Überschrift stehen Informationen zu den Experimenten, die durch Aufzählungszeichen markiert sind. Zu diesen Informationen gehören die übergebenen Guidelines, der zu annotierende Text, das/die übergebene(n) Ausgabebeispiel(e), die ausformulierte Promptanfrage, die an das Modell gestellt wurde, sowie die Antwort des Modells. In manchen Fällen gibt es zu Experimenten noch stichpunktartig Notizen oder Beobachtungen, die festgehalten wurden. 
Außerdem erhältst du die Dateien “Auch_ich_war_in_Arkadien_order_Annotator1.json”, die manuell erstellte, korrekte Annotationen (Goldstandard) enthält.
Schreibe auf Grundlage der übergebenen Dateien einen Text mit folgenden Inhalten: 1) Beschreibe die generelle Ausrichtung dieser Experimente und 2) beurteile die Ergebnisse jedes einzelnen Experiments, indem Du sie mit dem Goldstandard vergleichst, 3) Diskutiere danach Ähnlichkeiten und Unterschiede in der Qualität der Ergebnisse der einzelnen Experimente in Bezug auf den Goldstandard, die auffallend sind. Nenne dabei immer die Textstellen, die korrekt gefunden bzw. nicht gefunden wurden.

Modell-Output:

Einsatz von LLMs für literaturwissenschaftliche Textanalysen: Methodik und Ergebnisbewertung
Generelle Ausrichtung der Experimente

Die 31 durchgeführten Experimente zur Anwendung von Large Language Models (LLMs) in der literaturwissenschaftlichen Textanalyse wurden mit unterschiedlichen Prompt-Strategien gestaltet, um die Annotationen literarischer Texte zu evaluieren. Dazu wurden Zero-Shot-, One-Shot-, Two-Shot- und Three-Shot-Ansätze gewählt, die variieren, ob und wie viele Beispiele zur Erklärung der Annotationen bereitgestellt wurden. Ziel dieser Experimente war es, die Effektivität und Genauigkeit der LLMs bei der Erkennung spezifischer textueller Merkmale und annotativen Elemente zu prüfen und sie mit manuell erstellten, korrekten Annotationen (Goldstandard) zu vergleichen.

Die Experimente nutzten verschiedene Formen von Anfragen und Guidelines, die den Modellen zur Verfügung gestellt wurden. In den One-, Two- und Three-Shot-Experimenten wurden Beispielausgaben integriert, um das Modell zu steuern und eine präzisere Antwort zu erzielen. Jede Konfiguration zielte darauf ab, die Leistungsfähigkeit des Modells zu bewerten, indem die generierten Antworten auf annotierte Textpassagen überprüft und mit dem Goldstandard abgeglichen wurden.

Beurteilung der Ergebnisse der einzelnen Experimente im Vergleich zum Goldstandard

Die Ergebnisse der einzelnen Experimente wurden mit den manuell erstellten Annotationen des Textes Auch ich war in Arkadien verglichen, die verschiedene Kategorien wie zeitliche und iterative Ausdrücke sowie andere annotative Elemente enthielten. Die Goldstandard-Daten zeigten präzise markierte Stellen, darunter Formulierungen wie „seit langer Zeit“, „Julirevolution“, und „Eines Tages“, die spezifischen annotativen Kategorien zugeordnet waren.

Zero-Shot-Experimente: Diese Experimente, die ohne Beispielanfragen durchgeführt wurden, wiesen in der Regel eine geringere Genauigkeit auf. Viele der annotierten Textstellen wurden entweder nicht erkannt oder nur teilweise erfasst. Beispiele wie „seit langer Zeit“ und „unterdes“ wurden oftmals übersehen oder fehlerhaft kategorisiert.
One-Shot-Experimente: Mit der Bereitstellung eines einzelnen Beispiels verbesserten sich die Erkennungsraten leicht. Annotationsstellen wie „Julirevolution“ wurden in einigen Fällen korrekt identifiziert, doch blieben die Ergebnisse insgesamt inkonsistent. Der Einfluss des einen Beispiels auf die Modellantwort war spürbar, reichte aber nicht aus, um eine umfassende Abdeckung der Annotationen sicherzustellen.
Two-Shot- und Three-Shot-Experimente: Die Hinzufügung weiterer Beispiele trug zu einer verbesserten Leistung der LLMs bei. Zwei- und Drei-Shot-Experimente konnten komplexere zeitliche Strukturen wie „in diesem Augenblick“ oder „eh ich mich besinnen konnte“ präziser erkennen. Die Verwendung mehrerer Beispiele führte zu einer deutlicheren Verbesserung der Erkennungsqualität, insbesondere bei der Identifizierung subtiler zeitlicher Hinweise. Dennoch gab es auch hier einige Fehlzuordnungen und fehlende Annotationen im Vergleich zu den vollständigeren Goldstandard-Daten.
Vergleich der Experimente hinsichtlich der Übereinstimmung mit dem Goldstandard

Die Qualität der LLM-Ergebnisse in den verschiedenen Experimenten zeigte bemerkenswerte Unterschiede. Während die Zero-Shot-Ansätze durch eine niedrigere Erkennungsgenauigkeit geprägt waren, bewiesen die Experimente mit ein oder mehr Beispielanfragen eine zunehmende Robustheit. Textstellen wie „unterdes“, die im Goldstandard als „anaphoric_time-span“ gekennzeichnet waren, wurden beispielsweise in den komplexeren Shot-Experimenten häufiger erkannt.

Ein wiederkehrendes Muster war, dass die Modelle eher kürzere, prägnante Annotationen wie „eh“ oder „nun“ korrekt erfassten, während längere oder kompliziertere Ausdrücke wie „während dicke Sträuße hoher Pfauenfedern von ihrer turmähnlichen Frisur herabnickten“ häufiger übersehen wurden. Eine detaillierte Analyse zeigte zudem, dass iterative Ausdrücke wie „von Zeit zu Zeit“ in den meisten Versuchen nur sporadisch korrekt identifiziert wurden.

Diskussion der Ähnlichkeiten und Unterschiede

Es zeigte sich, dass die LLMs mit zunehmender Anzahl von Beispielen und spezifischen Prompts eine bessere Anpassung an die Annotationen gemäß dem Goldstandard zeigten. Eine zentrale Herausforderung war jedoch die konsistente Erkennung längerer Phrasen und kontextabhängiger Zeitpunkte. Die Diskrepanz zwischen den LLM-Ergebnissen und dem Goldstandard betraf insbesondere komplexe temporale Konstruktionen und seltener vorkommende Ausdrücke, die oft unberücksichtigt blieben.

Trotz der Verbesserungen durch den Einsatz von Beispielen konnte keine vollständige Übereinstimmung mit den Goldstandard-Daten erzielt werden. Dies deutet darauf hin, dass eine weitere Anpassung der Prompts und die Implementierung von Zusatztechniken, wie z.B. das Feintuning der Modelle auf spezifische literaturwissenschaftliche Korpora, erforderlich sein könnte, um eine höhere Übereinstimmungsrate zu erzielen.

Prompt + Output: https://chatgpt.com/share/67288623-0dc8-8004-9758-2d0bbb012f42 (04.11.2024, ChatGPT-4o)

## Experiment 3 - Auswertung in Tabellenform:
Prompt (und Upload der beiden im Prompt genannten Dateien):
Schreibe einen Abschnitt eines wissenschaftlichen Artikels über den Einsatz von LLMs für literaturwissenschaftliche Textanalysen. Es geht in diesem Abschnitt um 31 Zero Shot-, One Shot-, Two Shot- und Three-Shot-Experimente. Die angehängte Datei all_prompts_results.md enthält eine Übersicht zu diesen 31 Experimenten. Diese sind in der Markdowndatei nummeriert. Die Nummerierung ist der jeweiligen Überschrift zu entnehmen. Unter jeder Überschrift stehen Informationen zu den Experimenten, die durch Aufzählungszeichen markiert sind. Zu diesen Informationen gehören die übergebenen Guidelines, der zu annotierende Text, das/die übergebene(n) Ausgabebeispiel(e), die ausformulierte Promptanfrage, die an das Modell gestellt wurde, sowie die Antwort des Modells. In manchen Fällen gibt es zu Experimenten noch stichpunktartig Notizen oder Beobachtungen, die festgehalten wurden. 
Außerdem erhältst du die Dateien “Auch_ich_war_in_Arkadien_order_Annotator1.json”, die manuell erstellte, korrekte Annotationen (Goldstandard) enthält.
Schreibe auf Grundlage der übergebenen Dateien einen Text mit folgenden Inhalten: 1) Beschreibe die generelle Ausrichtung dieser Experimente und 2) beurteile die Ergebnisse jedes einzelnen Experiments, indem Du sie mit dem Goldstandard vergleichst, 3) Diskutiere danach Ähnlichkeiten und Unterschiede in der Qualität der Ergebnisse der einzelnen Experimente in Bezug auf den Goldstandard, die auffallend sind. Nenne dabei immer die Textstellen, die korrekt gefunden bzw. nicht gefunden wurden. 4) Gib abschließend einen Überblick, in dem Du alle Experimente zusammenfasst und eine Tabelle erstellst, in der die Anzahl der erzeugten Annotationen und in Zahlen und Prozent der Anteil der korrekten Annotationen, der falschen Annotationen und der fehlenden Annotationen für alle 31 Experimente steht.


Prompt + Output: https://chatgpt.com/share/672a40fd-3934-8004-a182-393406b5e757 (04.11.2024, ChatGPT-4o)