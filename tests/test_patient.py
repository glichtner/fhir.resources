# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import patient


def impl_patient_1(inst):
    assert inst.active is True
    assert inst.address[0].city == "上海市"
    assert inst.address[0].district == "黄埔区"
    assert inst.address[0].line[0] == "马当路190号"
    assert inst.address[0].period.start == fhirtypes.DateTime.validate("1974-12-25")
    assert inst.address[0].postalCode == "200000"
    assert inst.address[0].type == "both"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1974-12-25")
    assert inst.deceasedBoolean is False
    assert inst.gender == "male"
    assert inst.id == "ch-example"
    assert inst.identifier[0].assigner.display == "市卫生局"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2001-05-06")
    assert inst.identifier[0].system == "urn:oid:1.2.36.146.595.217.0.1"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "3112219680806371X"
    assert inst.managingOrganization.display == "上海东方医院"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2016-05-16T00:55:52Z")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.meta.versionId == "1"
    assert inst.name[0].text == "张无忌"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[1].system == "phone"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "18337177888"
    assert inst.text.status == "generated"


def test_patient_1(base_settings):
    """No. 1 tests collection for Patient.
    Test File: patient-example-chinese.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "patient-example-chinese.json"
    )
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_1(inst2)


def impl_patient_2(inst):
    assert inst.active is True
    assert inst.birthDate == fhirtypes.Date.validate("1932-09-24")
    assert inst.extension[0].url == "http://example.org/StructureDefinition/trials"
    assert inst.extension[0].valueCode == "renal"
    assert inst.gender == "male"
    assert inst.generalPractitioner[0].display == "Dr Adam Careful"
    assert inst.generalPractitioner[0].reference == "Practitioner/example"
    assert inst.id == "glossy"
    assert inst.identifier[0].system == "http://www.goodhealth.org/identifiers/mrn"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123456"
    assert inst.managingOrganization.display == "Good Health Clinic"
    assert inst.managingOrganization.reference == "Organization/2"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2014-11-13T11:41:00+11:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Levin"
    assert inst.name[0].given[0] == "Henry"
    assert inst.name[0].suffix[0] == "The 7th"
    assert inst.text.status == "generated"


def test_patient_2(base_settings):
    """No. 2 tests collection for Patient.
    Test File: patient-glossy-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "patient-glossy-example.json"
    )
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_2(inst2)


def impl_patient_3(inst):
    assert inst.active is True
    assert inst.address[0].line[0] == "2222 Home Street"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1973-05-31")
    assert inst.gender == "female"
    assert inst.id == "mom"
    assert inst.identifier[0].system == "http://hl7.org/fhir/sid/us-ssn"
    assert inst.identifier[0].type.coding[0].code == "SS"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].value == "444222222"
    assert inst.link[0].other.reference == "RelatedPerson/newborn-mom"
    assert inst.link[0].type == "seealso"
    assert inst.managingOrganization.reference == "Organization/hl7"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2012-05-29T23:45:32Z")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Everywoman"
    assert inst.name[0].given[0] == "Eve"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "555-555-2003"
    assert inst.text.status == "generated"


