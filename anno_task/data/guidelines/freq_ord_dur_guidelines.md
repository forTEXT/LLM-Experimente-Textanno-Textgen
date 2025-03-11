2.5 Zeitliches Verhältnis zwischen discours und histoire

Das Tagset für <time_relation_discours–histoire> enthält Kategorien zur Bestimmung des zeitlichen Zusammenhangs zwischen der Zeit des Diskurses und der Zeit der Geschichte.
Es ist in drei Untersets zum Taggen von Ordnung (<order>), Frequenz (<frequency>) und Dauer (<duration>) aufgeteilt.


2.5.1 Ordnung
Das Unterset <order> enthält Kategorien für die Annotation des Verhältnisses der zeitlichen Ordnung von Diskurs und Geschichte (ordo artiﬁcialis und ordo naturalis).

a. Ort <order>
Das Unterset <order> beﬁndet sich im heureCLÉA Tagset unter: TimeTagset → timerelation_discours–histoire → order. 
Es teilt sich in die Tags <chronology>, <anachrony> und <achrony> auf. Das <anachrony>-Tag ist weiterhin in Tags aufgeteilt, mit denen die einzelnen Typen einer narrativen Anachronie annotiert werden können (<analepsis>, <prolepsis> und <simullepsis>).

b. Operationalisierung <order>
Unter dem Begriﬀ „Ordnung“ behandeln Lahn und Meister (2013) das Verhältnis von ordo naturalis und ordo artiﬁcialis. Die zugrunde liegende Frage lautet dabei: „Folgt der Erzähler auf der Diskurs-Ebene der ’realen’ Anordnung der Begebenheiten auf der Ebene der Geschichte (ordo naturalis), oder bietet er in seinem Bericht die Geschehnisse in einer künstlichen Ordnung dar, die den Erfordernissen des Erzählens angemessenen ist (ordo artiﬁcialis)?“ Insgesamt existieren drei Formen von Ordnung, die zum Erzählen von Geschehnissen verwendet werden können. Folgt der Erzähler der realen Anordnung, spricht man von chronologischem Erzählen. Wird die Reihenfolge der Ereignisse umgestellt, liegen so genannte Permutationen vor. Die entsprechenden Handlungselemente werden narrative Anachronien genannt. Eine dritte Form liegt vor, wenn alle Zeitbezüge fehlen, die eine Verortung in der Geschichte (histoire) ermöglichen würden, also weder eine Chronologie noch eine Anachronie vorliegt: die Achronie. 
Bei Achronien ist eine zeitliche Verknüpfung zur Haupthandlung nicht möglich. Lahn und Meister folgern daraus: „Achronien sind somit in der Regel weniger an die Geschichte [(histoire)] als vielmehr an den (unzeitlichen) Diskurs gebunden“ Lahn und Meister (2013, S. 142). Nach Genette liegt hingegen eine achronische Struktur vor, wenn die Zeitstruktur aufgrund der komplexen Verschränkung von Analepsen und Prolepsen nicht rekonstruierbar ist. Dabei scheint die Abgrenzung der Achronie sowohl bei sehr anachronisch gestalteten Erzählungen als auch bei Erzählungen, die sich über weite Teile deskriptiver Pausen bedienen, nicht eindeutig deﬁniert zu sein.
Bei den narrativen Anachronien wird im Wesentlichen zwischen zwei Typen unterschieden: In Analepsen wird nachholend berichtet, was sich früher eignet hat, und in Prolepsen wird entsprechend vorwegnehmend berichtet, was sich später ereignet hat. Darüber hinaus führen Lahn und Meister (2013) den Begriﬀ „Simullepse“ ein, der die (notgedrungen) linear nacheinander erfolgende Darstellung simultan stattﬁnden- der Handlungen bezeichnet (Ken Ireland spricht hier von „co-occurence“) (Lahn und Meister, 2013, S. 140).  
Weiter weisen Lahn und Meister (2013) darauf hin, dass chronologisches Erzählen nur ab ovo möglich ist, Erzählungen, die in medias res oder in ultimas res beginnen, müssen die Eingangszene durch Analepsen nachholen.29 Schließlich ergänzen Lahn und Meister (2013) die Bestimmung von Anachronien um die Kriterien Reichweite und Umfang, denn: „Anachronien können schließlich auch stark variieren zum einen auf der Ebene der Erzählzeit in Bezug auf die Dauer und zum anderen in Bezug auf die zeitliche Distanz zwischen dem gegenwärtigen Zeitpunkt der Erzählung und dem nachgeholten Geschehensmoment“ (Lahn und Meister, 2013, S. 141-142, ohne Hervorhebungen des Originaltextes).



