# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EncounterHistory
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import encounterhistory


def impl_encounterhistory_1(inst):
    assert inst.class_fhir.coding[0].code == "IMP"
    assert inst.class_fhir.coding[0].display == "inpatient encounter"
    assert inst.class_fhir.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "in-progress"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Encounter with "
    "patient @example</div>"
    )
    assert inst.text.status == "generated"


def test_encounterhistory_1(base_settings):
    """No. 1 tests collection for EncounterHistory.
    Test File: encounterhistory-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounterhistory-example.json"
    )
    inst = encounterhistory.EncounterHistory.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EncounterHistory" == inst.resource_type

    impl_encounterhistory_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EncounterHistory" == data["resourceType"]

    inst2 = encounterhistory.EncounterHistory(**data)
    impl_encounterhistory_1(inst2)