def test_patient_3(base_settings):
    """No. 3 tests collection for Patient.
    Test File: patient-example-mom.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "patient-example-mom.json"
    )
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_3(inst2)


def impl_patient_4(inst):
    assert inst.active is True
    assert inst.birthDate == fhirtypes.Date.validate("1974-12-25")
    assert inst.deceasedBoolean is False
    assert inst.extension[0].extension[0].url == "value"
    assert inst.extension[0].extension[0].valueCodeableConcept.coding[0].code == "446141000124107"
    assert inst.extension[0].extension[0].valueCodeableConcept.coding[0].display == "Identifies as female gender (finding)"
    assert inst.extension[0].extension[0].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.extension[0].extension[1].url == "period"
    assert inst.extension[0].extension[1].valuePeriod.start == fhirtypes.DateTime.validate("2001-05-06")
    assert inst.extension[0].extension[2].url == "comment"
    assert inst.extension[0].extension[2].valueString == "Patient transitioned from male to female in 2001."
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/individual-"
    "genderIdentity"
    )
    assert inst.extension[1].extension[0].url == "value"
    assert inst.extension[1].extension[0].valueCodeableConcept.coding[0].code == "LA29519-8"
    assert inst.extension[1].extension[0].valueCodeableConcept.coding[0].display == "she/her/her/hers/herself"
    assert inst.extension[1].extension[0].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.extension[1].extension[1].url == "period"
    assert inst.extension[1].extension[1].valuePeriod.start == fhirtypes.DateTime.validate("2001-05-06")
    assert inst.extension[1].extension[2].url == "comment"
    assert inst.extension[1].extension[2].valueString == "Patient transitioned from male to female in 2001."
    assert inst.extension[1].url == "http://hl7.org/fhir/StructureDefinition/individual-pronouns"
    assert inst.extension[2].extension[0].url == "value"
    assert inst.extension[2].extension[0].valueCodeableConcept.coding[0].code == "male"
    assert inst.extension[2].extension[0].valueCodeableConcept.coding[0].display == "Male"
    assert inst.extension[2].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/administrative-gender"
    assert inst.extension[2].extension[1].url == "internationalEquivalent"
    assert inst.extension[2].extension[1].valueCodeableConcept.coding[0].code == "M"
    assert inst.extension[2].extension[1].valueCodeableConcept.coding[0].display == "Male"
    assert inst.extension[2].extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/icaosex"
    assert inst.extension[2].extension[2].url == "type"
    assert inst.extension[2].extension[2].valueCodeableConcept.coding[0].code == "76689-9"
    assert inst.extension[2].extension[2].valueCodeableConcept.coding[0].display == "Sex Assigned At Birth"
    assert inst.extension[2].extension[2].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.extension[2].extension[3].url == "effectivePeriod"
    assert inst.extension[2].extension[3].valuePeriod.start == fhirtypes.DateTime.validate("1974-12-25")
    assert inst.extension[2].extension[4].url == "acquisitionDate"
    assert inst.extension[2].extension[4].valueDateTime == fhirtypes.DateTime.validate("2005-12-06")
    assert inst.extension[2].extension[5].url == "sourceDocument"
    assert inst.extension[2].extension[5].valueCodeableReference.reference.reference == "DocumentReference/1"
    assert inst.extension[2].extension[6].url == "sourceField"
    assert inst.extension[2].extension[6].valueString == "SEX"
    assert inst.extension[2].extension[7].url == "jurisdiction"
    assert inst.extension[2].extension[7].valueCodeableConcept.coding[0].code == "OH"
    assert inst.extension[2].extension[7].valueCodeableConcept.coding[0].display == "Ohio"
    assert inst.extension[2].extension[7].valueCodeableConcept.coding[0].system == "https://www.usps.com/"
    assert inst.extension[2].extension[8].url == "comment"
    assert inst.extension[2].extension[8].valueString == (
    "Patient transitioned from male to female in 2001, but their "
    "birth certificate still indicates male."
    )
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/individual-"
    "recordedSexOrGender"
    )
    assert inst.extension[3].extension[0].url == "value"
    assert inst.extension[3].extension[0].valueCodeableConcept.coding[0].code == "male"
    assert inst.extension[3].extension[0].valueCodeableConcept.coding[0].display == "Male"
    assert inst.extension[3].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/administrative-gender"
    assert inst.extension[3].extension[1].url == "internationalEquivalent"
    assert inst.extension[3].extension[1].valueCodeableConcept.coding[0].code == "M"
    assert inst.extension[3].extension[1].valueCodeableConcept.coding[0].display == "Male"
    assert inst.extension[3].extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/icaosex"
    assert inst.extension[3].extension[2].url == "type"
    assert inst.extension[3].extension[2].valueCodeableConcept.coding[0].code == "insurance-card"
    assert inst.extension[3].extension[2].valueCodeableConcept.coding[0].display == "Insurance Card"
    assert inst.extension[3].extension[2].valueCodeableConcept.coding[0].system == "http://local-code-system.org/recorded-sex-or-gender-type"
    assert inst.extension[3].extension[3].url == "effectivePeriod"
    assert inst.extension[3].extension[3].valuePeriod.start == fhirtypes.DateTime.validate("2021-05-25")
    assert inst.extension[3].extension[4].url == "acquisitionDate"
    assert inst.extension[3].extension[4].valueDateTime == fhirtypes.DateTime.validate("2021-06-06")
    assert inst.extension[3].extension[5].url == "sourceDocument"
    assert inst.extension[3].extension[5].valueCodeableReference.reference.reference == "DocumentReference/2"
    assert inst.extension[3].extension[6].url == "sourceField"
    assert inst.extension[3].extension[6].valueString == "SEX"
    assert inst.extension[3].extension[7].url == "jurisdiction"
    assert inst.extension[3].extension[7].valueCodeableConcept.coding[0].code == "ICCA-P"
    assert inst.extension[3].extension[7].valueCodeableConcept.coding[0].display == "Indigo Crucifix Cobalt Aegis Payer"
    assert inst.extension[3].extension[7].valueCodeableConcept.coding[0].system == (
    "http://local-code-system.org/recorded-sex-or-gender-"
    "jurisdiction"
    )
    assert inst.extension[3].extension[8].url == "comment"
    assert inst.extension[3].extension[8].valueString == (
    "Patient transitioned from male to female in 2001, but their "
    "insurance card still indicates male."
    )
    assert inst.extension[3].url == (
    "http://hl7.org/fhir/StructureDefinition/individual-"
    "recordedSexOrGender"
    )
    assert inst.extension[4].extension[0].url == "value"
    assert inst.extension[4].extension[0].valueCodeableConcept.coding[0].code == "M"
    assert inst.extension[4].extension[0].valueCodeableConcept.coding[0].display == "Male"
    assert inst.extension[4].extension[0].valueCodeableConcept.coding[0].system == "http://ohio.example.gov/drivers-license-sex"
    assert inst.extension[4].extension[1].url == "internationalEquivalent"
    assert inst.extension[4].extension[1].valueCodeableConcept.coding[0].code == "M"
    assert inst.extension[4].extension[1].valueCodeableConcept.coding[0].display == "Male"
    assert inst.extension[4].extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/icaosex"
    assert inst.extension[4].extension[2].url == "type"
    assert inst.extension[4].extension[2].valueCodeableConcept.coding[0].code == "drivers-license"
    assert inst.extension[4].extension[2].valueCodeableConcept.coding[0].display == "Driver's License"
    assert inst.extension[4].extension[2].valueCodeableConcept.coding[0].system == (
    "http://jurisdiction-specific.example.com/document-type-code-"
    "system"
    )
    assert inst.extension[4].extension[3].url == "effectivePeriod"
    assert inst.extension[4].extension[3].valuePeriod.start == fhirtypes.DateTime.validate("1974-12-25")
    assert inst.extension[4].extension[4].url == "acquisitionDate"
    assert inst.extension[4].extension[4].valueDateTime == fhirtypes.DateTime.validate("2005-12-06")
    assert inst.extension[4].extension[5].url == "sourceDocument"
    assert inst.extension[4].extension[5].valueCodeableReference.reference.reference == "DocumentReference/1"
    assert inst.extension[4].extension[6].url == "jurisdiction"
    assert inst.extension[4].extension[6].valueCodeableConcept.coding[0].code == "OH"
    assert inst.extension[4].extension[6].valueCodeableConcept.coding[0].display == "Ohio"
    assert inst.extension[4].extension[6].valueCodeableConcept.coding[0].system == "https://www.usps.com/"
    assert inst.extension[4].extension[7].url == "comment"
    assert inst.extension[4].extension[7].valueString == (
    "Patient transitioned from male to female in 2001, but their "
    "driver's license still indicates male."
    )
    assert inst.extension[4].url == (
    "http://hl7.org/fhir/StructureDefinition/individual-"
    "recordedSexOrGender"
    )
    assert inst.extension[5].extension[0].url == "value"
    assert inst.extension[5].extension[0].valueCodeableConcept.coding[0].code == "specified"
    assert inst.extension[5].extension[0].valueCodeableConcept.coding[0].display == "Specified sex for clinical use"
    assert inst.extension[5].extension[0].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/sex-for-clinical-use"
    assert inst.extension[5].extension[1].url == "period"
    assert inst.extension[5].extension[1].valuePeriod.start == fhirtypes.DateTime.validate("2002-07-13")
    assert inst.extension[5].extension[2].url == "comment"
    assert inst.extension[5].extension[2].valueString == "Patient transitioned from male to female in 2001."
    assert inst.extension[5].extension[3].url == "supportingInfo"
    assert inst.extension[5].extension[3].valueCodeableReference.reference.reference == "Observation/1"
    assert inst.extension[5].extension[4].url == "supportingInfo"
    assert inst.extension[5].extension[4].valueCodeableReference.reference.reference == "MedicationUsage/2"
    assert inst.extension[5].url == (
    "http://hl7.org/fhir/StructureDefinition/patient-"
    "sexForClinicalUse"
    )
    assert inst.gender == "male"
    assert inst.id == "patient-example-sex-and-gender"
    assert inst.identifier[0].system == "urn:oid:1.2.36.146.595.217.0.1"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "12345"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Roth"
    assert inst.name[0].given[0] == "Patrick"
    assert inst.name[0].use == "official"
    assert inst.name[1].family == "Roth"
    assert inst.name[1].given[0] == "Patricia"
    assert inst.name[1].use == "usual"
    assert inst.name[2].given[0] == "Pat"
    assert inst.name[2].use == "nickname"
    assert inst.text.status == "generated"


def test_patient_4(base_settings):
    """No. 4 tests collection for Patient.
    Test File: patient-example-sex-and-gender.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "patient-example-sex-and-gender.json"
    )
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_4(inst2)


