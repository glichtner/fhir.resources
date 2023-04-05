# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Encounter
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import encounter


def impl_encounter_1(inst):
    assert inst.class_fhir[0].coding[0].code == "IMP"
    assert inst.class_fhir[0].coding[0].display == "inpatient encounter"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.id == "denovoEncounter"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "in-progress"
    assert inst.subject.reference == "Patient/denovoChild"
    assert inst.text.status == "generated"


def test_encounter_1(base_settings):
    """No. 1 tests collection for Encounter.
    Test File: Encounter-denovoEncounter.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Encounter-denovoEncounter.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_1(inst2)


def impl_encounter_2(inst):
    assert inst.admission.admitSource.coding[0].code == "305956004"
    assert inst.admission.admitSource.coding[0].display == "Referral by physician"
    assert inst.admission.admitSource.coding[0].system == "http://snomed.info/sct"
    assert inst.admission.dischargeDisposition.coding[0].code == "306689006"
    assert inst.admission.dischargeDisposition.coding[0].display == "Discharge to home"
    assert inst.admission.dischargeDisposition.coding[0].system == "http://snomed.info/sct"
    assert inst.admission.preAdmissionIdentifier.system == "http://www.bmc.nl/zorgportal/identifiers/pre-admissions"
    assert inst.admission.preAdmissionIdentifier.use == "official"
    assert inst.admission.preAdmissionIdentifier.value == "93042"
    assert inst.class_fhir[0].coding[0].code == "AMB"
    assert inst.class_fhir[0].coding[0].display == "ambulatory"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.id == "f003"
    assert inst.identifier[0].system == "http://www.bmc.nl/zorgportal/identifiers/encounters"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v6751"
    assert inst.length.code == "min"
    assert inst.length.system == "http://unitsofmeasure.org"
    assert inst.length.unit == "min"
    assert float(inst.length.value) == float(90)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.participant[0].actor.display == "E.M. van den Broek"
    assert inst.participant[0].actor.reference == "Practitioner/f001"
    assert inst.priority.coding[0].code == "103391001"
    assert inst.priority.coding[0].display == "Non-urgent ear, nose and throat admission"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].value[0].concept.coding[0].code == "18099001"
    assert inst.reason[0].value[0].concept.coding[0].display == "Retropharyngeal abscess"
    assert inst.reason[0].value[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.serviceProvider.reference == "Organization/f001"
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "270427003"
    assert inst.type[0].coding[0].display == "Patient-initiated encounter"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_2(base_settings):
    """No. 2 tests collection for Encounter.
    Test File: encounter-example-f003-abscess.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f003-abscess.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_2(inst2)


