import json
import pprint

# import defusedxml.ElementTree as ET
import xmltodict

res = """<?xml version="1.0" encoding="UTF-8"?>
<xmlio2>
  <patientinfores type="record">
    <Information_Date type="string">2018-10-02</Information_Date>
    <Information_Time type="string">11:25:31</Information_Time>
    <Api_Result type="string">00</Api_Result>
    <Api_Result_Message type="string">処理終了</Api_Result_Message>
    <Reskey type="string">Patient Info</Reskey>
    <Patient_Information type="record">
      <Patient_ID type="string">00200</Patient_ID>
      <WholeName type="string">てすと　受付</WholeName>
      <WholeName_inKana type="string">テスト　ウケツケ</WholeName_inKana>
      <BirthDate type="string">1975-01-01</BirthDate>
      <Sex type="string">2</Sex>
      <HouseHolder_WholeName type="string">てすと　受付</HouseHolder_WholeName>
      <TestPatient_Flag type="string">0</TestPatient_Flag>
      <Reduction_Reason type="string">00</Reduction_Reason>
      <Reduction_Reason_Name type="string">該当なし</Reduction_Reason_Name>
      <Discount type="string">00</Discount>
      <Discount_Name type="string">該当なし</Discount_Name>
      <Condition1 type="string">00</Condition1>
      <Condition1_Name type="string">該当なし</Condition1_Name>
      <Condition2 type="string">00</Condition2>
      <Condition2_Name type="string">該当なし</Condition2_Name>
      <Condition3 type="string">00</Condition3>
      <Condition3_Name type="string">該当なし</Condition3_Name>
      <Ic_Code type="string">01</Ic_Code>
      <Ic_Code_Name type="string">現金</Ic_Code_Name>
      <Community_Cid_Agree type="string">False</Community_Cid_Agree>
      <FirstVisit_Date type="string">2017-12-13</FirstVisit_Date>
      <LastVisit_Date type="string">2018-01-15</LastVisit_Date>
      <HealthInsurance_Information type="array">
        <HealthInsurance_Information_child type="record">
          <Insurance_Combination_Number type="string">0001</Insurance_Combination_Number>
          <InsuranceCombination_Rate_Admission type="string">0.30</InsuranceCombination_Rate_Admission>
          <InsuranceCombination_Rate_Outpatient type="string">0.30</InsuranceCombination_Rate_Outpatient>
          <Insurance_Nondisplay type="string">N</Insurance_Nondisplay>
          <InsuranceProvider_Class type="string">009</InsuranceProvider_Class>
          <InsuranceProvider_Number type="string">01320027</InsuranceProvider_Number>
          <InsuranceProvider_WholeName type="string">協会</InsuranceProvider_WholeName>
          <RelationToInsuredPerson type="string">1</RelationToInsuredPerson>
          <HealthInsuredPerson_WholeName type="string">てすと　受付</HealthInsuredPerson_WholeName>
          <Certificate_StartDate type="string">2017-11-21</Certificate_StartDate>
          <Certificate_ExpiredDate type="string">9999-12-31</Certificate_ExpiredDate>
          <Certificate_GetDate type="string">2010-10-10</Certificate_GetDate>
          <Insurance_CheckDate type="string">2017-11-21</Insurance_CheckDate>
        </HealthInsurance_Information_child>
      </HealthInsurance_Information>
      <Care_Information type="record">
        <Community_Disease type="array">
          <Community_Disease_child type="record">
            <Target_Disease type="string">True</Target_Disease>
          </Community_Disease_child>
          <Community_Disease_child type="record">
            <Target_Disease type="string">True</Target_Disease>
          </Community_Disease_child>
          <Community_Disease_child type="record">
            <Target_Disease type="string">True</Target_Disease>
          </Community_Disease_child>
          <Community_Disease_child type="record">
            <Target_Disease type="string">True</Target_Disease>
          </Community_Disease_child>
        </Community_Disease>
      </Care_Information>
      <Personally_Information type="record">
        <Pregnant_Class type="string">True</Pregnant_Class>
        <Community_Disease2 type="string">True</Community_Disease2>
        <Community_Disease3 type="string">True</Community_Disease3>
      </Personally_Information>
      <Auto_Management_Information type="array">
        <Auto_Management_Information_child type="record">
          <Medication_Code type="string">113002850</Medication_Code>
          <Medication_Name type="string">てんかん指導料</Medication_Name>
          <Medication_EndDate type="string">9999-12-31</Medication_EndDate>
        </Auto_Management_Information_child>
        <Auto_Management_Information_child type="record">
          <Medication_Code type="string">113002910</Medication_Code>
          <Medication_Name type="string">難病外来指導管理料</Medication_Name>
          <Medication_EndDate type="string">9999-12-31</Medication_EndDate>
        </Auto_Management_Information_child>
      </Auto_Management_Information>
      <Patient_Contra_Information type="record">
        <Patient_Contra_Info type="array">
          <Patient_Contra_Info_child type="record">
            <Medication_Code type="string">610406079</Medication_Code>
            <Medication_Name type="string">ガスター散２％</Medication_Name>
            <Medication_EndDate type="string">9999-12-31</Medication_EndDate>
            <Contra_StartDate type="string">2018-05-03</Contra_StartDate>
          </Patient_Contra_Info_child>
          <Patient_Contra_Info_child type="record">
            <Medication_Code type="string">610406047</Medication_Code>
            <Medication_Name type="string">ウテロン錠５ｍｇ</Medication_Name>
            <Medication_EndDate type="string">9999-12-31</Medication_EndDate>
          </Patient_Contra_Info_child>
        </Patient_Contra_Info>
      </Patient_Contra_Information>
    </Patient_Information>
  </patientinfores>
</xmlio2>"""