def impl_patient_5(inst):
    assert inst.active is True
    assert inst.address[0].city == "Amsterdam"
    assert inst.address[0].country == "NLD"
    assert inst.address[0].line[0] == "Bos en Lommerplein 280"
    assert inst.address[0].postalCode == "1055RW"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1960-03-13")
    assert inst.communication[0].language.coding[0].code == "nl-NL"
    assert inst.communication[0].language.coding[0].display == "Dutch"
    assert inst.communication[0].language.coding[0].system == "urn:ietf:bcp:47"
    assert inst.communication[0].preferred is True
    assert inst.contact[0].name.text == "Ariadne Bor-Jansma"
    assert inst.contact[0].name.use == "usual"
    assert inst.contact[0].relationship[0].coding[0].code == "127850001"
    assert inst.contact[0].relationship[0].coding[0].display == "Wife"
    assert inst.contact[0].relationship[0].coding[0].system == "http://snomed.info/sct"
    assert inst.contact[0].relationship[0].coding[1].code == "N"
    assert inst.contact[0].relationship[0].coding[1].system == "http://terminology.hl7.org/CodeSystem/v2-0131"
    assert inst.contact[0].relationship[0].coding[2].code == "WIFE"
    assert inst.contact[0].relationship[0].coding[2].system == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "home"
    assert inst.contact[0].telecom[0].value == "+31201234567"
    assert inst.deceasedBoolean is False
    assert inst.gender == "male"
    assert inst.id == "f201"
    assert inst.identifier[0].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[0].type.text == "BSN"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "123456789"
    assert inst.identifier[1].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[1].type.text == "BSN"
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "123456789"
    assert inst.managingOrganization.display == "AUMC"
    assert inst.managingOrganization.reference == "Organization/f201"
    assert inst.maritalStatus.coding[0].code == "36629006"
    assert inst.maritalStatus.coding[0].display == "Legally married"
    assert inst.maritalStatus.coding[0].system == "http://snomed.info/sct"
    assert inst.maritalStatus.coding[1].code == "M"
    assert inst.maritalStatus.coding[1].system == "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.multipleBirthBoolean is False
    assert inst.name[0].family == "Bor"
    assert inst.name[0].given[0] == "Roelof Olaf"
    assert inst.name[0].prefix[0] == "Drs."
    assert inst.name[0].suffix[0] == "PDEng."
    assert inst.name[0].text == "Roel"
    assert inst.name[0].use == "official"
    assert inst.photo[0].contentType == "image/jpeg"
    assert inst.photo[0].url == "Binary/f006"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "mobile"
    assert inst.telecom[0].value == "+31612345678"
    assert inst.telecom[1].system == "phone"
    assert inst.telecom[1].use == "home"
    assert inst.telecom[1].value == "+31201234567"
    assert inst.text.status == "generated"


