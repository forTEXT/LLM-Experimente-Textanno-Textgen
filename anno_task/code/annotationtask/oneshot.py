############################################################################################### IMPORTS
import os
import json

# Example: reuse your existing OpenAI setup
from openai import OpenAI


############################################################################################### FUNCTIONS
def read_guidelines(path):
    """reads annotation guidelines returns annotation guidelines as str"""
    file = open(path, "r")
    guidelines = file.read()

    return guidelines




def read_text_to_annotate(textpath):
    """Gets path, returns text to be annotated"""
    file_text = open(textpath, "r")
    testtext = file_text.read()
    print(len(testtext))
    return testtext


   

def read_json (path_to_json):
    with open(path_to_json, encoding="utf-8") as f:
        data = json.load(f)
    
    return data


def clean_json(path_to_json):
    """Cleans input json"""
    with open(path_to_json, encoding="utf-8") as f:
        data = json.load(f)

    #lösche IDS
    for item in data:
        if "anno_id" in item:
            del item["anno_id"]
        if "tag_id" in item:
            del item["tag_id"]
        # if "tag_name" in item:
        #     item["tag_name"] = ""

    
    print(len(data))
    #print(data)
    return data

def create_example_output(json1,json2,json3):
    """Reads JSONS and merges them"""

    merged_data = json1 + json2 + json3
    print(len(merged_data))
    print(merged_data)
    print(type(merged_data))
    
    return merged_data


# def save_json(merged_json):
#         #save json
#     #final_json = json.dumps(merged_json, indent = 4)
#     # x = json.dumps(merged_json)
#     # print(x)
#     # print(type(x))

#     with open("pathto/data/annotationen/json_notags/order_notags.json", "w") as new_f:
#         json.dump(merged_json, new_f, indent= 4, ensure_ascii=None)

    
# JSONS vorbereiten, COde ausführen 
#save_json(json_order_exampleoutput)



def call_llm(texttoannotate, guidelines, output_example):
    """Calls llm, returns output as chat completion"""
    # Point to the local server
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
    modelname= "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF"

    # mari: base_url="http://localhost:1234/v1"
    # evelyn : "http://127.0.0.1:1234/v1"
    
    if len(texttoannotate)==0:
        print("No text to annotate")

    if len(guidelines) == 0:
        print("No guidelines")

    completion = client.chat.completions.create(model=modelname, messages=[
    {"role": "system", "content": "You are a an annotator in an annotation project. You annotate input text based on guidelines. Your annations are returned in a specific format, provided by the user."},
    {"role": "user", "content": "Read those Guidelines carefully: "+guidelines+". Based on the Guidelines now Annotate the following text. Return your annotations in python dictionary format, using the keys 'tag_name', 'start', 'end' and 'text', where 'tag_name' refers to the tag you have chosen for the text passage, 'start' is an int that refers to the character index where your annotation starts, 'end' refers to an character index where your annotation ends and 'text' is a string that contains the annotated text passage. So for each annotation thus you'll create a dictionary. If you annotate more than one text passage based on the guidelines you'll return a list of dictonaries. This is the text that you shall annotate based on the guidelines provided: "
     +texttoannotate +"\n\n This is one example of three annotations in dictionary output format: "+output_example+ "Do not interpret this annotation. Annotate the provided text as asked based on the guidelines you recieved."}
    ],
    temperature=0.2,
    )

    print(completion.choices[0].message)
    return  completion.choices[0].message.content


