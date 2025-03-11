2.5 Zeitliches Verhältnis zwischen discours und histoire

Das Tagset für <time_relation_discours–histoire> enthält Kategorien zur Bestimmung des zeitlichen Zusammenhangs zwischen der Zeit des Diskurses und der Zeit der Geschichte.
Es ist in drei Untersets zum Taggen von Ordnung (<order>), Frequenz (<frequency>) und Dauer (<duration>) aufgeteilt.


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