def test_patient_5(base_settings):
    """No. 5 tests collection for Patient.
    Test File: patient-example-f201-roel.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "patient-example-f201-roel.json"
    )
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_5(inst2)


def impl_patient_6(inst):
    assert inst.active is True
    assert inst.birthDate == fhirtypes.Date.validate("2021-01-01")
    assert inst.gender == "unknown"
    assert inst.id == "denovoChild"
    assert inst.identifier[0].assigner.display == "Child Hospital"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2021-01-01")
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/persons"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].display == "Medical record number"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "11111"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Doe"
    assert inst.name[0].given[0] == "Child"
    assert inst.name[0].given[1] == "Junior"
    assert inst.name[0].use == "official"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Child "
    "Junior Doe (OFFICIAL)</b> (no stated gender) 2021-01-01 ( "
    "Medical record number: 11111 (TEMP))</p></div>"
    )
    assert inst.text.status == "generated"


def test_patient_6(base_settings):
    """No. 6 tests collection for Patient.
    Test File: Patient-denovoChild.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Patient-denovoChild.json"
    )
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_6(inst2)


def impl_patient_7(inst):
    assert inst.active is True
    assert inst.address[0].city == "Metropolis"
    assert inst.address[0].country == "USA"
    assert inst.address[0].line[0] == "100 Main St"
    assert inst.address[0].postalCode == "44130"
    assert inst.address[0].state == "Il"
    assert inst.birthDate == fhirtypes.Date.validate("1956-05-27")
    assert inst.gender == "male"
    assert inst.id == "xds"
    assert inst.identifier[0].system == "urn:oid:1.2.3.4.5"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "89765a87b"
    assert inst.managingOrganization.reference == "Organization/2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Doe"
    assert inst.name[0].given[0] == "John"
    assert inst.text.status == "generated"


