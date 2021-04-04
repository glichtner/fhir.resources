# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import medication


def impl_medication_1(inst):
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2016-07-09")
    assert inst.batch.lotNumber == "123455"
    assert inst.doseForm.coding[0].code == "385221006"
    assert inst.doseForm.coding[0].display == "Injection emulsion"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0318"
    assert inst.ingredient[0].item.concept.coding[0].code == "0338-1134-03"
    assert inst.ingredient[0].item.concept.coding[0].display == (
        "Clinimix 4.25/10 sulfite-free (4.25% Amino Acid in 10% "
        "Dextrose) Injection, 1000ml"
    )
    assert (
        inst.ingredient[0].item.concept.coding[0].system
        == "http://hl7.org/fhir/sid/ndc"
    )
    assert inst.ingredient[1].item.concept.coding[0].code == "0409-5779-01"
    assert (
        inst.ingredient[1].item.concept.coding[0].system
        == "http://hl7.org/fhir/sid/ndc"
    )
    assert inst.ingredient[2].item.concept.coding[0].code == "0338-0519-02"
    assert (
        inst.ingredient[2].item.concept.coding[0].display
        == "Intralipid 20% IV Fat Emulsion"
    )
    assert (
        inst.ingredient[2].item.concept.coding[0].system
        == "http://hl7.org/fhir/sid/ndc"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_1(base_settings):
    """No. 1 tests collection for Medication.
    Test File: medicationexample0318.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0318.json"
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
    assert inst.doseForm.coding[0].code == "385101003"
    assert inst.doseForm.coding[0].display == "Ointment"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.doseForm.text == "Ointment"
    assert inst.id == "med0319"
    assert inst.ingredient[0].item.concept.coding[0].code == "387253001"
    assert (
        inst.ingredient[0].item.concept.coding[0].display
        == "Salicyclic Acid (substance)"
    )
    assert inst.ingredient[0].item.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.ingredient[0].strengthRatio.denominator.code == "g"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(100)
    assert inst.ingredient[0].strengthRatio.numerator.code == "g"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(5)
    assert inst.ingredient[1].item.concept.coding[0].code == "396458002"
    assert (
        inst.ingredient[1].item.concept.coding[0].display
        == "Hydrocortisone (substance)"
    )
    assert inst.ingredient[1].item.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.ingredient[1].strengthRatio.denominator.code == "g"
    assert (
        inst.ingredient[1].strengthRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[1].strengthRatio.denominator.value) == float(100)
    assert inst.ingredient[1].strengthRatio.numerator.code == "g"
    assert (
        inst.ingredient[1].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[1].strengthRatio.numerator.value) == float(1)
    assert inst.ingredient[2].item.concept.coding[0].code == "126066007"
    assert (
        inst.ingredient[2].item.concept.coding[0].display
        == "White Petrolatum (substance)"
    )
    assert inst.ingredient[2].item.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.ingredient[2].strengthRatio.denominator.code == "g"
    assert (
        inst.ingredient[2].strengthRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[2].strengthRatio.denominator.value) == float(100)
    assert inst.ingredient[2].strengthRatio.numerator.code == "g"
    assert (
        inst.ingredient[2].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[2].strengthRatio.numerator.value) == float(94)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_2(base_settings):
    """No. 2 tests collection for Medication.
    Test File: medicationexample0319.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0319.json"
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
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2017-05-22")
    assert inst.batch.lotNumber == "9494788"
    assert inst.code.coding[0].code == "0409-6531-02"
    assert (
        inst.code.coding[0].display
        == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    )
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "org4"
    assert inst.doseForm.coding[0].code == "385219001"
    assert inst.doseForm.coding[0].display == "Injection Solution (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0301"
    assert inst.ingredient[0].isActive is True
    assert inst.ingredient[0].item.concept.coding[0].code == "66955"
    assert (
        inst.ingredient[0].item.concept.coding[0].display == "Vancomycin Hydrochloride"
    )
    assert (
        inst.ingredient[0].item.concept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.ingredient[0].strengthRatio.denominator.code == "mL"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(10)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(500)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.sponsor.reference == "#org4"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_medication_3(base_settings):
    """No. 3 tests collection for Medication.
    Test File: medicationexample0301.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0301.json"
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
    assert inst.code.coding[0].code == "50580-608-02"
    assert inst.code.coding[0].display == "Tylenol PM"
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "org2"
    assert inst.doseForm.coding[0].code == "385057009"
    assert inst.doseForm.coding[0].display == "Film-coated tablet (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0309"
    assert inst.ingredient[0].item.concept.coding[0].code == "315266"
    assert inst.ingredient[0].item.concept.coding[0].display == "Acetaminophen 500 MG"
    assert (
        inst.ingredient[0].item.concept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(500)
    assert inst.ingredient[1].item.concept.coding[0].code == "901813"
    assert (
        inst.ingredient[1].item.concept.coding[0].display
        == "Diphenhydramine Hydrochloride 25 mg"
    )
    assert (
        inst.ingredient[1].item.concept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.ingredient[1].strengthRatio.denominator.code == "TAB"
    assert (
        inst.ingredient[1].strengthRatio.denominator.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.ingredient[1].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[1].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[1].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[1].strengthRatio.numerator.value) == float(25)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.sponsor.reference == "#org2"
    assert inst.text.status == "generated"


def test_medication_4(base_settings):
    """No. 4 tests collection for Medication.
    Test File: medicationexample0309.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0309.json"
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
    assert inst.code.coding[0].code == "108761006"
    assert inst.code.coding[0].display == "Capecitabine (product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "sub03"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0321"
    assert inst.ingredient[0].item.reference.reference == "#sub03"
    assert inst.ingredient[0].strengthRatio.denominator.code == "385055001"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system == "http://snomed.info/sct"
    )
    assert inst.ingredient[0].strengthRatio.denominator.unit == "Tablet"
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(500)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_5(base_settings):
    """No. 5 tests collection for Medication.
    Test File: medicationexample0321.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0321.json"
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
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2020-07-31")
    assert inst.batch.lotNumber == "658484"
    assert inst.code.coding[0].code == "63481-623-70"
    assert inst.code.coding[0].display == "Percocet tablet"
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "org1"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0308"
    assert inst.ingredient[0].item.concept.coding[0].code == "82063"
    assert inst.ingredient[0].item.concept.coding[0].display == "Oxycodone HCl"
    assert (
        inst.ingredient[0].item.concept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(5)
    assert inst.ingredient[1].item.concept.coding[0].code == "161"
    assert inst.ingredient[1].item.concept.coding[0].display == "Acetaminophen"
    assert (
        inst.ingredient[1].item.concept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.ingredient[1].strengthRatio.denominator.code == "TAB"
    assert (
        inst.ingredient[1].strengthRatio.denominator.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.ingredient[1].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[1].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[1].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[1].strengthRatio.numerator.value) == float(325)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.sponsor.reference == "#org1"
    assert inst.text.status == "generated"


def test_medication_6(base_settings):
    """No. 6 tests collection for Medication.
    Test File: medicationexample0308.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0308.json"
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
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2017-05-22")
    assert inst.batch.lotNumber == "9494788"
    assert inst.code.coding[0].code == "1594660"
    assert inst.code.coding[0].display == "Alemtuzumab 10mg/ml (Lemtrada)"
    assert inst.code.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.contained[0].id == "org6"
    assert inst.doseForm.coding[0].code == "385219001"
    assert inst.doseForm.coding[0].display == "Injection solution (qualifier vallue)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0303"
    assert inst.ingredient[0].item.concept.coding[0].code == "129472003"
    assert (
        inst.ingredient[0].item.concept.coding[0].display == "Alemtuzamab (substance)"
    )
    assert inst.ingredient[0].item.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.ingredient[0].strengthRatio.denominator.code == "mL"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1.2)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(12)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.sponsor.reference == "#org6"
    assert inst.text.status == "generated"


