import json
from xml.dom.minidom import parseString

import dicttoxml


def res_to_json(data):

    if type(data) is list:
        json_data_array = []
        for json_data in data:
            json_data_array.append(res_to_json(json_data))
        data = json_data_array
    else:
        if data["@type"] == "record":
            for key in data.keys():
                if key != "@type":
                    if "#text" in data[key].keys():
                        data[key] = data[key]["#text"]
                    else:
                        data[key] = res_to_json(data[key])
            if "@type" in data.keys():
                del data["@type"]
        elif data["@type"] == "array":
            json_data_array = []
            for key in data.keys():
                if key != "@type":
                    if type(data[key]) is list:
                        json_data_array = res_to_json(data[key])
                    else:
                        json_data_array.append(res_to_json(data[key]))
            data = json_data_array
    return data


def req_to_xml(req_data):

    def item_del_func(x): return x+"_child"

    data = {"patientmodreq": json.loads(req_data)}

    xml = dicttoxml(data, root=True, custom_root="data",
                    attr_type=True, item_func=item_del_func)
    string_xml = parseString(xml).toxml()
    result_xml = string_xml.replace('type="str"', 'type="string"').replace(
        'type="dict"', 'type="record"').replace('type="list"', 'type="array"')
    return result_xml
