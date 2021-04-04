# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionProduct
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import nutritionproduct


def impl_nutritionproduct_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_nutritionproduct_1(base_settings):
    """No. 1 tests collection for NutritionProduct.
    Test File: nutritionproduct-example.json
    """
    filename = base_settings["unittest_data_dir"] / "nutritionproduct-example.json"
    inst = nutritionproduct.NutritionProduct.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionProduct" == inst.resource_type

    impl_nutritionproduct_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionProduct" == data["resourceType"]

    inst2 = nutritionproduct.NutritionProduct(**data)
    impl_nutritionproduct_1(inst2)
