# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Provenance
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import provenance


def impl_provenance_1(inst):
    assert inst.activity.coding[0].code == "CREATE"
    assert inst.activity.coding[0].display == "create"
    assert inst.activity.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-DataOperation"
    assert inst.activity.text == "antiviral resistance detection"
    assert inst.agent[0].type.coding[0].code == "AUT"
    assert inst.agent[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.agent[0].who.reference == "Practitioner/example"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.identifier.type.coding[0].code == "biocompute"
    assert inst.entity[0].what.identifier.type.coding[0].display == "obj.1001"
    assert inst.entity[0].what.identifier.type.coding[0].system == "https://hive.biochemistry.gwu.edu"
    assert inst.entity[0].what.identifier.value == (
    "https://hive.biochemistry.gwu.edu/cgi-"
    "bin/prd/htscsrs/servlet.cgi?pageid=bcoexample_1"
    )
    assert inst.id == "example-biocompute-object"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.occurredPeriod.start == fhirtypes.DateTime.validate("2017-06-06")
    assert inst.recorded == fhirtypes.Instant.validate("2016-06-09T08:12:14+10:00")
    assert inst.target[0].reference == "MolecularSequence/example/_history/1"
    assert inst.text.status == "generated"


def test_provenance_1(base_settings):
    """No. 1 tests collection for Provenance.
    Test File: provenance-example-biocompute-object.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example-biocompute-object.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_1(inst2)


def impl_provenance_2(inst):
    assert inst.activity.coding[0].code == "AU"
    assert inst.activity.coding[0].display == "authenticated"
    assert inst.activity.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion"
    assert inst.agent[0].role[0].coding[0].code == "AUT"
    assert inst.agent[0].role[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.agent[0].who.reference == "Patient/72"
    assert inst.id == "consent-signature"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.patient.reference == "Patient/example"
    assert inst.recorded == fhirtypes.Instant.validate("2016-05-26T00:41:10-04:00")
    assert inst.signature[0].data == bytes_validator("dGhpcyBibG9iIGlzIHNuaXBwZWQ=")
    assert inst.signature[0].sigFormat == "application/signature+xml"
    assert inst.signature[0].targetFormat == "application/fhir+xml"
    assert inst.signature[0].type[0].code == "1.2.840.10065.1.12.1.1"
    assert inst.signature[0].type[0].display == "Author's Signature"
    assert inst.signature[0].type[0].system == "urn:iso-astm:E1762-95:2013"
    assert inst.signature[0].when == fhirtypes.Instant.validate("2016-05-26T00:41:10-04:00")
    assert inst.signature[0].who.reference == "Patient/72"
    assert inst.target[0].reference == "Consent/consent-example-basic/_history/1"
    assert inst.text.status == "generated"


def test_provenance_2(base_settings):
    """No. 2 tests collection for Provenance.
    Test File: provenance-consent-signature.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-consent-signature.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_2(inst2)


def impl_provenance_3(inst):
    assert inst.activity.coding[0].code == "Derivation"
    assert inst.activity.coding[0].system == "http://hl7.org/fhir/w3c-provenance-activity-type"
    assert inst.agent[0].id == "a1"
    assert inst.agent[0].type.coding[0].code == "assembler"
    assert inst.agent[0].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/provenance-"
    "participant-type"
    )
    assert inst.agent[0].who.display == "Device/software"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.reference == "DocumentReference/example"
    assert inst.id == "example-import"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.patient.reference == "Patient/example"
    assert inst.policy[0] == "urn:ihe:pcc:qedm:2017:document-provenance-policy"
    assert inst.recorded == fhirtypes.Instant.validate("2015-06-27T08:39:24+10:00")
    assert inst.target[0].reference == "Condition/example"
    assert inst.target[1].reference == "Condition/example2"
    assert inst.target[2].reference == "Encounter/example"
    assert inst.target[3].reference == "Immunization/example"
    assert inst.text.status == "generated"


