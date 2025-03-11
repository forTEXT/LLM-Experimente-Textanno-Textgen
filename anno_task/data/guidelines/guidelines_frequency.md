2.5 Zeitliches Verhältnis zwischen discours und histoire

Das Tagset für <time_relation_discours–histoire> enthält Kategorien zur Bestimmung des zeitlichen Zusammenhangs zwischen der Zeit des Diskurses und der Zeit der Geschichte.
Es ist in drei Untersets zum Taggen von Ordnung (<order>), Frequenz (<frequency>) und Dauer (<duration>) aufgeteilt.

2.5.2 Frequenz
Das Unterset <frequency> dient der Annotation der Wiederholungshäuﬁgkeit von Ereignissen im Verhältnis zwischen der Ebene der Handlung (histoire) und der Ebene der
Darstellung (discours).


2.5 Zeitliches Verhältnis zwischen discours und histoire

a. Ort <frequency>
Das Unterset <frequency> beﬁndet sich im heureCLÉA Tagset unter: TimeTagset →
time_relation_discours–histoire → frequency. Es teilt sich in die Tags <singulative>, <repetitive> und <iterative> auf.

b. Operationalisierung <frequency>
Die Frequenz beschreibt „das Verhältnis der Wiederholungshäuﬁgkeit von Ereignissen auf der Ebene der Handlung einerseits und auf der Ebene der Darstellung andererseits“ (Lahn und Meister, 2013, S. 148). Da jedes Ereignis33 streng genommen einmalig ist, wird dabei von einem „Minimum an übereinstimmenden Ähnlichkeitskriterien“ (Lahn und Meister, 2013, S. 148) ausgegangen.

Lahn und Meister unterscheiden drei Relationen und eine Sonderform:
- Singulatives Erzählen: Ein Ereignis wird so oft erzählt, wie es sich ereignet hat
(1-mal erzählen, was 1-mal geschehen ist). Eine Sonderform ist das anaphorische
oder multi-singulative Erzählen, bei dem ein Ereignis, das sich wiederholt, so oft
erzählt wird, wie es stattﬁndet (n-mal erzählen, was n-mal geschehen ist).

- Repetitives Erzählen: Ein Ereignis wird öfter erzählt, als es sich ereignet hat
(n-mal erzählen, was 1-mal geschehen ist). Dies ist auch der Fall, wenn mehrere
Figuren dasselbe Ereignis schildern (Multiperspektivismus). Für die nähere Be-
stimmung des Inhalts und der Anzahl der Wiederholungen der Passagen werden
die Tag-Eigenschaften NARRATED_CONTENT und REPETITION_COUNT
operationalisiert.

- Iteratives Erzählen: Ein Ereignis wird seltener erzählt, als es sich ereignet hat
(1-mal erzählen, was n-mal geschehen ist). Iteratives Erzählen wird u.a. eingesetzt,
um eine einmalige Regelabweichung zu erzählen.

Die Kategorien des multi-singulativen und iterativen Erzählens sind nicht unproble-
matisch. Das liegt daran, dass dasselbe Ereignis natürlich immer nur einmal geschehen
kann. Das „Minimum an übereinstimmenden Ähnlichkeitskriterien“, auf das Lahn
& Meister verweisen, müsste hier genauer erforscht werden, damit die Nutzung der
fraglichen Frequenz-Kategorien zu einigermaßen robust reproduzierbaren Ergebnissen
führen kann.



c. Tagset <frequency>


d. Richtlinien für die Annotation von <frequency>

**Allgemein geltende Hinweise**

- Tagstring: Textpassagen (Mindestgröße: Teilsatz).

**Hinweise für einzelne Tags oder Untersets**