def impl_encounter_3(inst):
    assert inst.class_fhir[0].coding[0].code == "AMB"
    assert inst.class_fhir[0].coding[0].display == "ambulatory"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.diagnosis[0].condition[0].concept.text == (
    "Complications from Roel's TPF chemotherapy on January 28th, "
    "2013"
    )
    assert inst.diagnosis[0].use[0].coding[0].code == "AD"
    assert inst.diagnosis[0].use[0].coding[0].display == "Admission diagnosis"
    assert inst.diagnosis[0].use[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/diagnosis-role"
    assert inst.diagnosis[1].condition[0].concept.text == "The patient is treated for a tumor"
    assert inst.diagnosis[1].use[0].coding[0].code == "CC"
    assert inst.diagnosis[1].use[0].coding[0].display == "Chief complaint"
    assert inst.diagnosis[1].use[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/diagnosis-role"
    assert inst.id == "f202"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130128"
    assert inst.length.code == "min"
    assert inst.length.system == "http://unitsofmeasure.org"
    assert inst.length.unit == "minutes"
    assert float(inst.length.value) == float(56)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.participant[0].actor.reference == "Practitioner/f201"
    assert inst.priority.coding[0].code == "103391001"
    assert inst.priority.coding[0].display == "Urgent"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].value[0].concept.text == "The patient is treated for a tumor."
    assert inst.serviceProvider.reference == "Organization/f201"
    assert inst.status == "completed"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "367336001"
    assert inst.type[0].coding[0].display == "Chemotherapy"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_3(base_settings):
    """No. 3 tests collection for Encounter.
    Test File: encounter-example-f202-20130128.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f202-20130128.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_3(inst2)


def impl_encounter_4(inst):
    assert inst.class_fhir[0].coding[0].code == "AMB"
    assert inst.class_fhir[0].coding[0].display == "ambulatory"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.id == "f201"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130404"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.participant[0].actor.reference == "Practitioner/f201"
    assert inst.priority.coding[0].code == "17621005"
    assert inst.priority.coding[0].display == "Normal"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].value[0].concept.text == (
    "The patient had fever peaks over the last couple of days. He"
    " is worried about these peaks."
    )
    assert inst.serviceProvider.reference == "Organization/f201"
    assert inst.status == "completed"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "11429006"
    assert inst.type[0].coding[0].display == "Consultation"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_4(base_settings):
    """No. 4 tests collection for Encounter.
    Test File: encounter-example-f201-20130404.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f201-20130404.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_4(inst2)


def impl_encounter_5(inst):
    assert inst.actualPeriod.start == fhirtypes.DateTime.validate("2017-02-01T07:15:00+10:00")
    assert inst.admission.admitSource.coding[0].code == "emd"
    assert inst.admission.admitSource.coding[0].display == "From accident/emergency department"
    assert inst.admission.admitSource.coding[0].system == "http://terminology.hl7.org/CodeSystem/admit-source"
    assert inst.class_fhir[0].coding[0].code == "IMP"
    assert inst.class_fhir[0].coding[0].display == "inpatient encounter"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.id == "emerg"
    assert inst.location[0].location.display == "Emergency Waiting Room"
    assert inst.location[0].period.end == fhirtypes.DateTime.validate("2017-02-01T08:45:00+10:00")
    assert inst.location[0].period.start == fhirtypes.DateTime.validate("2017-02-01T07:15:00+10:00")
    assert inst.location[0].status == "active"
    assert inst.location[1].location.display == "Emergency"
    assert inst.location[1].period.end == fhirtypes.DateTime.validate("2017-02-01T09:27:00+10:00")
    assert inst.location[1].period.start == fhirtypes.DateTime.validate("2017-02-01T08:45:00+10:00")
    assert inst.location[1].status == "active"
    assert inst.location[2].location.display == "Ward 1, Room 42, Bed 1"
    assert inst.location[2].period.end == fhirtypes.DateTime.validate("2017-02-01T12:15:00+10:00")
    assert inst.location[2].period.start == fhirtypes.DateTime.validate("2017-02-01T09:27:00+10:00")
    assert inst.location[2].status == "active"
    assert inst.location[3].location.display == "Ward 1, Room 42, Bed 1"
    assert inst.location[3].period.end == fhirtypes.DateTime.validate("2017-02-01T12:45:00+10:00")
    assert inst.location[3].period.start == fhirtypes.DateTime.validate("2017-02-01T12:15:00+10:00")
    assert inst.location[3].status == "reserved"
    assert inst.location[4].location.display == "Ward 1, Room 42, Bed 1"
    assert inst.location[4].period.start == fhirtypes.DateTime.validate("2017-02-01T12:45:00+10:00")
    assert inst.location[4].status == "active"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "in-progress"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Emergency visit "
    "that escalated into inpatient patient @example</div>"
    )
    assert inst.text.status == "generated"


def test_encounter_5(base_settings):
    """No. 5 tests collection for Encounter.
    Test File: encounter-example-emerg.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-emerg.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_5(inst2)


def impl_encounter_6(inst):
    assert inst.actualPeriod.end == fhirtypes.DateTime.validate("2013-03-20")
    assert inst.actualPeriod.start == fhirtypes.DateTime.validate("2013-03-11")
    assert inst.class_fhir[0].coding[0].code == "IMP"
    assert inst.class_fhir[0].coding[0].display == "inpatient encounter"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.id == "colonoscopy"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.participant[0].actor.display == "Dr Adam Careful"
    assert inst.participant[0].actor.reference == "Practitioner/example"
    assert inst.participant[0].type[0].coding[0].code == "PART"
    assert inst.participant[0].type[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.reason[0].value[0].concept.text == "Routine investigation"
    assert inst.serviceProvider.display == "Gastroenterology @ Acme Hospital"
    assert inst.serviceProvider.reference == "Organization/1"
    assert inst.status == "completed"
    assert inst.subject.display == "Henry Levin the 7th"
    assert inst.subject.reference == "Patient/glossy"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "73761001"
    assert inst.type[0].coding[0].display == "Colonoscopy (procedure)"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"
    assert inst.type[0].text == "Colonoscopy"


def test_encounter_6(base_settings):
    """No. 6 tests collection for Encounter.
    Test File: encounter-example-colonoscopy.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-colonoscopy.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_6(inst2)