d. Richtlinien für die Annotation von <order>

**Allgemein geltende Richtlinien**
Bevor die Tags des <order>-Tagsets sinnvoll angewendet werden können, sollten die jeweiligen Texte in Bezug auf narrative Ebenenwechsel analysiert werden. Nicht einander zugehörige narrative Ebenen sollten voneinander getrennt auf die zeitliche Ordnung hin analysiert werden. Das heißt auch, dass ein Zeitsprung, der mit einem Ebenenwechsel einhergeht, nicht als Zeitsprung annotiert wird – sobald eine neue narrative Ebene beginnt, wird die zu Beginn der jeweiligen Erzählung genutzte Zeit als neuer temporaler Nullpunkt gesetzt, in Bezug zu welchem die zeitliche Ordnung dieser Ebene analysiert wird. Entsprechend korreliert die zeitliche Ordnung auch nicht mit dem Zeitpunkt des Erzählens.

- Tagstring allgemein: Annotiert werden Textpassagen (mindestens Teilsätze).


**Richtlinien für einzelne Tags oder Untersets**

- <chronology> (Chronologisches Erzählen)
  - Tagbeschreibung: Beim chronologischen Erzählen folgt der Erzähler der realen Anordnung (ordo naturalis) der Geschehnisse auf der Ebene der histoire. Diese Erzählweise gilt als default, d.h. als unmarkierter Standardfall, und wird daher nicht annotiert.

  - Beispiel: „Da kam über den Markt eine jugendliche Gestalt [. . . ]; jetzt wollte sie den letzten Schritt tun, und von ohngefähr erhob sie das Auge und traf mit dem blauesten Strahle in seinen Blick. Er ward wie von einem Blitz durchdrungen. Sie strauchelte, und so schnell er auch hinzusprang, konnte er doch nicht verhindern, daß sie nicht kurze Zeit in der reizendsten Stellung knieend vor seinen Füßen lag. Er hob sie auf, sie sah ihn nicht an [. . . ]“ (Der Pokal)

