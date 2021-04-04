# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Observation
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import observation


def impl_observation_1(inst):
    assert inst.bodySite.coding[0].code == "71341001:272741003=7771000"
    assert inst.bodySite.coding[0].system == "http://snomed.info/sct"
    assert inst.bodySite.text == "Left Femur"
    assert inst.code.coding[0].code == "24701-5"
    assert inst.code.coding[0].display == "Femur DXA Bone density"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "BMD - Left Femur"
    assert inst.id == "bmd"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].display == "Acme Imaging Diagnostics"
    assert (
        inst.performer[0].reference
        == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "g/cm-2"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "g/cm²"
    assert float(inst.valueQuantity.value) == float(0.887)


def test_observation_1(base_settings):
    """No. 1 tests collection for Observation.
    Test File: observation-example-bmd.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-bmd.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_1(inst2)


def impl_observation_2(inst):
    assert inst.code.coding[0].code == "789-8"
    assert (
        inst.code.coding[0].display
        == "Erythrocytes [#/volume] in Blood by Automated count"
    )
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2013-04-05T10:30:10+01:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2013-04-02T10:30:10+01:00"
    )
    assert inst.id == "f004"
    assert (
        inst.identifier[0].system
        == "http://www.bmc.nl/zorgportal/identifiers/observations"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "6326"
    assert inst.interpretation[0].coding[0].code == "L"
    assert inst.interpretation[0].coding[0].display == "Low"
    assert inst.interpretation[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpre" "tation"
    )
    assert inst.issued == fhirtypes.Instant.validate("2013-04-03T15:30:10+01:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].display == "A. Langeveld"
    assert inst.performer[0].reference == "Practitioner/f005"
    assert inst.status == "final"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "10*12/L"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "10^12/L"
    assert float(inst.valueQuantity.value) == float(4.12)


def test_observation_2(base_settings):
    """No. 2 tests collection for Observation.
    Test File: observation-example-f004-erythrocyte.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-f004-erythrocyte.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_2(inst2)


def impl_observation_3(inst):
    assert inst.code.text == "eye color"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-05-18")
    assert inst.id == "eye-color"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueString == "blue"


def test_observation_3(base_settings):
    """No. 3 tests collection for Observation.
    Test File: observation-example-eye-color.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-eye-color.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_3(inst2)


def impl_observation_4(inst):
    assert inst.category[0].coding[0].code == "survey"
    assert inst.category[0].coding[0].display == "Survey"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.category[0].text == "Survey"
    assert inst.code.coding[0].code == "9271-8"
    assert inst.code.coding[0].display == "10 minute Apgar Score"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.coding[1].code == "169922007"
    assert inst.code.coding[1].display == "Apgar at 10 minutes"
    assert inst.code.coding[1].system == "http://snomed.info/sct"
    assert inst.code.text == "10 minute Apgar Score"
    assert inst.component[0].code.coding[0].code == "32401-2"
    assert inst.component[0].code.coding[0].display == "10 minute Apgar Color"
    assert inst.component[0].code.coding[0].system == "http://loinc.org"
    assert inst.component[0].code.coding[1].code == "249227004"
    assert inst.component[0].code.coding[1].display == "Apgar color score"
    assert inst.component[0].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[0].code.text == "Apgar color score"
    assert inst.component[0].valueCodeableConcept.coding[0].code == "LA6724-4"
    assert (
        inst.component[0].valueCodeableConcept.coding[0].display
        == "Good color all over"
    )
    assert (
        inst.component[0].valueCodeableConcept.coding[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(
        inst.component[0].valueCodeableConcept.coding[0].extension[0].valueDecimal
    ) == float(2)
    assert inst.component[0].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[0].valueCodeableConcept.coding[1].code == "2"
    assert (
        inst.component[0].valueCodeableConcept.coding[1].system
        == "http://acme.ped/apgarcolor"
    )
    assert inst.component[0].valueCodeableConcept.text == "2. Good color all over"
    assert inst.component[1].code.coding[0].code == "32402-0"
    assert inst.component[1].code.coding[0].display == "10 minute Apgar Heart Rate"
    assert inst.component[1].code.coding[0].system == "http://loinc.org"
    assert inst.component[1].code.coding[1].code == "249223000"
    assert inst.component[1].code.coding[1].display == "Apgar heart rate score"
    assert inst.component[1].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[1].code.text == "Apgar respiratory effort score"
    assert inst.component[1].valueCodeableConcept.coding[0].code == "LA6718-6"
    assert (
        inst.component[1].valueCodeableConcept.coding[0].display
        == "At least 100 beats per minute"
    )
    assert (
        inst.component[1].valueCodeableConcept.coding[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(
        inst.component[1].valueCodeableConcept.coding[0].extension[0].valueDecimal
    ) == float(2)
    assert inst.component[1].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[1].valueCodeableConcept.coding[1].code == "2"
    assert (
        inst.component[1].valueCodeableConcept.coding[1].system
        == "http://acme.ped/apgarheartrate"
    )
    assert (
        inst.component[1].valueCodeableConcept.text
        == "2. At least 100 beats per minute"
    )
    assert inst.component[2].code.coding[0].code == "32404-6"
    assert (
        inst.component[2].code.coding[0].display
        == "10 minute Apgar Reflex Irritability"
    )
    assert inst.component[2].code.coding[0].system == "http://loinc.org"
    assert inst.component[2].code.coding[1].code == "249226008"
    assert (
        inst.component[2].code.coding[1].display == "Apgar response to stimulus score"
    )
    assert inst.component[2].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[2].code.text == "Apgar response to stimulus score"
    assert inst.component[2].valueCodeableConcept.coding[0].code == "LA6721-0"
    assert (
        inst.component[2].valueCodeableConcept.coding[0].display
        == "Grimace and pulling away, cough, or sneeze during suctioning"
    )
    assert (
        inst.component[2].valueCodeableConcept.coding[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(
        inst.component[2].valueCodeableConcept.coding[0].extension[0].valueDecimal
    ) == float(2)
    assert inst.component[2].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[2].valueCodeableConcept.coding[1].code == "2"
    assert (
        inst.component[2].valueCodeableConcept.coding[1].system
        == "http://acme.ped/apgarreflexirritability"
    )
    assert inst.component[2].valueCodeableConcept.text == (
        "2. Grimace and pulling away, cough, or sneeze during " "suctioning"
    )
    assert inst.component[3].code.coding[0].code == "32403-8"
    assert inst.component[3].code.coding[0].display == "10 minute Apgar Muscle Tone"
    assert inst.component[3].code.coding[0].system == "http://loinc.org"
    assert inst.component[3].code.coding[1].code == "249225007"
    assert inst.component[3].code.coding[1].display == "Apgar muscle tone score"
    assert inst.component[3].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[3].code.text == "Apgar muscle tone score"
    assert inst.component[3].valueCodeableConcept.coding[0].code == "LA6715-2"
    assert inst.component[3].valueCodeableConcept.coding[0].display == "Active motion "
    assert (
        inst.component[3].valueCodeableConcept.coding[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(
        inst.component[3].valueCodeableConcept.coding[0].extension[0].valueDecimal
    ) == float(2)
    assert inst.component[3].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[3].valueCodeableConcept.coding[1].code == "2"
    assert (
        inst.component[3].valueCodeableConcept.coding[1].system
        == "http://acme.ped/apgarmuscletone"
    )
    assert inst.component[3].valueCodeableConcept.text == "2. Active motion"
    assert inst.component[4].code.coding[0].code == "32405-3"
    assert (
        inst.component[4].code.coding[0].display == "10 minute Apgar Respiratory effort"
    )
    assert inst.component[4].code.coding[0].system == "http://loinc.org"
    assert inst.component[4].code.coding[1].code == "249224006"
    assert inst.component[4].code.coding[1].display == "Apgar respiratory effort score"
    assert inst.component[4].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[4].code.text == "Apgar respiratory effort score"
    assert inst.component[4].valueCodeableConcept.coding[0].code == "LA6727-7"
    assert (
        inst.component[4].valueCodeableConcept.coding[0].display
        == "Good, strong cry; normal rate and effort of breathing    "
    )
    assert (
        inst.component[4].valueCodeableConcept.coding[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(
        inst.component[4].valueCodeableConcept.coding[0].extension[0].valueDecimal
    ) == float(2)
    assert inst.component[4].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[4].valueCodeableConcept.coding[1].code == "2"
    assert (
        inst.component[4].valueCodeableConcept.coding[1].system
        == "http://acme.ped/apgarrespiratoryeffort"
    )
    assert (
        inst.component[4].valueCodeableConcept.text
        == "2. Good, strong cry; normal rate and effort of breathing"
    )
    assert inst.contained[0].id == "newborn"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-05-18T22:33:22Z")
    assert inst.id == "10minute-apgar-score"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.status == "final"
    assert inst.subject.reference == "#newborn"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "{score}"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.valueQuantity.value) == float(10)


def test_observation_4(base_settings):
    """No. 4 tests collection for Observation.
    Test File: observation-example-10minute-apgar-score.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "observation-example-10minute-apgar-score.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_4(inst2)


def impl_observation_5(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "2708-6"
    assert inst.code.coding[0].display == "Oxygen saturation in Arterial blood"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.coding[1].code == "59408-5"
    assert (
        inst.code.coding[1].display
        == "Oxygen saturation in Arterial blood by Pulse oximetry"
    )
    assert inst.code.coding[1].system == "http://loinc.org"
    assert inst.code.coding[2].code == "150456"
    assert inst.code.coding[2].display == "MDC_PULS_OXIM_SAT_O2"
    assert inst.code.coding[2].system == "urn:iso:std:iso:11073:10101"
    assert inst.device.reference == "DeviceMetric/example"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2014-12-05T09:30:10+01:00"
    )
    assert inst.id == "satO2"
    assert inst.identifier[0].system == "http://goodcare.org/observation/id"
    assert inst.identifier[0].value == "o1223435-10"
    assert inst.interpretation[0].coding[0].code == "N"
    assert inst.interpretation[0].coding[0].display == "Normal"
    assert inst.interpretation[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpre" "tation"
    )
    assert inst.interpretation[0].text == "Normal (applies to non-numeric results)"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.partOf[0].reference == "Procedure/ob"
    assert inst.referenceRange[0].high.code == "%"
    assert inst.referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[0].high.unit == "%"
    assert float(inst.referenceRange[0].high.value) == float(99)
    assert inst.referenceRange[0].low.code == "%"
    assert inst.referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[0].low.unit == "%"
    assert float(inst.referenceRange[0].low.value) == float(90)
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "%"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "%"
    assert float(inst.valueQuantity.value) == float(95)


def test_observation_5(base_settings):
    """No. 5 tests collection for Observation.
    Test File: observation-example-satO2.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-satO2.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_5(inst2)


def impl_observation_6(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.code.coding[0].code == "29463-7"
    assert inst.code.coding[0].display == "Body Weight"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.coding[1].code == "3141-9"
    assert inst.code.coding[1].display == "Body weight Measured"
    assert inst.code.coding[1].system == "http://loinc.org"
    assert inst.code.coding[2].code == "27113001"
    assert inst.code.coding[2].display == "Body weight"
    assert inst.code.coding[2].system == "http://snomed.info/sct"
    assert inst.code.coding[3].code == "body-weight"
    assert inst.code.coding[3].display == "Body Weight"
    assert inst.code.coding[3].system == "http://acme.org/devices/clinical-codes"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-03-28")
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "[lb_av]"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "lbs"
    assert float(inst.valueQuantity.value) == float(185)


def test_observation_6(base_settings):
    """No. 6 tests collection for Observation.
    Test File: observation-example.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_6(inst2)


def impl_observation_7(inst):
    assert inst.category[0].coding[0].code == "laboratory"
    assert inst.category[0].coding[0].display == "Laboratory"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.category[0].text == "Laboratory"
    assert inst.code.coding[0].code == "883-9"
    assert inst.code.coding[0].display == "ABO group [Type] in Blood"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Blood Group"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2018-03-11T16:07:54+00:00"
    )
    assert inst.id == "bloodgroup"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/infant"
    assert inst.text.status == "generated"
    assert inst.valueCodeableConcept.coding[0].code == "112144000"
    assert inst.valueCodeableConcept.coding[0].display == "Blood group A (finding)"
    assert inst.valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.valueCodeableConcept.text == "A"


