# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Observation
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import observation


def impl_observation_1(inst):
    assert inst.code.text == "eye color"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-05-18")
    assert inst.id == "eye-color"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueString == "blue"


def test_observation_1(base_settings):
    """No. 1 tests collection for Observation.
    Test File: observation-example-eye-color.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-eye-color.json"
    )
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
    assert inst.category[0].coding[0].code == "survey"
    assert inst.category[0].coding[0].display == "Survey"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/observation-category"
    assert inst.category[0].text == "AOE"
    assert inst.code.coding[0].code == "8665-2"
    assert inst.code.coding[0].display == "Date last menstrual period"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Date last menstrual period"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-01-24")
    assert inst.id == "date-lastmp"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"
    assert inst.valueDateTime == fhirtypes.DateTime.validate("2016-12-30")


def test_observation_2(base_settings):
    """No. 2 tests collection for Observation.
    Test File: observation-example-date-lastmp.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-date-lastmp.json"
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
    assert inst.code.coding[0].code == "15074-8"
    assert inst.code.coding[0].display == "Glucose [Moles/volume] in Blood"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2013-04-02T09:30:10+01:00")
    assert inst.id == "f001"
    assert inst.identifier[0].system == "http://www.bmc.nl/zorgportal/identifiers/observations"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "6323"
    assert inst.interpretation[0].coding[0].code == "H"
    assert inst.interpretation[0].coding[0].display == "High"
    assert inst.interpretation[0].coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpre"
    "tation"
    )
    assert inst.issued == fhirtypes.Instant.validate("2013-04-03T15:30:10+01:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
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


def test_observation_3(base_settings):
    """No. 3 tests collection for Observation.
    Test File: observation-example-f001-glucose.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-f001-glucose.json"
    )
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
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/observation-category"
    assert inst.category[0].text == "Survey"
    assert inst.code.coding[0].code == "9273-4"
    assert inst.code.coding[0].display == "2 minute Apgar Score"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "2 minute Apgar Score"
    assert inst.component[0].code.coding[0].code == "249227004"
    assert inst.component[0].code.coding[0].display == "Apgar color score"
    assert inst.component[0].code.coding[0].system == "http://snomed.info/sct"
    assert inst.component[0].code.text == "Apgar color score"
    assert inst.component[0].valueCodeableConcept.coding[0].code == "LA6723-6"
    assert inst.component[0].valueCodeableConcept.coding[0].display == "Good color in body with bluish hands or feet"
    assert inst.component[0].valueCodeableConcept.coding[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/itemWeight"
    assert float(inst.component[0].valueCodeableConcept.coding[0].extension[0].valueDecimal) == float(1)
    assert inst.component[0].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[0].valueCodeableConcept.coding[1].code == "1"
    assert inst.component[0].valueCodeableConcept.coding[1].system == "http://acme.ped/apgarcolor"
    assert inst.component[0].valueCodeableConcept.text == "1. Good color in body with bluish hands or feet"
    assert inst.component[1].code.coding[0].code == "249223000"
    assert inst.component[1].code.coding[0].display == "Apgar heart rate score"
    assert inst.component[1].code.coding[0].system == "http://snomed.info/sct"
    assert inst.component[1].code.text == "Apgar respiratory effort score"
    assert inst.component[1].valueCodeableConcept.coding[0].code == "LA6720-2"
    assert inst.component[1].valueCodeableConcept.coding[0].display == "Fewer than 100 beats per minute"
    assert inst.component[1].valueCodeableConcept.coding[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/itemWeight"
    assert float(inst.component[1].valueCodeableConcept.coding[0].extension[0].valueDecimal) == float(1)
    assert inst.component[1].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[1].valueCodeableConcept.coding[1].code == "1"
    assert inst.component[1].valueCodeableConcept.coding[1].system == "http://acme.ped/apgarheartrate"
    assert inst.component[1].valueCodeableConcept.text == "1. Fewer than 100 beats per minute"
    assert inst.component[2].code.coding[0].code == "249226008"
    assert inst.component[2].code.coding[0].display == "Apgar response to stimulus score"
    assert inst.component[2].code.coding[0].system == "http://snomed.info/sct"
    assert inst.component[2].code.text == "Apgar response to stimulus score"
    assert inst.component[2].valueCodeableConcept.coding[0].code == "LA6721-0"
    assert inst.component[2].valueCodeableConcept.coding[0].display == "Grimace during suctioning"
    assert inst.component[2].valueCodeableConcept.coding[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/itemWeight"
    assert float(inst.component[2].valueCodeableConcept.coding[0].extension[0].valueDecimal) == float(1)
    assert inst.component[2].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[2].valueCodeableConcept.coding[1].code == "1"
    assert inst.component[2].valueCodeableConcept.coding[1].system == "http://acme.ped/apgarreflexirritability"
    assert inst.component[2].valueCodeableConcept.text == "1. Grimace during suctioning"
    assert inst.component[3].code.coding[0].code == "249225007"
    assert inst.component[3].code.coding[0].display == "Apgar muscle tone score"
    assert inst.component[3].code.coding[0].system == "http://snomed.info/sct"
    assert inst.component[3].code.text == "Apgar muscle tone score"
    assert inst.component[3].valueCodeableConcept.coding[0].code == "LA6714-5"
    assert inst.component[3].valueCodeableConcept.coding[0].display == "Some flexion of arms and legs"
    assert inst.component[3].valueCodeableConcept.coding[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/itemWeight"
    assert float(inst.component[3].valueCodeableConcept.coding[0].extension[0].valueDecimal) == float(1)
    assert inst.component[3].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[3].valueCodeableConcept.coding[1].code == "1"
    assert inst.component[3].valueCodeableConcept.coding[1].system == "http://acme.ped/apgarmuscletone"
    assert inst.component[3].valueCodeableConcept.text == "1. Some flexion of arms and legs"
    assert inst.component[4].code.coding[0].code == "249224006"
    assert inst.component[4].code.coding[0].display == "Apgar respiratory effort score"
    assert inst.component[4].code.coding[0].system == "http://snomed.info/sct"
    assert inst.component[4].code.text == "Apgar respiratory effort score"
    assert inst.component[4].valueCodeableConcept.coding[0].code == "LA6726-9"
    assert inst.component[4].valueCodeableConcept.coding[0].display == (
    "Weak cry; may sound like whimpering, slow or irregular "
    "breathing"
    )
    assert inst.component[4].valueCodeableConcept.coding[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/itemWeight"
    assert float(inst.component[4].valueCodeableConcept.coding[0].extension[0].valueDecimal) == float(1)
    assert inst.component[4].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.component[4].valueCodeableConcept.coding[1].code == "1"
    assert inst.component[4].valueCodeableConcept.coding[1].system == "http://acme.ped/apgarrespiratoryeffort"
    assert inst.component[4].valueCodeableConcept.text == (
    "1. Weak cry; may sound like whimpering, slow or irregular "
    "breathing"
    )
    assert inst.contained[0].id == "newborn"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-05-18T22:33:22Z")
    assert inst.id == "2minute-apgar-score"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.status == "final"
    assert inst.subject.reference == "#newborn"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "{score}"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.valueQuantity.value) == float(5)


def test_observation_4(base_settings):
    """No. 4 tests collection for Observation.
    Test File: observation-example-2minute-apgar-score.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-2minute-apgar-score.json"
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
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/observation-category"
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "85353-1"
    assert inst.code.coding[0].display == (
    "Vital signs, weight, height, head circumference, oxygen "
    "saturation and BMI panel"
    )
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Vital signs Panel"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.hasMember[0].display == "Respiratory Rate"
    assert inst.hasMember[0].reference == "Observation/respiratory-rate"
    assert inst.hasMember[1].display == "Heart Rate"
    assert inst.hasMember[1].reference == "Observation/heart-rate"
    assert inst.hasMember[2].display == "Blood Pressure"
    assert inst.hasMember[2].reference == "Observation/blood-pressure"
    assert inst.hasMember[3].display == "Body Temperature"
    assert inst.hasMember[3].reference == "Observation/body-temperature"
    assert inst.id == "vitals-panel"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_observation_5(base_settings):
    """No. 5 tests collection for Observation.
    Test File: observation-example-vitals-panel.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-vitals-panel.json"
    )
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
    assert inst.bodySite.coding[0].code == "368209003"
    assert inst.bodySite.coding[0].display == "Right arm"
    assert inst.bodySite.coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/observation-category"
    assert inst.code.coding[0].code == "85354-9"
    assert inst.code.coding[0].display == "Blood pressure panel with all children optional"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Blood pressure systolic & diastolic"
    assert inst.component[0].code.coding[0].code == "8480-6"
    assert inst.component[0].code.coding[0].display == "Systolic blood pressure"
    assert inst.component[0].code.coding[0].system == "http://loinc.org"
    assert inst.component[0].code.coding[1].code == "271649006"
    assert inst.component[0].code.coding[1].display == "Systolic blood pressure"
    assert inst.component[0].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[0].code.coding[2].code == "bp-s"
    assert inst.component[0].code.coding[2].display == "Systolic Blood pressure"
    assert inst.component[0].code.coding[2].system == "http://acme.org/devices/clinical-codes"
    assert inst.component[0].dataAbsentReason.coding[0].code == "not-asked"
    assert inst.component[0].dataAbsentReason.coding[0].display == "Not Asked"
    assert inst.component[0].dataAbsentReason.coding[0].system == "http://terminology.hl7.org/CodeSystem/data-absent-reason"
    assert inst.component[1].code.coding[0].code == "8462-4"
    assert inst.component[1].code.coding[0].display == "Diastolic blood pressure"
    assert inst.component[1].code.coding[0].system == "http://loinc.org"
    assert inst.component[1].dataAbsentReason.coding[0].code == "not-asked"
    assert inst.component[1].dataAbsentReason.coding[0].display == "Not Asked"
    assert inst.component[1].dataAbsentReason.coding[0].system == "http://terminology.hl7.org/CodeSystem/data-absent-reason"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2012-09-17")
    assert inst.id == "blood-pressure-cancel"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:uuid:187e0c12-8dd2-67e2-99b2-bf273c878281"
    assert inst.interpretation[0].coding[0].code == "L"
    assert inst.interpretation[0].coding[0].display == "low"
    assert inst.interpretation[0].coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpre"
    "tation"
    )
    assert inst.interpretation[0].text == "Below low normal"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.note[0].text == (
    "In this example, the blood pressure measurements are not "
    "available due to cancellation of the order.  Data absent "
    "reason is present for each component"
    )
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.status == "cancelled"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_observation_6(base_settings):
    """No. 6 tests collection for Observation.
    Test File: observation-example-bloodpressure-cancel.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-bloodpressure-cancel.json"
    )
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
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/observation-category"
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "9279-1"
    assert inst.code.coding[0].display == "Respiratory rate"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Respiratory rate"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.id == "respiratory-rate"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "/min"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "breaths/minute"
    assert float(inst.valueQuantity.value) == float(26)


