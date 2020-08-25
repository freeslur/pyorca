import json
import pprint

from bs4 import BeautifulSoup

# import defusedxml.ElementTree as ET
from dicttoxml import dicttoxml

req = """{
  "Patient_Information": {
    "Patient_ID": "00200",
    "WholeName": "てすと　受付",
    "WholeName_inKana": "テスト　ウケツケ",
    "BirthDate": "1975-01-01",
    "Sex": "2",
    "HouseHolder_WholeName": "てすと　受付",
    "TestPatient_Flag": "0",
    "Reduction_Reason": "00",
    "Reduction_Reason_Name": "該当なし",
    "Discount": "00",
    "Discount_Name": "該当なし",
    "Condition1": "00",
    "Condition1_Name": "該当なし",
    "Condition2": "00",
    "Condition2_Name": "該当なし",
    "Condition3": "00",
    "Condition3_Name": "該当なし",
    "Ic_Code": "01",
    "Ic_Code_Name": "現金",
    "Community_Cid_Agree": "False",
    "FirstVisit_Date": "2017-12-13",
    "LastVisit_Date": "2018-01-15",
    "HealthInsurance_Information": [
      {
        "Insurance_Combination_Number": "0001",
        "InsuranceCombination_Rate_Admission": "0.30",
        "InsuranceCombination_Rate_Outpatient": "0.30",
        "Insurance_Nondisplay": "N",
        "InsuranceProvider_Class": "009",
        "InsuranceProvider_Number": "01320027",
        "InsuranceProvider_WholeName": "協会",
        "RelationToInsuredPerson": "1",
        "HealthInsuredPerson_WholeName": "てすと　受付",
        "Certificate_StartDate": "2017-11-21",
        "Certificate_ExpiredDate": "9999-12-31",
        "Certificate_GetDate": "2010-10-10",
        "Insurance_CheckDate": "2017-11-21"
      }
    ],
    "Care_Information": {
      "Community_Disease": [
        {
          "Target_Disease": "True"
        },
        {
          "Target_Disease": "True"
        },
        {
          "Target_Disease": "True"
        },
        {
          "Target_Disease": "True"
        }
      ]
    },
    "Personally_Information": {
      "Pregnant_Class": "True",
      "Community_Disease2": "True",
      "Community_Disease3": "True"
    },
    "Auto_Management_Information": [
      {
        "Medication_Code": "113002850",
        "Medication_Name": "てんかん指導料",
        "Medication_EndDate": "9999-12-31"
      },
      {
        "Medication_Code": "113002910",
        "Medication_Name": "難病外来指導管理料",
        "Medication_EndDate": "9999-12-31"
      }
    ],
    "Patient_Contra_Information": {
      "Patient_Contra_Info": [
        {
          "Medication_Code": "610406079",
          "Medication_Name": "ガスター散２％",
          "Medication_EndDate": "9999-12-31",
          "Contra_StartDate": "2018-05-03"
        },
        {
          "Medication_Code": "610406047",
          "Medication_Name": "ウテロン錠５ｍｇ",
          "Medication_EndDate": "9999-12-31"
        }
      ]
    }
  }
}"""

json_dict = json.loads(req)
pprint.pprint(json_dict)
xml = dicttoxml(json_dict, root=False)
soup = BeautifulSoup(xml, "xml")
print(soup.prettify())
# result = xmltodict.parse(res)
# result_json = dict(json.loads(json.dumps(result)))

# i = 0


# pprint.pprint(result_json["xmlio2"])
# print("======================================================")
# # pprint.pprint(parse_res("patientinfores", origin=result_json["xmlio2"]))

# origin = result_json["xmlio2"]
# with open(file="result.json", mode="w", encoding="utf-8") as fp:
#     json.dump(origin, fp, ensure_ascii=False, indent=2)


# def orca_api_formatter(origin):
#     if type(origin) is list:
#         origin_array = []
#         for origin_data in origin:
#             origin_array.append(orca_api_formatter(origin_data))
#         origin = origin_array
#     else:
#         if origin["@type"] == "record":
#             for key in origin.keys():
#                 if key != "@type":
#                     if "#text" in origin[key].keys():
#                         origin[key] = origin[key]["#text"]
#                     else:
#                         origin[key] = orca_api_formatter(origin[key])
#             if "@type" in origin.keys():
#                 del origin["@type"]
#         elif origin["@type"] == "array":
#             origin_array = []
#             for key in origin.keys():
#                 if key != "@type":
#                     if type(origin[key]) is list:
#                         origin_array = orca_api_formatter(origin[key])
#                     else:
#                         origin_array.append(orca_api_formatter(origin[key]))
#             origin = origin_array

#     return origin


# last_data = orca_api_formatter(origin["patientinfores"])
# pprint.pprint(last_data)
# with open(file="result2.json", mode="w", encoding="utf-8") as fp:
#     json.dump(last_data, fp, ensure_ascii=False, indent=2)