- <singulative> (Singulatives Erzählen)
  - Tagbeschreibung: Singulatives Erzählen liegt vor, wenn Ereignis so oft erzählt wird, wie es sich ereignet hat. Dabei gilt der Fall „1-mal erzählen, was sich 1-mal ereignet hat“ als default, d.h. als unmarkierter Standardfall, der nicht annotiert wird.
    - <multi-singulative>: Multi-singulatives Erzählen ist ein Sonderfall des singulativen Erzählens. Es liegt vor, wenn ein Ereignis, das sich wiederholt, so oft erzählt wird, wie es stattﬁndet (n-mal erzählen, was sich n-mal ereignet hat). Wird das <multi_singulative>-Tag vergeben, müssen die Werte der Tag-Eigenschaften NARRATED_CONTENT und REPETITI-ON_COUNT bestimmt werden. Dabei wird im für die Tag-Eigenschaft NARRATED_CONTENT der Inhalt der repetitiven Passage kurz in Form eines Propertywertes zusammengefasst. Für die Eigenschaft REPETITI-ON_COUNT wird die Anzahl des Vorkommens der Wiederholung an Form eines Wertes angegeben. Für das erste Vorkommen wird der Wert „0“ angegeben. Bei kollaborativer Textarbeit sollten die Werte der Tag-Eigenschaft NARRATED_CONTENT unter den Mitarbeitern aufeinander abgestimmt bzw. vereinheitlicht werden. Wenn ein ähnliches Ereignis mehrmals, aber auf ontologisch verschiedenen Erzählebenen geschieht, dann liegt kein multi-singulatives Erzählen vor: Durch den ontologischen Unterschied können die Ereignisse nicht als hinreichend ähnlich gelten. Ein Beispiel wäre ein Ereignis, das einmal im Kontextes eines Wunsches erzählt wird und ein zweites Mal, wenn es ‘tatsächlich’ geschieht.
        - Multi-Singulative können auch zusammen mit iterativen Passagen (s.u.) auftreten, z. B. in folgender Passage: „Und das war das erstemal im Leben des Knaben, daß er an einem Tage den Becher der Seligkeit und den der Qual trank, er, der verurteilt war, noch oft von den Extremen der tiefsten Qualen und des wildesten Glückes erschüttert zu werden“ (Ein Nachmittag). Dabei ist „das erstemal“ multi-singulativ zu „noch oft“. „Noch oft“ ist aber zusätzlich auch iterativ, d.h. es wird ein Ereignis, das häuﬁger geschieht, mithilfe dieses Ausdrucks nur einmal erzählt. Da für Multi-Singulative die Property REPETITION_COUNT bestimmt werden soll, werden in Fällen, in denen erst der Multi-Singulativ und dann der Iterativ auftritt, als Repetition Counts „1“ und „1 + n“ vergeben; wenn erst der Iterativ, dann der Multi-Singulativ auftritt, werden „n“ und „n + 1“ vergeben.
        - Es kann ein Sonderfall auftreten, der als „incomplete_multi-singulative“ bezeichnet werden kann. Dieser Fall tritt dann auf, wenn im Text suggeriert wird, dass etwas erzählt wird, das so schon vorher einmal geschehen und erzählt worden ist, wobei das erste Vorkommnis dieses Ereignisses de facto aber nicht erzählt worden ist. Um diesen Sonderfall adäquat beschreiben zu können, wurde für das <multi-singulative>-Tag die Eigenschaft COMPLETENESS mit den Werten [complete] und [incomplete] eingeführt. Der Wert für diese Property sollte aber in der Regel aus arbeitsökonomischen Gründen nur für unvollständige Multi-Singulative, also für den Sonderfall, bestimmt werden.
  - Indikatoren:
    - Wiederholung anzeigende Begriﬀe wie „wieder“ (Indikator für multi-singulatives Erzählen)
  - Beispiele:
    - <singulative>: „[. . . ] fast noch ehe man den Knall hörte, hörte man den Hansjörg gottserbärmlich schreien. Die Pistole entﬁel seiner Hand [. . . ]“ (Die Kriegspfeife)
    - <multi-singulative>: „Als er schon einige Stunden darauf im Wundﬁeber lag, war es ihm, als ob ein Engel zu ihm heranschwebte und ihm Kühlung zuwehte.“ [. . . ] „Dann erschien dem Hansjörg im Traume wieder eine ganz verhüllte Gestalt [. . . ]“ (Die Kriegspfeife)

