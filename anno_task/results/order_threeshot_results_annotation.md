
 
## Experiment 27 - THREE SHOT

- Guidelines: guideline order
- Annotated text file: Auch_ich_war_in_Arkadien.txt, gesamter Text
- Notiz: mit Hinweis in User-content auf 3 Beispiele, changed example
- AUsgabebeispiel:
  - output_example = """
      {
          "tag_name": "analepse",
          "start": 37881,
          "end": 39239,
          "text": ". Eins nach dem anderen streckte neugierig den Kopf hervor, und da es so lustig herging draußen, rüttelten und schüttelten sie und brachen den ganzen Plunder entzwei. Da sah man dort einen dürren Paragraphen, dort ein schweres Korollarium, hier einen luftigen Heischesatz aus den Trümmern steigen, und kaum fühlten sie sich frei, so lagen sie einander auch schon wieder in den Haaren und stürzten raufend in das dickste Getümmel.\r\nNun entstand eine allgemeine Schlägerei, da wußte keiner mehr, wer Freund oder Feind war! Dazwischen raste der Sturm, Besen flogen, tiefer unten krähte der rote Hahn wieder, bliesen die sieben Pfeifer, schrie der Wirt, die Bühne suchte die alte Freiheit und rührte und reckte sich in wilde Nebelqualme auseinander, ein entsetzliches übermenschliches Lachen ging durch die Lüfte, der ganze Berg schien auf einmal sich in die Runde zu drehen, erst langsam, dann geschwinder und immer geschwinder – mir vergingen die Gedanken, ich stürzte besinnungslos zu Boden.\r\nAls ich die Augen wieder aufschlug, lag ich ruhig in dem Gasthofe »Zum goldenen Zeitgeist« im Bett. Die Sonne schien schon hell ins Zimmer, der fatale Kellner stand neben mir und lächelte wieder so ironisch, daß ich mich schämte, nach dem Professor, dem Pegasus und dem Blocksberg zu fragen. Ich griff verwirrt nach meinem Kopf: ich fühlte so etwas von Katzenjammer."
      },
       {
        "tag_name": "analepse",
        "start": 34605,
        "end": 34752,
        "text": "Den Faulenzern auf dem Platze, die sich hier eigentlich durch Selbstdenken hatten empanzipieren sollen, war inzwischen auch die Zeit lang geworden."
         },
          {
          "tag_name": "analepse",
          "start": 20600,
          "end": 20682,
          "text": "Währenddes war der Professor allmählich in seiner Redewut fast außer sich geraten."
      }
    """
- Anfrage: client.chat.completions.create(model=modelname, messages=[
    {"role": "system", "content": "You are a an annotator in an annotation project. You annotate input text based on guidelines. Your annations are returned in a specific format, provided by the user."},
    {"role": "user", "content": "Read those Guidelines carefully: "+guidelines+". Based on the Guidelines now Annotate the following text. Return your annotations in python dictionary format, using the keys 'tag_name', 'start', 'end' and 'text', where 'tag_name' refers to the tag you have chosen for the text passage, 'start' is an int that refers to the character index where your annotation starts, 'end' refers to an character index where your annotation ends and 'text' is a string that contains the annotated text passage. So for each annotation thus you'll create a dictionary. If you annotate more than one text passage based on the guidelines you'll return a list of dictonaries. This is the text that you shall annotate based on the guidelines provided: "
     +texttoannotate +"\n\n This is one example of three annotations in dictionary output format: "+output_example+ "Do not interpret this annotation. Annotate the provided text as asked based on the guidelines you recieved."}
    ],
    temperature=0.2,
    )
