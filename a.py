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

i = 0


pprint.pprint(result_json["xmlio2"])
print("======================================================")
# pprint.pprint(parse_res("patientinfores", origin=result_json["xmlio2"]))

origin = result_json["xmlio2"]
with open(file="result.json", mode="w", encoding="utf-8") as fp:
    json.dump(origin, fp, ensure_ascii=False, indent=2)


def orca_api_formatter(origin):
    if type(origin) is list:
        origin_array = []
        for origin_data in origin:
            origin_array.append(orca_api_formatter(origin_data))
        origin = origin_array
    else:
        if origin["@type"] == "record":
            for key in origin.keys():
                if key != "@type":
                    if "#text" in origin[key].keys():
                        origin[key] = origin[key]["#text"]
                    else:
                        origin[key] = orca_api_formatter(origin[key])
            if "@type" in origin.keys():
                del origin["@type"]
        elif origin["@type"] == "array":
            origin_array = []
            for key in origin.keys():
                if key != "@type":
                    if type(origin[key]) is list:
                        origin_array = orca_api_formatter(origin[key])
                    else:
                        origin_array.append(orca_api_formatter(origin[key]))
            origin = origin_array

    return origin


last_data = orca_api_formatter(origin["patientinfores"])
pprint.pprint(last_data)
with open(file="result2.json", mode="w", encoding="utf-8") as fp:
    json.dump(last_data, fp, ensure_ascii=False, indent=2)