def test_patient_7(base_settings):
    """No. 7 tests collection for Patient.
    Test File: patient-example-xds.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "patient-example-xds.json"
    )
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_7(inst2)


def impl_patient_8(inst):
    assert inst.active is True
    assert inst.address[0].city == "PleasantVille"
    assert inst.address[0].district == "Rainbow"
    assert inst.address[0].line[0] == "534 Erewhon St"
    assert inst.address[0].period.start == fhirtypes.DateTime.validate("1974-12-25")
    assert inst.address[0].postalCode == "3999"
    assert inst.address[0].state == "Vic"
    assert inst.address[0].text == "534 Erewhon St PeasantVille, Rainbow, Vic  3999"
    assert inst.address[0].type == "both"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1974-12-25")
    assert inst.contact[0].address.city == "PleasantVille"
    assert inst.contact[0].address.district == "Rainbow"
    assert inst.contact[0].address.line[0] == "534 Erewhon St"
    assert inst.contact[0].address.period.start == fhirtypes.DateTime.validate("1974-12-25")
    assert inst.contact[0].address.postalCode == "3999"
    assert inst.contact[0].address.state == "Vic"
    assert inst.contact[0].address.type == "both"
    assert inst.contact[0].address.use == "home"
    assert inst.contact[0].gender == "female"
    assert inst.contact[0].name.family == "du Marché"
    assert inst.contact[0].name.given[0] == "Bénédicte"
    assert inst.contact[0].period.start == fhirtypes.DateTime.validate("2012")
    assert inst.contact[0].relationship[0].coding[0].code == "N"
    assert inst.contact[0].relationship[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0131"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].value == "+33 (237) 998327"
    assert inst.deceasedBoolean is False
    assert inst.gender == "male"
    assert inst.id == "example"
    assert inst.identifier[0].assigner.display == "Acme Healthcare"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2001-05-06")
    assert inst.identifier[0].system == "urn:oid:1.2.36.146.595.217.0.1"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "12345"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Chalmers"
    assert inst.name[0].given[0] == "Peter"
    assert inst.name[0].given[1] == "James"
    assert inst.name[0].use == "official"
    assert inst.name[1].given[0] == "Jim"
    assert inst.name[1].use == "usual"
    assert inst.name[2].family == "Windsor"
    assert inst.name[2].given[0] == "Peter"
    assert inst.name[2].given[1] == "James"
    assert inst.name[2].period.end == fhirtypes.DateTime.validate("2002")
    assert inst.name[2].use == "maiden"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[1].rank == 1
    assert inst.telecom[1].system == "phone"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "(03) 5555 6473"
    assert inst.telecom[2].rank == 2
    assert inst.telecom[2].system == "phone"
    assert inst.telecom[2].use == "mobile"
    assert inst.telecom[2].value == "(03) 3410 5613"
    assert inst.telecom[3].period.end == fhirtypes.DateTime.validate("2014")
    assert inst.telecom[3].system == "phone"
    assert inst.telecom[3].use == "old"
    assert inst.telecom[3].value == "(03) 5555 8834"
    assert inst.text.status == "generated"


def test_patient_8(base_settings):
    """No. 8 tests collection for Patient.
    Test File: patient-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "patient-example.json"
    )
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_8(inst2)


