"""
Catmapy wird importiert, damit Annotationen und Textdaten zusammengeführt werdern können --> Daraus wird XML
Alle Pfade müssen manuell angepasst werden.


"""

import catmapy
import os
import re
import json
#import pandas as pd


def rename_files():
   # Artikeldatein umbennenen

    import os

    # Pfad zu dem Ordner, in dem die Dateien umbenannt werden sollen
    dir = "pathto/heureclea-time-annotations-compared-public-076c83a"

    # Durch alle Dateien im Ordner iterieren
    for dateiname in os.listdir(dir):
        neuer_dateiname = dateiname.replace(" ", "_") #replace space by _
        
        # Alten und neuen Dateipfad erstellen
        alter_dateipfad = os.path.join(dir, dateiname)
        neuer_dateipfad = os.path.join(dir, neuer_dateiname)
        
        # Datei umbenennen
        os.rename(alter_dateipfad, neuer_dateipfad)
        
        print(f"'{dateiname}' wurde in '{neuer_dateiname}' umbenannt.")




def add_inline_annos():
    """Basierend auf Originaltexten (txt files) und Xml-Dateien (annotationen) wird hier jeweils eine XML-Datei erstellt, die Inline-Annotationen enthält """
    collections_ordner = "pathto/heureclea-time-annotations-compared"
    source_texts_ordner = "pathto/heureclea-sourcedocuments"
    output_ordner = "pathto/annostotxt"

    os.makedirs(output_ordner, exist_ok=True)

    # Alle Source-Text-Dateien sammeln
    source_texts = {os.path.splitext(f)[0]: os.path.join(source_texts_ordner, f) for f in os.listdir(source_texts_ordner) if f.endswith('.txt')}

    # Alle Collections durchlaufen
    for collection_datei in os.listdir(collections_ordner):
        if collection_datei.endswith('.xml'):
            # Extrahiere den Namensteil vor dem letzten Unterstrich
            match = re.match(r"^(.*)_[^_]+_[^_]+\.xml$", collection_datei)
            #^(.*)_[^_]+_[^_]+_[^_]+\.xml$
            #^(.*)_[^_]+_[^_]+\.xml$
            if match:
                collection_name_part = match.group(1)
                
                # Suche nach einem passenden Source-Text
                source_text = source_texts.get(collection_name_part)
                
                
                if source_text:
                    # Pfade zur Collection und zur Zieldatei
                    collection_pfad = os.path.join(collections_ordner, collection_datei)
                    output_datei_pfad = os.path.join(output_ordner, collection_datei)
                    
                    # Anwenden der Funktion und Speichern des Ergebnisses
                    catmapy.convert_ptr_refs_to_text(collection_pfad, source_text, output_datei_pfad)
                    print(f"Verarbeitet: {collection_datei} mit {os.path.basename(source_text)}")
                else:
                    print(f"Kein passender Source-Text für {collection_datei} gefunden.")





def extract_annos_per_doc(xml_file, source_text):
    """Funktion wird aufgerudfen, um über mehre collections und die jeweiliten Originaltexte zu iteriieren. Dabei wird eine liste von tuples erstellt; die Informationen werden sopäter in einer JSON gespeichert"""

    reader = catmapy.TEIAnnotationReader(filename=xml_file)

    # Originaltext aus der txt-Datei laden
    with open(source_text, 'r', encoding='utf-8', newline="") as file:
        original_text = file.read()

    # Tuple list
    annotations_data = []
    # Extrahieren der Annotationsdaten
    annotations = reader.annotations


    for annotation in annotations:
        #print(f"Annotation UUID: {annotation.anno_uuid}")
        #print(f"Tag: {annotation.tag.name}")
        #print(f"Properties: {annotation.properties}")
        #print(f"Ranges: {annotation.ranges}")
        tag_name = annotation.tag.name
        annotationsid = annotation.uuid  # UUID der Annotation #<class 'uuid.UUID'>
        tagid = annotation.tag.uuid  # UUID des Tags
        #properties = annotation.properties # display color
        #print(type(annotationsid))
        #print(annotationsid)

        #annotationsid = annotationsid.rstrip("UUID('")

        # Für jede Annotation die zugehörigen Textstellen (Ranges) ausgeben
        for anno_range in annotation.ranges:
            start = anno_range.start  # Startindex des Ranges
            end = anno_range.end  # Endindex des Ranges
            text_segment = original_text[start:end]  # Relevante Textstelle aus dem Originaltext extrahieren
            #print(f"Text Segment: {text_segment}")

            annotation_tuple = (annotationsid, tagid,tag_name, start, end, text_segment)
            annotations_data.append(annotation_tuple)


    return annotations_data



def tuple_to_dict(listoftuples):
    """List of tuples are converted to a list of dicts"""
    dict_list = list()
    for t in listoftuples:
        anno_dict = {
        "anno_id" : str(t[0]),
        "tag_id" : str(t[1]),
        "tag_name" : t[2],
        "start" : t[3],
        "end": t[4],
        "text": t[5]
        }
        dict_list.append(anno_dict)

    #print(anno_dict.items())
    #print(anno_dict.keys())
    return dict_list


# test = tuple_to_dict(annotations_data[:5])

# print(tuple_to_dict(annotations_data[:5]))

# json_result = json.dumps(test, indent = 2)
# with open("test_datei_annos.json", "w") as outfile: 
#     outfile.write(json_result)


