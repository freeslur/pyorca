import json
import pprint

# import defusedxml.ElementTree as ET
import xmltodict

res1 = """<?xml version="1.0" encoding="UTF-8"?>
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

res2 = """<xmlio2>
  <patientmodres type="record">
    <Information_Date type="string">2014-07-17</Information_Date>
    <Information_Time type="string">10:38:30</Information_Time>
    <Api_Result type="string">00</Api_Result>
    <Api_Result_Message type="string">登録終了</Api_Result_Message>
    <Reskey type="string">Acceptance_Info</Reskey>
    <Patient_Information type="record">
      <Patient_ID type="string">00036</Patient_ID>
      <WholeName type="string">日医　太郎</WholeName>
      <WholeName_inKana type="string">ニチイ　タロウ</WholeName_inKana>
      <BirthDate type="string">1970-01-01</BirthDate>
      <Sex type="string">1</Sex>
      <HouseHolder_WholeName type="string">日医　太郎</HouseHolder_WholeName>
      <Relationship type="string">本人</Relationship>
      <Occupation type="string">会社員</Occupation>
      <CellularNumber type="string">09011112222</CellularNumber>
      <FaxNumber type="string">03-0011-2233</FaxNumber>
      <EmailAddress type="string">test@tt.dot.jp</EmailAddress>
      <Home_Address_Information type="record">
        <Address_ZipCode type="string">1130021</Address_ZipCode>
        <WholeAddress1 type="string">東京都文京区本駒込</WholeAddress1>
        <WholeAddress2 type="string">６−１６−３</WholeAddress2>
        <PhoneNumber1 type="string">03-3333-2222</PhoneNumber1>
        <PhoneNumber2 type="string">03-3333-1133</PhoneNumber2>
      </Home_Address_Information>
      <WorkPlace_Information type="record">
        <WholeName type="string">てすと　株式会社</WholeName>
        <Address_ZipCode type="string">1130022</Address_ZipCode>
        <WholeAddress1 type="string">東京都文京区本駒込</WholeAddress1>
        <WholeAddress2 type="string">５−１２−１１</WholeAddress2>
        <PhoneNumber type="string">03-3333-2211</PhoneNumber>
      </WorkPlace_Information>
      <Contraindication1 type="string">状態</Contraindication1>
      <Allergy1 type="string">アレルギ</Allergy1>
      <Infection1 type="string">感染症</Infection1>
      <Comment1 type="string">コメント</Comment1>
      <HealthInsurance_Information type="array">
        <HealthInsurance_Information_child type="record">
          <Insurance_Combination_Number type="string">0001</Insurance_Combination_Number>
          <InsuranceProvider_Class type="string">060</InsuranceProvider_Class>
          <InsuranceProvider_Number type="string">138057</InsuranceProvider_Number>
          <InsuranceProvider_WholeName type="string">国保</InsuranceProvider_WholeName>
          <HealthInsuredPerson_Symbol type="string">０１</HealthInsuredPerson_Symbol>
          <HealthInsuredPerson_Number type="string">１２３４５６７</HealthInsuredPerson_Number>
          <HealthInsuredPerson_Assistance type="string">3</HealthInsuredPerson_Assistance>
          <RelationToInsuredPerson type="string">1</RelationToInsuredPerson>
          <Certificate_StartDate type="string">2010-05-01</Certificate_StartDate>
          <Certificate_ExpiredDate type="string">9999-12-31</Certificate_ExpiredDate>
        </HealthInsurance_Information_child>
        <HealthInsurance_Information_child type="record">
          <Insurance_Combination_Number type="string">0002</Insurance_Combination_Number>
          <InsuranceProvider_Class type="string">060</InsuranceProvider_Class>
          <InsuranceProvider_Number type="string">138057</InsuranceProvider_Number>
          <InsuranceProvider_WholeName type="string">国保</InsuranceProvider_WholeName>
          <HealthInsuredPerson_Symbol type="string">０１</HealthInsuredPerson_Symbol>
          <HealthInsuredPerson_Number type="string">１２３４５６７</HealthInsuredPerson_Number>
          <HealthInsuredPerson_Assistance type="string">3</HealthInsuredPerson_Assistance>
          <RelationToInsuredPerson type="string">1</RelationToInsuredPerson>
          <Certificate_StartDate type="string">2010-05-01</Certificate_StartDate>
          <Certificate_ExpiredDate type="string">9999-12-31</Certificate_ExpiredDate>
          <PublicInsurance_Information type="array">
            <PublicInsurance_Information_child type="record">
              <PublicInsurance_Class type="string">010</PublicInsurance_Class>
              <PublicInsurance_Name type="string">感３７の２</PublicInsurance_Name>
              <PublicInsurer_Number type="string">10131142</PublicInsurer_Number>
              <PublicInsuredPerson_Number type="string">1234566</PublicInsuredPerson_Number>
              <Rate_Admission type="string">0.05</Rate_Admission>
              <Money_Admission type="string">     0</Money_Admission>
              <Rate_Outpatient type="string">0.05</Rate_Outpatient>
              <Money_Outpatient type="string">     0</Money_Outpatient>
              <Certificate_IssuedDate type="string">2010-05-01</Certificate_IssuedDate>
              <Certificate_ExpiredDate type="string">9999-12-31</Certificate_ExpiredDate>
            </PublicInsurance_Information_child>
          </PublicInsurance_Information>
        </HealthInsurance_Information_child>
      </HealthInsurance_Information>
      <Payment_Information type="record">
        <Reduction_Reason type="string">01</Reduction_Reason>
        <Reduction_Reason_Name type="string">低所得</Reduction_Reason_Name>
        <Discount type="string">01</Discount>
        <Discount_Name type="string">10(%)</Discount_Name>
        <Ic_Code type="string">02</Ic_Code>
        <Ic_Code_Name type="string">振込</Ic_Code_Name>
      </Payment_Information>
    </Patient_Information>
  </patientmodres>
</xmlio2>"""

res = res2

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


last_data = orca_api_formatter(origin["patientmodres"])
pprint.pprint(last_data)
with open(file="result3.json", mode="w", encoding="utf-8") as fp:
    json.dump(last_data, fp, ensure_ascii=False, indent=2)