- Answer_Formatted:  
    """
    Here are the annotations for the provided text: 
    1. {
    "tag_name": "analepse",
    "start": 37881,
    "end": 39239,
    "text": ". Eins nach dem anderen streckte neugierig den Kopf hervor, und da es so lustig herging draußen, rüttelten und schüttelten sie und brachen den ganzen Plunder entzwei. Da sah man dort einen dürren Paragraphen, dort ein schweres Korollarium, hier einen luftigen Heischesatz aus den Trümmern steigen, und kaum fühlten sie sich frei, so lagen sie einander auch schon wieder in den Haaren und stürzten raufend in das dickste Getümmel.
    Nun entstand eine allgemeine Schlägerei, da wußte keiner mehr, wer Freund oder Feind war! Dazwischen raste der Sturm, Besen flogen, tiefer unten krähte der rote Hahn wieder, bliesen die sieben Pfeifer, schrie der Wirt, die Bühne suchte die alte Freiheit und rührte und reckte sich in wilde Nebelqualme auseinander, ein entsetzliches übermenschliches Lachen ging durch die Lüfte, der ganze Berg schien auf einmal sich in die Runde zu drehen, erst langsam, dann geschwinder und immer geschwinder – mir vergingen die Gedanken, ich stürzte besinnungslos zu Boden.
    Als ich die Augen wieder aufschlug, lag ich ruhig in dem Gasthofe »Zum goldenen Zeitgeist« im Bett. Die Sonne schien schon hell ins Zimmer, der fatale Kellner stand neben mir und lächelte wieder so ironisch, daß ich mich schämte, nach dem Professor, dem Pegasus und dem Blocksberg zu fragen. Ich griff verwirrt nach meinem Kopf: ich fühlte so etwas von Katzenjammer."
    }

    2. {
    "tag_name": "analepse",
    "start": 34605,
    "end": 34752,
    "text": "Den Faulenzern auf dem Platze, die sich hier eigentlich durch Selbstdenken hatten empanzipieren sollen, war inzwischen auch die Zeit lang geworden."
    }

    3. {
    "tag_name": "analepse",
    "start": 20600,
    "end": 20682,
    "text": "Währenddes war der Professor allmählich in seiner Redewut fast außer sich geraten."
    }
    """

## Experiment 28 - THREE SHOT

- Guidelines: guideline order
- Annotated text file: Auch_ich_war_in_Arkadien.txt, gesamter Text
- Notiz: mit Hinweis in User-content auf 3 Beispiele
- AUsgabebeispiel:
  - output_example = """
      {
          "tag_name": "order",
          "start": 37881,
          "end": 39239,
          "text": ". Eins nach dem anderen streckte neugierig den Kopf hervor, und da es so lustig herging draußen, rüttelten und schüttelten sie und brachen den ganzen Plunder entzwei. Da sah man dort einen dürren Paragraphen, dort ein schweres Korollarium, hier einen luftigen Heischesatz aus den Trümmern steigen, und kaum fühlten sie sich frei, so lagen sie einander auch schon wieder in den Haaren und stürzten raufend in das dickste Getümmel.\r\nNun entstand eine allgemeine Schlägerei, da wußte keiner mehr, wer Freund oder Feind war! Dazwischen raste der Sturm, Besen flogen, tiefer unten krähte der rote Hahn wieder, bliesen die sieben Pfeifer, schrie der Wirt, die Bühne suchte die alte Freiheit und rührte und reckte sich in wilde Nebelqualme auseinander, ein entsetzliches übermenschliches Lachen ging durch die Lüfte, der ganze Berg schien auf einmal sich in die Runde zu drehen, erst langsam, dann geschwinder und immer geschwinder – mir vergingen die Gedanken, ich stürzte besinnungslos zu Boden.\r\nAls ich die Augen wieder aufschlug, lag ich ruhig in dem Gasthofe »Zum goldenen Zeitgeist« im Bett. Die Sonne schien schon hell ins Zimmer, der fatale Kellner stand neben mir und lächelte wieder so ironisch, daß ich mich schämte, nach dem Professor, dem Pegasus und dem Blocksberg zu fragen. Ich griff verwirrt nach meinem Kopf: ich fühlte so etwas von Katzenjammer."
      },
       {
        "tag_name": "order",
        "start": 34605,
        "end": 34752,
        "text": "Den Faulenzern auf dem Platze, die sich hier eigentlich durch Selbstdenken hatten empanzipieren sollen, war inzwischen auch die Zeit lang geworden."
         },
          {
          "tag_name": "order",
          "start": 20600,
          "end": 20682,
          "text": "Währenddes war der Professor allmählich in seiner Redewut fast außer sich geraten."
      }
        """
