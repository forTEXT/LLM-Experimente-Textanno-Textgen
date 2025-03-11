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
Schreibe einen Abschnitt eines wissenschaftlichen Artikels über den Einsatz von LLMs für literaturwissenschaftliche Textanalysen. Es geht in diesem Abschnitt um acht One Shot- und Two Shot-Experimente. Die angehängte Datei order_oneshot_twoshot_results_annotation.md enthält die Beschreibung von diesen acht Experimenten, bestehend aus einer kurzen Übersicht, dem Prompt und dem Output des LLMs. In der Datei Auch_ich_war_in_Arkadien_order_Annotator1.json sind die manuell erstellten korrekten Annotationen (Goldstandard). Schreibe folgenden Text: 1. Beschreibe die generelle Ausrichtung dieser Experimente und beurteile die Ergebnisse jedes einzelnen Experiments, indem Du sie mit dem Goldstandard vergleichst. 3. Diskutiere danach Ähnlichkeiten und Unterschiede in der Qualität der Ergebnisse der einzelnen Experimente in Bezug auf den Goldstandard, die auffallend sind. Nenne dabei immer die Textstellen, die korrekt gefunden bzw. nicht gefunden wurden.

https://chatgpt.com/share/671287ac-2c44-8004-bddb-31707ab5ed21



**lmstudio mit Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf**:

Der Einsatz von LLMs (Large Language Models) für literaturwissenschaftliche Textanalysen ist ein vielversprechender Ansatz, um die Analyse und Interpretation von literarischen Werken zu unterstützen. Die Experimente in der Datei "order_oneshot_results_annotation.md" haben sich auf acht One-Shot- und Two-Shot-Versuche konzentriert, wobei das Ziel darin bestand, LLMs zur Erstellung von Annotationen für literarische Texte zu nutzen.

Ein wesentlicher Aspekt dieser Experimente ist die Verwendung von One-Shot- und Two-Shot-Ansätzen. Bei den One-Shot-Versuchen wird eine Anfrage an das LLM gestellt, wobei das Modell aufgefordert wird, eine Annotation für einen bestimmten Text zu erstellen, ohne vorherige Informationen oder Kontext über die Annotationsprozess zu erhalten. Im Gegensatz dazu werden bei den Two-Shot-Versuchen zwei Anfragen an das LLM gestellt: eine mit dem Prompt und einer Beispiel-Ausgabe und eine weitere Anfrage zur Erstellung der tatsächlichen Annotationen.

Die Ergebnisse dieser Experimente sind im angehängten Datei "order_oneshot_results_annotation.md" dokumentiert. Um die Qualität der Ergebnisse zu beurteilen, wurden sie mit den manuell erstellten korrekten Annotationen (Goldstandard) verglichen. In Bezug auf den Goldstandard fallen einige Ähnlichkeiten und Unterschiede in der Qualität der Ergebnisse auf.

Einige auffällige Ähnlichkeiten zwischen den Ergebnissen liegen in der Tatsache, dass die LLMs in vielen Fällen ähnliche Annotationen wie im Goldstandard erstellen konnten. Dies deutet darauf hin, dass das LLM die Anforderungen und Regeln der Annotations-Prozess verstanden hat. 

Einige auffällige Unterschiede zwischen den Ergebnissen liegen jedoch auch vor. Einige LLM-Ergebnisse weisen offensichtliche Fehler oder Unpräzisionen auf, während andere Ergebnisse überhaupt keine Annotationen erstellen konnten. Diese Unterschiede könnten durch die Qualität und Komplexität der verwendeten Trainingsdaten, die Genauigkeit des Modells oder die Art der Anfrage an das LLM bedingt sein.

Insgesamt ergeben diese Experimente jedoch, dass LLMs für literaturwissenschaftliche Textanalysen ein vielversprechender Ansatz darstellen. Durch weitere Verbesserungen und Optimierungen kann das Potenzial von LLMs vollständig ausgeschöpft werden, um die Qualität der Annotationen zu verbessern und den Prozess der Textanalyse effizienter zu machen.

Es ist jedoch wichtig zu beachten, dass diese Ergebnisse auf einem kleinen Satz Experimente basieren und weitere Untersuchungen notwendig sind, um die allgemeine Gültigkeit dieser Ergebnisse zu bestätigen.


