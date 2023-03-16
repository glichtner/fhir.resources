# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Appointment
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import appointment


def impl_appointment_1(inst):
    assert inst.appointmentType.coding[0].code == "FOLLOWUP"
    assert inst.appointmentType.coding[0].display == "A follow up visit from a previous appointment"
    assert inst.appointmentType.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0276"
    assert inst.description == "Discussion about Peter Chalmers ultrasound results"
    assert inst.end == fhirtypes.Instant.validate("2013-12-09T11:00:00Z")
    assert inst.id == "2docs"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.note[0].text == (
    "Clarify the results of the ultrasound to ensure context of "
    "test was correct"
    )
    assert inst.participant[0].actor.display == "Dr Adam Careful"
    assert inst.participant[0].actor.reference == "Practitioner/example"
    assert inst.participant[0].required is True
    assert inst.participant[0].status == "accepted"
    assert inst.participant[1].actor.display == "Luigi Maas"
    assert inst.participant[1].actor.reference == "Practitioner/f202"
    assert inst.participant[1].required is True
    assert inst.participant[1].status == "accepted"
    assert inst.serviceCategory[0].coding[0].code == "gp"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert inst.serviceCategory[0].coding[0].system == "http://example.org/service-category"
    assert inst.serviceType[0].concept.coding[0].code == "52"
    assert inst.serviceType[0].concept.coding[0].display == "General Discussion"
    assert inst.specialty[0].coding[0].code == "394814009"
    assert inst.specialty[0].coding[0].display == "General practice"
    assert inst.specialty[0].coding[0].system == "http://snomed.info/sct"
    assert inst.start == fhirtypes.Instant.validate("2013-12-09T09:00:00Z")
    assert inst.status == "booked"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.supportingInformation[0].reference == "DiagnosticReport/ultrasound"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Discussion of "
    "Peter's ultrasound results to plan ongoing treatment "
    "options</div>"
    )
    assert inst.text.status == "generated"


def test_appointment_1(base_settings):
    """No. 1 tests collection for Appointment.
    Test File: appointment-example2doctors.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "appointment-example2doctors.json"
    )
    inst = appointment.Appointment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Appointment" == inst.resource_type

    impl_appointment_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Appointment" == data["resourceType"]

    inst2 = appointment.Appointment(**data)
    impl_appointment_1(inst2)


def impl_appointment_2(inst):
    assert inst.appointmentType.coding[0].code == "FOLLOWUP"
    assert inst.appointmentType.coding[0].display == "A follow up visit from a previous appointment"
    assert inst.appointmentType.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0276"
    assert inst.basedOn[0].reference == "ServiceRequest/myringotomy"
    assert inst.class_fhir[0].coding[0].code == "AMB"
    assert inst.class_fhir[0].coding[0].display == "ambulatory"
    assert inst.class_fhir[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.created == fhirtypes.DateTime.validate("2013-10-10")
    assert inst.description == "Discussion on the results of your recent MRI"
    assert inst.end == fhirtypes.Instant.validate("2013-12-10T11:00:00Z")
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.note[0].text == (
    "Further expand on the results of the MRI and determine the "
    "next actions that may be appropriate."
    )
    assert inst.participant[0].actor.display == "Peter James Chalmers"
    assert inst.participant[0].actor.reference == "Patient/example"
    assert inst.participant[0].required is True
    assert inst.participant[0].status == "accepted"
    assert inst.participant[1].actor.display == "Dr Adam Careful"
    assert inst.participant[1].actor.reference == "Practitioner/example"
    assert inst.participant[1].required is True
    assert inst.participant[1].status == "accepted"
    assert inst.participant[1].type[0].coding[0].code == "ATND"
    assert inst.participant[1].type[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.participant[2].actor.display == "South Wing, second floor"
    assert inst.participant[2].actor.reference == "Location/1"
    assert inst.participant[2].required is True
    assert inst.participant[2].status == "accepted"
    assert inst.patientInstruction[0].concept.text == (
    "Please avoid excessive travel (specifically flying) before "
    "this appointment"
    )
    assert inst.reason[0].reference.display == "Severe burn of left ear"
    assert inst.reason[0].reference.reference == "Condition/example"
    assert inst.serviceCategory[0].coding[0].code == "gp"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert inst.serviceCategory[0].coding[0].system == "http://example.org/service-category"
    assert inst.serviceType[0].concept.coding[0].code == "52"
    assert inst.serviceType[0].concept.coding[0].display == "General Discussion"
    assert inst.specialty[0].coding[0].code == "394814009"
    assert inst.specialty[0].coding[0].display == "General practice"
    assert inst.specialty[0].coding[0].system == "http://snomed.info/sct"
    assert inst.start == fhirtypes.Instant.validate("2013-12-10T09:00:00Z")
    assert inst.status == "booked"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Brian MRI "
    "results discussion</div>"
    )
    assert inst.text.status == "generated"


def test_appointment_2(base_settings):
    """No. 2 tests collection for Appointment.
    Test File: appointment-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "appointment-example.json"
    )
    inst = appointment.Appointment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Appointment" == inst.resource_type

    impl_appointment_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Appointment" == data["resourceType"]

    inst2 = appointment.Appointment(**data)
    impl_appointment_2(inst2)