def impl_patient_9(inst):
    assert inst.active is True
    assert inst.address[0].line[0] == "2222 Home Street"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1973-05-31")
    assert inst.gender == "female"
    assert inst.id == "genetics-example1"
    assert inst.identifier[0].system == "http://hl7.org/fhir/sid/us-ssn"
    assert inst.identifier[0].type.coding[0].code == "SS"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].value == "444222222"
    assert inst.managingOrganization.reference == "Organization/hl7"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2012-05-29T23:45:32Z")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Everywoman"
    assert inst.name[0].given[0] == "Eve"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "555-555-2003"
    assert inst.text.status == "generated"


def test_patient_9(base_settings):
    """No. 9 tests collection for Patient.
    Test File: patient-genetics-example1.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "patient-genetics-example1.json"
    )
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_9(inst2)


def impl_patient_10(inst):
    assert inst.active is True
    assert inst.birthDate == fhirtypes.Date.validate("2000-01-01")
    assert inst.gender == "male"
    assert inst.id == "denovoFather"
    assert inst.identifier[0].assigner.display == "Child Hospital"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2021-01-01")
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/persons"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].display == "Medical record number"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "11113"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Doe"
    assert inst.name[0].given[0] == "John"
    assert inst.name[0].given[1] == "Father"
    assert inst.name[0].use == "official"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>John "
    "Father Doe (OFFICIAL)</b> (no stated gender) 2000-01-01 ( "
    "Medical record number: 11113 (TEMP))</p></div>"
    )
    assert inst.text.status == "generated"


def test_patient_10(base_settings):
    """No. 10 tests collection for Patient.
    Test File: Patient-denovoFather.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Patient-denovoFather.json"
    )
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_10(inst2)