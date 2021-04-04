# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import medicationknowledge


def impl_medicationknowledge_1(inst):
    assert inst.amount.unit == "mg/ml"
    assert float(inst.amount.value) == float(50)
    assert inst.code.coding[0].code == "0409-6531-02"
    assert (
        inst.code.coding[0].display
        == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    )
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "org4"
    assert inst.doseForm.coding[0].code == "385268001"
    assert inst.doseForm.coding[0].display == "Oral Dose Form (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.sponsor.reference == "#org4"
    assert inst.status == "active"
    assert inst.synonym[0] == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    assert inst.text.status == "generated"


def test_medicationknowledge_1(base_settings):
    """No. 1 tests collection for MedicationKnowledge.
    Test File: medicationknowledge-example.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationknowledge-example.json"
    inst = medicationknowledge.MedicationKnowledge.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationKnowledge" == inst.resource_type

    impl_medicationknowledge_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationKnowledge" == data["resourceType"]

    inst2 = medicationknowledge.MedicationKnowledge(**data)
    impl_medicationknowledge_1(inst2)
