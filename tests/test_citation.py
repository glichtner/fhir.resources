# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Citation
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import citation


def impl_citation_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_citation_1(base_settings):
    """No. 1 tests collection for Citation.
    Test File: citation-example.json
    """
    filename = base_settings["unittest_data_dir"] / "citation-example.json"
    inst = citation.Citation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Citation" == inst.resource_type

    impl_citation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Citation" == data["resourceType"]

    inst2 = citation.Citation(**data)
    impl_citation_1(inst2)