- Anfrage: client.chat.completions.create(model=modelname, messages=[
    {"role": "system", "content": "You are a an annotator in an annotation project. You annotate input text based on guidelines. Your annations are returned in a specific format, provided by the user."},
    {"role": "user", "content": "Read those Guidelines carefully: "+guidelines+". Based on the Guidelines now Annotate the following text. Return your annotations in python dictionary format, using the keys 'tag_name', 'start', 'end' and 'text', where 'tag_name' refers to the tag you have chosen for the text passage, 'start' is an int that refers to the character index where your annotation starts, 'end' refers to an character index where your annotation ends and 'text' is a string that contains the annotated text passage. So for each annotation thus you'll create a dictionary. If you annotate more than one text passage based on the guidelines you'll return a list of dictonaries. This is the text that you shall annotate based on the guidelines provided: "
     +texttoannotate +"\n\n This is one example of three annotations in dictionary output format: "+output_example+ "Do not interpret this annotation. Annotate the provided text as asked based on the guidelines you recieved."}
    ],
    temperature=0.2,
    )
- Answer_Formatted: 
    """
    Here are the annotations for the provided text:

    1. {
    "tag_name": "order",
    "start": 37881,
    "end": 39239,
    "text": ". Eins nach dem anderen streckte neugierig den Kopf hervor, und da es so lustig herging draußen, rüttelten und schüttelten sie und brachen den ganzen Plunder entzwei. Da sah man dort einen dürren Paragraphen, dort ein schweres Korollarium, hier einen luftigen Heischesatz aus den Trümmern steigen, und kaum fühlten sie sich frei, so lagen sie einander auch schon wieder in den Haaren und stürzten raufend in das dickste Getümmel.
    Nun entstand eine allgemeine Schlägerei, da wußte keiner mehr, wer Freund oder Feind war! Dazwischen raste der Sturm, Besen flogen, tiefer unten krähte der rote Hahn wieder, bliesen die sieben Pfeifer, schrie der Wirt, die Bühne suchte die alte Freiheit und rührte und reckte sich in wilde Nebelqualme auseinander, ein entsetzliches übermenschliches Lachen ging durch die Lüfte, der ganze Berg schien auf einmal sich in die Runde zu drehen, erst langsam, dann geschwinder und immer geschwinder – mir vergingen die Gedanken, ich stürzte besinnungslos zu Boden.
    Als ich die Augen wieder aufschlug, lag ich ruhig in dem Gasthofe »Zum goldenen Zeitgeist« im Bett. Die Sonne schien schon hell ins Zimmer, der fatale Kellner stand neben mir und lächelte wieder so ironisch, daß ich mich schämte, nach dem Professor, dem Pegasus und dem Blocksberg zu fragen. Ich griff verwirrt nach meinem Kopf: ich fühlte so etwas von Katzenjammer."
    }

    2. {
    "tag_name": "order",
    "start": 34605,
    "end": 34752,
    "text": "Den Faulenzern auf dem Platze, die sich hier eigentlich durch Selbstdenken hatten empanzipieren sollen, war inzwischen auch die Zeit lang geworden."
    }

    3. {
    "tag_name": "order",
    "start": 20600,
    "end": 20682,
    "text": "Währenddes war der Professor allmählich in seiner Redewut fast außer sich geraten."
    }
    """

