import json
import pprint

import requests
import xmltodict

url = "http://localhost:8000/api01rv2/systeminfv2"
xml = """<data>
        <private_objects type="record">
                <Request_Date type="string">2014-10-23</Request_Date>
                <Request_Time type="string">16:52:00</Request_Time>
        </private_objects>
</data>"""
headers = {"Content-Type": "application/xml"}
res = requests.post(url=url, data=xml, headers=headers, auth=("ormaster", "ormaster"))
ress = res.content.decode("utf-8")
result = json.loads(json.dumps(xmltodict.parse(ress), indent=2))
pprint.pprint(ress)
pprint.pprint(result)
