# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import medicationrequest


def impl_medicationrequest_1(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.category[0].coding[0].code == "inpatient"
    assert inst.category[0].coding[0].display == "Inpatient"
    assert inst.category[0].coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/medicationrequest-"
    "admin-location"
    )
    assert inst.contained[0].id == "med0310"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert inst.dispenseRequest.expectedSupplyDuration.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(10)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 1
    assert inst.dispenseRequest.quantity.code == "TAB"
    assert inst.dispenseRequest.quantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dispenseRequest.quantity.unit == "TAB"
    assert float(inst.dispenseRequest.quantity.value) == float(30)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate("2016-01-15")
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "418914006"
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].display == (
    "Warning. May cause drowsiness. If affected do not drive or "
    "operate machinery. Avoid alcoholic drink (qualifier value)"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.high.code == "TAB"
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.high.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.high.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseRange.high.value) == float(2)
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.low.code == "TAB"
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.low.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.low.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseRange.low.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].method.coding[0].code == "421521009"
    assert inst.dosageInstruction[0].method.coding[0].display == "Swallow - dosing instruction imperative (qualifier value)"
    assert inst.dosageInstruction[0].method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "one tablet one time daily in the morning for rib pain"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.dosageInstruction[0].timing.repeat.when[0] == "MORN"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx0333"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0310"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.note[0].text == "Patient told to take with food"
    assert inst.reason[0].concept.coding[0].code == "297217002"
    assert inst.reason[0].concept.coding[0].display == "Rib Pain (finding)"
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is True
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert inst.substitution.reason.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.supportingInformation[0].reference == "Procedure/biopsy"
    assert inst.text.status == "generated"


def test_medicationrequest_1(base_settings):
    """No. 1 tests collection for MedicationRequest.
    Test File: medicationrequest0333.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationrequest0333.json"
    )
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_1(inst2)


def impl_medicationrequest_2(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0318"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mL"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mL"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(1000)
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.code == "h"
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.unit == "h"
    assert float(inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.code == "mL"
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.unit == "mL"
    assert float(inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.value) == float(50)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].method.text == "PICC line"
    assert inst.dosageInstruction[0].route.coding[0].code == "255560000"
    assert inst.dosageInstruction[0].route.coding[0].display == "Intravenous"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].site.coding[0].code == "6073002"
    assert inst.dosageInstruction[0].site.coding[0].display == "Structure of ligament of left superior vena cava"
    assert inst.dosageInstruction[0].site.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].text == "1000mL infused at 50ml/hour for 4 hours - hung at 2200 hours"
    assert inst.dosageInstruction[0].timing.event[0] == fhirtypes.DateTime.validate("2015-01-15T22:00:00+11:00")
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(24)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx0323"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0318"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_2(base_settings):
    """No. 2 tests collection for MedicationRequest.
    Test File: medicationrequest0323.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationrequest0323.json"
    )
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_2(inst2)


def impl_medicationrequest_3(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0317"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "meq"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "meq"
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
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "medrx0322"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.display == "Potassium Chloride 20mEq in 1L Normal Saline"
    assert inst.medication.reference.reference == "#med0317"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.reason[0].concept.coding[0].code == "237840007"
    assert inst.reason[0].concept.coding[0].display == "Disorder of Electrolytes (disorder)"
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_3(base_settings):
    """No. 3 tests collection for MedicationRequest.
    Test File: medicationrequest0322.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationrequest0322.json"
    )
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_3(inst2)


def impl_medicationrequest_4(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0350"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert inst.dispenseRequest.expectedSupplyDuration.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(30)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 3
    assert inst.dispenseRequest.quantity.code == "TAB"
    assert inst.dispenseRequest.quantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dispenseRequest.quantity.unit == "TAB"
    assert float(inst.dispenseRequest.quantity.value) == float(30)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate("2016-01-15")
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(7)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "7mg once daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "medrx0331"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0350"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is True
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert inst.substitution.reason.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_medicationrequest_4(base_settings):
    """No. 4 tests collection for MedicationRequest.
    Test File: medicationrequest0331.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationrequest0331.json"
    )
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_4(inst2)


