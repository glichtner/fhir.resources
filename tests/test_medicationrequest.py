# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import medicationrequest


def impl_medicationrequest_1(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0320"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(5)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 1
    assert inst.dispenseRequest.quantity.code == "TAB"
    assert (
        inst.dispenseRequest.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dispenseRequest.quantity.unit == "TAB"
    assert float(inst.dispenseRequest.quantity.value) == float(6)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "311504000"
    )
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].display
        == "With or after food"
    )
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        2
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].method.coding[0].code == "421521009"
    assert (
        inst.dosageInstruction[0].method.coding[0].display
        == "Swallow - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosageInstruction[0].method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Two tablets at once"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert (
        inst.dosageInstruction[1].additionalInstruction[0].coding[0].code == "311504000"
    )
    assert (
        inst.dosageInstruction[1].additionalInstruction[0].coding[0].display
        == "With or after food"
    )
    assert (
        inst.dosageInstruction[1].additionalInstruction[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.dosageInstruction[1].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosageInstruction[1].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[1].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[1].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[1].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[1].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[1].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[1].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[1].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[1].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[1].sequence == 2
    assert inst.dosageInstruction[1].text == "One tablet daily for 4 days"
    assert inst.dosageInstruction[1].timing.repeat.frequency == 4
    assert float(inst.dosageInstruction[1].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[1].timing.repeat.periodUnit == "d"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx0302"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0320"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Patient told to take with food"
    assert inst.reason[0].concept.coding[0].code == "11840006"
    assert inst.reason[0].concept.coding[0].display == "Traveller's Diarrhea (disorder)"
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is True
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert (
        inst.substitution.reason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.supportingInformation[0].reference == "Coverage/SP1234"
    assert inst.text.status == "generated"


def test_medicationrequest_1(base_settings):
    """No. 1 tests collection for MedicationRequest.
    Test File: medicationrequest0302.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0302.json"
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
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-03-01")
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Take one tablet daily as directed"
    assert inst.encounter.display == "encounter that leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx002"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345"
    assert inst.intent == "order"
    assert inst.medication.reference.display == "prescribed medication"
    assert inst.medication.reference.reference == "Medication/med0316"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reason[0].concept.coding[0].code == "59621000"
    assert (
        inst.reason[0].concept.coding[0].display == "Essential hypertension (disorder)"
    )
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_2(base_settings):
    """No. 2 tests collection for MedicationRequest.
    Test File: medicationrequestexample2.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequestexample2.json"
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
    assert inst.contained[0].id == "med0302"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "g"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "g"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        4.5
    )
    assert inst.dosageInstruction[0].doseAndRate[0].rateQuantity.code == "ml/h"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].rateQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.dosageInstruction[0].doseAndRate[0].rateQuantity.value) == float(
        50
    )
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
    assert inst.dosageInstruction[0].text == (
        "4.5 grams in D5W 250 ml. IV every 6 hours.Infuse over 30 min" " at 8L/min "
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
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reason[0].concept.coding[0].code == "385093006"
    assert (
        inst.reason[0].concept.coding[0].display
        == "Community acquired pneumonia (disorder)"
    )
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_3(base_settings):
    """No. 3 tests collection for MedicationRequest.
    Test File: medicationrequest0319.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0319.json"
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
    assert inst.contained[0].id == "med0315"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(30)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 3
    assert inst.dispenseRequest.quantity.code == "ml"
    assert inst.dispenseRequest.quantity.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.quantity.unit == "ml"
    assert float(inst.dispenseRequest.quantity.value) == float(30)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
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
    assert inst.dosageInstruction[0].text == "Use 1 spray twice daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "medrx0328"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0315"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is True
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert (
        inst.substitution.reason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medicationrequest_4(base_settings):
    """No. 4 tests collection for MedicationRequest.
    Test File: medicationrequest0328.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0328.json"
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
    assert inst.contained[0].id == "med0314"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(10)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 1
    assert inst.dispenseRequest.quantity.code == "TAB"
    assert (
        inst.dispenseRequest.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dispenseRequest.quantity.unit == "TAB"
    assert float(inst.dispenseRequest.quantity.value) == float(30)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
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
    assert inst.dosageInstruction[0].maxDosePerAdministration.code == "mg"
    assert (
        inst.dosageInstruction[0].maxDosePerAdministration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].maxDosePerAdministration.unit == "mg"
    assert float(inst.dosageInstruction[0].maxDosePerAdministration.value) == float(4)
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
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx0305"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0314"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is True
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert (
        inst.substitution.reason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medicationrequest_5(base_settings):
    """No. 5 tests collection for MedicationRequest.
    Test File: medicationrequest0305.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0305.json"
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
    assert inst.contained[0].id == "med0305"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(30)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 1
    assert inst.dispenseRequest.quantity.code == "mL"
    assert inst.dispenseRequest.quantity.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.quantity.unit == "mL"
    assert float(inst.dispenseRequest.quantity.value) == float(10)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "OPDROP"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "OPDROP"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].method.coding[0].code == "421538008"
    assert (
        inst.dosageInstruction[0].method.coding[0].display
        == "Instill - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosageInstruction[0].method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].route.coding[0].code == "54485002"
    assert (
        inst.dosageInstruction[0].route.coding[0].display
        == "Ophthalmic route (qualifier value)"
    )
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Instil one drop in each eye twice daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f002"
    assert inst.id == "medrx0330"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0305"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is False
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert (
        inst.substitution.reason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medicationrequest_6(base_settings):
    """No. 6 tests collection for MedicationRequest.
    Test File: medicationrequest0330.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0330.json"
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
    assert inst.basedOn[0].reference == "CarePlan/gpvisit"
    assert inst.contained[0].id == "med0311"
    assert inst.dispenseRequest.dispenser.reference == "Organization/f001"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(21)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 1
    assert inst.dispenseRequest.quantity.code == "TAB"
    assert (
        inst.dispenseRequest.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dispenseRequest.quantity.unit == "TAB"
    assert float(inst.dispenseRequest.quantity.value) == float(51)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        4
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].method.coding[0].code == "421521009"
    assert (
        inst.dosageInstruction[0].method.coding[0].display
        == "Swallow - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosageInstruction[0].method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert (
        inst.dosageInstruction[0].text
        == "Take 4 tablets daily for 7 days starting January 16, 2015"
    )
    assert inst.dosageInstruction[
        0
    ].timing.repeat.boundsPeriod.end == fhirtypes.DateTime.validate("2015-01-22")
    assert inst.dosageInstruction[
        0
    ].timing.repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2015-01-16")
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.dosageInstruction[1].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosageInstruction[1].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[1].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[1].doseAndRate[0].doseQuantity.value) == float(
        2
    )
    assert inst.dosageInstruction[1].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[1].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[1].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[1].method.coding[0].code == "421521009"
    assert (
        inst.dosageInstruction[1].method.coding[0].display
        == "Swallow - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosageInstruction[1].method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[1].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[1].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[1].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[1].sequence == 2
    assert (
        inst.dosageInstruction[1].text
        == "Take 2 tablets daily for 7 days starting January 23, 2015"
    )
    assert inst.dosageInstruction[
        1
    ].timing.repeat.boundsPeriod.end == fhirtypes.DateTime.validate("2015-01-29")
    assert inst.dosageInstruction[
        1
    ].timing.repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2015-01-23")
    assert inst.dosageInstruction[1].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[1].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[1].timing.repeat.periodUnit == "d"
    assert inst.dosageInstruction[2].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosageInstruction[2].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[2].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[2].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[2].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[2].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[2].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[2].method.coding[0].code == "421521009"
    assert (
        inst.dosageInstruction[2].method.coding[0].display
        == "Swallow - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosageInstruction[2].method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[2].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[2].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[2].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[2].sequence == 3
    assert (
        inst.dosageInstruction[2].text
        == "Take 1 tablets daily for 7 days starting January 30, 2015"
    )
    assert inst.dosageInstruction[
        2
    ].timing.repeat.boundsPeriod.end == fhirtypes.DateTime.validate("2015-02-05")
    assert inst.dosageInstruction[
        2
    ].timing.repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2015-01-30")
    assert inst.dosageInstruction[2].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[2].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[2].timing.repeat.periodUnit == "d"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.groupIdentifier.system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.groupIdentifier.use == "official"
    assert inst.groupIdentifier.value == "983939393"
    assert inst.id == "medrx0303"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0311"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Patient told to take with food"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedCodeableConcept.coding[0].code == "TB"
    assert (
        inst.substitution.allowedCodeableConcept.coding[0].display
        == "Therapeutic Brand"
    )
    assert inst.substitution.allowedCodeableConcept.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/v3-substanceAdminSubst" "itution"
    )
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert (
        inst.substitution.reason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medicationrequest_7(base_settings):
    """No. 7 tests collection for MedicationRequest.
    Test File: medicationrequest0303.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0303.json"
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
    assert inst.contained[0].id == "med0301"
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
    assert inst.dosageInstruction[0].timing.event[0] == fhirtypes.DateTime.validate(
        "2020-01-01"
    )
    assert inst.dosageInstruction[
        0
    ].timing.repeat.boundsPeriod.end == fhirtypes.DateTime.validate("2020-01-10")
    assert inst.dosageInstruction[
        0
    ].timing.repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2020-01-01")
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(6)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx0318"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0301"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == (
        "culture expected back in 12 hours - may switch depending on " "results"
    )
    assert inst.reason[0].concept.coding[0].code == "11840006"
    assert inst.reason[0].concept.coding[0].display == "Traveller's Diarrhea (disorder)"
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_8(base_settings):
    """No. 8 tests collection for MedicationRequest.
    Test File: medicationrequest0318.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0318.json"
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
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(30)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 3
    assert inst.dispenseRequest.quantity.code == "mL"
    assert inst.dispenseRequest.quantity.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.quantity.unit == "mL"
    assert float(inst.dispenseRequest.quantity.value) == float(360)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        100
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
    assert inst.id == "medrx0312"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.concept.coding[0].code == "1313112"
    assert (
        inst.medication.concept.coding[0].display == "Phenytoin 25mg/ml oral suspension"
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
    assert (
        inst.note[0].text
        == "Patient should be counselled to ensure good dental hygiene"
    )
    assert inst.priorPrescription.reference == "MedicationRequest/medrx0304"
    assert inst.reason[0].concept.coding[0].code == "230456007"
    assert inst.reason[0].concept.coding[0].display == "Status epilepticus (disorder)"
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is True
    assert inst.substitution.reason.coding[0].code == "CT"
    assert inst.substitution.reason.coding[0].display == "Continuing therapy"
    assert (
        inst.substitution.reason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medicationrequest_9(base_settings):
    """No. 9 tests collection for MedicationRequest.
    Test File: medicationrequest0312.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0312.json"
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
    assert inst.contained[0].id == "med0313"
    assert inst.dosageInstruction[0].asNeededBoolean is True
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.high.code == "mg/kg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseRange.high.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.high.unit == "mg/kg"
    assert float(
        inst.dosageInstruction[0].doseAndRate[0].doseRange.high.value
    ) == float(0.1)
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.low.code == "mg/kg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseRange.low.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.low.unit == "mg/kg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseRange.low.value) == float(
        0.05
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
    assert inst.dosageInstruction[0].text == (
        "0.05 - 0.1mg/kg IV over 2-5 minutes every 15 minutes as " "needed"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(15)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "min"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx0315"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medication.reference.reference == "#med0313"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reason[0].concept.coding[0].code == "84757009"
    assert inst.reason[0].concept.coding[0].display == "Epilepsy (disorder)"
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_10(base_settings):
    """No. 10 tests collection for MedicationRequest.
    Test File: medicationrequest0315.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0315.json"
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
