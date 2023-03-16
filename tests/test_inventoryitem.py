# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/InventoryItem
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import inventoryitem


def impl_inventoryitem_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_inventoryitem_1(base_settings):
    """No. 1 tests collection for InventoryItem.
    Test File: inventoryitem-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "inventoryitem-example.json"
    )
    inst = inventoryitem.InventoryItem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "InventoryItem" == inst.resource_type

    impl_inventoryitem_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "InventoryItem" == data["resourceType"]

    inst2 = inventoryitem.InventoryItem(**data)
    impl_inventoryitem_1(inst2)