import json

import requests
import xmltodict

import orcalib.orca_default as orca

xml = """<data>
        <private_objects type="record">
                <Request_Date type="string">2014-10-23</Request_Date>
                <Request_Time type="string">16:52:00</Request_Time>
        </private_objects>
</data>"""
res = xmltodict.parse(
    requests.post(
        url=orca.default_url + orca.system_info,
        data=xml,
        headers=orca.post_headers,
        auth=orca.auth,
    ).content
)["xmlio2"]["private_objects"]
result = json.dumps(res, indent=2, ensure_ascii=False,)


def result_item(item_name):
    return json.dumps(res[item_name], indent=2, ensure_ascii=False,)