def test_observation_7(base_settings):
    """No. 7 tests collection for Observation.
    Test File: observation-example-respiratory-rate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-respiratory-rate.json"
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
    assert inst.code.coding[0].code == "1963-8"
    assert inst.code.coding[0].display == "Bicarbonate [Moles/?volume] in Serum"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.coding[1].code == "365722008"
    assert inst.code.coding[1].display == "Bicarbonate level"
    assert inst.code.coding[1].system == "http://snomed.info/sct"
    assert inst.id == "f203"
    assert inst.identifier[0].system == "https://intranet.aumc.nl/labvalues"
    assert inst.identifier[0].value == "1304-03720-Bicarbonate"
    assert inst.interpretation[0].coding[0].code == "166698001"
    assert inst.interpretation[0].coding[0].display == "Serum bicarbonate level normal"
    assert inst.interpretation[0].coding[0].system == "http://snomed.info/sct"
    assert inst.interpretation[0].coding[1].code == "N"
    assert inst.interpretation[0].coding[1].system == (
    "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpre"
    "tation"
    )
    assert inst.issued == fhirtypes.Instant.validate("2013-04-04T14:34:00+01:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.method.text == "enzymatic method"
    assert inst.performer[0].display == "Luigi Maas"
    assert inst.performer[0].reference == "Practitioner/f202"
    assert float(inst.referenceRange[0].high.value) == float(29)
    assert float(inst.referenceRange[0].low.value) == float(22)
    assert inst.referenceRange[0].type.coding[0].code == "normal"
    assert inst.referenceRange[0].type.coding[0].display == "Normal Range"
    assert inst.referenceRange[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/referencerange-meaning"
    assert inst.status == "final"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "258813002"
    assert inst.valueQuantity.system == "http://snomed.info/sct"
    assert inst.valueQuantity.unit == "mmol/L"
    assert float(inst.valueQuantity.value) == float(28)


def test_observation_8(base_settings):
    """No. 8 tests collection for Observation.
    Test File: observation-example-f203-bicarbonate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-f203-bicarbonate.json"
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
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/observation-category"
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
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "[lb_av]"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "lbs"
    assert float(inst.valueQuantity.value) == float(185)


