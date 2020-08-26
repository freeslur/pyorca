import json
# import pprint
# import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

# from bs4 import BeautifulSoup
# import defusedxml.ElementTree as ET
from dicttoxml import dicttoxml

req1 = """{
  "Patient_ID": "00036",
  "WholeName": "日医　太郎",
  "WholeName_inKana": "ニチイ　タロウ",
  "BirthDate": "1970-01-01",
  "Sex": "1",
  "HouseHolder_WholeName": "日医　太郎",
  "Relationship": "本人",
  "Occupation": "会社員",
  "CellularNumber": "09011112222",
  "FaxNumber": "03-0011-2233",
  "EmailAddress": "test@tt.dot.jp",
  "Home_Address_Information": {
    "Address_ZipCode": "1130021",
    "WholeAddress1": "東京都文京区本駒込",
    "WholeAddress2": "６−１６−３",
    "PhoneNumber1": "03-3333-2222",
    "PhoneNumber2": "03-3333-1133"
  },
  "WorkPlace_Information": {
    "WholeName": "てすと　株式会社",
    "Address_ZipCode": "1130022",
    "WholeAddress1": "東京都文京区本駒込",
    "WholeAddress2": "５−１２−１１",
    "PhoneNumber": "03-3333-2211"
  },
  "Contraindication1": "状態",
  "Allergy1": "アレルギ",
  "Infection1": "感染症",
  "Comment1": "コメント",
  "HealthInsurance_Information": [
    {
      "Insurance_Combination_Number": "0001",
      "InsuranceProvider_Class": "060",
      "InsuranceProvider_Number": "138057",
      "InsuranceProvider_WholeName": "国保",
      "HealthInsuredPerson_Symbol": "０１",
      "HealthInsuredPerson_Number": "１２３４５６７",
      "HealthInsuredPerson_Assistance": "3",
      "RelationToInsuredPerson": "1",
      "Certificate_StartDate": "2010-05-01",
      "Certificate_ExpiredDate": "9999-12-31"
    },
    {
      "Insurance_Combination_Number": "0002",
      "InsuranceProvider_Class": "060",
      "InsuranceProvider_Number": "138057",
      "InsuranceProvider_WholeName": "国保",
      "HealthInsuredPerson_Symbol": "０１",
      "HealthInsuredPerson_Number": "１２３４５６７",
      "HealthInsuredPerson_Assistance": "3",
      "RelationToInsuredPerson": "1",
      "Certificate_StartDate": "2010-05-01",
      "Certificate_ExpiredDate": "9999-12-31",
      "PublicInsurance_Information": [
        {
          "PublicInsurance_Class": "010",
          "PublicInsurance_Name": "感３７の２",
          "PublicInsurer_Number": "10131142",
          "PublicInsuredPerson_Number": "1234566",
          "Rate_Admission": "0.05",
          "Money_Admission": "0",
          "Rate_Outpatient": "0.05",
          "Money_Outpatient": "0",
          "Certificate_IssuedDate": "2010-05-01",
          "Certificate_ExpiredDate": "9999-12-31"
        }
      ]
    }
  ],
  "Payment_Information": {
    "Reduction_Reason": "01",
    "Reduction_Reason_Name": "低所得",
    "Discount": "01",
    "Discount_Name": "10(%)",
    "Ic_Code": "02",
    "Ic_Code_Name": "振込"
  }
}"""


req = req1


def item_del_func(x): return x+"_child"


data = {"patientmodreq": json.loads(req)}

xml = dicttoxml(data, root=True, custom_root="data",
                attr_type=True, item_func=item_del_func)
string_xml = parseString(xml).toxml()
result_xml = string_xml.replace('type="str"', 'type="string"').replace(
    'type="dict"', 'type="record"').replace('type="list"', 'type="array"')
print(result_xml)
print("------------------------------------------------")
