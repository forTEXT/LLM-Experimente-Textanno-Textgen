2.5 Zeitliches Verhältnis zwischen discours und histoire

Das Tagset für <time_relation_discours–histoire> enthält Kategorien zur Bestimmung des
zeitlichen Zusammenhangs zwischen der Zeit des Diskurses und der Zeit der Geschichte.
Es ist in drei Untersets zum Taggen von Ordnung (<order>), Frequenz (<frequency>)
und Dauer (<duration>) aufgeteilt.

2.5.1 Ordnung
Das Unterset <order> enthält Kategorien für die Annotation des Verhältnisses der
zeitlichen Ordnung von Diskurs und Geschichte (ordo artiﬁcialis und ordo naturalis).

a. Ort <order>
Das Unterset <order> beﬁndet sich im heureCLÉA Tagset unter: TimeTagset →
timerelation_discours–histoire → order.

Es teilt sich in die Tags <chronology>, <anachrony> und <achrony> auf. Das <anachrony>-
Tag ist weiterhin in Tags aufgeteilt, mit denen die einzelnen Typen einer narrativen
Anachronie annotiert werden können (<analepsis>, <prolepsis> und <simullepsis>).

b. Operationalisierung <order>
Unter dem Begriﬀ „Ordnung“ behandeln Lahn und Meister (2013) das Verhältnis
von ordo naturalis und ordo artiﬁcialis. Die zugrunde liegende Frage lautet dabei:
„Folgt der Erzähler auf der Diskurs-Ebene der ’realen’ Anordnung der Begebenheiten
auf der Ebene der Geschichte (ordo naturalis), oder bietet er in seinem Bericht die
Geschehnisse in einer künstlichen Ordnung dar, die den Erfordernissen des Erzählens
angemessenen ist (ordo artiﬁcialis)?“ Insgesamt existieren drei Formen von Ordnung,
die zum Erzählen von Geschehnissen verwendet werden können. Folgt der Erzähler der
realen Anordnung, spricht man von chronologischem Erzählen. Wird die Reihenfolge
der Ereignisse umgestellt, liegen so genannte Permutationen vor. Die entsprechenden
Handlungselemente werden narrative Anachronien genannt. Eine dritte Form liegt vor,
wenn alle Zeitbezüge fehlen, die eine Verortung in der Geschichte (histoire) ermöglichen
würden, also weder eine Chronologie noch eine Anachronie vorliegt: die Achronie.

Bei Achronien ist eine zeitliche Verknüpfung zur Haupthandlung nicht möglich.
Lahn und Meister folgern daraus: „Achronien sind somit in der Regel weniger an die
Geschichte [(histoire)] als vielmehr an den (unzeitlichen) Diskurs gebunden“ Lahn und
Meister (2013, S. 142). Nach Genette liegt hingegen eine achronische Struktur vor,
wenn die Zeitstruktur aufgrund der komplexen Verschränkung von Analepsen und
Prolepsen nicht rekonstruierbar ist. Dabei scheint die Abgrenzung der Achronie sowohl
bei sehr anachronisch gestalteten Erzählungen als auch bei Erzählungen, die sich über
weite Teile deskriptiver Pausen bedienen, nicht eindeutig deﬁniert zu sein.

Bei den narrativen Anachronien wird im Wesentlichen zwischen zwei Typen un-
terschieden: In Analepsen wird nachholend berichtet, was sich früher eignet hat, und
in Prolepsen wird entsprechend vorwegnehmend berichtet, was sich später ereignet
hat. Darüber hinaus führen Lahn und Meister (2013) den Begriﬀ „Simullepse“ ein, der 
die (notgedrungen) linear nacheinander erfolgende Darstellung simultan stattﬁnden-
der Handlungen bezeichnet (Ken Ireland spricht hier von „co-occurence“) (Lahn und
Meister, 2013, S. 140).