def manyshot_call_llm(baseurl, texttoannotate, guidelines, output_example):
    """Calls llm, returns output as chat completion. basurl as a parameter if multiple coders use code"""
    # Point to the local server
    client = OpenAI(base_url=baseurl, api_key="lm-studio")
    modelname= "meta-llama-3.1-8b-instruct"


    if len(texttoannotate)==0:
        print("No text to annotate")

    if len(guidelines) == 0:
        print("No guidelines")

    completion = client.chat.completions.create(model=modelname, messages=[
    {"role": "system", "content": "You are a an annotator in an annotation project. You annotate input text based on guidelines. Your annations are returned in a specific format, provided by the user."},
    {"role": "user", "content": "Read those Guidelines carefully: "+guidelines+". Based on the Guidelines now Annotate the following text. Return your annotations in python dictionary format, using the keys 'tag_name', 'start', 'end' and 'text', where 'tag_name' refers to the tag you have chosen for the text passage, ‚start‘ is an int that refers to the character index where your annotation starts, 'end' refers to an character index where your annotation ends and 'text' is a string that contains the annotated text passage. So for each annotation thus you'll create a dictionary. If you annotate more than one text passage based on the guidelines you'll return a list of dictonaries. This is the text that you shall annotate based on the guidelines provided: "
     +texttoannotate +"\n\n This is one example of annotations in dictionary output format for another text: "+output_example+ "Do not interpret this annotation. Annotate the provided text as asked based on the guidelines you recieved."}
    ],
    temperature=0.2,
    )

    print(completion.choices[0].message)
    return  completion.choices[0].message.content



def call_and_write_llm(baseurl, texttoannotate, guideline_path, anno_example):
    """
    Führt LLM-Prompt aus, ruft dafür manyshot_call_llm auf.
    Extrahiert den Dateinamen aus den gegebenen Pfaden für Guidelines und Inputannotationen, 
    formatiert die Informationen und schreibt sie in die angegebene Datei.

    :baseurl: initiiert den Local Server
    :texttoannotate: Text, der annotiert werden soll
    :param guideline_path: Der Pfad zur Guidelines-Datei.
    :param anno_example: Beispiel von Annotationen 
    """
    
    #output_file = "pathto/Code/annotate_ord_freq_dur/order_fullshot_results.md"
    output_file = "/Users/Gius/github/LLMs_LiLi/annotate_ord_freq_dur/order_fullshot_results.md"


    # Dateinamen aus den Pfaden extrahieren
    guideline_filename = os.path.basename(guideline_path)
    example_annotation_filename = os.path.basename(anno_example)
    texttoannotate_filename = os.path.basename(texttoannotate)
    # Formatieren der Ausgabe
    guideline_info = f"- Guidelines: {guideline_filename}"
    example_annotations = f"- Input Annotation: {example_annotation_filename}"

    # annotation_text = read_text_to_annotate("pathto/data/raw/heureclea-sourcedocuments/Blumen.txt")
    # print("TYPE OF ANNO TEXT: ", type(annotation_text))

    modelanswer = manyshot_call_llm(baseurl, read_text_to_annotate(texttoannotate), read_guidelines(guideline_path), str(clean_json(anno_example)))
    
    # Informationen in die Datei schreiben
    with open(output_file, 'a') as file:
        file.write('\n' + guideline_info + '\n')
        file.write(example_annotations + '\n')
        file.write('- Annotated text file: ' + texttoannotate_filename + '\n')
        file.write('- Answer: '+ modelanswer + '\n')
    
    print(modelanswer)


# Beispielaufruf der Funktion
# input_annotation_path = "pathto/data/input_annotations/annotations.txt"
# custom_string = "Ein Beispiel"
# output_file = "pathto/Code/annotate_ord_freq_dur/order_fullshot_results.md"

# texttobeannotated_path = "pathto/Code/data/annotationen/annotationsjson/Blumen_order_Annotator3.json"



############################################################################################### APPLY FUNCTIONS


# GUIDELINES
guidelinepath_mari = "pathto/Code/data/guidelines/guideline_order.md"
guidelinepath_evelyn = "/Users/Gius/github/LLMs_LiLi/data/guidelines/guideline_order.md"


# TEXT TO ANNOTATE

anno_text_mari ="pathto/Code/data/raw/heureclea-sourcedocuments/Blumen.txt"
anno_text_evelyn = "/Users/Gius/github/LLMs_LiLi/data/raw/heureclea-sourcedocuments/Blumen.txt"