result = xmltodict.parse(res)
result_json = dict(json.loads(json.dumps(result)))

# pprint.pprint(result_json)
# pprint.pprint(result_json)

a = result_json.keys()
i = 0
dict_data = {}


def parse_res(key, origin, result={}, sub_dict={}, sub_list=[]):
    global i
    print("-----------------------------------------")
    # print(origin)
    print("------ result ------", result)
    print("-----------------------------------------")
    data = origin[key]
    keys = data.keys()
    for sub_key in keys:
        i = i + 1
        print(i)
        if sub_key == "@type":
            if data[sub_key] == "record":
                result[key] = {}
                print("result : record : : : ", result)
            elif data[sub_key] == "array":
                result[key] = []
                print("result : array : : : ", result)
            print("1. repeat--------------------->")
            # print(i)
            # print(i, sub_key)
            # result[key][sub_key] = parse_res(sub_key, data)
            print("1. sub_key", result)
        else:
            if "#text" in data[sub_key].keys():
                print(i, sub_key, data[sub_key]["#text"])
                result[key][sub_key] = data[sub_key]["#text"]
            else:
                print("2. repeat--------------------->")
                print(i, sub_key, "!!!!!!!!!!!!!!!!!!!!", result[key])
                result[key][sub_key] = {parse_res(sub_key, data)}
                # result[key][sub_key] = parse_res(sub_key, data)
    # if "@type" in data:
    #     if data["@type"] == "record":
    #         dict_data[key] = {}
    #     elif data["@type"] == "array":
    #         dict_data[key] = []
    # for key in keys:
    #     if key != "@type":
    #         sub_data = data[key]
    #         print(i, key, sub_data)
    #         i = i + 1
    #         if ("#text" in sub_data.keys()):
    #             dict_data[key] = sub_data["#text"]
    #             print(i, dict_data)
    #             i = i + 1
    #         else:
    #             print(i, key)
    #             i = i + 1
    #             parse_res(key, origin=sub_data)
    return result


pprint.pprint(result_json["xmlio2"])
print("======================================================")
pprint.pprint(parse_res("patientinfores", origin=result_json["xmlio2"]))
# main_dict = {
#     "test": {
#         "a1": "a1",
#         "b1": {
#             "bb1": "bb1",
#             "bb2": "bb2",
#             "bb3": {
#                 "bbb1": "bbb1",
#                 "bbb2": "bbb2",
#                 "bbb3": [
#                     {
#                         "bbbb": {
#                             "bbbb1": "bbbb1"
#                         }
#                     },
#                     {
#                         "bbbb": {
#                             "bbbb2": "bbbb2"
#                         }
#                     }
#                 ]
#             }
#         }
#     }
# }


# def repeatdict(original_data={}, key="test", result_data={}):
#     data = original_data[key]
#     result_data[key] = {}
#     for sub_key in data.keys():
#         result_data[key][sub_key] = data[sub_key]
#         print(sub_key, data[sub_key])

#     pprint.pprint(data)

#     return result_data


# odata = repeatdict(original_data=main_dict)

# print("--> result <--")
# pprint.pprint(odata)