Weiter weisen Lahn und Meister (2013) darauf hin, dass chronologisches Erzählen
nur ab ovo möglich ist, Erzählungen, die in medias res oder in ultimas res beginnen,
müssen die Eingangszene durch Analepsen nachholen.29 Schließlich ergänzen Lahn und
Meister (2013) die Bestimmung von Anachronien um die Kriterien Reichweite und
Umfang, denn: „Anachronien können schließlich auch stark variieren zum einen auf der
Ebene der Erzählzeit in Bezug auf die Dauer und zum anderen in Bezug auf die zeitliche
Distanz zwischen dem gegenwärtigen Zeitpunkt der Erzählung und dem nachgeholten
Geschehensmoment“ (Lahn und Meister, 2013, S. 141-142, ohne Hervorhebungen des
Originaltextes).



d. Richtlinien für die Annotation von <order>
Allgemein geltende Richtlinien

Bevor die Tags des <order>-Tagsets sinnvoll angewendet werden können, sollten
die jeweiligen Texte in Bezug auf narrative Ebenenwechsel analysiert werden. Nicht
einander zugehörige narrative Ebenen sollten voneinander getrennt auf die zeitliche
Ordnung hin analysiert werden. Das heißt auch, dass ein Zeitsprung, der mit einem
Ebenenwechsel einhergeht, nicht als Zeitsprung annotiert wird – sobald eine neue
narrative Ebene beginnt, wird die zu Beginn der jeweiligen Erzählung genutzte Zeit als
neuer temporaler Nullpunkt gesetzt, in Bezug zu welchem die zeitliche Ordnung dieser
Ebene analysiert wird. Entsprechend korreliert die zeitliche Ordnung auch nicht mit
dem Zeitpunkt des Erzählens.

- Tagstring allgemein: Annotiert werden Textpassagen (mindestens Teilsätze).



Richtlinien für einzelne Tags oder Untersets
<chronology> (Chronologisches Erzählen)
- Tagbeschreibung: Beim chronologischen Erzählen folgt der Erzähler der realen
Anordnung (ordo naturalis) der Geschehnisse auf der Ebene der histoire. Diese
Erzählweise gilt als default, d.h. als unmarkierter Standardfall, und wird daher
nicht annotiert.

- Beispiel: „Da kam über den Markt eine jugendliche Gestalt [. . . ]; jetzt wollte sie
den letzten Schritt tun, und von ohngefähr erhob sie das Auge und traf mit dem
blauesten Strahle in seinen Blick. Er ward wie von einem Blitz durchdrungen. Sie
strauchelte, und so schnell er auch hinzusprang, konnte er doch nicht verhindern,
daß sie nicht kurze Zeit in der reizendsten Stellung knieend vor seinen Füßen lag.
Er hob sie auf, sie sah ihn nicht an [. . . ]“ (Der Pokal)

<anachrony> (Anachronisches Erzählen)
- Tagbeschreibung: Beim anachronischen Erzählen weicht der Erzähler von der
chronologischen Reihenfolge der Ereignisse ab. Generell ist es möglich, dass eine
Anachronie eine weitere Anachronie enthält. Dabei sind alle Kombinationen
möglich. Die Annotationen werden in diesem Fall verschachtelt. Anachronisches
Erzählen kann drei verschiedene Formen annehmen:

– <analepsis>: Analepsen sind Abweichungen von der chronologischen Rei-
henfolge, in denen nachholend berichtet wird, was sich früher ereignet hat.
Dabei werden nur tatsächliche Rückgriﬀe als Analepse annotiert, also solche,
die nicht im Laufe der Erzählung falsiﬁziert werden oder von Vornherein als
hypothetisch gekennzeichnet sind, sich also als unzutreﬀende Darstellungen
der Ereignisse der ﬁktiven Welt herausstellen. Manche Iterative (siehe Un-
terunterabschnitt 2.5.2 „Frequenz“, S. 54) mit eindeutiger Verweisrichtung
in die Vergangenheit können zugleich auch Analepsen sein (bspw. „jeden
Tag seit zwei Jahren“).
Analepsen können mithilfe von Tag-Eigenschaften genauer hinsichtlich Reich-
weite (REACH) und Umfang (EXTENT) diﬀerenziert werden. Die Reich-
weite bezeichnet den Zeitpunkt der Analepse in Bezug auf den Abstand zur
gegenwärtigen Handlung. Finden die in einer Analepse berichteten Ereignisse
im Rahmen der Basiserzählung statt, wird der Propertywert [internal] verge-
ben. Liegt der Zeitpunkt der Ereignisse außerhalb der Basiserzählung, wird
dementsprechend die Analepse als [external] markiert. Auch Mischformen
der Reichweite können annotiert werden. Beginnt eine Analepse außerhalb
der Basiserzählung und reicht in sie hinein, wird der Propertywert [external-
internal] vergeben (vgl. Abbildung 8). Wenn Analepsen im Rahmen größerer
Anachronien vorkommen, können die Analepsen auch in der Basiserzählung
beginnen und später über diese hinausreichen. Dann wird der Propertywert
[internal-external] vergeben. Auch ist es möglich, dass Analepsen in Anachro-
nien vor der Basiserzählung beginnen, in sie hineinreichen und schließlich
über sie hinausgehen. In diesem Falle werden beide Propertywerte vergeben.


