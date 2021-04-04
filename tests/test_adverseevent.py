# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import adverseevent


def impl_adverseevent_1(inst):
    assert inst.actuality == "actual"
    assert inst.category[0].coding[0].code == "medication-mishap"
    assert inst.category[0].coding[0].display == "Medication Mishap"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/adverse-event-category"
    )
    assert inst.code.coding[0].code == "304386008"
    assert inst.code.coding[0].display == "O/E - itchy rash"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "This was a mild rash on the left forearm"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://acme.com/ids/patients/risks"
    assert inst.identifier[0].value == "49476534"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2017-01-29T12:34:56+00:00"
    )
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.seriousness.coding[0].code == "non-serious"
    assert inst.seriousness.coding[0].display == "Non-serious"
    assert inst.seriousness.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/adverse-event-" "seriousness"
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.suspectEntity[0].instanceReference.reference == "Medication/example"
    assert inst.text.status == "generated"


def test_adverseevent_1(base_settings):
    """No. 1 tests collection for AdverseEvent.
    Test File: adverseevent-example.json
    """
    filename = base_settings["unittest_data_dir"] / "adverseevent-example.json"
    inst = adverseevent.AdverseEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AdverseEvent" == inst.resource_type

    impl_adverseevent_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AdverseEvent" == data["resourceType"]

    inst2 = adverseevent.AdverseEvent(**data)
    impl_adverseevent_1(inst2)