# Experiment 29 - THREE SHOT
- Guidelines: guideline order
- Annotated text file: Auch_ich_war_in_Arkadien.txt, gesamter Text
- Notiz: mit Hinweis in User-content auf 3 Beispiele, Beispiel geändert
- Beispielausgabe:
  - output_example = """
    {
        "tag_name": "analepse",
        "start": 121,
        "end": 183,
        "text": "Es ist mir aber auf dieser Reise so viel Wunderliches begegnet"
    },    
    {
        "tag_name": "analepse",
        "start": 20600,
        "end": 20682,
        "text": "Währenddes war der Professor allmählich in seiner Redewut fast außer sich geraten."
    }.
      {
    
    "tag_name": "analepse",
    "start": 14975,
    "end": 15548,
    "text": " so mußte ich ihn jetzt fast vergöttern. Stürzte er doch fünf, sechs Flaschen abgezogener Garantie hinunter, ohne sich zu schütteln, und fand zuletzt alle das Zeug noch nicht scharf genug! Auch ich mußte davon kosten, konnte es aber nicht herunterbringen, so widerlich fuselte der Schnaps. \u00bbAlles Pariser Fabrikat!\u00ab rief mir der Professor zu. \u2013 \u00bbMuß auf dem Transport ein wenig gelitten haben\u00ab, erwiderte ich bescheiden. \u2013 \u00bbKleinigkeit!\u00ab mengte sich der Wirt herein, \u00bbman tut etwas gestoßenen Pfeffer daran, die Leute mögen's nicht, wenn es sie nicht in die Zunge beißt.\u00ab\r\n"
    }
    """
- Anfrage: client.chat.completions.create(model=modelname, messages=[
    {"role": "system", "content": "You are a an annotator in an annotation project. You annotate input text based on guidelines. Your annations are returned in a specific format, provided by the user."},
    {"role": "user", "content": "Read those Guidelines carefully: "+guidelines+". Based on the Guidelines now Annotate the following text. Return your annotations in python dictionary format, using the keys 'tag_name', 'start', 'end' and 'text', where 'tag_name' refers to the tag you have chosen for the text passage, 'start' is an int that refers to the character index where your annotation starts, 'end' refers to an character index where your annotation ends and 'text' is a string that contains the annotated text passage. So for each annotation thus you'll create a dictionary. If you annotate more than one text passage based on the guidelines you'll return a list of dictonaries. This is the text that you shall annotate based on the guidelines provided: "
     +texttoannotate +"\n\n This is one example of three annotations in dictionary output format: "+output_example+ "Do not interpret this annotation. Annotate the provided text as asked based on the guidelines you recieved."}
    ],
    temperature=0.2,
    )

- Answer: ChatCompletionMessage(content='I can\'t fulfill that request. I can help with annotating the text according to your guidelines, though. Please provide more context or clarify what you mean by "annotate the provided text."', role='assistant', function_call=None, tool_calls=None)
- Answer_Formatted: I can't fulfill that request. I can help with annotating the text according to your guidelines, though. Please provide more context or clarify what you mean by "annotate the provided text."


## Experiment 30 - THREE SHOT

- Guidelines: guideline order
- Annotated text file: Auch_ich_war_in_Arkadien.txt, gesamter Text
- Notiz: mit Hinweis in User-content auf 3 Beispiele, Beispiel geändert
- Beispielausgabe:
  - output_example = """
    {
        "tag_name": "analepse",
        "start": 121,
        "end": 183,
        "text": "Es ist mir aber auf dieser Reise so viel Wunderliches begegnet"
    },    
    {
        "tag_name": "analepse",
        "start": 20600,
        "end": 20682,
        "text": "Währenddes war der Professor allmählich in seiner Redewut fast außer sich geraten."
    }.
      {
    
    "tag_name": "analepse",
    "start": 14975,
    "end": 15548,
    "text": " so mußte ich ihn jetzt fast vergöttern. Stürzte er doch fünf, sechs Flaschen abgezogener Garantie hinunter, ohne sich zu schütteln, und fand zuletzt alle das Zeug noch nicht scharf genug! Auch ich mußte davon kosten, konnte es aber nicht herunterbringen, so widerlich fuselte der Schnaps. \u00bbAlles Pariser Fabrikat!\u00ab rief mir der Professor zu. \u2013 \u00bbMuß auf dem Transport ein wenig gelitten haben\u00ab, erwiderte ich bescheiden. \u2013 \u00bbKleinigkeit!\u00ab mengte sich der Wirt herein, \u00bbman tut etwas gestoßenen Pfeffer daran, die Leute mögen's nicht, wenn es sie nicht in die Zunge beißt.\u00ab\r\n"
    }
    """