Mit der Property für den Umfang von Analepsen wird der Zeitraum, den
die Analepse in der Erzählung umfasst, bestimmt. Reicht die Anachronie
direkt an den Unterbrechungszeitpunkt in der Erzählung heran, bekommt
die Analepse den Propertywert [complete]. Endet die Anachronie aber an
einem beliebigen Punkt vor dem Unterbrechungszeitpunkt, wird der Wert
[partial] zugewiesen (vgl. Abbildung 9).

– <prolepsis>: Prolepsen sind Abweichungen von der chronologischen Reihen-
folge, in denen vorwegnehmend berichtet wird, was sich später ereignet hat.
Dabei werden nur tatsächliche Vorgriﬀe als Prolepsen annotiert, also solche,
die nicht im Laufe der Erzählung falsiﬁziert werden oder von vornherein als
Hypothesen formuliert sind, sich also als unzutreﬀende Darstellungen der
Ereignisse der ﬁktiven Welt bzw. als bloße Ahnungen, Wünsche, Hoﬀnungen
oder Vorhersagen herausstellen.
Prolepsen können mithilfe von Tag-Eigenschaften genauer hinsichtlich Reich-
weite (REACH) und Umfang (EXTENT) diﬀerenziert werden. Die Reich-
weite bezeichnet den Zeitpunkt der Prolepse in Bezug auf den Abstand zur
gegenwärtigen Handlung. Finden die in einer Prolepse berichteten Ereignisse
im Rahmen der Basiserzählung31 statt, wird der Propertywert [internal] ver-
geben. Liegt der Zeitpunkt der Ereignisse außerhalb der Basiserzählung, wird
dementsprechend die Prolepse als [external] markiert. Auch Mischformen
der Reichweite können annotiert werden. Liegt der Beginn einer Prolepse
innerhalb der Basiserzählung und ihr Ende außerhalb, wird der Propertywert
[internal-external] vergeben (vgl. Abbildung 8). Wenn Prolepsen im Rahmen
größerer Anachronien vorkommen, können die Prolepsen auch außerhalb
der Basiserzählung beginnen und später in diese hineinreichen. Dann wird
der Propertywert [external-internal] vergeben. Auch ist es möglich, dass
Prolepsen in Anachronien vor der Basiserzählung beginnen, in sie hinein-
reichen und schließlich über sie hinausgehen. In diesem Falle werden beide
Propertywerte vergeben.
Mit der Property für den Umfang von Prolepsen wird der Zeitraum, den
die Prolepse in der Erzählung umfasst, bestimmt. Beginnt die Prolepse am Unterbrechungszeitpunkt, wird der Wert [complete] vergeben. Beginnt die
Prolepse aber an einem beliebigen Punkt nach dem Unterbrechungszeitpunkt,
wird [partial] zugewiesen (vgl. Abbildung 9).

– <simullepsis>: Eine Simullepse ist die nacheinander erfolgende Darstellung gleichzeitig geschehender Ereignisse.

- Indikatoren:

– Zeitausdrücke, die Vorzeitigkeit, Nachzeitigkeit oder Gleichzeitigkeit aus-
drücken („vor einigen Jahren“, „am vorausgegangenen Tage“, „ein Jahr
später“, „nach drei Tagen“, „in demselben Augenblick“, „gleichzeitig“)

