import json

import xmltodict


def res_to_json(response, key):
    result = xmltodict.parse(response)
    origin = dict(json.loads(json.dumps(result)))["xmlio2"][key]

    if type(origin) is list:
        origin_array = []
        for origin_data in origin:
            origin_array.append(res_to_json(origin_data))
        origin = origin_array
    else:
        if origin["@type"] == "record":
            for key in origin.keys():
                if key != "@type":
                    if "#text" in origin[key].keys():
                        origin[key] = origin[key]["#text"]
                    else:
                        origin[key] = res_to_json(origin[key])
            if "@type" in origin.keys():
                del origin["@type"]
        elif origin["@type"] == "array":
            origin_array = []
            for key in origin.keys():
                if key != "@type":
                    if type(origin[key]) is list:
                        origin_array = res_to_json(origin[key])
                    else:
                        origin_array.append(res_to_json(origin[key]))
            origin = origin_array

    return origin


def req_to_xml():
    return "null"
