# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalUseIssue
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import clinicaluseissue


def impl_clinicaluseissue_1(inst):
    assert (
        inst.contraindication.comorbidity[0].concept.coding[0].code == "Hepaticdisease"
    )
    assert (
        inst.contraindication.comorbidity[0].concept.coding[0].system
        == "http://ema.europa.eu/example/comorbidity"
    )
    assert (
        inst.contraindication.diseaseSymptomProcedure.concept.coding[0].code
        == "Coagulopathiesandbleedingdiatheses(exclthrombocytopenic)"
    )
    assert inst.contraindication.diseaseSymptomProcedure.concept.coding[0].system == (
        "http://ema.europa.eu/example/contraindicationsasdisease-" "symptom-procedure"
    )
    assert inst.contraindication.diseaseSymptomProcedure.concept.text == (
        "Hepatic disease associated with coagulopathy and clinically "
        "relevant bleeding risk"
    )
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"
    assert inst.type == "contraindication"


def test_clinicaluseissue_1(base_settings):
    """No. 1 tests collection for ClinicalUseIssue.
    Test File: clinicaluseissue-example.json
    """
    filename = base_settings["unittest_data_dir"] / "clinicaluseissue-example.json"
    inst = clinicaluseissue.ClinicalUseIssue.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ClinicalUseIssue" == inst.resource_type

    impl_clinicaluseissue_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ClinicalUseIssue" == data["resourceType"]

    inst2 = clinicaluseissue.ClinicalUseIssue(**data)
    impl_clinicaluseissue_1(inst2)