– Tempus (z. B. Plusquamperfekt in Texten, die generell im Präteritum erzählt sind, für Analepsen; Futur für Prolepsen)


- Beispiele:

– <analepsis> + [complete] + [external-internal]: „Noch nie seit sie hier war,
habe sie einen Mann Eisenstangen schleppen sehen.“ (Das polierte Männchen)
– <analepsis> + [partial] + [internal]: „Jetzt sah man, was geschehen war: der
Hansjörg hatte sich am mittleren Gelenk den Zeigeﬁnger der rechten Hand
abgeschossen.“ (Die Kriegspfeife)

– <prolepsis> + [complete] + [internal-external]: „Gleich beim ersten Anblick
des Hundes war er von der Zuneigung ergriﬀen worden, die dauern sollte bis
zu seinem letzten Atemzuge.“ (Krambambuli)

– <prolepsis> + [partial] + [external]: „Zwanzig Jahre lang habe ich den Tod
auf den Tag herbeigezogen, der in einer Stunde beginnen wird [. . . ]“ (Der
Tod)

– <simullepsis>: „’Ich bin nicht allein’, sagte ich [. . . ]. Dabei preßte sich mein
Arm, der die Decke über ihren Kopf gelegt hatte, krampfhaft auf jene Stelle,
wo ich den Mund vermutete [. . . ]“ (Die Schutzimpfung)

<achrony> (Achronisches Erzählen)

- Tagbeschreibung: Eine Achronie liegt vor, wenn in einer Textpassage alle
Zeitbezüge, die eine Verortung in der Geschichte ermöglichen, fehlen. Für die An-
notation konkreter Textpassagen wird normalerweise das Tag <achronic_element>
genutzt. Achronien können selbst Anachronien enthalten.

- Indikatoren:

– Tempus (Präsens)
– Allgemeine/verallgemeinernde Aussagen

- Beispiel:

– „Vorliebe empﬁndet der Mensch für allerlei Gegenstände. Liebe, die ech-
te, unvergängliche, die lernt er – wenn überhaupt – nur einmal kennen.“
(Krambambuli)


e. Überblick <order>
Tagstring
- Textabschnitte – Mindestgröße: Teilsatz

Unmarkierter Fall
- Chronologisches Erzählen

Indikatoren auf der Textoberﬂäche

- Zeitausdrücke, die Vorzeitigkeit, Gleichzeitigkeit oder Nachzeitigkeit ausdrücken
- Tempuswechsel

Tagging-Routine

1. Annotation aller nicht chronologisch dargestellten Textpassagen als Prolepse, Analepse, Simullepse oder Achronie.

2. Bei Anachronien: Speziﬁzierung von Umfang und Reichweite.

Beispiele

- <chronology>: „von ohngefähr erhob sie das Auge und traf mit dem blauesten
Strahle in seinen Blick. Er ward wie von einem Blitz durchdrungen. Sie strau-
chelte, und so schnell er auch hinzusprang, konnte er doch nicht verhindern,
daß sie nicht kurze Zeit in der reizendsten Stellung knieend vor seinen Füßen
lag“ (Der Pokal)
- <analepsis>: „Jetzt sah man, was geschehen war: der Hansjörg hatte sich
am mittleren Gelenk den Zeigeﬁnger der rechten Hand abgeschossen“ (Die
Kriegspfeife)
- <prolepsis>: „Zwanzig Jahre lang habe ich den Tod auf den Tag herbeigezogen, der in einer Stunde beginnen wird [. . . ]“ (Der Tod)
- <simullepsis>: „’Ich bin nicht allein’, sagte ich [. . . ]. Dabei preßte sich mein
Arm, der die Decke über ihren Kopf gelegt hatte, krampfhaft auf jene Stelle,
wo ich den Mund vermutete [. . . ]“ (Die Schutzimpfung)
- <achrony>: „Vorliebe empﬁndet der Mensch für allerlei Gegenstände. Liebe,
die echte, unvergängliche, die lernt er – wenn überhaupt – nur einmal kennen.“
(Krambambuli)