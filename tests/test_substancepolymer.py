# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstancePolymer
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import substancepolymer


def impl_substancepolymer_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_substancepolymer_1(base_settings):
    """No. 1 tests collection for SubstancePolymer.
    Test File: substancepolymer-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "substancepolymer-example.json"
    )
    inst = substancepolymer.SubstancePolymer.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubstancePolymer" == inst.resource_type

    impl_substancepolymer_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubstancePolymer" == data["resourceType"]

    inst2 = substancepolymer.SubstancePolymer(**data)
    impl_substancepolymer_1(inst2)