# OUTPUT EXAMPLE ANNOTATIONS
annotation_examples_mari = "pathto/Code/data/annotationen/annotationsjson/Auch_ich_war_in_Arkadien_order_Annotator1.json"
annotation_examples_evelyn = "/Users/Gius/github/LLMs_LiLi/data/annotationen/annotationsjson/Auch_ich_war_in_Arkadien_order_Annotator1_kurz.json"


# OUTPUT EXAMPLE SOURCE TEXT
anno_example_text =read_text_to_annotate("Heurecla/Code/data/raw/heureclea-sourcedocuments/Auch_ich_war_in_Arkadien.txt")



# marispfad = pathto/Code/data/annotationen/annotationsjson/Auch_ich_war_in_Arkadien_order_Annotator1.json
# evelyns pfad: /Users/Gius/github/LLMs_LiLi/data/annotationen/annotationsjson/Auch_ich_war_in_Arkadien_order_Annotator1.json"

# baseurls

mari_base_url= "http://localhost:1234/v1"
evelyn_base_url =  "http://127.0.0.1:1234/v1"
    

#call_and_write_llm(mari_base_url, anno_text_mari, guidelinepath_mari, annotation_examples_mari)

call_and_write_llm(evelyn_base_url, anno_text_evelyn, guidelinepath_evelyn, annotation_examples_evelyn)

#print(read_text_to_annotate("pathto/Code/data/raw/heureclea-sourcedocuments/Blumen.txt"))
#print(type(read_text_to_annotate("pathto/Code/data/raw/heureclea-sourcedocuments/Blumen.txt")))

# Function
# call llm, Write result to txt, info example text, example annotations an

# print(anno_text)
# print(guidelines_order)


# output_example = """
#       {
#           "tag_name": "analepse",
#           "start": 121,
#           "end": 183,
#           "text": "Es ist mir aber auf dieser Reise so viel Wunderliches begegnet"
#       },    
#       {
#           "tag_name": "analepse",
#           "start": 20600,
#           "end": 20682,
#           "text": "Währenddes war der Professor allmählich in seiner Redewut fast außer sich geraten."
#       }
#         """

output_example = """
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

#first_one_shot = call_llm(anno_example_text,read_guidelines(guidelinepath_mari),output_example)


#print(first_one_shot)



############### OLD

# output_example = """
#     {
#         "tag_name": "analepse",
#         "start": 121,
#         "end": 183,
#         "text": "Es ist mir aber auf dieser Reise so viel Wunderliches begegnet"
#     },    
#     {
#         "tag_name": "analepse",
#         "start": 20600,
#         "end": 20682,
#         "text": "Währenddes war der Professor allmählich in seiner Redewut fast außer sich geraten."
#     }.
#       {
    
#     "tag_name": "analepse",
#     "start": 14975,
#     "end": 15548,
#     "text": " so mußte ich ihn jetzt fast vergöttern. Stürzte er doch fünf, sechs Flaschen abgezogener Garantie hinunter, ohne sich zu schütteln, und fand zuletzt alle das Zeug noch nicht scharf genug! Auch ich mußte davon kosten, konnte es aber nicht herunterbringen, so widerlich fuselte der Schnaps. \u00bbAlles Pariser Fabrikat!\u00ab rief mir der Professor zu. \u2013 \u00bbMuß auf dem Transport ein wenig gelitten haben\u00ab, erwiderte ich bescheiden. \u2013 \u00bbKleinigkeit!\u00ab mengte sich der Wirt herein, \u00bbman tut etwas gestoßenen Pfeffer daran, die Leute mögen's nicht, wenn es sie nicht in die Zunge beißt.\u00ab\r\n"
#   }
#       """


# json_duration = clean_json("duration", "Heurecla/Code/data/annotationen/json_filtered/Auch_ich_war_in_Arkadien_duration_Annotator5_duration.json")
# json_frequency = clean_json("frequency","Heurecla/Code/data/annotationen/json_filtered/Auch_ich_war_in_Arkadien_frequency_Annotator5_frequency.json")
