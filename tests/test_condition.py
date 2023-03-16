# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Condition
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import condition


def impl_condition_1(inst):
    assert inst.abatementAge.code == "a"
    assert inst.abatementAge.system == "http://unitsofmeasure.org"
    assert inst.abatementAge.unit == "years"
    assert float(inst.abatementAge.value) == float(54)
    assert inst.bodySite[0].coding[0].code == "361355005"
    assert inst.bodySite[0].coding[0].display == "Entire head and neck"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].coding[0].code == "encounter-diagnosis"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-category"
    assert inst.clinicalStatus.coding[0].code == "resolved"
    assert inst.clinicalStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    assert inst.code.coding[0].code == "363346000"
    assert inst.code.coding[0].display == "Malignant neoplastic disease"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.evidence[0].reference.display == "Erasmus' diagnostic report of Roel's tumor"
    assert inst.evidence[0].reference.reference == "DiagnosticReport/f201"
    assert inst.id == "f202"
    assert inst.meta.security[0].code == "TBOO"
    assert inst.meta.security[0].display == "taboo"
    assert inst.meta.security[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.onsetAge.code == "a"
    assert inst.onsetAge.system == "http://unitsofmeasure.org"
    assert inst.onsetAge.unit == "years"
    assert float(inst.onsetAge.value) == float(52)
    assert inst.recordedDate == fhirtypes.DateTime.validate("2012-12-01")
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-ver-status"


def test_condition_1(base_settings):
    """No. 1 tests collection for Condition.
    Test File: condition-example-f202-malignancy.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-f202-malignancy.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type

    impl_condition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_1(inst2)


def impl_condition_2(inst):
    assert inst.category[0].coding[0].code == "problem-list-item"
    assert inst.category[0].coding[0].display == "Problem List Item"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-category"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    assert inst.code.text == "Asthma"
    assert inst.id == "example2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.onsetString == "approximately November 2012"
    assert inst.severity.coding[0].code == "255604002"
    assert inst.severity.coding[0].display == "Mild"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Mild Asthma "
    "(Date: 12-Nov 2012)</div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-ver-status"


def test_condition_2(base_settings):
    """No. 2 tests collection for Condition.
    Test File: condition-example2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example2.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type

    impl_condition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_2(inst2)


def impl_condition_3(inst):
    assert inst.category[0].coding[0].code == "encounter-diagnosis"
    assert inst.category[0].coding[0].display == "Encounter Diagnosis"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-category"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    assert inst.code.coding[0].code == "422504002"
    assert inst.code.coding[0].display == "Ischemic stroke (disorder)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Stroke"
    assert inst.id == "stroke"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.onsetDateTime == fhirtypes.DateTime.validate("2010-07-18")
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Ischemic stroke,"
    " July 18, 2010</div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-ver-status"


def test_condition_3(base_settings):
    """No. 3 tests collection for Condition.
    Test File: condition-example-stroke.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-stroke.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type

    impl_condition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_3(inst2)


def impl_condition_4(inst):
    assert inst.bodySite[0].coding[0].code == "51185008"
    assert inst.bodySite[0].coding[0].display == "Thorax"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].coding[0].code == "439401001"
    assert inst.category[0].coding[0].display == "diagnosis"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    assert inst.code.coding[0].code == "254637007"
    assert inst.code.coding[0].display == "NSCLC - Non-small cell lung cancer"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/f002"
    assert inst.evidence[0].concept.coding[0].code == "169069000"
    assert inst.evidence[0].concept.coding[0].display == "CT of thorax"
    assert inst.evidence[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "f002"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.onsetDateTime == fhirtypes.DateTime.validate("2011-05-05")
    assert inst.participant[0].actor.display == "P. van de Heuvel"
    assert inst.participant[0].actor.reference == "Patient/f001"
    assert inst.participant[0].function.coding[0].code == "informant"
    assert inst.participant[0].function.coding[0].display == "Informant"
    assert inst.participant[0].function.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/provenance-"
    "participant-type"
    )
    assert inst.recordedDate == fhirtypes.DateTime.validate("2012-06-03")
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.stage[0].summary.coding[0].code == "258219007"
    assert inst.stage[0].summary.coding[0].display == "stage II"
    assert inst.stage[0].summary.coding[0].system == "http://snomed.info/sct"
    assert inst.stage[0].type.coding[0].code == "260998006"
    assert inst.stage[0].type.coding[0].display == "Clinical staging (qualifier value)"
    assert inst.stage[0].type.coding[0].system == "http://snomed.info/sct"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-ver-status"


def test_condition_4(base_settings):
    """No. 4 tests collection for Condition.
    Test File: condition-example-f002-lung.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-f002-lung.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type

    impl_condition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_4(inst2)


def impl_condition_5(inst):
    assert inst.bodySite[0].coding[0].code == "281158006"
    assert inst.bodySite[0].coding[0].display == "Pulmonary vascular structure"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].coding[0].code == "55607006"
    assert inst.category[0].coding[0].display == "Problem"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].coding[1].code == "problem-list-item"
    assert inst.category[0].coding[1].system == "http://terminology.hl7.org/CodeSystem/condition-category"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    assert inst.code.coding[0].code == "10001005"
    assert inst.code.coding[0].display == "Bacterial sepsis"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.display == "Roel's encounter on March elevanth"
    assert inst.encounter.reference == "Encounter/f203"
    assert inst.evidence[0].reference.display == "Diagnostic report for Roel's sepsis"
    assert inst.evidence[0].reference.reference == "DiagnosticReport/f202"
    assert inst.id == "f203"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.onsetDateTime == fhirtypes.DateTime.validate("2013-03-08")
    assert inst.participant[0].actor.reference == "Practitioner/f201"
    assert inst.participant[0].function.coding[0].code == "author"
    assert inst.participant[0].function.coding[0].display == "Author"
    assert inst.participant[0].function.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/provenance-"
    "participant-type"
    )
    assert inst.recordedDate == fhirtypes.DateTime.validate("2013-03-11")
    assert inst.severity.coding[0].code == "371924009"
    assert inst.severity.coding[0].display == "Moderate to severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-ver-status"