- <anachrony> (Anachronisches Erzählen)
  - Tagbeschreibung: Beim anachronischen Erzählen weicht der Erzähler von der chronologischen Reihenfolge der Ereignisse ab. Generell ist es möglich, dass eine Anachronie eine weitere Anachronie enthält. Dabei sind alle Kombinationen möglich. Die Annotationen werden in diesem Fall verschachtelt. Anachronisches Erzählen kann drei verschiedene Formen annehmen:
    - <analepsis>: Analepsen sind Abweichungen von der chronologischen Reihenfolge, in denen nachholend berichtet wird, was sich früher ereignet hat. Dabei werden nur tatsächliche Rückgriﬀe als Analepse annotiert, also solche, die nicht im Laufe der Erzählung falsiﬁziert werden oder von Vornherein als hypothetisch gekennzeichnet sind, sich also als unzutreﬀende Darstellungen der Ereignisse der ﬁktiven Welt herausstellen. Manche Iterative (siehe Unterunterabschnitt 2.5.2 „Frequenz“, S. 54) mit eindeutiger Verweisrichtung in die Vergangenheit können zugleich auch Analepsen sein (bspw. „jeden Tag seit zwei Jahren“). Analepsen können mithilfe von Tag-Eigenschaften genauer hinsichtlich Reichweite (REACH) und Umfang (EXTENT) diﬀerenziert werden. Die Reichweite bezeichnet den Zeitpunkt der Analepse in Bezug auf den Abstand zur gegenwärtigen Handlung. Finden die in einer Analepse berichteten Ereignisse im Rahmen der Basiserzählung statt, wird der Propertywert [internal] vergeben. Liegt der Zeitpunkt der Ereignisse außerhalb der Basiserzählung, wird dementsprechend die Analepse als [external] markiert. Auch Mischformen der Reichweite können annotiert werden. Beginnt eine Analepse außerhalb der Basiserzählung und reicht in sie hinein, wird der Propertywert [external-internal] vergeben (vgl. Abbildung 8). Wenn Analepsen im Rahmen größerer Anachronien vorkommen, können die Analepsen auch in der Basiserzählung beginnen und später über diese hinausreichen. Dann wird der Propertywert [internal-external] vergeben. Auch ist es möglich, dass Analepsen in Anachronien vor der Basiserzählung beginnen, in sie hineinreichen und schließlich über sie hinausgehen. In diesem Falle werden beide Propertywerte vergeben. Mit der Property für den Umfang von Analepsen wird der Zeitraum, den die Analepse in der Erzählung umfasst, bestimmt. Reicht die Anachronie direkt an den Unterbrechungszeitpunkt in der Erzählung heran, bekommt die Analepse den Propertywert [complete]. Endet die Anachronie aber an einem beliebigen Punkt vor dem Unterbrechungszeitpunkt, wird der Wert [partial] zugewiesen.
    - <prolepsis>: Prolepsen sind Abweichungen von der chronologischen Reihenfolge, in denen vorwegnehmend berichtet wird, was sich später ereignet hat. Dabei werden nur tatsächliche Vorgriﬀe als Prolepsen annotiert, also solche, die nicht im Laufe der Erzählung falsiﬁziert werden oder von vornherein als Hypothesen formuliert sind, sich also als unzutreﬀende Darstellungen der Ereignisse der ﬁktiven Welt bzw. als bloße Ahnungen, Wünsche, Hoﬀnungen oder Vorhersagen herausstellen. Prolepsen können mithilfe von Tag-Eigenschaften genauer hinsichtlich Reich- weite (REACH) und Umfang (EXTENT) diﬀerenziert werden. Die Reichweite bezeichnet den Zeitpunkt der Prolepse in Bezug auf den Abstand zur gegenwärtigen Handlung. Finden die in einer Prolepse berichteten Ereignisse im Rahmen der Basiserzählung31 statt, wird der Propertywert [internal] vergeben. Liegt der Zeitpunkt der Ereignisse außerhalb der Basiserzählung, wird dementsprechend die Prolepse als [external] markiert. Auch Mischformen der Reichweite können annotiert werden. Liegt der Beginn einer Prolepse innerhalb der Basiserzählung und ihr Ende außerhalb, wird der Propertywert [internal-external] vergeben (vgl. Abbildung 8). Wenn Prolepsen im Rahmen größerer Anachronien vorkommen, können die Prolepsen auch außerhalb der Basiserzählung beginnen und später in diese hineinreichen. Dann wird der Propertywert [external-internal] vergeben. Auch ist es möglich, dass Prolepsen in Anachronien vor der Basiserzählung beginnen, in sie hinein- reichen und schließlich über sie hinausgehen. In diesem Falle werden beide Propertywerte vergeben. Mit der Property für den Umfang von Prolepsen wird der Zeitraum, den die Prolepse in der Erzählung umfasst, bestimmt. Beginnt die Prolepse am Unterbrechungszeitpunkt, wird der Wert [complete] vergeben. Beginnt die Prolepse aber an einem beliebigen Punkt nach dem Unterbrechungszeitpunkt, wird [partial] zugewiesen.
    - <simullepsis>: Eine Simullepse ist die nacheinander erfolgende Darstellung gleichzeitig geschehender Ereignisse.
  - Indikatoren:
    - Zeitausdrücke, die Vorzeitigkeit, Nachzeitigkeit oder Gleichzeitigkeit ausdrücken („vor einigen Jahren“, „am vorausgegangenen Tage“, „ein Jahr später“, „nach drei Tagen“, „in demselben Augenblick“, „gleichzeitig“)
    - Tempus (z. B. Plusquamperfekt in Texten, die generell im Präteritum erzählt sind, für Analepsen; Futur für Prolepsen)
    - Beispiele:
      - <analepsis> + [complete] + [external-internal]: „Noch nie seit sie hier war, habe sie einen Mann Eisenstangen schleppen sehen.“ (Das polierte Männchen)
      - <analepsis> + [partial] + [internal]: „Jetzt sah man, was geschehen war: der Hansjörg hatte sich am mittleren Gelenk den Zeigeﬁnger der rechten Hand abgeschossen.“ (Die Kriegspfeife)
      - <prolepsis> + [complete] + [internal-external]: „Gleich beim ersten Anblick des Hundes war er von der Zuneigung ergriﬀen worden, die dauern sollte bis zu seinem letzten Atemzuge.“ (Krambambuli)
      - <prolepsis> + [partial] + [external]: „Zwanzig Jahre lang habe ich den Tod auf den Tag herbeigezogen, der in einer Stunde beginnen wird [. . . ]“ (Der Tod)
      - <simullepsis>: „’Ich bin nicht allein’, sagte ich [. . . ]. Dabei preßte sich mein Arm, der die Decke über ihren Kopf gelegt hatte, krampfhaft auf jene Stelle, wo ich den Mund vermutete [. . . ]“ (Die Schutzimpfung)

