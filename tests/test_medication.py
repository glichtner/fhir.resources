# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import medication


def impl_medication_1(inst):
    assert inst.code.coding[0].code == "373994007"
    assert inst.code.coding[0].display == "Prednisone 5mg tablet (Product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "sub03"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0311"
    assert inst.ingredient[0].item.reference.reference == "#sub03"
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert inst.ingredient[0].strengthRatio.denominator.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(5)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_medication_1(base_settings):
    """No. 1 tests collection for Medication.
    Test File: medicationexample0311.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationexample0311.json"
    )
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_1(inst2)


def impl_medication_2(inst):
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2019-10-31")
    assert inst.batch.lotNumber == "12345"
    assert inst.code.coding[0].code == "51144-050-01"
    assert inst.code.coding[0].display == "Adcetris"
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "mmanu"
    assert inst.doseForm.coding[0].code == "421637006"
    assert inst.doseForm.coding[0].display == (
    "Lyophilized powder for injectable solution (qualifier value)"
    " "
    )
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0306"
    assert inst.marketingAuthorizationHolder.reference == "#mmanu"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_medication_2(base_settings):
    """No. 2 tests collection for Medication.
    Test File: medicationexample0306.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationexample0306.json"
    )
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_2(inst2)


def impl_medication_3(inst):
    assert inst.code.text == "Amoxicillin 250mg/5ml Suspension"
    assert inst.id == "medicationexample1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Amoxicillin "
    "250mg/5ml Suspension</div>"
    )
    assert inst.text.status == "generated"


def test_medication_3(base_settings):
    """No. 3 tests collection for Medication.
    Test File: medicationexample1.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationexample1.json"
    )
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_3(inst2)


def impl_medication_4(inst):
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2017-05-22")
    assert inst.batch.lotNumber == "9494788"
    assert inst.code.coding[0].code == "213293"
    assert inst.code.coding[0].display == "Capecitabine 500mg oral tablet (Xeloda)"
    assert inst.code.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.contained[0].id == "mmanu"
    assert inst.contained[1].id == "sub04"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "medexample015"
    assert inst.ingredient[0].item.reference.reference == "#sub04"
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert inst.ingredient[0].strengthRatio.denominator.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(500)
    assert inst.marketingAuthorizationHolder.reference == "#mmanu"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_medication_4(base_settings):
    """No. 4 tests collection for Medication.
    Test File: medicationexample15.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationexample15.json"
    )
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_4(inst2)


def impl_medication_5(inst):
    assert inst.code.coding[0].code == "0206-8862-02"
    assert inst.code.coding[0].display == "Zosyn (piperacillin/tazobactam) 4.5gm injection"
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "mmanu"
    assert inst.doseForm.coding[0].code == "385219001"
    assert inst.doseForm.coding[0].display == "Injection solution (qualifier vallue)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0302"
    assert inst.ingredient[0].item.concept.coding[0].code == "203134"
    assert inst.ingredient[0].item.concept.coding[0].display == "Piperacillin Sodium"
    assert inst.ingredient[0].item.concept.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.ingredient[0].strengthRatio.denominator.code == "mL"
    assert inst.ingredient[0].strengthRatio.denominator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(20)
    assert inst.ingredient[0].strengthRatio.numerator.code == "g"
    assert inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(4)
    assert inst.ingredient[1].item.concept.coding[0].code == "221167"
    assert inst.ingredient[1].item.concept.coding[0].display == "Tazobactam Sodium"
    assert inst.ingredient[1].item.concept.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.ingredient[1].strengthRatio.denominator.code == "mL"
    assert inst.ingredient[1].strengthRatio.denominator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[1].strengthRatio.denominator.value) == float(20)
    assert inst.ingredient[1].strengthRatio.numerator.code == "g"
    assert inst.ingredient[1].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[1].strengthRatio.numerator.value) == float(0.5)
    assert inst.marketingAuthorizationHolder.reference == "#mmanu"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_medication_5(base_settings):
    """No. 5 tests collection for Medication.
    Test File: medicationexample0302.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationexample0302.json"
    )
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_5(inst2)


def impl_medication_6(inst):
    assert inst.code.coding[0].code == "308047"
    assert inst.code.coding[0].display == "Alprazolam 0.25mg Oral Tablet"
    assert inst.code.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0314"
    assert inst.ingredient[0].item.concept.coding[0].code == "386983007"
    assert inst.ingredient[0].item.concept.coding[0].display == "Alprazolam (substance)"
    assert inst.ingredient[0].item.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.ingredient[0].strengthRatio.denominator.code == "385055001"
    assert inst.ingredient[0].strengthRatio.denominator.system == "http://snomed.info/sct"
    assert inst.ingredient[0].strengthRatio.denominator.unit == "Tablet"
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(0.25)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_medication_6(base_settings):
    """No. 6 tests collection for Medication.
    Test File: medicationexample0314.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationexample0314.json"
    )
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_6(inst2)