def impl_encounter_7(inst):
    assert inst.actualPeriod.end == fhirtypes.DateTime.validate("2015-01-17T16:30:00+10:00")
    assert inst.actualPeriod.start == fhirtypes.DateTime.validate("2015-01-17T16:00:00+10:00")
    assert inst.class_fhir[0].coding[0].code == "HH"
    assert inst.class_fhir[0].coding[0].display == "home health"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.contained[0].id == "home"
    assert inst.id == "home"
    assert inst.location[0].location.display == "Client's home"
    assert inst.location[0].location.reference == "#home"
    assert inst.location[0].period.end == fhirtypes.DateTime.validate("2015-01-17T16:30:00+10:00")
    assert inst.location[0].period.start == fhirtypes.DateTime.validate("2015-01-17T16:00:00+10:00")
    assert inst.location[0].status == "completed"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.participant[0].actor.display == "Dr Adam Careful"
    assert inst.participant[0].actor.reference == "Practitioner/example"
    assert inst.participant[0].period.end == fhirtypes.DateTime.validate("2015-01-17T16:30:00+10:00")
    assert inst.participant[0].period.start == fhirtypes.DateTime.validate("2015-01-17T16:00:00+10:00")
    assert inst.participant[0].type[0].coding[0].code == "PPRF"
    assert inst.participant[0].type[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.participant[1].actor.reference == "Patient/example"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Encounter with "
    "patient @example who is at home</div>"
    )
    assert inst.text.status == "generated"


def test_encounter_7(base_settings):
    """No. 7 tests collection for Encounter.
    Test File: encounter-example-home.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-home.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_7(inst2)


def impl_encounter_8(inst):
    assert inst.admission.admitSource.coding[0].code == "305956004"
    assert inst.admission.admitSource.coding[0].display == "Referral by physician"
    assert inst.admission.admitSource.coding[0].system == "http://snomed.info/sct"
    assert inst.admission.dischargeDisposition.coding[0].code == "306689006"
    assert inst.admission.dischargeDisposition.coding[0].display == "Discharge to home"
    assert inst.admission.dischargeDisposition.coding[0].system == "http://snomed.info/sct"
    assert inst.admission.preAdmissionIdentifier.system == "http://www.amc.nl/zorgportal/identifiers/pre-admissions"
    assert inst.admission.preAdmissionIdentifier.use == "official"
    assert inst.admission.preAdmissionIdentifier.value == "93042"
    assert inst.class_fhir[0].coding[0].code == "AMB"
    assert inst.class_fhir[0].coding[0].display == "ambulatory"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.id == "f001"
    assert inst.identifier[0].system == "http://www.amc.nl/zorgportal/identifiers/visits"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v1451"
    assert inst.length.code == "min"
    assert inst.length.system == "http://unitsofmeasure.org"
    assert inst.length.unit == "min"
    assert float(inst.length.value) == float(140)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.participant[0].actor.display == "P. Voigt"
    assert inst.participant[0].actor.reference == "Practitioner/f002"
    assert inst.priority.coding[0].code == "310361003"
    assert inst.priority.coding[0].display == "Non-urgent cardiological admission"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].value[0].concept.coding[0].code == "34068001"
    assert inst.reason[0].value[0].concept.coding[0].display == "Heart valve replacement"
    assert inst.reason[0].value[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.serviceProvider.display == "Burgers University Medical Center"
    assert inst.serviceProvider.reference == "Organization/f001"
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "270427003"
    assert inst.type[0].coding[0].display == "Patient-initiated encounter"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_8(base_settings):
    """No. 8 tests collection for Encounter.
    Test File: encounter-example-f001-heart.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f001-heart.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_8(inst2)


