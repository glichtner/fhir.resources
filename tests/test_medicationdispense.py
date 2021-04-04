# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import medicationdispense


def impl_medicationdispense_1(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0318"
    assert inst.contained[0].id == "med0301"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(3)
    assert inst.destination.reference == "Location/ph"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        500
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].method.coding[0].code == "420620005"
    assert (
        inst.dosageInstruction[0].method.coding[0].display
        == "Push - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosageInstruction[0].method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].route.coding[0].code == "255560000"
    assert inst.dosageInstruction[0].route.coding[0].display == "Intravenous"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "500mg IV q6h x 3 days"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(6)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "meddisp0301"
    assert inst.location.display == "Pharmacy"
    assert inst.location.reference == "Location/ukp"
    assert inst.medication.reference.display == "Vancomycin Hydrochloride"
    assert inst.medication.reference.reference == "#med0301"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "733026001"
    assert inst.quantity.system == "http://snomed.info.sct"
    assert inst.quantity.unit == "Vial"
    assert float(inst.quantity.value) == float(12)
    assert inst.receiver[0].display == "Donald Duck"
    assert inst.receiver[0].reference == "Patient/pat1"
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.supportingInformation[0].reference == "Condition/f203"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "EM"
    assert inst.type.coding[0].display == "Emergency Supply"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_1(base_settings):
    """No. 1 tests collection for MedicationDispense.
    Test File: medicationdispense0301.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0301.json"
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
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0315"
    assert inst.contained[0].id == "med0313"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(1)
    assert inst.dosageInstruction[0].asNeededBoolean is True
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        7
    )
    assert inst.dosageInstruction[0].doseAndRate[0].rateRange.high.code == "min"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].rateRange.high.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].rateRange.high.unit == "min"
    assert float(
        inst.dosageInstruction[0].doseAndRate[0].rateRange.high.value
    ) == float(5)
    assert inst.dosageInstruction[0].doseAndRate[0].rateRange.low.code == "min"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].rateRange.low.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].rateRange.low.unit == "min"
    assert float(inst.dosageInstruction[0].doseAndRate[0].rateRange.low.value) == float(
        2
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].method.coding[0].code == "420620005"
    assert (
        inst.dosageInstruction[0].method.coding[0].display
        == "Push - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosageInstruction[0].method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].route.coding[0].code == "255560000"
    assert inst.dosageInstruction[0].route.coding[0].display == "Intravenous"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert (
        inst.dosageInstruction[0].text
        == "7mg IV over 2-5 minutes every 15 minutes as needed"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(15)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "min"
    assert inst.id == "meddisp0314"
    assert inst.medication.reference.reference == "#med0313"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "415818005"
    assert inst.quantity.system == "http://snomed.info/sct"
    assert float(inst.quantity.value) == float(1)
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck "
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "TF"
    assert inst.type.coding[0].display == "Trial Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenHandedOver == fhirtypes.DateTime.validate(
        "2015-06-26T07:13:00+05:00"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-06-25T07:13:00+05:00")


def test_medicationdispense_2(base_settings):
    """No. 2 tests collection for MedicationDispense.
    Test File: medicationdispense0314.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0314.json"
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
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0307"
    assert inst.contained[0].id == "med0308"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(30)
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "418914006"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].display == (
        "Warning. May cause drowsiness. If affected do not drive or "
        "operate machinery. Avoid alcoholic drink (qualifier value)"
    )
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].code == "203082005"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].display
        == "Fibromyalgia (disorder)"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert (
        inst.dosageInstruction[0].text == "1 tablet every four hours as needed for pain"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(4)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "meddisp0310"
    assert inst.medication.reference.display == "Percocet"
    assert inst.medication.reference.reference == "#med0308"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "TAB"
    assert (
        inst.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.quantity.unit == "TAB"
    assert float(inst.quantity.value) == float(30)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck "
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "EM"
    assert inst.type.coding[0].display == "Emergency Supply"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_3(base_settings):
    """No. 3 tests collection for MedicationDispense.
    Test File: medicationdispense0310.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0310.json"
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
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0321"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(10)
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "418914006"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].display == (
        "Warning. May cause drowsiness. If affected do not drive or "
        "operate machinery. Avoid alcoholic drink (qualifier value)"
    )
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].code == "203082005"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].display
        == "Fibromyalgia (disorder)"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert (
        inst.dosageInstruction[0].text == "1 tablet every four hours as needed for pain"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(4)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "meddisp0321"
    assert inst.medication.concept.coding[0].code == "0074-3043-13"
    assert (
        inst.medication.concept.coding[0].display
        == "Vicodin 5mg Hydrocodone, 500mg Acetaminophen tablet "
    )
    assert inst.medication.concept.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "TAB"
    assert (
        inst.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.quantity.value) == float(30)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_4(base_settings):
    """No. 4 tests collection for MedicationDispense.
    Test File: medicationdispense0321.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0321.json"
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
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0305"
    assert inst.contained[0].id == "med0314"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(10)
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "418914006"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].display == (
        "Warning. May cause drowsiness. If affected do not drive or "
        "operate machinery. Avoid alcoholic drink (qualifier value)"
    )
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].code == "266599000"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].display
        == "Dysmenorrhea (disorder)"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == (
        "0.25mg PO every 6-12 hours as needed for menses from Jan "
        "15-20, 2015.  Do not exceed more than 4mg per day"
    )
    assert inst.dosageInstruction[
        0
    ].timing.repeat.boundsPeriod.end == fhirtypes.DateTime.validate("2015-01-20")
    assert inst.dosageInstruction[
        0
    ].timing.repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(6)
    assert float(inst.dosageInstruction[0].timing.repeat.periodMax) == float(12)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "meddisp0315"
    assert inst.medication.reference.display == "Alprazolam 0.25mg (Xanax)"
    assert inst.medication.reference.reference == "#med0314"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "TAB"
    assert (
        inst.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.quantity.value) == float(30)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck "
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenHandedOver == fhirtypes.DateTime.validate(
        "2015-06-26T07:13:00+05:00"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-06-25T07:13:00+05:00")


def test_medicationdispense_5(base_settings):
    """No. 5 tests collection for MedicationDispense.
    Test File: medicationdispense0315.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0315.json"
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
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0322"
    assert inst.contained[0].id == "med0317"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "meq"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mEq"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        20
    )
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.code == "h"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.value
    ) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.code == "mL"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.system
        == "http://unitsofmeasure.org"
    )
    assert float(
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.value
    ) == float(100)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "47625008"
    assert (
        inst.dosageInstruction[0].route.coding[0].display
        == "Intravenous route (qualifier value)"
    )
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "KCl 20 mEq in 1 L 0.9%NS IV at 100 ml/hr"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0313"
    assert (
        inst.medication.reference.display
        == "Potassium Chloride 20mEq in 1L Normal Saline"
    )
    assert inst.medication.reference.reference == "#med0317"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenHandedOver == fhirtypes.DateTime.validate(
        "2016-04-28T07:13:00+05:00"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2016-04-28T07:13:00+05:00")


def test_medicationdispense_6(base_settings):
    """No. 6 tests collection for MedicationDispense.
    Test File: medicationdispense0313.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0313.json"
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
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0321"
    assert inst.contained[0].id == "med0360"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(30)
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].text
        == "Check sugar level before taking Novolog"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "U"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "U"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        10
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Before Breakfast"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert (
        inst.dosageInstruction[1].additionalInstruction[0].text
        == "Check sugar level before taking Novolog"
    )
    assert inst.dosageInstruction[1].doseAndRate[0].doseQuantity.code == "U"
    assert (
        inst.dosageInstruction[1].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[1].doseAndRate[0].doseQuantity.unit == "U"
    assert float(inst.dosageInstruction[1].doseAndRate[0].doseQuantity.value) == float(
        15
    )
    assert inst.dosageInstruction[1].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[1].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[1].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[1].sequence == 1
    assert inst.dosageInstruction[1].text == "15 units before lunch"
    assert inst.dosageInstruction[1].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[1].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[1].timing.repeat.periodUnit == "d"
    assert (
        inst.dosageInstruction[2].additionalInstruction[0].text
        == "Check sugar level before taking Novolog"
    )
    assert inst.dosageInstruction[2].doseAndRate[0].doseQuantity.code == "U"
    assert (
        inst.dosageInstruction[2].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[2].doseAndRate[0].doseQuantity.unit == "U"
    assert float(inst.dosageInstruction[2].doseAndRate[0].doseQuantity.value) == float(
        20
    )
    assert inst.dosageInstruction[2].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[2].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[2].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[2].sequence == 1
    assert inst.dosageInstruction[2].text == "20 units before dinner"
    assert inst.dosageInstruction[2].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[2].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[2].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0302"
    assert inst.medication.reference.display == "Novolog 100u/ml"
    assert inst.medication.reference.reference == "#med0360"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.performer[0].function.coding[0].code == "finalchecker"
    assert inst.performer[0].function.coding[0].display == "Final Checker"
    assert inst.performer[0].function.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/medicationdispense-" "performer-function"
    )
    assert inst.quantity.code == "ml"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert float(inst.quantity.value) == float(10)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2015-01-15T16:20:00Z")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_7(base_settings):
    """No. 7 tests collection for MedicationDispense.
    Test File: medicationdispense0302.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0302.json"
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
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0312"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(30)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "ml"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "ml"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        4
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert (
        inst.dosageInstruction[0].route.coding[0].display
        == "Oral Route (qualifier value)"
    )
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "100mg (4ml) three times daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 3
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0322"
    assert inst.medication.concept.coding[0].code == "0071-2214-20"
    assert (
        inst.medication.concept.coding[0].display
        == "Dilantin 125mg/5ml Oral Suspension"
    )
    assert inst.medication.concept.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "ml"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert float(inst.quantity.value) == float(360)
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenHandedOver == fhirtypes.DateTime.validate(
        "2015-01-18T07:13:00+05:00"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-16T07:13:00+05:00")


def test_medicationdispense_8(base_settings):
    """No. 8 tests collection for MedicationDispense.
    Test File: medicationdispense0322.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0322.json"
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
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0329"
    assert inst.contained[0].id == "med0319"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(10)
    assert inst.dosageInstruction[0].additionalInstruction[0].text == "Apply sparingly"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "OINT"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "ea"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "359540000"
    assert (
        inst.dosageInstruction[0].route.coding[0].display == "Topical (qualifier value)"
    )
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].site.coding[0].code == "72098002"
    assert (
        inst.dosageInstruction[0].site.coding[0].display
        == "Entire left upper arm (body structure)"
    )
    assert inst.dosageInstruction[0].site.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.dosageInstruction[0].text
        == "Apply twice daily to affected area on left arm"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0329"
    assert inst.medication.reference.reference == "#med0319"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2015-01-15T16:20:00Z")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_9(base_settings):
    """No. 9 tests collection for MedicationDispense.
    Test File: medicationdispense0329.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0329.json"
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
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0321"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(30)
    assert inst.dosageInstruction[0].additionalInstruction[0].text == "Shake Well"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "NASINHL"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "ea"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Use two sprays twice daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0328"
    assert inst.medication.concept.coding[0].code == "1797870"
    assert (
        inst.medication.concept.coding[0].display
        == "Nasonex 0.05mg/ACTUAT Nasal Inhaler"
    )
    assert (
        inst.medication.concept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "ml"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert float(inst.quantity.value) == float(30)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "EM"
    assert inst.type.coding[0].display == "Emergency Supply"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_10(base_settings):
    """No. 10 tests collection for MedicationDispense.
    Test File: medicationdispense0328.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0328.json"
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