def impl_medicationrequest_5(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert inst.dispenseRequest.expectedSupplyDuration.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(5)
    assert inst.dispenseRequest.quantity.code == "TAB"
    assert inst.dispenseRequest.quantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dispenseRequest.quantity.unit == "Tab"
    assert float(inst.dispenseRequest.quantity.value) == float(5)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate("2016-01-15")
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "421984009"
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].display == (
    "Until finished - dosing instruction fragment (qualifier "
    "value)"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(500)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route (qualifier value)"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "500mg daily for 5 days"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "medrx0313"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.concept.coding[0].code == "324252006"
    assert inst.medication.concept.coding[0].display == "Azithromycin 250mg capsule (product)"
    assert inst.medication.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.priorPrescription.display == "Vancomycin IV"
    assert inst.priorPrescription.reference == "MedicationRequest/medrx0318"
    assert inst.reason[0].concept.coding[0].code == "11840006"
    assert inst.reason[0].concept.coding[0].display == "Traveller's Diarrhea (disorder)"
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_5(base_settings):
    """No. 5 tests collection for MedicationRequest.
    Test File: medicationrequest0313.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationrequest0313.json"
    )
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_5(inst2)


def impl_medicationrequest_6(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert inst.dispenseRequest.expectedSupplyDuration.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(30)
    assert inst.dispenseRequest.quantity.code == "TAB"
    assert inst.dispenseRequest.quantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dispenseRequest.quantity.unit == "Tab"
    assert float(inst.dispenseRequest.quantity.value) == float(100)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate("2016-01-15")
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "ug"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mcg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(75)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route (qualifier value)"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "75mcg daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "medrx0314"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.concept.coding[0].code == "376988009"
    assert inst.medication.concept.coding[0].display == "Levothyroxine Sodium 75micrograms tablet (product)"
    assert inst.medication.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.priority == "routine"
    assert inst.reason[0].concept.coding[0].code == "40930008"
    assert inst.reason[0].concept.coding[0].display == "Hypothyroidism (disorder)"
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_6(base_settings):
    """No. 6 tests collection for MedicationRequest.
    Test File: medicationrequest0314.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationrequest0314.json"
    )
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_6(inst2)


def impl_medicationrequest_7(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0302"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "g"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "g"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(4.5)
    assert inst.dosageInstruction[0].doseAndRate[0].rateQuantity.code == "ml/h"
    assert inst.dosageInstruction[0].doseAndRate[0].rateQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.dosageInstruction[0].doseAndRate[0].rateQuantity.value) == float(50)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].route.coding[0].code == "47625008"
    assert inst.dosageInstruction[0].route.coding[0].display == "Intravenous route (qualifier value)"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == (
    "4.5 grams in D5W 250 ml. IV every 6 hours.Infuse over 30 min"
    " at 8L/min "
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(6)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "medrx0319"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.display == "Piperacillin/Tazobactam 4.5gm"
    assert inst.medication.reference.reference == "#med0302"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.reason[0].concept.coding[0].code == "385093006"
    assert inst.reason[0].concept.coding[0].display == "Community acquired pneumonia (disorder)"
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_7(base_settings):
    """No. 7 tests collection for MedicationRequest.
    Test File: medicationrequest0319.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationrequest0319.json"
    )
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_7(inst2)


def impl_medicationrequest_8(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0319"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert inst.dispenseRequest.expectedSupplyDuration.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(10)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 3
    assert inst.dispenseRequest.quantity.code == "g"
    assert inst.dispenseRequest.quantity.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.quantity.unit == "g"
    assert float(inst.dispenseRequest.quantity.value) == float(30)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate("2016-01-15")
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dosageInstruction[0].additionalInstruction[0].text == "Apply sparingly"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "OINT"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "ea"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].route.coding[0].code == "359540000"
    assert inst.dosageInstruction[0].route.coding[0].display == "Topical (qualifier value)"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].site.coding[0].code == "72098002"
    assert inst.dosageInstruction[0].site.coding[0].display == "Entire left upper arm (body structure)"
    assert inst.dosageInstruction[0].site.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].text == "Apply twice daily to affected area on left arm"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "medrx0329"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0319"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "on-hold"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_8(base_settings):
    """No. 8 tests collection for MedicationRequest.
    Test File: medicationrequest0329.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationrequest0329.json"
    )
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_8(inst2)


def impl_medicationrequest_9(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0309"
    assert inst.dosageInstruction[0].additionalInstruction[0].text == "Take at bedtime"
    assert inst.dosageInstruction[0].asNeededFor[0].coding[0].code == "32914008"
    assert inst.dosageInstruction[0].asNeededFor[0].coding[0].display == "Restless Legs"
    assert inst.dosageInstruction[0].asNeededFor[0].coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.high.code == "TAB"
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.high.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.high.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseRange.high.value) == float(2)
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.low.code == "TAB"
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.low.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.low.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseRange.low.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == (
    "Take 1-2 tablets once daily at bedtime as needed for "
    "restless legs"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx0310"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0309"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_9(base_settings):
    """No. 9 tests collection for MedicationRequest.
    Test File: medicationrequest0310.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationrequest0310.json"
    )
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_9(inst2)


def impl_medicationrequest_10(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert inst.dispenseRequest.expectedSupplyDuration.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(14)
    assert inst.dispenseRequest.quantity.code == "PATCH"
    assert inst.dispenseRequest.quantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dispenseRequest.quantity.unit == "patch"
    assert float(inst.dispenseRequest.quantity.value) == float(6)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate("2016-01-15")
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "PATCH"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "patch"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "apply one patch three times per week"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 3
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "wk"
    assert inst.id == "medrx0327"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.concept.coding[0].code == "333919005"
    assert inst.medication.concept.coding[0].display == "Fentanyl 25micrograms/hour patch (product)"
    assert inst.medication.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_10(base_settings):
    """No. 10 tests collection for MedicationRequest.
    Test File: medicationrequest0327.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationrequest0327.json"
    )
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_10(inst2)