- <achrony> (Achronisches Erzählen)
  - Tagbeschreibung: Eine Achronie liegt vor, wenn in einer Textpassage alle Zeitbezüge, die eine Verortung in der Geschichte ermöglichen, fehlen. Für die Annotation konkreter Textpassagen wird normalerweise das Tag <achronic_element> genutzt. Achronien können selbst Anachronien enthalten.
  - Indikatoren:
    - Tempus (Präsens)
    - Allgemeine/verallgemeinernde Aussagen
    - Beispiel:
      - „Vorliebe empﬁndet der Mensch für allerlei Gegenstände. Liebe, die echte, unvergängliche, die lernt er – wenn überhaupt – nur einmal kennen.“ (Krambambuli)



2.5.3 Dauer
Das Unterset <duration> enthält Kategorien zur Bestimmung von Phänomenen der Dauer, also zum Erzähltempo bzw. der Erzählgeschwindigkeit.

a. Ort <duration>
Das Unterset <duration> zum Taggen von Phänomenen der Dauer in Texten (Erzähltempo bzw. Erzählgeschwindigkeit) beﬁndet sich im heureCLÉA Tagset unter: TimeTagset → time_relation_discours–histoire → duration. Es unterteilt sich in die Kategorien <isochrony> und <anisochrony>, wobei nur <anisochrony> weitere Tags enthält.

b. Operationalisierung <duration>
Die Kategorie Dauer beschreibt Phänomene, die das Erzähltempo bzw. die Erzählgeschwindigkeit betreﬀen. Dabei wird „[d]ie Zeitdauer eines Elements der Geschichte 
(der erzählten Zeit) [. . . ] in Beziehung gesetzt zu der Zeitdauer seiner Schilderung im Diskurs (der Erzählzeit)“ (Lahn und Meister, 2013, S. 143).
Relevant ist bei der Analyse des Erzähltempos meist nicht das Verhältnis von erzählter Zeit zu Erzählzeit im Gesamttext, da Angaben der Art Seitenanzahl/Tag eher wenig aussagekräftig sind (hier kann man von absolutem Erzähltempo sprechen). Interessanter ist es vielmehr, die Variation im Erzähltempo in den einzelnen Textabschnitten zu analysieren, da die einzelnen Typen meist im Wechsel zum Einsatz kommen. Im Wesentlichen werden drei Typen des Erzähltempos unterschieden:

- Zeitraﬀung: Hier ist die erzählte Zeit (histoire) deutlich länger als die Erzählzeit (discours). Es liegt also eine geringe Informationsmenge vor. Der Extremfall, in dem Zeiträume übersprungen und bestimmte Geschehenselemente nicht dargestellt werden, heißt „Ellipse“ bzw. „Aussparung“ oder „Zeitsprung“. Je nachdem, ob die Ellipse markiert oder unmarkiert ist, unterscheidet man weiter zwischen expliziter und impliziter Ellipse.

- Zeitdeckendes bzw. synchrones Erzählen: Hier stimmen erzählte Zeit und Erzählzeit überein. Typischerweise ist das in längeren Dialogpassagen in direkter Rede der Fall.