- <repetitive> (Repetitives Erzählen)
  - Tagbeschreibung: Repetitives Erzählen liegt vor, wenn ein Ereignis öfter erzählt wird, als es sich ereignet hat (n-mal erzählen, was 1-mal geschehen ist). Dies gilt auch, wenn mehrere Figuren multiperspektiv dasselbe Ereignis schildern. Wie beim <multi-singulative>-Tag müssen auch für das <repetitive>-Tag die Werte der Tag-Eigenschaften NARRATED_CONTENT und REPETITION_COUNT bestimmt werden (s.o.). werden. Bei repetitivem Erzählen reicht es nicht aus, dass auf ein bereits erzähltes Ereignis lediglich noch einmal verwiesen wird (z. B. durch eine Phrase wie „wie letztes Mal“) – stattdessen muss das Ereignis tatsächlich ein weiteres Mal erzählt werden, d.h. mindestens durch einen Teilsatz mit Verb. Es gilt auch als repetitiv, wenn ein Ereignis, das bereits ein- oder mehrmals erzählt wurde, noch einmal von einem anderen Erzähler (z. B. einer Figur) erzählt wird (Stichwort: multiperspektivisches Erzählen) oder wenn es in Form von Gedankenrede erinnert wird. Das geht auch auf unterschiedlichen ontologischen Ebenen.
  - Beispiele:
    - <repetitive> mit NARRATED_CONTENT und REPETITION_COUNT: 
      - „Ich halte Sie nämlich für einen Philosophen [. . . ]“ (27. September, Der Tod)
        → NARRATED_CONTENT: Doktor hält Erzähler für Philosophen
        → REPETITION_COUNT: 0
      - „Doktor Gudehus hält mich für einen Philosophen [. . . ]“ (30. September, Der Tod)
        → NARRATED_CONTENT: Doktor hält Erzähler für Philosophen
        → REPETITION_COUNT: 1

- <iterative> (Iteratives Erzählen)
  - Tagbeschreibung: Iteratives Erzählen liegt vor, wenn ein Ereignis seltener erzählt wird, als es sich ereignet hat (1-mal erzählen, was n-mal geschehen ist). Allgemein wird iteratives Erzählen u.a. eingesetzt, um eine einmalige Regelabweichung zu erzählen.
  - Ereignisse gelten gemeinhin nur dann als hinreichend ähnlich, um als iterativ eingestuft zu werden, wenn die handelnden Personen (sofern welche involviert sind) identisch bleiben. In einigen Sonderfällen kann es aber Interpretationssache sein, ob bspw. eine handelnde Gruppe sich jedes Mal aus den gleichen Individuen zusammensetzt.
  - Es kann manchmal schwer zu entscheiden sein, ob es sich um zeitraﬀendes Erzählen (vgl. Unterunterabschnitt 2.5.3 „Dauer“, S. 61) handelt oder (zusätzlich) um iteratives Erzählen: Die Entscheidung ist davon abhängig, ob von mehreren wiederkehrenden Ereignissen berichtet wird oder von einem lang andauernden Ereignis. Dies ist aber oft nur interpretativ feststellbar – die Interpretation kann davon beeinﬂusst werden, auf welche Weise das Ereignis/die Ereignisse beschrieben werden („Sie drehte sich viele Male um die eigene Achse“ vs. „Sie drehte sich lange im Kreis“).
  - Generalisierungen lassen sich häuﬁg in Konditionale der Form „immer wenn, dann“ übersetzen. Solche Konditionale sind aber nicht automatisch Iterative. Sie sind es nur dann, wenn sie von tatsächlich in der ﬁktiven Welt stattgefundenen Ereignissen berichten (z. B. „immer wenn dies passierte, passierte auch jenes“). Wenn es sich dagegen um abstrakte Regelmäßigkeitsaussagen handelt, die keine Informationen darüber enthalten, ob so etwas tatsächlich passiert ist, liegt kein Iterativ vor.
  - Wenn zwei iterative Passagen direkt aneinander anschließen, werden diese trotzdem einzeln getaggt, sofern sich die sich wiederholenden Ereignisse eindeutig unterscheiden lassen. Wenn sich das iterativ erzählte Ereignis langsam verändert, so dass keine zwei separaten Sets von Ereignissen identiﬁziert werden können, wird ein Gesamttag vergeben.
  - Indikatoren: iterative Ausdrücke
  - Beispiel:
    - „Oftmals, wenn meine Gedanken sich wie graue Gewässer vor mir ausbreiten, die mir unendlich scheinen, weil sie umnebelt sind, sehe ich etwas wie den Zusammenhang der Dinge und glaube die Nichtigkeit der Begriﬀe zu erkennen.“ (Der Tod)