def test_condition_5(base_settings):
    """No. 5 tests collection for Condition.
    Test File: condition-example-f203-sepsis.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-f203-sepsis.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type

    impl_condition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_5(inst2)


def impl_condition_6(inst):
    assert inst.bodySite[0].coding[0].code == "49521004"
    assert inst.bodySite[0].coding[0].display == "Left external ear structure"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.bodySite[0].text == "Left Ear"
    assert inst.category[0].coding[0].code == "encounter-diagnosis"
    assert inst.category[0].coding[0].display == "Encounter Diagnosis"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-category"
    assert inst.category[0].coding[1].code == "439401001"
    assert inst.category[0].coding[1].display == "Diagnosis"
    assert inst.category[0].coding[1].system == "http://snomed.info/sct"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    assert inst.code.coding[0].code == "39065001"
    assert inst.code.coding[0].display == "Burn of ear"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Burnt Ear"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.onsetDateTime == fhirtypes.DateTime.validate("2012-05-24")
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Severe burn of "
    "left ear (Date: 24-May 2012)</div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-ver-status"


def test_condition_6(base_settings):
    """No. 6 tests collection for Condition.
    Test File: condition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type

    impl_condition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_6(inst2)


def impl_condition_7(inst):
    assert inst.bodySite[0].coding[0].code == "40768004"
    assert inst.bodySite[0].coding[0].display == "Left thorax"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.bodySite[0].text == "heart structure"
    assert inst.category[0].coding[0].code == "439401001"
    assert inst.category[0].coding[0].display == "diagnosis"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    assert inst.code.coding[0].code == "368009"
    assert inst.code.coding[0].display == "Heart valve disorder"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.evidence[0].concept.coding[0].code == "426396005"
    assert inst.evidence[0].concept.coding[0].display == "Cardiac chest pain"
    assert inst.evidence[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "f001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.onsetDateTime == fhirtypes.DateTime.validate("2011-08-05")
    assert inst.participant[0].actor.display == "P. van de Heuvel"
    assert inst.participant[0].actor.reference == "Patient/f001"
    assert inst.participant[0].function.coding[0].code == "informant"
    assert inst.participant[0].function.coding[0].display == "Informant"
    assert inst.participant[0].function.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/provenance-"
    "participant-type"
    )
    assert inst.recordedDate == fhirtypes.DateTime.validate("2011-10-05")
    assert inst.severity.coding[0].code == "6736007"
    assert inst.severity.coding[0].display == "Moderate"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-ver-status"


