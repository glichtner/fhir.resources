# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/FormularyItem
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import formularyitem


def impl_formularyitem_1(inst):
    assert inst.code.coding[0].code == "323418000"
    assert inst.code.coding[0].display == "Phenoxymethylpenicillin 125mg/5mL oral solution (product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.coding[1].code == "22571011000036102"
    assert inst.code.coding[1].display == (
    "phenoxymethylpenicillin 125 mg / 5 mL oral liquid, 5 mL "
    "measure"
    )
    assert inst.code.coding[1].system == "http://nehta.gov.au/amt/v2"
    assert inst.id == "formularyitemexample01"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_formularyitem_1(base_settings):
    """No. 1 tests collection for FormularyItem.
    Test File: formularyitemexample01.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "formularyitemexample01.json"
    )
    inst = formularyitem.FormularyItem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "FormularyItem" == inst.resource_type

    impl_formularyitem_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "FormularyItem" == data["resourceType"]

    inst2 = formularyitem.FormularyItem(**data)
    impl_formularyitem_1(inst2)