def impl_appointment_3(inst):
    assert inst.appointmentType.coding[0].code == "WALKIN"
    assert inst.appointmentType.coding[0].display == "A previously unscheduled walk-in visit"
    assert inst.appointmentType.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0276"
    assert inst.created == fhirtypes.DateTime.validate("2015-12-02")
    assert inst.description == "Discussion on the results of your recent MRI"
    assert inst.id == "examplereq"
    assert inst.identifier[0].system == "http://example.org/sampleappointment-identifier"
    assert inst.identifier[0].value == "123"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.minutesDuration == 15
    assert inst.note[0].text == (
    "Further expand on the results of the MRI and determine the "
    "next actions that may be appropriate."
    )
    assert inst.participant[0].actor.display == "Peter James Chalmers"
    assert inst.participant[0].actor.reference == "Patient/example"
    assert inst.participant[0].required is True
    assert inst.participant[0].status == "needs-action"
    assert inst.participant[1].required is True
    assert inst.participant[1].status == "needs-action"
    assert inst.participant[1].type[0].coding[0].code == "ATND"
    assert inst.participant[1].type[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    assert inst.participant[2].actor.display == "South Wing, second floor"
    assert inst.participant[2].actor.reference == "Location/1"
    assert inst.participant[2].required is True
    assert inst.participant[2].status == "accepted"
    assert inst.reason[0].concept.coding[0].code == "413095006"
    assert inst.reason[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].concept.text == "Clinical Review"
    assert inst.requestedPeriod[0].end == fhirtypes.DateTime.validate("2016-06-09")
    assert inst.requestedPeriod[0].start == fhirtypes.DateTime.validate("2016-06-02")
    assert inst.serviceCategory[0].coding[0].code == "gp"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert inst.serviceCategory[0].coding[0].system == "http://example.org/service-category"
    assert inst.slot[0].reference == "Slot/example"
    assert inst.specialty[0].coding[0].code == "394814009"
    assert inst.specialty[0].coding[0].display == "General practice"
    assert inst.specialty[0].coding[0].system == "http://snomed.info/sct"
    assert inst.status == "proposed"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Brian MRI "
    "results discussion</div>"
    )
    assert inst.text.status == "generated"


def test_appointment_3(base_settings):
    """No. 3 tests collection for Appointment.
    Test File: appointment-example-request.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "appointment-example-request.json"
    )
    inst = appointment.Appointment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Appointment" == inst.resource_type

    impl_appointment_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Appointment" == data["resourceType"]

    inst2 = appointment.Appointment(**data)
    impl_appointment_3(inst2)