def annos_to_json():
    """Annotationen werden extrahiert und annotierte Textstellen werden in JSON abgelegt"""
    collections_ordner = "pathto//heureclea-time-annotations-compared"
    results_dir = "pathto/annotationsjson_new"
    source_texts_ordner = "pathto/heureclea-sourcedocuments"
    source_texts = {os.path.splitext(f)[0]: os.path.join(source_texts_ordner, f) for f in os.listdir(source_texts_ordner) if f.endswith('.txt')}


    for collection_datei in os.listdir(collections_ordner):
        if collection_datei.endswith('.xml'):
            #Extrahiere den Namensteil vor dem letzten Unterstrich
            match = re.match(r"^(.*)_[^_]+_[^_]+\.xml$", collection_datei)
                #^(.*)_[^_]+_[^_]+_[^_]+\.xml$
                #^(.*)_[^_]+_[^_]+\.xml$
            if match:
                collection_name_part = match.group(1)

                # GET MATCHING SOURCE TEXT
                source_text = source_texts.get(collection_name_part)

                if source_text:
                    print("LEN SOURCE TEXT, ",len(source_text))

                    collection_pfad = os.path.join(collections_ordner, collection_datei)
                    output_datei_pfad = os.path.join(results_dir, collection_datei.replace(".xml",".json"))
                
                    # Anwenden der Funktion und Speichern des Ergebnisses
                    anno_tuples = extract_annos_per_doc(collection_pfad, source_text)
                    anno_dict_list = tuple_to_dict(anno_tuples)

                    json_result = json.dumps(anno_dict_list, indent = 2,ensure_ascii=False)
                    with open(output_datei_pfad, "w") as outfile: 
                        outfile.write(json_result)

                    print(f"Verarbeitet: {collection_datei}")
                    print(len(anno_tuples))
            # else:
            #     print(f"Kein passender Source-Text für {collection_datei} gefunden.")

            # with open(output_datei_pfad, "w") as outfile: 
            #     json.dump(anno_dict, outfile)

annos_to_json()


def filtered_annos_to_json():
    """Iteriert über die erstellten JSONS und filtert nur die relevanten Annotationsstellen je Tag raus"""
    tags_path = "./LLMs/Heurecla/Code/data/tags_frequency.json"
    json_ordner = "./LLMs/Heurecla/Code/data/annotationen/annotationsjson"
    results_dir = "./LLMs/Heurecla/Code/data/annotationen/json_filtered"

    with open(tags_path, "r", encoding="utf-8") as tagfile:
        tagdict = json.load(tagfile)

    taglist = [v.strip("CATMA_").lower() for k,v in tagdict.items()] #only keep tag ids
    
    #print(taglist)

    info_list=list() #tuples mit file name und anzahl der annotation zu dur/order/frequency

    for jsonfile in os.listdir(json_ordner):
        if jsonfile.endswith(".json"):
            new_list=list()
            json_pfad = os.path.join(json_ordner,jsonfile)
            output_datei_pfad = os.path.join(results_dir, jsonfile.strip(".json")+"_frequency"+".json")

            jsoncontent = open(json_pfad,"r", encoding = "utf-8")
            jsondata =  json.load(jsoncontent)

            # print(jsondata)
            #print("List before ", len(jsondata))
            # print(type(jsondata))

            for entry in jsondata:
                #print(entry["tag_id"])
                if entry["tag_id"] in taglist:
                    new_list.append(entry)
            
            #print("length of new list ", len(new_list))
            
################################################################
            info_file_annono = (jsonfile,len(new_list)) #tuples 
            info_list.append(info_file_annono)
################################################################
            
            if len(new_list) > 0:
                new_json = json.dumps(new_list, indent = 2)
                
                with open(output_datei_pfad, "w") as outfile: 
                    outfile.write(new_json)
            
            print(f"Verarbeitet: {jsonfile}")


    df = pd.DataFrame(info_list, columns = ["Dateiname","Frequency_Annotationen"])
    df = df.sort_values(by=["Dateiname"])
    print(df.head())

    df.to_csv("pathto/Code/data/annotationen/frequency.csv", index = False, encoding="utf-8")

            # for entry in jsondata:
            #     if tag_id in 
            # #     if entry
            #     print(entry["tag_id"])



    # for collection_datei in os.listdir(collections_ordner):
    #     if collection_datei.endswith('.xml'):
    #         #Extrahiere den Namensteil vor dem letzten Unterstrich
    #         match = re.match(r"^(.*)_[^_]+_[^_]+\.xml$", collection_datei)
    #             #^(.*)_[^_]+_[^_]+_[^_]+\.xml$
    #             #^(.*)_[^_]+_[^_]+\.xml$
    #         if match:
    #             collection_name_part = match.group(1)

    #             # GET MATCHING SOURCE TEXT
    #             source_text = source_texts.get(collection_name_part)

    #             if source_text:

    #                 collection_pfad = os.path.join(collections_ordner, collection_datei)
    #                 output_datei_pfad = os.path.join(results_dir, collection_datei.replace(".xml",".json"))
                
    #                 # Anwenden der Funktion und Speichern des Ergebnisses
    #                 anno_tuples = extract_annos_per_doc(collection_pfad, source_text)
    #                 anno_dict_list = tuple_to_dict(anno_tuples)

    #                 json_result = json.dumps(anno_dict_list, indent = 2)
    #                 with open(output_datei_pfad, "w") as outfile: 
    #                     outfile.write(json_result)

    #                 print(f"Verarbeitet: {collection_datei}")
    #                 print(len(anno_tuples))
    #         # else:
            #     print(f"Kein passender Source-Text für {collection_datei} gefunden.")

            # with open(output_datei_pfad, "w") as outfile: 
            #     json.dump(anno_dict, outfile)

#filtered_annos_to_json()