def test_provenance_3(base_settings):
    """No. 3 tests collection for Provenance.
    Test File: provenance-example-import.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example-import.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_3(inst2)


def impl_provenance_4(inst):
    assert inst.activity.coding[0].code == "CREATE"
    assert inst.activity.coding[0].display == "create"
    assert inst.activity.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-DataOperation"
    assert inst.agent[0].type.coding[0].code == "assembler"
    assert inst.agent[0].type.coding[0].display == "Assembler"
    assert inst.agent[0].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/provenance-"
    "participant-type"
    )
    assert inst.agent[0].who.display == "LEAP Consent Management Service"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.reference == (
    "http://example.org/fhir/QuestionnaireResponse/some-"
    "questionnaire-response"
    )
    assert inst.id == "example-create-consent"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.patient.reference == "Patient/example"
    assert inst.recorded == fhirtypes.Instant.validate("2021-09-10T07:08:21.722+00:00")
    assert inst.target[0].reference == "Consent/consent-example-basic/_history/1"
    assert inst.text.status == "generated"


def test_provenance_4(base_settings):
    """No. 4 tests collection for Provenance.
    Test File: provenance-example-create-consent.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example-create-consent.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_4(inst2)


def impl_provenance_5(inst):
    assert inst.activity.coding[0].code == "originate"
    assert inst.activity.coding[0].system == "http://terminology.hl7.org/CodeSystem/iso-21089-lifecycle"
    assert inst.agent[0].type.coding[0].code == "110153"
    assert inst.agent[0].type.coding[0].display == "Source Role ID"
    assert inst.agent[0].type.coding[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.agent[0].who.display == "myMachine.example.org"
    assert inst.agent[1].type.coding[0].code == "110152"
    assert inst.agent[1].type.coding[0].display == "Destination Role ID"
    assert inst.agent[1].type.coding[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.agent[1].who.reference == "Device/example"
    assert inst.agent[2].type.coding[0].code == "INF"
    assert inst.agent[2].type.coding[0].display == "Informant"
    assert inst.agent[2].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.agent[2].who.display == "Betty Jones"
    assert inst.authorization[0].concept.coding[0].code == "TREAT"
    assert inst.authorization[0].concept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.basedOn[0].reference == "CarePlan/example"
    assert inst.encounter.reference == "Encounter/home"
    assert inst.id == "example-advanced"
    assert inst.location.reference == "Location/1/_history/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.occurredDateTime == fhirtypes.DateTime.validate("2020-04-29T09:49:00.000Z")
    assert inst.patient.reference == "Patient/example"
    assert inst.policy[0] == "http://example.org/policy/1234"
    assert inst.recorded == fhirtypes.Instant.validate("2020-04-29T09:49:00.000Z")
    assert inst.signature[0].sigFormat == "image/jpeg"
    assert inst.signature[0].type[0].code == "1.2.840.10065.1.12.1.5"
    assert inst.signature[0].type[0].display == "Verification Signature"
    assert inst.signature[0].type[0].system == "urn:iso-astm:E1762-95:2013"
    assert inst.signature[0].when == fhirtypes.Instant.validate("2020-04-29T09:49:00.000Z")
    assert inst.signature[0].who.display == "Betty Jones"
    assert inst.target[0].reference == "List/example"
    assert inst.text.status == "generated"


def test_provenance_5(base_settings):
    """No. 5 tests collection for Provenance.
    Test File: provenance-example-advanced.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example-advanced.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_5(inst2)


def impl_provenance_6(inst):
    assert inst.agent[0].type.coding[0].code == "INF"
    assert inst.agent[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.agent[0].who.reference == "Patient/pat3"
    assert inst.id == "example1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.recorded == fhirtypes.Instant.validate("2021-12-07T12:23:45+11:00")
    assert inst.target[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/targetElement"
    assert inst.target[0].extension[0].valueUri == "n1"
    assert inst.target[0].reference == "Patient/pat3/_history/1"
    assert inst.text.status == "generated"


def test_provenance_6(base_settings):
    """No. 6 tests collection for Provenance.
    Test File: provenance-example1.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example1.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_6(inst2)


def impl_provenance_7(inst):
    assert inst.agent[0].type.coding[0].code == "INF"
    assert inst.agent[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.agent[0].who.reference == "RelatedPerson/f001"
    assert inst.id == "example2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.recorded == fhirtypes.Instant.validate("2021-12-08T16:54:24+11:00")
    assert inst.target[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/targetElement"
    assert inst.target[0].extension[0].valueUri == "n2"
    assert inst.target[0].reference == "Patient/pat3/_history/1"
    assert inst.text.status == "generated"


def test_provenance_7(base_settings):
    """No. 7 tests collection for Provenance.
    Test File: provenance-example2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example2.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_7(inst2)


def impl_provenance_8(inst):
    assert inst.activity.coding[0].code == "3457005"
    assert inst.activity.coding[0].display == "Referral"
    assert inst.activity.coding[0].system == "http://snomed.info/sct"
    assert inst.agent[0].type.coding[0].code == "AUT"
    assert inst.agent[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.agent[0].who.reference == "Practitioner/xcda-author"
    assert inst.agent[1].id == "a1"
    assert inst.agent[1].type.coding[0].code == "DEV"
    assert inst.agent[1].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.agent[1].who.display == "Device/software"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.display == "CDA Document in XDS repository"
    assert inst.entity[0].what.reference == "DocumentReference/example"
    assert inst.id == "example"
    assert inst.location.reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.occurredPeriod.end == fhirtypes.DateTime.validate("2015-06-28")
    assert inst.occurredPeriod.start == fhirtypes.DateTime.validate("2015-06-27")
    assert inst.policy[0] == "http://acme.com/fhir/Consent/25"
    assert inst.recorded == fhirtypes.Instant.validate("2015-06-27T08:39:24+10:00")
    assert inst.target[0].reference == "Procedure/example/_history/1"
    assert inst.text.status == "generated"


def test_provenance_8(base_settings):
    """No. 8 tests collection for Provenance.
    Test File: provenance-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_8(inst2)


def impl_provenance_9(inst):
    assert inst.activity.coding[0].code == "CREATE"
    assert inst.activity.coding[0].display == "create"
    assert inst.activity.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-DataOperation"
    assert inst.activity.text == (
    "profiling Short Tandem Repeats (STRs) from high throughput "
    "sequencing data."
    )
    assert inst.agent[0].type.coding[0].code == "AUT"
    assert inst.agent[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.agent[0].who.reference == "Patient/example"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.identifier.type.coding[0].code == "CWL"
    assert inst.entity[0].what.identifier.type.coding[0].display == "lobSTR"
    assert inst.entity[0].what.identifier.type.coding[0].system == "https://github.com/common-workflow-language/workflows"
    assert inst.entity[0].what.identifier.value == (
    "https://github.com/common-workflow-"
    "language/workflows/blob/master/workflows/lobSTR/lobSTR-"
    "workflow.cwl"
    )
    assert inst.id == "example-cwl"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.occurredPeriod.start == fhirtypes.DateTime.validate("2016-11-30")
    assert inst.recorded == fhirtypes.Instant.validate("2016-12-01T08:12:14+10:00")
    assert inst.target[0].reference == "MolecularSequence/example-pgx-1/_history/1"
    assert inst.text.status == "generated"


def test_provenance_9(base_settings):
    """No. 9 tests collection for Provenance.
    Test File: provenance-example-cwl.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example-cwl.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_9(inst2)


def impl_provenance_10(inst):
    assert inst.agent[0].type.coding[0].code == "AUT"
    assert inst.agent[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.agent[0].who.reference == "Practitioner/f007"
    assert inst.id == "example3"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.recorded == fhirtypes.Instant.validate("2021-12-08T16:54:24+11:00")
    assert inst.target[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/targetPath"
    assert inst.target[0].extension[0].valueString == "Procedure.followUp.text"
    assert inst.target[0].reference == "Procedure/example/_history/1"
    assert inst.text.status == "generated"


def test_provenance_10(base_settings):
    """No. 10 tests collection for Provenance.
    Test File: provenance-example3.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example3.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_10(inst2)