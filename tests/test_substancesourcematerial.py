# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceSourceMaterial
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import substancesourcematerial


def impl_substancesourcematerial_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated '
        "Narrative</b></p></div>"
    )
    assert inst.text.status == "generated"


def test_substancesourcematerial_1(base_settings):
    """No. 1 tests collection for SubstanceSourceMaterial.
    Test File: substancesourcematerial-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "substancesourcematerial-example.json"
    )
    inst = substancesourcematerial.SubstanceSourceMaterial.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubstanceSourceMaterial" == inst.resource_type

    impl_substancesourcematerial_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubstanceSourceMaterial" == data["resourceType"]

    inst2 = substancesourcematerial.SubstanceSourceMaterial(**data)
    impl_substancesourcematerial_1(inst2)