def test_condition_7(base_settings):
    """No. 7 tests collection for Condition.
    Test File: condition-example-f001-heart.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-f001-heart.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type

    impl_condition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_7(inst2)


def impl_condition_8(inst):
    assert inst.abatementDateTime == fhirtypes.DateTime.validate("2013-03-20")
    assert inst.bodySite[0].coding[0].code == "181414000"
    assert inst.bodySite[0].coding[0].display == "Kidney"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].coding[0].code == "55607006"
    assert inst.category[0].coding[0].display == "Problem"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].coding[1].code == "problem-list-item"
    assert inst.category[0].coding[1].system == "http://terminology.hl7.org/CodeSystem/condition-category"
    assert inst.clinicalStatus.coding[0].code == "inactive"
    assert inst.clinicalStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    assert inst.code.coding[0].code == "36225005"
    assert inst.code.coding[0].display == "Acute renal insufficiency specified as due to procedure"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.display == "Roel's encounter on March elevanth"
    assert inst.encounter.reference == "Encounter/f203"
    assert inst.id == "f204"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.note[0].text == "The patient is anuric."
    assert inst.onsetDateTime == fhirtypes.DateTime.validate("2013-03-11")
    assert inst.participant[0].actor.reference == "Practitioner/f201"
    assert inst.participant[0].function.coding[0].code == "author"
    assert inst.participant[0].function.coding[0].display == "Author"
    assert inst.participant[0].function.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/provenance-"
    "participant-type"
    )
    assert inst.recordedDate == fhirtypes.DateTime.validate("2013-03-11")
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.stage[0].assessment[0].display == "Genetic analysis master panel"
    assert inst.stage[0].summary.coding[0].code == "14803004"
    assert inst.stage[0].summary.coding[0].display == "Temporary"
    assert inst.stage[0].summary.coding[0].system == "http://snomed.info/sct"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "differential"
    assert inst.verificationStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-ver-status"


def test_condition_8(base_settings):
    """No. 8 tests collection for Condition.
    Test File: condition-example-f204-renal.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-f204-renal.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type

    impl_condition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_8(inst2)


def impl_condition_9(inst):
    assert inst.category[0].coding[0].code == "problem-list-item"
    assert inst.category[0].coding[0].display == "Problem List Item"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-category"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    assert inst.code.coding[0].code == "312824007"
    assert inst.code.coding[0].display == "Family history of cancer of colon"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "family-history"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Family history "
    "of cancer of colon</div>"
    )
    assert inst.text.status == "generated"


def test_condition_9(base_settings):
    """No. 9 tests collection for Condition.
    Test File: condition-example-family-history.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-family-history.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type

    impl_condition_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_9(inst2)


def impl_condition_10(inst):
    assert inst.bodySite[0].coding[0].code == "49521004"
    assert inst.bodySite[0].coding[0].display == "Left external ear structure"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.bodySite[0].text == "Left Ear"
    assert inst.category[0].coding[0].code == "encounter-diagnosis"
    assert inst.category[0].coding[0].display == "Encounter Diagnosis"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-category"
    assert inst.category[0].coding[1].code == "439401001"
    assert inst.category[0].coding[1].display == "Diagnosis"
    assert inst.category[0].coding[1].system == "http://snomed.info/sct"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    assert inst.code.coding[0].code == "39065001"
    assert inst.code.coding[0].display == "Burn of ear"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Burnt Ear"
    assert inst.id == "example-linkage"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.onsetDateTime == fhirtypes.DateTime.validate("2012-05-24")
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Severe burn of "
    "left ear (Date: 24-May 2012)</div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].system == "http://terminology.hl7.org/CodeSystem/condition-ver-status"


def test_condition_10(base_settings):
    """No. 10 tests collection for Condition.
    Test File: condition-example-linkage.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-linkage.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type

    impl_condition_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_10(inst2)