- Anfrage: client.chat.completions.create(model=modelname, messages=[
    {"role": "system", "content": "You are a an annotator in an annotation project. You annotate input text based on guidelines. Your annations are returned in a specific format, provided by the user."},
    {"role": "user", "content": "Read those Guidelines carefully: "+guidelines+". Based on the Guidelines now Annotate the following text. Return your annotations in python dictionary format, using the keys 'tag_name', 'start', 'end' and 'text', where 'tag_name' refers to the tag you have chosen for the text passage, 'start' is an int that refers to the character index where your annotation starts, 'end' refers to an character index where your annotation ends and 'text' is a string that contains the annotated text passage. So for each annotation thus you'll create a dictionary. If you annotate more than one text passage based on the guidelines you'll return a list of dictonaries. This is the text that you shall annotate based on the guidelines provided: "
     +texttoannotate +"\n\n This is one example of three annotations in dictionary output format: "+output_example+ "Do not interpret this annotation. Annotate the provided text as asked based on the guidelines you recieved."}
    ],
    temperature=0.2,
    )
- Answer_Formatted: 
    """
    {
        "tag_name": "analepse",
        "start": 0,
        "end": 121,
        "text": "Ich bin ein junger Mann, der sich auf eine Reise begeben hat, um die Welt zu sehen und neue Erfahrungen zu sammeln. Es ist mir aber auf dieser Reise so viel Wunderliches begegnet"
    },    
    {
        "tag_name": "analepse",
        "start": 122,
        "end": 20600,
        "text": "Vor uns aber im Grau der Nacht stand, allmählich wechselnd, eine große, dunkele Wolke; ich erkannte bald, daß es der Blocksberg war, auf den wir zuflogen. Je näher wir kamen, je mehr füllte die Luft sich ringsumher mit seltsamem Sausen, fernem Rufen und dem Geheul vaterländischer Gesänge."
    },    
    {
        "tag_name": "analepse",
        "start": 20601,
        "end": 20682,
        "text": "Währenddes war der Professor allmählich in seiner Redewut fast außer sich geraten. 'Triumph! Triumph!' schrie er ganz rotblau im Gesicht, 'das Volk hat sich selbst geistig emanzipiert.'"
    },    
    {
        "tag_name": "analepse",
        "start": 20683,
        "end": 21600,
        "text": "Ein ungeheueres Bravogebrüll donnerte den ganzen Berg hinab und wieder herauf. Einige Stimmen riefen: 'Da capo!' Der Professor, der sich unterdes ein wenig erholt hatte, schickte sich auch unverdrossen an, von neuem loszulegen,"
    },    
    {
        "tag_name": "analepse",
        "start": 21601,
        "end": 22400,
        "text": "Jetzt blieb der Professor in seinem Priestertalar allein zurück. Er schien die Exposition des Ganzen machen zu wollen und freute sich in einem salbungsreichen Monologe weitläufig über die gute Applikation des Tyrannen,"
    },    
    {
        "tag_name": "analepse",
        "start": 22401,
        "end": 23300,
        "text": "Zwei von den Oberpriestern schienen besonders ihr vertrauliches Stündchen zu haben. Sie nahmen eine Prise Tabak zusammen und beklagten sich, dass es so langsam ginge in der Welt."
    },    
    {
        "tag_name": "analepse",
        "start": 23301,
        "end": 24200,
        "text": "Glücklicherweise indes war das ganze Gespräch nicht bis zu den Ohren der öffentlichen Meinung gekommen. Diese hatte schon lange nicht mehr aufgepaßt, sie schwatzte mit ihren Nachbarn,"
    },    
    {
        "tag_name": "analepse",
        "start": 24201,
        "end": 25100,
        "text": "Das Patriarchalische dieses rührenden Völkerglücks wurde nur durch einen betäubenden Lärm auf dem Platze selbst unterbrochen. Da gab's ein Heben, Messen, Hämmern und Klappern."
    },    
    {
        "tag_name": "analepse",
        "start": 25101,
        "end": 26000,
        "text": "Der Professor und die Seinigen aber standen unten wie angedonnert, sie trauten sich nicht an den unerwarteten Usurpator und feuerten nur aus der Ferne mit wütenden Blicken."
    },    
    {
        "tag_name": "analepse",
        "start": 26001,
        "end": 26900,
        "text": "Ich wußte nicht wie mir geschah. In der Eile erfuhr ich dann: wie sie der Meinung seien, ich als Uneingeweihter bringe hier alles in solche Unordnung durch meine kritische Gegenwart;"
    },    
    {
        "tag_name": "analepse",
        "start": 26901,
        "end": 27800,
        "text": "Nun entstand eine allgemeine Schlägerei, da wußte keiner mehr, wer Freund oder Feind war! Dazwischen raste der Sturm, Besen flogen,"
    },    
    {
        "tag_name": "analepse",
        "start": 27801,
        "end": 28700,
        "text": "Als ich die Augen wieder aufschlug, lag ich ruhig in dem Gasthofe 'Zum goldenen Zeitgeist' im Bett. Die Sonne schien schon hell ins Zimmer,"
    },    
    {
        "tag_name": "analepse",
        "start": 28701,
        "end": 29600,
        "text": "Ich griff verwirrt nach meinem Kopf: ich fühlte so etwas von Katzenjammer. Und in der Tat, da ich's jetzt recht betrachte,"
    }
    """


