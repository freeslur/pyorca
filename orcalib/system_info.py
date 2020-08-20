import requests
import xmltodict

import orcalib.orca_default as orca

xml = orca.post_param_default("private_objects",
                              """<Request_Date type="string">2014-10-23</Request_Date>
                <Request_Time type="string">16:52:00</Request_Time>"""
                              )
result = xmltodict.parse(
    requests.post(
        url=orca.default_url + orca.system_info,
        data=xml,
        headers=orca.post_headers,
        auth=orca.auth,
    ).content
)["xmlio2"]["private_objects"]
