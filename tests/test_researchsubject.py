# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import researchsubject


def impl_researchsubject_1(inst):
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://example.org/studysubjectids"
    assert inst.identifier[0].type.text == "Subject id"
    assert inst.identifier[0].value == "123"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.progress[0].startDate == fhirtypes.DateTime.validate("2019-06-10")
    assert inst.progress[0].subjectState.coding[0].code == "on-study"
    assert inst.progress[0].subjectState.coding[0].system == "http://terminology.hl7.org/CodeSystem/research-subject-state"
    assert inst.progress[0].type.coding[0].code == "state"
    assert inst.progress[1].milestone.coding[0].code == "SignedUp"
    assert inst.progress[1].startDate == fhirtypes.DateTime.validate("2019-06-06")
    assert inst.progress[1].type.coding[0].code == "milestone"
    assert inst.progress[2].milestone.coding[0].code == "Randomized"
    assert inst.progress[2].startDate == fhirtypes.DateTime.validate("2019-06-10")
    assert inst.progress[2].type.coding[0].code == "milestone"
    assert inst.status == "active"
    assert inst.study.reference == "ResearchStudy/example"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering "
    "here]</div>"
    )
    assert inst.text.status == "generated"


def test_researchsubject_1(base_settings):
    """No. 1 tests collection for ResearchSubject.
    Test File: researchsubject-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "researchsubject-example.json"
    )
    inst = researchsubject.ResearchSubject.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ResearchSubject" == inst.resource_type

    impl_researchsubject_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ResearchSubject" == data["resourceType"]

    inst2 = researchsubject.ResearchSubject(**data)
    impl_researchsubject_1(inst2)