def test_observation_7(base_settings):
    """No. 7 tests collection for Observation.
    Test File: observation-example-bloodgroup.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-bloodgroup.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_7(inst2)


def impl_observation_8(inst):
    assert inst.category[0].coding[0].code == "survey"
    assert inst.category[0].coding[0].display == "Survey"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.category[0].text == "Survey"
    assert inst.code.coding[0].code == "9274-2"
    assert inst.code.coding[0].display == "5 minute Apgar Score"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.coding[1].code == "169909004"
    assert inst.code.coding[1].display == "Apgar at 5 minutes"
    assert inst.code.coding[1].system == "http://snomed.info/sct"
    assert inst.code.text == "5 minute Apgar Score"
    assert inst.component[0].code.coding[0].code == "32411-1"
    assert inst.component[0].code.coding[0].display == "5 minute Apgar Color"
    assert inst.component[0].code.coding[0].system == "http://loinc.org"
    assert inst.component[0].code.coding[1].code == "249227004"
    assert inst.component[0].code.coding[1].display == "Apgar color score"
    assert inst.component[0].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[0].code.text == "Apgar color score"
    assert inst.component[0].valueCodeableConcept.coding[0].code == "LA6724-4"
    assert (
        inst.component[0].valueCodeableConcept.coding[0].display
        == "Good color all over"
    )
    assert (
        inst.component[0].valueCodeableConcept.coding[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(
        inst.component[0].valueCodeableConcept.coding[0].extension[0].valueDecimal
    ) == float(2)
    assert inst.component[0].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[0].valueCodeableConcept.coding[1].code == "2"
    assert (
        inst.component[0].valueCodeableConcept.coding[1].system
        == "http://acme.ped/apgarcolor"
    )
    assert inst.component[0].valueCodeableConcept.text == "2. Good color all over"
    assert inst.component[1].code.coding[0].code == "32412-9"
    assert inst.component[1].code.coding[0].display == "5 minute Apgar Heart Rate"
    assert inst.component[1].code.coding[0].system == "http://loinc.org"
    assert inst.component[1].code.coding[1].code == "249223000"
    assert inst.component[1].code.coding[1].display == "Apgar heart rate score"
    assert inst.component[1].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[1].code.text == "Apgar respiratory effort score"
    assert inst.component[1].valueCodeableConcept.coding[0].code == "LA6718-6"
    assert (
        inst.component[1].valueCodeableConcept.coding[0].display
        == "At least 100 beats per minute"
    )
    assert (
        inst.component[1].valueCodeableConcept.coding[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(
        inst.component[1].valueCodeableConcept.coding[0].extension[0].valueDecimal
    ) == float(2)
    assert inst.component[1].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[1].valueCodeableConcept.coding[1].code == "2"
    assert (
        inst.component[1].valueCodeableConcept.coding[1].system
        == "http://acme.ped/apgarheartrate"
    )
    assert (
        inst.component[1].valueCodeableConcept.text
        == "2. At least 100 beats per minute"
    )
    assert inst.component[2].code.coding[0].code == "32414-5"
    assert (
        inst.component[2].code.coding[0].display == "5 minute Apgar Reflex Irritability"
    )
    assert inst.component[2].code.coding[0].system == "http://loinc.org"
    assert inst.component[2].code.coding[1].code == "249226008"
    assert (
        inst.component[2].code.coding[1].display == "Apgar response to stimulus score"
    )
    assert inst.component[2].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[2].code.text == "Apgar response to stimulus score"
    assert inst.component[2].valueCodeableConcept.coding[0].code == "LA6721-0"
    assert (
        inst.component[2].valueCodeableConcept.coding[0].display
        == "Grimace and pulling away, cough, or sneeze during suctioning"
    )
    assert (
        inst.component[2].valueCodeableConcept.coding[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(
        inst.component[2].valueCodeableConcept.coding[0].extension[0].valueDecimal
    ) == float(2)
    assert inst.component[2].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[2].valueCodeableConcept.coding[1].code == "2"
    assert (
        inst.component[2].valueCodeableConcept.coding[1].system
        == "http://acme.ped/apgarreflexirritability"
    )
    assert inst.component[2].valueCodeableConcept.text == (
        "2. Grimace and pulling away, cough, or sneeze during " "suctioning"
    )
    assert inst.component[3].code.coding[0].code == "32413-7"
    assert inst.component[3].code.coding[0].display == "5 minute Apgar Muscle Tone"
    assert inst.component[3].code.coding[0].system == "http://loinc.org"
    assert inst.component[3].code.coding[1].code == "249225007"
    assert inst.component[3].code.coding[1].display == "Apgar muscle tone score"
    assert inst.component[3].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[3].code.text == "Apgar muscle tone score"
    assert inst.component[3].valueCodeableConcept.coding[0].code == "LA6715-2"
    assert inst.component[3].valueCodeableConcept.coding[0].display == "Active motion "
    assert (
        inst.component[3].valueCodeableConcept.coding[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(
        inst.component[3].valueCodeableConcept.coding[0].extension[0].valueDecimal
    ) == float(2)
    assert inst.component[3].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[3].valueCodeableConcept.coding[1].code == "2"
    assert (
        inst.component[3].valueCodeableConcept.coding[1].system
        == "http://acme.ped/apgarmuscletone"
    )
    assert inst.component[3].valueCodeableConcept.text == "2. Active motion"
    assert inst.component[4].code.coding[0].code == "32415-2"
    assert (
        inst.component[4].code.coding[0].display == "5 minute Apgar Respiratory effort"
    )
    assert inst.component[4].code.coding[0].system == "http://loinc.org"
    assert inst.component[4].code.coding[1].code == "249224006"
    assert inst.component[4].code.coding[1].display == "Apgar respiratory effort score"
    assert inst.component[4].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[4].code.text == "Apgar respiratory effort score"
    assert inst.component[4].valueCodeableConcept.coding[0].code == "LA6727-7"
    assert (
        inst.component[4].valueCodeableConcept.coding[0].display
        == "Good, strong cry; normal rate and effort of breathing    "
    )
    assert (
        inst.component[4].valueCodeableConcept.coding[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(
        inst.component[4].valueCodeableConcept.coding[0].extension[0].valueDecimal
    ) == float(2)
    assert inst.component[4].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[4].valueCodeableConcept.coding[1].code == "2"
    assert (
        inst.component[4].valueCodeableConcept.coding[1].system
        == "http://acme.ped/apgarrespiratoryeffort"
    )
    assert (
        inst.component[4].valueCodeableConcept.text
        == "2. Good, strong cry; normal rate and effort of breathing"
    )
    assert inst.contained[0].id == "newborn"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-05-18T22:33:22Z")
    assert inst.id == "5minute-apgar-score"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.status == "final"
    assert inst.subject.reference == "#newborn"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "{score}"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.valueQuantity.value) == float(10)


def test_observation_8(base_settings):
    """No. 8 tests collection for Observation.
    Test File: observation-example-5minute-apgar-score.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "observation-example-5minute-apgar-score.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_8(inst2)


