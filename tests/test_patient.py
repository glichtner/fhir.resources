# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import patient


def impl_patient_1(inst):
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
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123456"
    assert inst.managingOrganization.display == "Good Health Clinic"
    assert inst.managingOrganization.reference == "Organization/2"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2014-11-13T11:41:00+11:00"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "Levin"
    assert inst.name[0].given[0] == "Henry"
    assert inst.name[0].suffix[0] == "The 7th"
    assert inst.text.status == "generated"


def test_patient_1(base_settings):
    """No. 1 tests collection for Patient.
    Test File: patient-glossy-example.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-glossy-example.json"
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
    assert inst.gender == "other"
    assert inst.id == "pat2"
    assert inst.identifier[0].system == "urn:oid:0.1.2.3.4.5.6.7"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123456"
    assert inst.link[0].other.reference == "Patient/pat1"
    assert inst.link[0].type == "seealso"
    assert inst.managingOrganization.display == "ACME Healthcare, Inc"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "Donald"
    assert inst.name[0].given[0] == "Duck"
    assert inst.name[0].given[1] == "D"
    assert inst.name[0].use == "official"
    assert inst.photo[0].contentType == "image/gif"
    assert inst.text.status == "generated"


def test_patient_2(base_settings):
    """No. 2 tests collection for Patient.
    Test File: patient-example-b.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-b.json"
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
    assert inst.contact[0].name.family == "Organa"
    assert inst.contact[0].name.given[0] == "Leia"
    assert inst.contact[0].name.use == "maiden"
    assert inst.contact[0].relationship[0].coding[0].code == "72705000"
    assert inst.contact[0].relationship[0].coding[0].display == "Mother"
    assert inst.contact[0].relationship[0].coding[0].system == "http://snomed.info/sct"
    assert inst.contact[0].relationship[0].coding[1].code == "N"
    assert (
        inst.contact[0].relationship[0].coding[1].system
        == "http://terminology.hl7.org/CodeSystem/v2-0131"
    )
    assert inst.contact[0].relationship[0].coding[2].code == "MTH"
    assert (
        inst.contact[0].relationship[0].coding[2].system
        == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "mobile"
    assert inst.contact[0].telecom[0].value == "+31201234567"
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/patient-" "mothersMaidenName"
    )
    assert inst.extension[0].valueString == "Organa"
    assert inst.gender == "male"
    assert inst.id == "infant-fetal"
    assert (
        inst.identifier[0].system
        == "http://coruscanthealth.org/main-hospital/patient-identifier"
    )
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].value == "MRN657865757378"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "extensions"


def test_patient_3(base_settings):
    """No. 3 tests collection for Patient.
    Test File: patient-example-infant-fetal.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-infant-fetal.json"
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
    assert inst.id == "ihe-pcd"
    assert inst.identifier[0].type.text == "Internal Identifier"
    assert inst.identifier[0].value == "AB60001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "BROOKS"
    assert inst.name[0].given[0] == "ALBERT"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Albert Brooks, ' "Id: AB60001</div>"
    )
    assert inst.text.status == "generated"


def test_patient_4(base_settings):
    """No. 4 tests collection for Patient.
    Test File: patient-example-ihe-pcd.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-ihe-pcd.json"
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
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "3112219680806371X"
    assert inst.managingOrganization.display == "上海东方医院"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2016-05-16T00:55:52Z")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.meta.versionId == "1"
    assert inst.name[0].text == "张无忌"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[1].system == "phone"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "18337177888"
    assert inst.text.status == "generated"