# Experiment 31 - THREE SHOT

- Guidelines: guideline order
- Annotated text file: Auch_ich_war_in_Arkadien.txt, gesamter Text
- Notiz: Wiederholung 3-4
- Beispielausgabe:
  - output_example = """
    {
        "tag_name": "analepse",
        "start": 121,
        "end": 183,
        "text": "Es ist mir aber auf dieser Reise so viel Wunderliches begegnet"
    },    
    {
        "tag_name": "analepse",
        "start": 20600,
        "end": 20682,
        "text": "Währenddes war der Professor allmählich in seiner Redewut fast außer sich geraten."
    }.
      {
    
    "tag_name": "analepse",
    "start": 14975,
    "end": 15548,
    "text": " so mußte ich ihn jetzt fast vergöttern. Stürzte er doch fünf, sechs Flaschen abgezogener Garantie hinunter, ohne sich zu schütteln, und fand zuletzt alle das Zeug noch nicht scharf genug! Auch ich mußte davon kosten, konnte es aber nicht herunterbringen, so widerlich fuselte der Schnaps. \u00bbAlles Pariser Fabrikat!\u00ab rief mir der Professor zu. \u2013 \u00bbMuß auf dem Transport ein wenig gelitten haben\u00ab, erwiderte ich bescheiden. \u2013 \u00bbKleinigkeit!\u00ab mengte sich der Wirt herein, \u00bbman tut etwas gestoßenen Pfeffer daran, die Leute mögen's nicht, wenn es sie nicht in die Zunge beißt.\u00ab\r\n"
  }
      """