- Zeitdehnung: Hier ist die erzählte Zeit deutlich kürzer als die Erzählzeit. Es liegt also eine hohe Informationsmenge vor. Im Extremfall kommt es zu einer so genannten deskriptiven Pause, wenn der Eindruck entsteht, dass die Zeit stillsteht. Dies ist z. B. der Fall, wenn der Erzähler einen Kommentar oder eine Beschreibung einführt.

Zeitdeckendes Erzählen ist demnach eine Isochronie, während Zeitraﬀung und Zeitdehnung Anisochronien sind. Das Tagset wird daher so aufgebaut, dass vorerst in diese zwei Kategorien unterschieden wird. In Anlehnung an die fünf Kategorien der Erzähldauer nach Lahn und Meister werden die Anisochronien weiter diﬀerenziert.
Zum Überblick (Lahn und Meister, 2013, S. 146):

- Ellipse: erzählte Zeit ∞ > Erzählzeit
- Zeitraﬀung: erzählte Zeit > Erzählzeit
- Zeitdeckendes Erzählen (Isochronie): erzählte Zeit = Erzählzeit
- Zeitdehnung: erzählte Zeit < Erzählzeit
- Deskriptive Pause: erzählte Zeit < ∞ Erzählzeit

Eine besondere Eigenschaft der Kategorie Dauer besteht darin, dass Dauerphänomene für jede neu auftretende Erzählebene jeweils in Relation zu jeder bestehenden Ebene analysiert werden muss. So kann die Dauer einer Binnenerzählung mit einem neuen Erzähler beispielsweise zum einen daraufhin analysiert werden, mit welcher Geschwindigkeit der Redebeitrag des Binnenerzählers wiedergegeben wird – beispielsweise zeitdeckend, sofern er wörtlich zitiert wird. In diesem Fall wird die Dauer in Relation zur primären Erzählebene analysiert. Zum anderen kann die Dauer der fraglichen Passage jedoch auch danach analysiert werden, mit welcher Erzählgeschwindigkeit der Binnenerzähler im Rahmen seiner Binnenerzählung von Ereignissen berichtet – beispielsweise, um den Standardfall zu nennen, leicht geraﬀt. Dauer wird in diesem Fall in Relation zur sekundären Erzählebene analysiert. Ähnlich verhält es sich mit neuen Ebenen, die eine andere Welt beinhalten (= ontologische Ebenenüberschreitung), hier handelt es sich allerdings auf der primären Ebenen meist um eine Pause. Wie diese Ebenenabhängigkeit von Dauer im Untertagset <duration> umgesetzt ist, wird im Abschnitt „Richtlinien für die Annotation von <duration>“ erläutert (S. 63).

Wie die Anwendung gezeigt hat, birgt die Kategorie Dauer noch einige Probleme, die eine robuste Anwendung des Dauer-Konzepts entweder generell erschweren oder aber weiter erforscht werden müssten, um die Reproduzierbarkeit von Dauer-Annotationen zu befördern:

1. Generell ist es häuﬁg schwierig festzustellen, über welche Zeitspanne sich Ereignisse in der ﬁktiven Welt erstrecken. Da Dauer die Relation zwischen Zeitspannen in der ﬁktiven Welt und Erzählzeit beschreibt, wird die Anwendung dieser Kategorie somit nicht selten zu einer tentativen Angelegenheit.

2. Um Dauer robust analysieren zu können, wäre es weiterhin eigentlich notwendig, einen geeigneten Ereignisbegriﬀ zu deﬁnieren, um herauszuﬁnden, was jeweils als kleinste Ereigniseinheit verstanden wird. Diese Frage ist beispielsweise relevant, um Ellipsen sinnvoll bestimmen zu können: Ab welcher Größenordnung gilt die Aussparung einer Zustandsveränderung aus der Erzählung als Ellipse?

3. Es ist ein bisher nicht ausreichend beachtetes Problem, dass die Analyse der Dauer deutlich von der Segmentierung eines Textes abhängt: Die Einschätzung der Erzähldauer variiert je nachdem, wie lang die Textpassage ist, für die die Dauer bestimmt werden soll.