def test_medication_7(base_settings):
    """No. 7 tests collection for Medication.
    Test File: medicationexample0303.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0303.json"
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
    assert inst.code.coding[0].code == "324252006"
    assert inst.code.coding[0].display == "Azithromycin 250mg capsule (product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "sub03"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0320"
    assert inst.ingredient[0].item.reference.reference == "#sub03"
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(250)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_8(base_settings):
    """No. 8 tests collection for Medication.
    Test File: medicationexample0320.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0320.json"
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
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(5)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_9(base_settings):
    """No. 9 tests collection for Medication.
    Test File: medicationexample0310.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0310.json"
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
    assert inst.doseForm.coding[0].code == "385219001"
    assert inst.doseForm.coding[0].display == "Injection Solution (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.doseForm.text == "Injection Solution (qualifier value)"
    assert inst.id == "med0317"
    assert inst.ingredient[0].item.concept.coding[0].code == "204520"
    assert inst.ingredient[0].item.concept.coding[0].display == "Potassium Chloride"
    assert (
        inst.ingredient[0].item.concept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.ingredient[0].strengthRatio.denominator.code == "mL"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "meq"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(2)
    assert inst.ingredient[1].item.concept.coding[0].code == "313002"
    assert (
        inst.ingredient[1].item.concept.coding[0].display
        == "Sodium Chloride 0.9% injectable solution"
    )
    assert (
        inst.ingredient[1].item.concept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.ingredient[1].strengthRatio.denominator.code == "mL"
    assert (
        inst.ingredient[1].strengthRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[1].strengthRatio.denominator.value) == float(100)
    assert inst.ingredient[1].strengthRatio.numerator.code == "g"
    assert (
        inst.ingredient[1].strengthRatio.numerator.system == "http://unitsofmeasure.org"
    )
    assert float(inst.ingredient[1].strengthRatio.numerator.value) == float(0.9)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_10(base_settings):
    """No. 10 tests collection for Medication.
    Test File: medicationexample0317.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0317.json"
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