def test_patient_5(base_settings):
    """No. 5 tests collection for Patient.
    Test File: patient-example-chinese.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-chinese.json"
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
    assert inst.birthDate == fhirtypes.Date.validate("2010-03-23")
    assert inst.contact[0].name.family == "Chalmers"
    assert inst.contact[0].name.given[0] == "Peter"
    assert inst.contact[0].name.given[1] == "James"
    assert inst.contact[0].relationship[0].coding[0].code == "C"
    assert (
        inst.contact[0].relationship[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0131"
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "(03) 5555 6473"
    assert inst.extension[0].extension[0].url == "species"
    assert (
        inst.extension[0].extension[0].valueCodeableConcept.coding[0].code == "canislf"
    )
    assert (
        inst.extension[0].extension[0].valueCodeableConcept.coding[0].display == "Dog"
    )
    assert (
        inst.extension[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/animal-species"
    )
    assert inst.extension[0].extension[1].url == "breed"
    assert (
        inst.extension[0].extension[1].valueCodeableConcept.coding[0].code == "58108001"
    )
    assert (
        inst.extension[0].extension[1].valueCodeableConcept.coding[0].display
        == "Golden retriever"
    )
    assert (
        inst.extension[0].extension[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.extension[0].extension[1].valueCodeableConcept.coding[1].code == "gret"
    assert (
        inst.extension[0].extension[1].valueCodeableConcept.coding[1].display
        == "Golden Retriever"
    )
    assert (
        inst.extension[0].extension[1].valueCodeableConcept.coding[1].system
        == "http://example.org/fhir/CodeSystem/animal-breed"
    )
    assert inst.extension[0].extension[2].url == "genderStatus"
    assert (
        inst.extension[0].extension[2].valueCodeableConcept.coding[0].code == "neutered"
    )
    assert (
        inst.extension[0].extension[2].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/animal-genderstatus"
    )
    assert (
        inst.extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/patient-animal"
    )
    assert inst.gender == "female"
    assert inst.id == "animal"
    assert inst.identifier[0].assigner.display == "Maroondah City Council"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2010-05-31")
    assert (
        inst.identifier[0].system
        == "http://www.maroondah.vic.gov.au/AnimalRegFees.aspx"
    )
    assert inst.identifier[0].type.text == "Dog Tag"
    assert inst.identifier[0].value == "1234123"
    assert inst.managingOrganization.display == "Pete's Vetinary Services"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].given[0] == "Kenzi"
    assert inst.name[0].use == "usual"
    assert inst.text.status == "generated"


def test_patient_6(base_settings):
    """No. 6 tests collection for Patient.
    Test File: patient-example-animal.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-animal.json"
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
    assert (
        inst.contact[0].relationship[0].coding[1].system
        == "http://terminology.hl7.org/CodeSystem/v2-0131"
    )
    assert inst.contact[0].relationship[0].coding[2].code == "WIFE"
    assert (
        inst.contact[0].relationship[0].coding[2].system
        == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
    )
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
    assert (
        inst.maritalStatus.coding[1].system
        == "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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


def test_patient_7(base_settings):
    """No. 7 tests collection for Patient.
    Test File: patient-example-f201-roel.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-f201-roel.json"
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
    assert inst.address[0].line[0] == "2222 Home Street"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1973-05-31")
    assert inst.gender == "female"
    assert inst.id == "mom"
    assert inst.identifier[0].system == "http://hl7.org/fhir/sid/us-ssn"
    assert inst.identifier[0].type.coding[0].code == "SS"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].value == "444222222"
    assert inst.link[0].other.reference == "RelatedPerson/newborn-mom"
    assert inst.link[0].type == "seealso"
    assert inst.managingOrganization.reference == "Organization/hl7"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2012-05-29T23:45:32Z")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "Everywoman"
    assert inst.name[0].given[0] == "Eve"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "555-555-2003"
    assert inst.text.status == "generated"


def test_patient_8(base_settings):
    """No. 8 tests collection for Patient.
    Test File: patient-example-mom.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-mom.json"
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
    assert inst.contact[0].address.period.start == fhirtypes.DateTime.validate(
        "1974-12-25"
    )
    assert inst.contact[0].address.postalCode == "3999"
    assert inst.contact[0].address.state == "Vic"
    assert inst.contact[0].address.type == "both"
    assert inst.contact[0].address.use == "home"
    assert inst.contact[0].gender == "female"
    assert inst.contact[0].name.family == "du Marché"
    assert inst.contact[0].name.given[0] == "Bénédicte"
    assert inst.contact[0].period.start == fhirtypes.DateTime.validate("2012")
    assert inst.contact[0].relationship[0].coding[0].code == "N"
    assert (
        inst.contact[0].relationship[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0131"
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].value == "+33 (237) 998327"
    assert inst.deceasedBoolean is False
    assert inst.gender == "male"
    assert inst.id == "example"
    assert inst.identifier[0].assigner.display == "Acme Healthcare"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2001-05-06")
    assert inst.identifier[0].system == "urn:oid:1.2.36.146.595.217.0.1"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "12345"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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


def test_patient_9(base_settings):
    """No. 9 tests collection for Patient.
    Test File: patient-example.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example.json"
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
    assert inst.address[0].city == "PleasantVille"
    assert inst.address[0].line[0] == "534 Erewhon St"
    assert inst.address[0].postalCode == "3999"
    assert inst.address[0].state == "Vic"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1974-12")
    assert inst.contact[0].name.family == "du Marché"
    assert inst.contact[0].name.given[0] == "Bénédicte"
    assert inst.contact[0].name.given[1] == "Denise"
    assert inst.contact[0].name.given[2] == "Marie"
    assert inst.contact[0].relationship[0].coding[0].code == "partner"
    assert inst.contact[0].relationship[0].coding[0].system == (
        "http://example.org/fhir/CodeSystem/patient-contact-" "relationship"
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].value == "+33 (237) 998327"
    assert inst.contained[0].id == "pic1"
    assert inst.contained[1].id == "org3141"
    assert inst.deceasedBoolean is True
    assert (
        inst.extension[0].url
        == "http://example.org/fhir/StructureDefinition/patientAvatar"
    )
    assert inst.extension[0].valueReference.display == "Duck image"
    assert inst.extension[0].valueReference.reference == "#pic1"
    assert inst.extension[1].extension[0].url == "nestedA"
    assert inst.extension[1].extension[0].valueCoding.code == "AB45"
    assert (
        inst.extension[1].extension[0].valueCoding.extension[0].extension[0].url
        == "extra1"
    )
    assert (
        inst.extension[1].extension[0].valueCoding.extension[0].extension[0].valueString
        == "extra info"
    )
    assert inst.extension[1].extension[0].valueCoding.extension[0].url == (
        "http://example.org/fhir/StructureDefinition/extraforcodingWi" "thExt"
    )
    assert inst.extension[1].extension[0].valueCoding.extension[1].url == (
        "http://example.org/fhir/StructureDefinition/extraforcodingWi" "thValue"
    )
    assert inst.extension[1].extension[0].valueCoding.extension[1].valueInteger == 45
    assert inst.extension[1].extension[0].valueCoding.system == "http://demo.org/id/4"
    assert inst.extension[1].extension[1].extension[0].url == "nestedB1"
    assert inst.extension[1].extension[1].extension[0].valueString == "hello"
    assert inst.extension[1].extension[1].id == "q4"
    assert inst.extension[1].extension[1].url == "nestedB"
    assert inst.extension[1].url == (
        "http://example.org/fhir/StructureDefinition/complexExtension" "Example"
    )
    assert inst.gender == "male"
    assert inst.generalPractitioner[0].reference == "#org3141"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2001-05-06")
    assert inst.identifier[0].system == "urn:oid:1.2.36.146.595.217.0.1"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "12345"
    assert inst.managingOrganization.reference == "Organization/1"
    assert (
        inst.maritalStatus.extension[0].url
        == "http://example.org/fhir/StructureDefinition/nullFlavor"
    )
    assert inst.maritalStatus.extension[0].valueCode == "ASKU"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.modifierExtension[0].url
        == "http://example.org/fhir/StructureDefinition/pi"
    )
    assert float(inst.modifierExtension[0].valueDecimal) == float(3.141592653589793)
    assert inst.modifierExtension[1].url == (
        "http://example.org/fhir/StructureDefinition/max-decimal-" "precision"
    )
    assert float(inst.modifierExtension[1].valueDecimal) == float(1.0006502214162465)
    assert inst.multipleBirthInteger == 3
    assert inst.name[0].family == "Chalmers"
    assert inst.name[0].given[0] == "Peter"
    assert inst.name[0].given[1] == "James"
    assert inst.name[0].use == "official"
    assert inst.name[1].given[0] == "Jim"
    assert inst.name[1].use == "usual"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[1].system == "phone"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "(03) 5555 6473"
    assert inst.text.status == "generated"


def test_patient_10(base_settings):
    """No. 10 tests collection for Patient.
    Test File: json-edge-cases.json
    """
    filename = base_settings["unittest_data_dir"] / "json-edge-cases.json"
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