4. Dauer müsste eventuell relational zum noch genauer zu bestimmenden Konzept der Handlungsstränge analysiert werden: Nicht selten wird in narrativen Texten das, was wir tentativ als „Haupterzählung“ bezeichnen würden, durch Einschübe unterbrochen, in denen von weniger zentralen ‘Nebenhandlungen’ berichtet wird. In Relation zur ‘Haupterzählung’ würde ein solcher Einschub eine Erzählpause darstellen – allerdings kann die Erzähldauer auch separat für den Einschub selbst bestimmt werden. Denkbar ist hier eine Handhabung vergleichbar zu derjenigen, die wir oben für die Dauer-Analyse relational zu narrativen Ebenen vorgestellt haben.

5. Ein Problem, das mit dem unterschiedlicher Handlungsstränge verwandt zu sein scheint, ergibt sich, wenn dieselbe Zeitspanne mehrmals mit jeweils unterschiedlichem Fokus erzählt wird, ohne dass sich Ort, Zeit und Personal ändern. Möglich erscheint hier die Handhabung, die Wiederholung als Pause zu betrachten, da gewissermaßen kein ‘neuer Teil’ des Zeitstrahls der Geschichte abgedeckt wird. Allerdings erscheint diese Regelung nicht unproblematisch. Hier sind also weitere Untersuchungen, auch unter Einbeziehung von Frequenz-Phänomenen wie Repetition, erforderlich.

c. Tagset <duration>

d. Richtlinien für die Annotation von <duration>

**Allgemein gültige Hinweise**

- Tagstring allgemein: Annotiert werden Textpassagen (mindestens Teilsätze). Wenn zwei Passagen mit dem gleichen Dauerphänomen aneinander anschließen, dann ist es sinnvoll, dennoch zwei einzelne Tags zu vergeben, sofern sich die Passagen inhaltlich voneinander abgrenzen lassen oder das fragliche Dauerphänomen in verschiedener Ausprägung vorkommt (z. B. stark geraﬀtes vs. leicht geraﬀtes Erzählen.)

**Hinweise für einzelne Tags oder Untersets**

- <isochrony> (Zeitdeckendes Erzählen)
  - Tagbeschreibung: Zeitdeckendes Erzählen liegt in Passagen vor, in denen erzählte Zeit und Erzählzeit übereinstimmen. Das ist beispielsweise in längeren Passagen wörtlicher Rede der Fall – dies gilt für die Dauer der Sprechaktwiedergabe und stellt damit eine Daueranalyse relativ zur primären Erzählebene dar.
  - Indikatoren: zitierte Rede
  - Beispiel: „‘Drei! Nicht wahr?’ ‘Ja! Erst!!’ ‘Schön! . . . Ist noch Bier da?’ ‘Ja! Ich glaube.’ Jens ging nachsehn. Seine dicken Filzsocken machten seine Schritte unhörbar. Vor dem Bette blieb er einen Augenblick stehn. ‘Du! Vielleicht wird’s doch besser!’ Olaf zuckte nur die Achseln. Eins . . . zwei . . . drei . . . fünf Stück noch. ‘Dir auch eine?’ ‘Nein! Danke!’ ‘Aah! das tut wohl! – Übrigens . . . scheußlicher Muﬀ hier!’ ‘Ja! Zum Zerschneiden!’ ‘Schauderhaft! Schauderhaft! ’“ (Ein Tod)

