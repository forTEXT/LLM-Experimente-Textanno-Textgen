"""Datei enthält alle relevanten Tags; sowie die Möglichkeit JSON-Files zu speichern. Am Ende Außerdem die relevanten Guidelines"""
import json

duration_dict = {"name":"duration","tag_id":"CATMA_2CCEA787-42BD-4DE6-BC2E-9AAD95498989", 
                    "subtags":[
                        {"name":"isochrony","tag_id":"CATMA_850DE553-F5C1-4640-8DA0-DE63BE9E1CD1"},
                        {"name":"anisochrony","tag_id":"CATMA_3B66F36E-CCB4-4918-851C-8133CAE55C64", 
                            "subtags":[{"name":"summary","tag_id":"CATMA_77F85047-1C0F-4D58-B32D-C82934E780FC",
                                        "subtags":[{"name":"ellipsis","tag_id":"CATMA_644354B5-7F9A-4C3C-9DF4-12EC94C8ECA3", "subtags":[{"name":"expl-ellipsis","tag_id":"CATMA_938A525E-4D0C-4AC1-B4AD-A13D1B330D3B"},{"name":"impl-ellipsis","tag_id":"CATMA_F74C1EAE-F02B-47B7-B215-637BCCD28F7C"}]}]},
                                        {"name":"scene","tag_id":"CATMA_25346C01-67CF-42AD-B0BF-BCFFA016996D", "subtags":[{"name":"pause","tag_id":"CATMA_D574BEF6-17EB-417D-8463-6CC99EA40B7F"}]}]}   
                    ] }

frequency_dict = {"name":"frequency","tag_id":"CATMA_38B27FD8-6164-49DB-BE67-949DCDA9AAFA",
                  "subtags":[
                      {"name":"singulative","tag_id": "CATMA_74802F3F-3444-4099-8C01-806E276713A8", "subtags":[{"name":"multi-singulative","tag_id":"CATMA_62B5E93E-11E7-4FF5-9211-1E115F0CE804"}]},
                      {"name":"repetitive","tag_id": "CATMA_9E3B59BA-B381-4ED2-B36A-7C6F844674D1"},
                      {"name":"iterative","tag_id": "CATMA_F1FC83FB-8C45-4236-AFF4-8B926B7AEFAC"}
                  ]}

order_dict  = {"name":"order","tag_id":"CATMA_8E04036F-CF09-41F5-9A7B-CB70795C8CEB",
                  "subtags":[
                      {"name":"chronology","tag_id": "CATMA_27A6EAA6-1A59-4514-B3C6-ADA38301649E"},
                      {"name":"anachrony","tag_id": "CATMA_2E2415F7-D2A4-4923-945D-ED6FED88B18A", "subtags":[{"name":"prolepsis","tag_id":"CATMA_EECCC55E-96A1-4E00-8217-02661717B1E0"},{"name":"simullepsis","tag_id":"CATMA_AEA74722-F9FF-454B-A918-740E71556D33"},{"name":"analepsis","tag_id":"CATMA_757BF8B0-3A71-44F8-8C75-CDE8657D4EB0","subtags":[{"name":"reach_analepse","tag_id":"CATMA_056B4BCD-DAFD-4323-B895-8F953F7E5626"},{"name":"extent_analepse","tag_id":"CATMA_E9681996-EC4E-4FF8-8836-592C9A1DDF39"}]}]},
                      {"name":"achrony","tag_id": "CATMA_B440B7B3-5E77-416A-A61F-475D3A29C59E","subtags":[{"name":"achronic element","tag_id":"CATMA_D895D767-A157-4A1A-93C0-FB65FEA5653C","subtags":[{"name":"link_theme","tag_id":"CATMA_3F11915F-272B-49CD-9C24-82E224A3D0B5"},{"name":"link_space","tag_id":"CATMA_7766CF57-B02C-4DA1-BB9E-7EE7E6541AF2"}]}]}
                  ]}