def impl_medication_7(inst):
    assert inst.code.coding[0].code == "430127000"
    assert inst.code.coding[0].display == "Oral Form Oxycodone (product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "sub03"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0310"
    assert inst.ingredient[0].item.reference.reference == "#sub03"
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert inst.ingredient[0].strengthRatio.denominator.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(5)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_medication_7(base_settings):
    """No. 7 tests collection for Medication.
    Test File: medicationexample0310.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationexample0310.json"
    )
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_7(inst2)


def impl_medication_8(inst):
    assert inst.code.text == "WHO Hand Sanitizer Formulation 1% - 10L"
    assert inst.contained[0].id == "sub10"
    assert inst.contained[1].id == "sub11"
    assert inst.contained[2].id == "sub12"
    assert inst.contained[3].id == "sub13"
    assert inst.doseForm.coding[0].code == "739006009"
    assert inst.doseForm.coding[0].display == "Solution (basic dose form) (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0323"
    assert inst.ingredient[0].item.reference.reference == "#sub10"
    assert inst.ingredient[0].strengthQuantity.code == "mL"
    assert inst.ingredient[0].strengthQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strengthQuantity.value) == float(8333)
    assert inst.ingredient[1].item.reference.reference == "#sub11"
    assert inst.ingredient[1].strengthQuantity.code == "mL"
    assert inst.ingredient[1].strengthQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[1].strengthQuantity.value) == float(417)
    assert inst.ingredient[2].item.reference.reference == "#sub12"
    assert inst.ingredient[2].strengthQuantity.code == "mL"
    assert inst.ingredient[2].strengthQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[2].strengthQuantity.value) == float(145)
    assert inst.ingredient[3].item.reference.reference == "#sub13"
    assert inst.ingredient[3].strengthCodeableConcept.coding[0].code == "qs"
    assert inst.ingredient[3].strengthCodeableConcept.coding[0].display == "QS"
    assert inst.ingredient[3].strengthCodeableConcept.coding[0].system == "http://hl7.org/fhir/CodeSystem/medication-ingredientstrength"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_medication_8(base_settings):
    """No. 8 tests collection for Medication.
    Test File: medicationexample0323.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationexample0323.json"
    )
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_8(inst2)


def impl_medication_9(inst):
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2020-07-31")
    assert inst.batch.lotNumber == "658484"
    assert inst.code.coding[0].code == "63481-623-70"
    assert inst.code.coding[0].display == "Percocet tablet"
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "mmanu"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0308"
    assert inst.ingredient[0].item.concept.coding[0].code == "82063"
    assert inst.ingredient[0].item.concept.coding[0].display == "Oxycodone HCl"
    assert inst.ingredient[0].item.concept.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert inst.ingredient[0].strengthRatio.denominator.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(5)
    assert inst.ingredient[1].item.concept.coding[0].code == "161"
    assert inst.ingredient[1].item.concept.coding[0].display == "Acetaminophen"
    assert inst.ingredient[1].item.concept.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.ingredient[1].strengthRatio.denominator.code == "TAB"
    assert inst.ingredient[1].strengthRatio.denominator.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert float(inst.ingredient[1].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[1].strengthRatio.numerator.code == "mg"
    assert inst.ingredient[1].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[1].strengthRatio.numerator.value) == float(325)
    assert inst.marketingAuthorizationHolder.reference == "#mmanu"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_medication_9(base_settings):
    """No. 9 tests collection for Medication.
    Test File: medicationexample0308.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationexample0308.json"
    )
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_9(inst2)


def impl_medication_10(inst):
    assert inst.code.coding[0].code == "400621001"
    assert inst.code.coding[0].display == "Lorazepam 2mg/ml injection solution 1ml vial (product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.doseForm.coding[0].code == "385219001"
    assert inst.doseForm.coding[0].display == "Injection solution (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0313"
    assert inst.ingredient[0].item.concept.coding[0].code == "387106007"
    assert inst.ingredient[0].item.concept.coding[0].display == "Lorazepam (substance)"
    assert inst.ingredient[0].item.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.ingredient[0].strengthRatio.denominator.code == "mL"
    assert inst.ingredient[0].strengthRatio.denominator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(2)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"
    assert inst.totalVolume.denominator.code == "vial"
    assert inst.totalVolume.denominator.system == (
    "http://terminology.hl7.org/CodeSystem/medicationknowledge-"
    "package-type"
    )
    assert float(inst.totalVolume.denominator.value) == float(1)
    assert inst.totalVolume.numerator.code == "ml"
    assert inst.totalVolume.numerator.system == "http://unitsofmeasure.org"
    assert inst.totalVolume.numerator.unit == "ml"
    assert float(inst.totalVolume.numerator.value) == float(1)


def test_medication_10(base_settings):
    """No. 10 tests collection for Medication.
    Test File: medicationexample0313.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationexample0313.json"
    )
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_10(inst2)