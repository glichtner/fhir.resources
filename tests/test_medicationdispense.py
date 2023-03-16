# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import medicationdispense


def impl_medicationdispense_1(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0331"
    assert inst.contained[0].id == "med0352"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(1)
    assert inst.dosageInstruction[0].additionalInstruction[0].text == (
    "Take along with one 2mg Coumadin tablet for a total daily "
    "dose of 7mg as prescribed by physician"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(2)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "7mg (=one 5mg tablet PLUS one 2mg tablet) once daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0331"
    assert inst.medication.reference.display == "Coumadin 2mg tablet"
    assert inst.medication.reference.reference == "#med0352"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "415818006"
    assert inst.quantity.system == "http://snomed.info/sct"
    assert float(inst.quantity.value) == float(1)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "DF"
    assert inst.type.coding[0].display == "Daily Fill"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_1(base_settings):
    """No. 1 tests collection for MedicationDispense.
    Test File: medicationdispense0331.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationdispense0331.json"
    )
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_1(inst2)


def impl_medicationdispense_2(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0319"
    assert inst.contained[0].id == "med0312"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(10)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "DROP"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "drop"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(10)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == (
    "10 drops four times daily - apply in mouth using cotton swab"
    " or finger"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 4
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0309"
    assert inst.medication.reference.display == "Nystatin 100,000 units/ml oral suspension (product)"
    assert inst.medication.reference.reference == "#med0312"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "ml"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert inst.quantity.unit == "ml"
    assert float(inst.quantity.value) == float(10)
    assert inst.status == "entered-in-error"
    assert inst.subject.display == "Donald Duck "
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "FF"
    assert inst.type.coding[0].display == "First Fill"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2016-01-15")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15")


def test_medicationdispense_2(base_settings):
    """No. 2 tests collection for MedicationDispense.
    Test File: medicationdispense0309.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationdispense0309.json"
    )
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_2(inst2)


def impl_medicationdispense_3(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0321"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(10)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "OINT"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "ea"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Apply to affected areas four times daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 4
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0324"
    assert inst.medication.concept.coding[0].code == "884375"
    assert inst.medication.concept.coding[0].display == "Nystex 100,000 UNT/GM Topical Ointment"
    assert inst.medication.concept.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "g"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert float(inst.quantity.value) == float(30)
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2015-01-15T16:20:00Z")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_3(base_settings):
    """No. 3 tests collection for MedicationDispense.
    Test File: medicationdispense0324.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationdispense0324.json"
    )
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_3(inst2)


def impl_medicationdispense_4(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0306"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(30)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(6)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "calculated"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Calculated"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Take 3 tablets (6mg) once daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0307"
    assert inst.medication.concept.coding[0].code == "76388-713-25"
    assert inst.medication.concept.coding[0].display == "Myleran 2mg tablet, film coated"
    assert inst.medication.concept.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "TAB"
    assert inst.quantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert float(inst.quantity.value) == float(90)
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2015-01-15T16:20:00Z")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_4(base_settings):
    """No. 4 tests collection for MedicationDispense.
    Test File: medicationdispense0307.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationdispense0307.json"
    )
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_4(inst2)


def impl_medicationdispense_5(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0324"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(10)
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "418637003"
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].display == (
    "Do not take with any other paracetamol products (qualifier "
    "value)"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].asNeededFor[0].coding[0].code == "386661006"
    assert inst.dosageInstruction[0].asNeededFor[0].coding[0].display == "Fever (finding)"
    assert inst.dosageInstruction[0].asNeededFor[0].coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(240)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].maxDosePerPeriod[0].denominator.code == "d"
    assert inst.dosageInstruction[0].maxDosePerPeriod[0].denominator.system == "http://unitsofmeasure.org"
    assert float(inst.dosageInstruction[0].maxDosePerPeriod[0].denominator.value) == float(1)
    assert inst.dosageInstruction[0].maxDosePerPeriod[0].numerator.code == "mg"
    assert inst.dosageInstruction[0].maxDosePerPeriod[0].numerator.system == "http://unitsofmeasure.org"
    assert float(inst.dosageInstruction[0].maxDosePerPeriod[0].numerator.value) == float(720)
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == (
    "Insert two suppositories (240mg) rectally twice daily as "
    "needed for fever to a maximim of 6 per day"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0311"
    assert inst.medication.concept.coding[0].code == "0713-0118"
    assert inst.medication.concept.coding[0].display == "Acetaminophen 120mg Suppository"
    assert inst.medication.concept.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "RECSUPP"
    assert inst.quantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert float(inst.quantity.value) == float(60)
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2015-01-15T16:20:00Z")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_5(base_settings):
    """No. 5 tests collection for MedicationDispense.
    Test File: medicationdispense0311.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationdispense0311.json"
    )
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_5(inst2)


def impl_medicationdispense_6(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0307"
    assert inst.contained[0].id == "med0308"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(30)
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "418914006"
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].display == (
    "Warning. May cause drowsiness. If affected do not drive or "
    "operate machinery. Avoid alcoholic drink (qualifier value)"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].asNeededFor[0].coding[0].code == "203082005"
    assert inst.dosageInstruction[0].asNeededFor[0].coding[0].display == "Fibromyalgia (disorder)"
    assert inst.dosageInstruction[0].asNeededFor[0].coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "TAB"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "1 tablet every four hours as needed for pain"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(4)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "meddisp0310"
    assert inst.medication.reference.display == "Percocet"
    assert inst.medication.reference.reference == "#med0308"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "TAB"
    assert inst.quantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.quantity.unit == "TAB"
    assert float(inst.quantity.value) == float(30)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck "
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "EM"
    assert inst.type.coding[0].display == "Emergency Supply"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_6(base_settings):
    """No. 6 tests collection for MedicationDispense.
    Test File: medicationdispense0310.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationdispense0310.json"
    )
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_6(inst2)