all_tags= ["CATMA_2CCEA787-42BD-4DE6-BC2E-9AAD95498989","CATMA_850DE553-F5C1-4640-8DA0-DE63BE9E1CD1","CATMA_3B66F36E-CCB4-4918-851C-8133CAE55C64","CATMA_77F85047-1C0F-4D58-B32D-C82934E780FC","CATMA_644354B5-7F9A-4C3C-9DF4-12EC94C8ECA3","CATMA_938A525E-4D0C-4AC1-B4AD-A13D1B330D3B","CATMA_F74C1EAE-F02B-47B7-B215-637BCCD28F7C",
          "CATMA_25346C01-67CF-42AD-B0BF-BCFFA016996D","CATMA_D574BEF6-17EB-417D-8463-6CC99EA40B7F","CATMA_38B27FD8-6164-49DB-BE67-949DCDA9AAFA","CATMA_74802F3F-3444-4099-8C01-806E276713A8","CATMA_62B5E93E-11E7-4FF5-9211-1E115F0CE804","CATMA_9E3B59BA-B381-4ED2-B36A-7C6F844674D1","CATMA_F1FC83FB-8C45-4236-AFF4-8B926B7AEFAC",
          "CATMA_8E04036F-CF09-41F5-9A7B-CB70795C8CEB","CATMA_27A6EAA6-1A59-4514-B3C6-ADA38301649E","CATMA_2E2415F7-D2A4-4923-945D-ED6FED88B18A","CATMA_EECCC55E-96A1-4E00-8217-02661717B1E0","CATMA_AEA74722-F9FF-454B-A918-740E71556D33","CATMA_757BF8B0-3A71-44F8-8C75-CDE8657D4EB0","CATMA_056B4BCD-DAFD-4323-B895-8F953F7E5626",
          "CATMA_E9681996-EC4E-4FF8-8836-592C9A1DDF39","CATMA_B440B7B3-5E77-416A-A61F-475D3A29C59E","CATMA_D895D767-A157-4A1A-93C0-FB65FEA5653C","CATMA_3F11915F-272B-49CD-9C24-82E224A3D0B5","CATMA_7766CF57-B02C-4DA1-BB9E-7EE7E6541AF2"]

tag_tuples= {"duration":"CATMA_2CCEA787-42BD-4DE6-BC2E-9AAD95498989",
             "isochrony":"CATMA_850DE553-F5C1-4640-8DA0-DE63BE9E1CD1",
             "anisochrony":"CATMA_3B66F36E-CCB4-4918-851C-8133CAE55C64", 
             "summary":"CATMA_77F85047-1C0F-4D58-B32D-C82934E780FC",
             "ellipsis":"CATMA_644354B5-7F9A-4C3C-9DF4-12EC94C8ECA3",
             "expl-ellipsis":"CATMA_938A525E-4D0C-4AC1-B4AD-A13D1B330D3B",
             "impl-ellipsis":"CATMA_F74C1EAE-F02B-47B7-B215-637BCCD28F7C",
             "scene":"CATMA_25346C01-67CF-42AD-B0BF-BCFFA016996D",
             "pause":"CATMA_D574BEF6-17EB-417D-8463-6CC99EA40B7F",
             "frequency":"CATMA_38B27FD8-6164-49DB-BE67-949DCDA9AAFA",
             "singulative": "CATMA_74802F3F-3444-4099-8C01-806E276713A8",
             "multi-singulative":"CATMA_62B5E93E-11E7-4FF5-9211-1E115F0CE804",
             "repetitive": "CATMA_9E3B59BA-B381-4ED2-B36A-7C6F844674D1",
             "iterative": "CATMA_F1FC83FB-8C45-4236-AFF4-8B926B7AEFAC",
             "order":"CATMA_8E04036F-CF09-41F5-9A7B-CB70795C8CEB",
            "chronology": "CATMA_27A6EAA6-1A59-4514-B3C6-ADA38301649E",
            "anachrony": "CATMA_2E2415F7-D2A4-4923-945D-ED6FED88B18A",
            "prolepsis":"CATMA_EECCC55E-96A1-4E00-8217-02661717B1E0",
            "simullepsis":"CATMA_AEA74722-F9FF-454B-A918-740E71556D33",
            "analepsis":"CATMA_757BF8B0-3A71-44F8-8C75-CDE8657D4EB0",
            "reach_analepse":"CATMA_056B4BCD-DAFD-4323-B895-8F953F7E5626",
            "extent_analepse":"CATMA_E9681996-EC4E-4FF8-8836-592C9A1DDF39",
            "achrony": "CATMA_B440B7B3-5E77-416A-A61F-475D3A29C59E",
            "achronic element":"CATMA_D895D767-A157-4A1A-93C0-FB65FEA5653C",
            "link_theme":"CATMA_3F11915F-272B-49CD-9C24-82E224A3D0B5",
            "link_space":"CATMA_7766CF57-B02C-4DA1-BB9E-7EE7E6541AF2"
            }


with open("pathto/tags_order.json","w",encoding="UTF-8") as outjson:
    json.dump(tag_tuples,outjson)



