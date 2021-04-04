# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
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
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.progress[0].startDate == fhirtypes.DateTime.validate("2019-06-10")
    assert inst.progress[0].state.text == "local version of on-study"
    assert inst.progress[0].type.text == "Local enrollment system"
    assert inst.progress[1].milestone.text == "Local versdion of signed up"
    assert inst.progress[1].startDate == fhirtypes.DateTime.validate("2019-06-06")
    assert inst.progress[1].type.text == "Local milestone system"
    assert inst.progress[2].milestone.text == "Local version of randomised"
    assert inst.progress[2].startDate == fhirtypes.DateTime.validate("2019-06-10")
    assert inst.progress[2].type.text == "Local milestone system"
    assert inst.status == "candidate"
    assert inst.study.reference == "ResearchStudy/example"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_researchsubject_1(base_settings):
    """No. 1 tests collection for ResearchSubject.
    Test File: researchsubject-example.json
    """
    filename = base_settings["unittest_data_dir"] / "researchsubject-example.json"
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