def impl_medicationdispense_7(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0320"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(30)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "U"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "U"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(20)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].route.coding[0].code == "263887005"
    assert inst.dosageInstruction[0].route.coding[0].display == "Subcutaneous (qualifier value)"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "20 Units SC three times daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 3
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0316"
    assert inst.medication.concept.coding[0].code == "285018"
    assert inst.medication.concept.coding[0].display == "Lantus 100 unit/ml injectable solution"
    assert inst.medication.concept.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "ml"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert float(inst.quantity.value) == float(10)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck "
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-06-25T07:13:00+05:00")


def test_medicationdispense_7(base_settings):
    """No. 7 tests collection for MedicationDispense.
    Test File: medicationdispense0316.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationdispense0316.json"
    )
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_7(inst2)


def impl_medicationdispense_8(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0309"
    assert inst.contained[0].id == "medexample015"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(500)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].route.coding[0].code == "394899003"
    assert inst.dosageInstruction[0].route.coding[0].display == "oral administration of treatment"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(21)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp008"
    assert inst.medication.reference.reference == "#medexample015"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationdispense_8(base_settings):
    """No. 8 tests collection for MedicationDispense.
    Test File: medicationdispenseexample8.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationdispenseexample8.json"
    )
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_8(inst2)


def impl_medicationdispense_9(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0319"
    assert inst.contained[0].id == "med0302"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "g"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(4.5)
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.code == "min"
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.system == "http://unitsofmeasure.org"
    assert float(inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.code == "ml"
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.value) == float(8)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "calculated"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Calculated"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].route.coding[0].code == "47625008"
    assert inst.dosageInstruction[0].route.coding[0].display == "IV intravascular route that begins within a vein)"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].site.coding[0].code == "255560000"
    assert inst.dosageInstruction[0].site.coding[0].display == "Intravenous route (qualifier value)"
    assert inst.dosageInstruction[0].site.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].text == (
    "4.5 grams in D5W 250 ml. IV every 6 hours. Infuse over 30 "
    "min at 8L/min"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(6)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "meddisp0304"
    assert inst.medication.reference.display == "Zosyn (piperacillin/tazobactam) 4.5gm injection"
    assert inst.medication.reference.reference == "#med0302"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "mL"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert float(inst.quantity.value) == float(250)
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "FF"
    assert inst.type.coding[0].display == "First Fill"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2015-06-26T07:13:00+05:00")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-06-25T07:13:00+05:00")


def test_medicationdispense_9(base_settings):
    """No. 9 tests collection for MedicationDispense.
    Test File: medicationdispense0304.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationdispense0304.json"
    )
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_9(inst2)


def impl_medicationdispense_10(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0322"
    assert inst.contained[0].id == "med0317"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "meq"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mEq"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(20)
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.code == "h"
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.system == "http://unitsofmeasure.org"
    assert float(inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.code == "mL"
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.value) == float(100)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].route.coding[0].code == "47625008"
    assert inst.dosageInstruction[0].route.coding[0].display == "Intravenous route (qualifier value)"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "KCl 20 mEq in 1 L 0.9%NS IV at 100 ml/hr"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0313"
    assert inst.medication.reference.display == "Potassium Chloride 20mEq in 1L Normal Saline"
    assert inst.medication.reference.reference == "#med0317"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "ml"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert float(inst.quantity.value) == float(1000)
    assert inst.status == "stopped"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "FF"
    assert inst.type.coding[0].display == "First Fill"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2016-04-28T07:13:00+05:00")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2016-04-28T07:13:00+05:00")


def test_medicationdispense_10(base_settings):
    """No. 10 tests collection for MedicationDispense.
    Test File: medicationdispense0313.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationdispense0313.json"
    )
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_10(inst2)