def test_observation_9(base_settings):
    """No. 9 tests collection for Observation.
    Test File: observation-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example.json"
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
    assert inst.code.coding[0].code == "11555-0"
    assert inst.code.coding[0].display == "Base excess in Blood by calculation"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2013-04-02T10:30:10+01:00")
    assert inst.id == "f002"
    assert inst.identifier[0].system == "http://www.bmc.nl/zorgportal/identifiers/observations"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "6324"
    assert inst.interpretation[0].coding[0].code == "H"
    assert inst.interpretation[0].coding[0].display == "High"
    assert inst.interpretation[0].coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpre"
    "tation"
    )
    assert inst.issued == fhirtypes.Instant.validate("2013-04-03T15:30:10+01:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].display == "A. Langeveld"
    assert inst.performer[0].reference == "Practitioner/f005"
    assert inst.referenceRange[0].high.code == "mmol/L"
    assert inst.referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[0].high.unit == "mmol/l"
    assert float(inst.referenceRange[0].high.value) == float(11.2)
    assert inst.referenceRange[0].low.code == "mmol/L"
    assert inst.referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[0].low.unit == "mmol/l"
    assert float(inst.referenceRange[0].low.value) == float(7.1)
    assert inst.status == "final"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "mmol/L"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "mmol/l"
    assert float(inst.valueQuantity.value) == float(12.6)


def test_observation_10(base_settings):
    """No. 10 tests collection for Observation.
    Test File: observation-example-f002-excess.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-f002-excess.json"
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