- <anisochrony> (Nicht-zeitdeckendes Erzählen)
  - Tagbeschreibung: Nicht-zeitdeckendes Erzählen liegt in Passagen vor, in denen die erzählte Zeit länger (<summary>) oder kürzer ist (<scene>) als die Erzählzeit.
    - <summary>: <summary> liegt vor, wenn zeitraﬀend erzählt wird, d.h. wenn in kurzer Zeit viele Ereignisse berichtet werden. Eine Extremform des zeitraffenden Erzählens stellt der Zeitsprung dar, der als <ellipsis>in Form eines Untertags für <summary> operationalisiert ist. Ein Zeitsprung liegt dann vor, wenn Ereignisse von der Erzählung übersprungen werden. Dabei gelten allerdings rein inhaltliche Auslassungen nicht als Ellipse, z. B. das Übergehen einer bestimmten (wenn auch ggf. relevanten) Eigenschaft eines Ereignisses, von dem insgesamt aber berichtet wird – für das Vorliegen einer Ellipse ist es notwendig, dass ein Teil des Zeitstrahls der Geschichte gar nicht erzählt wird. Zeitsprünge werden weiter danach diﬀerenziert, ob sie explizit oder implizit im Text vorliegen (mithilfe der Werte [explicit] und [implicit] der Property ELLIPSIS_TYPE). Da implizite Ellipsen nicht an der Textoberﬂäche festgemacht werden können, wird das Tag für sie einem Leerzeichen an der betreﬀenden Position im Text zugewiesen.35 Satzzeichen, die Ellipsen anzeigen, werden dabei als implizite Ellipsen gewertet. Da implizite Ellipsen nicht sprachlich kodiert sind, werden hier – sofern sie nicht durch Satzzeichen repräsentiert werden, Leerzeichen annotiert.
    - <scene>: <scene> liegt vor, wenn zeitdehnend erzählt wird, d.h. wenn viel Zeit aufgewandt wird, um von wenigen Ereignissen zu berichten. Eine Extremform des zeitdehnenden Erzählens stellt die Pause, die als <pause> in Form eines Untertags für <scene> operationalisiert ist. Eine Pause liegt dann vor, wenn die Erzählung von Ereignissen unterbrochen wird, beispielsweise durch deskriptive Einschübe, wertende Kommentare oder Kapitelüberschriften. Zu unterscheiden sind allerdings solche deskriptiven Einschübe, die mit (impliziten) Zeitinformationen einhergehen, von solchen, die ohne solche Marker vorkommen: Nur bei letzteren handelt es sich durchweg um Erzählpausen. Werden dagegen Zustände mit identiﬁzierbarer zeitlicher Ausdehnung geschildert (z. B. „Drei Tage lang blieb ihr Zimmer unverändert“), dann können auch andere Dauerphänomene vorliegen (– im hier angeführten Beispiel wird raﬀend erzählt). 
    Wie oben angemerkt, muss Dauer muss in Passagen, in denen zusätzliche illokutionäre Ebenen auftreten, jeweils in Relation zu jeder Ebene analysiert werden. Dafür wird eine Property für alle Dauer-Kategorien angelegt, die NARRATIVE_LEVEL heißt und für die als Wert jeweils die Ebene bestimmt wird, in Bezug auf welche das jeweilige <duration>-Tag zu verstehen ist. Für jede Passage mit zusätzlicher Ebene wird dann zum einen die Dauer der Sprechakt-Wiedergabe bestimmt (Propertywert [primary_narration]) und zum anderen die Dauer der auf der neuen Ebene erzählten Geschichte (Propertywert [secondary_narration]).

  - Indikatoren:
    - Adjektive, die die Dauer von Ereignissen anzeigen
    - Zeitausdrücke, die Zeitspannen oder Zeitsprünge anzeigen
    - Metanarration

  - Beispiele:
    - <summary>: „Acht Wochen habe ich in dieser Entlegenheit verlebt“ (Traum-land. Eine Episode.)
    - <ellipsis> [explicit]: „So war ein Jahr vorübergegangen.“ (Der Pokal)
    - <ellipsis> [implicit]: „[. . . ] ich stürzte besinnungslos zu Boden. Als ich die Augen wieder aufschlug, lag ich ruhig in dem Gasthofe »Zum goldenen Zeitgeist« im Bett.“ (Auch ich war in Arkadien)
    - <scene>: „Ich trat an das Fenster und bemerkte – obgleich wir uns im zweiten Stockwerk befanden – dicht vor den Scheiben ein gewaltiges, störriges und sträubiges Roß, das mit ﬂatternder Mähne in der Luft zu schweben schien.“(Auch ich war in Arkadien)
    - <pause>: „Albert schloß endlich auf und sagte: »Nun sind wir zur Stelle.«
    Ein großes hohes Zimmer empﬁng sie, das mit rotem Damast ausgeschlagen
    war, den goldene Leisten einfaßten, die Sessel waren von dem nämlichen
    Zeuge, und durch rote schwerseidne Vorhänge, welche niedergelassen waren,
    schimmerte ein purpurnes Licht. »Verweilt einen Augenblick«, sagte der Alte,
    indem er in ein anderes Gemach ging.“ (Der Pokal)



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