def impl_observation_9(inst):
    assert inst.category[0].coding[0].code == "procedure"
    assert inst.category[0].coding[0].display == "Procedure"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.code.coding[0].code == "131328"
    assert inst.code.coding[0].display == "MDC_ECG_ELEC_POTL"
    assert inst.code.coding[0].system == "urn:oid:2.16.840.1.113883.6.24"
    assert inst.component[0].code.coding[0].code == "131329"
    assert inst.component[0].code.coding[0].display == "MDC_ECG_ELEC_POTL_I"
    assert inst.component[0].code.coding[0].system == "urn:oid:2.16.840.1.113883.6.24"
    assert inst.component[0].valueSampledData.dimensions == 1
    assert float(inst.component[0].valueSampledData.factor) == float(1.612)
    assert float(inst.component[0].valueSampledData.lowerLimit) == float(-3300)
    assert float(inst.component[0].valueSampledData.origin.value) == float(2048)
    assert float(inst.component[0].valueSampledData.period) == float(10)
    assert float(inst.component[0].valueSampledData.upperLimit) == float(3300)
    assert inst.component[1].code.coding[0].code == "131330"
    assert inst.component[1].code.coding[0].display == "MDC_ECG_ELEC_POTL_II"
    assert inst.component[1].code.coding[0].system == "urn:oid:2.16.840.1.113883.6.24"
    assert inst.component[1].valueSampledData.dimensions == 1
    assert float(inst.component[1].valueSampledData.factor) == float(1.612)
    assert float(inst.component[1].valueSampledData.lowerLimit) == float(-3300)
    assert float(inst.component[1].valueSampledData.origin.value) == float(2048)
    assert float(inst.component[1].valueSampledData.period) == float(10)
    assert float(inst.component[1].valueSampledData.upperLimit) == float(3300)
    assert inst.component[2].code.coding[0].code == "131389"
    assert inst.component[2].code.coding[0].display == "MDC_ECG_ELEC_POTL_III"
    assert inst.component[2].code.coding[0].system == "urn:oid:2.16.840.1.113883.6.24"
    assert inst.component[2].valueSampledData.dimensions == 1
    assert float(inst.component[2].valueSampledData.factor) == float(1.612)
    assert float(inst.component[2].valueSampledData.lowerLimit) == float(-3300)
    assert float(inst.component[2].valueSampledData.origin.value) == float(2048)
    assert float(inst.component[2].valueSampledData.period) == float(10)
    assert float(inst.component[2].valueSampledData.upperLimit) == float(3300)
    assert inst.device.display == "12 lead EKG Device Metric"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2015-02-19T09:30:35+01:00"
    )
    assert inst.id == "ekg"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].display == "A. Langeveld"
    assert inst.performer[0].reference == "Practitioner/f005"
    assert inst.status == "final"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_observation_9(base_settings):
    """No. 9 tests collection for Observation.
    Test File: observation-example-sample-data.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-sample-data.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_9(inst2)


def impl_observation_10(inst):
    assert inst.code.coding[0].code == "15074-8"
    assert inst.code.coding[0].display == "Glucose [Moles/volume] in Blood"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2013-04-02T09:30:10+01:00"
    )
    assert inst.id == "f001"
    assert (
        inst.identifier[0].system
        == "http://www.bmc.nl/zorgportal/identifiers/observations"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "6323"
    assert inst.interpretation[0].coding[0].code == "H"
    assert inst.interpretation[0].coding[0].display == "High"
    assert inst.interpretation[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpre" "tation"
    )
    assert inst.issued == fhirtypes.Instant.validate("2013-04-03T15:30:10+01:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].display == "A. Langeveld"
    assert inst.performer[0].reference == "Practitioner/f005"
    assert inst.referenceRange[0].high.code == "mmol/L"
    assert inst.referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[0].high.unit == "mmol/l"
    assert float(inst.referenceRange[0].high.value) == float(6.2)
    assert inst.referenceRange[0].low.code == "mmol/L"
    assert inst.referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[0].low.unit == "mmol/l"
    assert float(inst.referenceRange[0].low.value) == float(3.1)
    assert inst.status == "final"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "mmol/L"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "mmol/l"
    assert float(inst.valueQuantity.value) == float(6.3)


def test_observation_10(base_settings):
    """No. 10 tests collection for Observation.
    Test File: observation-example-f001-glucose.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-f001-glucose.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_10(inst2)