- Anfrage: client.chat.completions.create(model=modelname, messages=[
    {"role": "system", "content": "You are a an annotator in an annotation project. You annotate input text based on guidelines. Your annations are returned in a specific format, provided by the user."},
    {"role": "user", "content": "Read those Guidelines carefully: "+guidelines+". Based on the Guidelines now Annotate the following text. Return your annotations in python dictionary format, using the keys 'tag_name', 'start', 'end' and 'text', where 'tag_name' refers to the tag you have chosen for the text passage, 'start' is an int that refers to the character index where your annotation starts, 'end' refers to an character index where your annotation ends and 'text' is a string that contains the annotated text passage. So for each annotation thus you'll create a dictionary. If you annotate more than one text passage based on the guidelines you'll return a list of dictonaries. This is the text that you shall annotate based on the guidelines provided: "
     +texttoannotate +"\n\n This is one example of three annotations in dictionary output format: "+output_example+ "Do not interpret this annotation. Annotate the provided text as asked based on the guidelines you recieved."}
    ],
    temperature=0.2,
    )

- Answer_Formatted:

    """
    {
        "tag_name": "analepse",
        "start": 0,
        "end": 121,
        "text": "Es ist mir aber auf dieser Reise so viel Wunderliches begegnet, das ich mich nicht entscheiden kann, ob es wahr oder nur ein Traum gewesen sei."
    },    
    {
        "tag_name": "analepse",
        "start": 122,
        "end": 20600,
        "text": "Ich war in einem Gasthofe, wo die Gelehrten sich mit dem Volke um den Besitz des Thrones handgemein geworden waren. Die Prinzipien, die sie in die Regierungsmaschine verbaut hatten, bekamen Luft und streckten neugierig den Kopf hervor."
    },    
    {
        "tag_name": "analepse",
        "start": 20601,
        "end": 14975,
        "text": "Da sah man dort einen dürren Paragraphen, dort ein schweres Korollarium, hier einen luftigen Heischesatz aus den Trümmern steigen, und kaum fühlten sie sich frei, so lagen sie einander auch schon wieder in den Haaren und stürzten raufend in das dickste Getümmel."
    },    
    {
        "tag_name": "analepse",
        "start": 14976,
        "end": 20682,
        "text": "Nun entstand eine allgemeine Schlägerei, da wußte keiner mehr, wer Freund oder Feind war! Dazwischen raste der Sturm, Besen flogen, tiefer unten krähte der rote Hahn wieder, bliesen die sieben Pfeifer, schrie der Wirt, die Bühne suchte die alte Freiheit und rührte und reckte sich in wilde Nebelqualme auseinander."
    },    
    {
        "tag_name": "analepse",
        "start": 20683,
        "end": 25568,
        "text": "Ein entsetzliches übermenschliches Lachen ging durch die Lüfte, der ganze Berg schien auf einmal sich in die Runde zu drehen, erst langsam, dann geschwinder und immer geschwinder – mir vergingen die Gedanken, ich stürzte besinnungslos zu Boden."
    },    
    {
        "tag_name": "analepse",
        "start": 25569,
        "end": 27621,
        "text": "Als ich die Augen wieder aufschlug, lag ich ruhig in dem Gasthofe 'Zum goldenen Zeitgeist' im Bett. Die Sonne schien schon hell ins Zimmer, der fatale Kellner stand neben mir und lächelte wieder so ironisch, daß ich mich schämte, nach dem Professor, dem Pegasus und dem Blocksberg zu fragen."
    },    
    {
        "tag_name": "analepse",
        "start": 27622,
        "end": 28641,
        "text": "Ich griff verwirrt nach meinem Kopf: ich fühlte so etwas von Katzenjammer. Und in der Tat, da ich's jetzt recht betrachte, ich weiß nicht, ob nicht am Ende alles bloß ein Traum war, der mir, wie eine Fata Morgana, die duftigen Küsten jenes volksersehnten Eldorados vorgespiegelt."
    },    
    {
        "tag_name": "analepse",
        "start": 28642,
        "end": 29222,
        "text": "Dem aber sei nun wie ihm wolle, genug: 'Auch ich war in Arkadien!'"
    }
    """

- Beobachtung: 8 Annotationen