def impl_encounter_9(inst):
    assert inst.account[0].reference == "Account/example"
    assert inst.actualPeriod.end == fhirtypes.DateTime.validate("2013-03-20")
    assert inst.actualPeriod.start == fhirtypes.DateTime.validate("2013-03-11")
    assert inst.admission.admitSource.coding[0].code == "309902002"
    assert inst.admission.admitSource.coding[0].display == "Clinical Oncology Department"
    assert inst.admission.admitSource.coding[0].system == "http://snomed.info/sct"
    assert inst.admission.destination.reference == "Location/2"
    assert inst.admission.origin.reference == "Location/2"
    assert inst.admission.reAdmission.coding[0].display == "readmitted"
    assert inst.appointment[0].reference == "Appointment/example"
    assert inst.basedOn[0].reference == "ServiceRequest/myringotomy"
    assert inst.class_fhir[0].coding[0].code == "IMP"
    assert inst.class_fhir[0].coding[0].display == "inpatient encounter"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.diagnosis[0].condition[0].reference.reference == "Condition/stroke"
    assert inst.diagnosis[0].use[0].coding[0].code == "AD"
    assert inst.diagnosis[0].use[0].coding[0].display == "Admission diagnosis"
    assert inst.diagnosis[0].use[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/diagnosis-role"
    assert inst.diagnosis[1].condition[0].reference.reference == "Condition/f201"
    assert inst.diagnosis[1].use[0].coding[0].code == "DD"
    assert inst.diagnosis[1].use[0].coding[0].display == "Discharge diagnosis"
    assert inst.diagnosis[1].use[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/diagnosis-role"
    assert inst.dietPreference[0].coding[0].code == "276026009"
    assert inst.dietPreference[0].coding[0].display == "Fluid balance regulation"
    assert inst.dietPreference[0].coding[0].system == "http://snomed.info/sct"
    assert inst.episodeOfCare[0].reference == "EpisodeOfCare/example"
    assert inst.id == "f203"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130311"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.partOf.reference == "Encounter/f203"
    assert inst.participant[0].actor.reference == "Practitioner/f201"
    assert inst.participant[0].type[0].coding[0].code == "PART"
    assert inst.participant[0].type[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.priority.coding[0].code == "394849002"
    assert inst.priority.coding[0].display == "High priority"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].value[0].concept.text == (
    "The patient seems to suffer from bilateral pneumonia and "
    "renal insufficiency, most likely due to chemotherapy."
    )
    assert inst.serviceProvider.reference == "Organization/2"
    assert inst.specialArrangement[0].coding[0].code == "wheel"
    assert inst.specialArrangement[0].coding[0].display == "Wheelchair"
    assert inst.specialArrangement[0].coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/encounter-special-"
    "arrangements"
    )
    assert inst.specialCourtesy[0].coding[0].code == "NRM"
    assert inst.specialCourtesy[0].coding[0].display == "normal courtesy"
    assert inst.specialCourtesy[0].coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/v3-EncounterSpecialCou"
    "rtesy"
    )
    assert inst.status == "completed"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "183807002"
    assert inst.type[0].coding[0].display == "Inpatient stay for nine days"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_9(base_settings):
    """No. 9 tests collection for Encounter.
    Test File: encounter-example-f203-20130311.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f203-20130311.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_9(inst2)


def impl_encounter_10(inst):
    assert inst.careTeam[0].reference == "Encounter/example"
    assert inst.class_fhir[0].coding[0].code == "IMP"
    assert inst.class_fhir[0].coding[0].display == "inpatient encounter"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "in-progress"
    assert inst.subject.reference == "Patient/example"
    assert inst.subjectStatus.coding[0].code == "receiving-care"
    assert inst.subjectStatus.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/encounter-subject-"
    "status"
    )
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Encounter with "
    "patient @example</div>"
    )
    assert inst.text.status == "generated"


def test_encounter_10(base_settings):
    """No. 10 tests collection for Encounter.
    Test File: encounter-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_10(inst2)