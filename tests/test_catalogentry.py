# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CatalogEntry
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import catalogentry


def impl_catalogentry_1(inst):
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate("2018-12-16")
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://example.com/identifier"
    assert inst.identifier[0].value == "456"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "Serum electrolyte panel"
    assert inst.note[0].authorString == "Adam Man"
    assert inst.note[0].text == "created as an example"
    assert inst.orderable is True
    assert (
        inst.referencedItem.reference
        == "http://example.org/fhir/ActivityDefinition/789"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.type == "ActivityDefinition"
    assert inst.updatedBy.reference == "Person/2"


def test_catalogentry_1(base_settings):
    """No. 1 tests collection for CatalogEntry.
    Test File: catalogentry-example.json
    """
    filename = base_settings["unittest_data_dir"] / "catalogentry-example.json"
    inst = catalogentry.CatalogEntry.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CatalogEntry" == inst.resource_type

    impl_catalogentry_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CatalogEntry" == data["resourceType"]

    inst2 = catalogentry.CatalogEntry(**data)
    impl_catalogentry_1(inst2)
