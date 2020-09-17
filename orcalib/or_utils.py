import json
from datetime import date
from xml.dom.minidom import parseString

import requests
import xmltodict
from dicttoxml import dicttoxml

import orcalib.or_default as orca


def check_new(create_date, update_date, update_time):
    return 0


def post_request(api_uri, res_key, post_data):
    r_data = xmltodict.parse(
        requests.post(
            url=orca.default_url + api_uri,
            data=post_data.encode("utf-8"),
            headers=orca.post_headers,
            auth=orca.auth,
        ).content
    )
    result = res_data(r_data, res_key)
    return result


def get_request(api_uri, res_key, params):
    r_data = xmltodict.parse(
        requests.get(
            url=orca.default_url + api_uri + params,
            auth=orca.auth,
        ).content
    )
    result = res_data(r_data, res_key)
    return result


def res_data(r_data, res_key):
    return res_to_json(dict(json.loads(json.dumps(r_data)))["xmlio2"][res_key])


def calc_age(birth_date):
    ymd = birth_date.split("-")
    today = date.today()
    age = (
        today.year
        - int(ymd[0])
        - ((today.month, today.day) < (int(ymd[1]), int(ymd[2])))
    )
    return str(age) + "才"


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


def req_to_xml(req_key, req_data):
    def item_del_func(x):
        return x + "_child"

    data = {req_key: req_data}
    xml = dicttoxml(
        data, root=True, custom_root="data", attr_type=True, item_func=item_del_func
    )
    string_xml = parseString(xml).toxml()
    result_xml = (
        string_xml.replace('type="str"', 'type="string"')
        .replace('type="dict"', 'type="record"')
        .replace('type="list"', 'type="array"')
    )
    return result_xml
