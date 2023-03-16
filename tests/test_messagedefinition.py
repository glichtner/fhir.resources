# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import messagedefinition


def impl_messagedefinition_1(inst):
    assert inst.allowedResponse[0].message == "http://hl7.org/fhir/MessageDefinition/patient-link-response"
    assert inst.allowedResponse[0].situation == (
    "Optional response message that may provide additional "
    "information"
    )
    assert inst.base == "http://hl7.org/fhir/MessageDefinition/example"
    assert inst.category == "notification"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org"
    assert inst.copyright == "� HL7.org 2011+"
    assert inst.date == fhirtypes.DateTime.validate("2017-02-03")
    assert inst.description == (
    "Notification of two patient records that represent the same "
    "individual that require an established linkage."
    )
    assert inst.eventCoding.code == "admin-notify"
    assert inst.eventCoding.system == "http://example.org/fhir/message-events"
    assert inst.experimental is True
    assert inst.focus[0].code == "Patient"
    assert inst.focus[0].max == "2"
    assert inst.focus[0].min == 2
    assert inst.focus[0].profile == "http://hl7.org/fhir/StructureDefinition/example"
    assert inst.id == "patient-link-notification"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.15.2"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.name == "PATIENTLINKNOTIFICATION"
    assert inst.publisher == "Health Level Seven, Int'l"
    assert inst.purpose == (
    "Notifies recipient systems that two patients have been "
    "'linked' - meaning they represent the same individual"
    )
    assert inst.status == "draft"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Link Patients "
    "Notification</div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Link Patients Notification"
    assert inst.url == (
    "http://hl7.org/fhir/MessageDefinition/patient-link-"
    "notification"
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "positive"
    assert inst.useContext[0].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/variant-state"
    assert inst.version == "1"


def test_messagedefinition_1(base_settings):
    """No. 1 tests collection for MessageDefinition.
    Test File: messagedefinition-patient-link-notification.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "messagedefinition-patient-link-notification.json"
    )
    inst = messagedefinition.MessageDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MessageDefinition" == inst.resource_type

    impl_messagedefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MessageDefinition" == data["resourceType"]

    inst2 = messagedefinition.MessageDefinition(**data)
    impl_messagedefinition_1(inst2)


def impl_messagedefinition_2(inst):
    assert inst.base == "http://hl7.org/fhir/MessageDefinition/example"
    assert inst.category == "consequence"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org"
    assert inst.copyright == "� HL7.org 2011+"
    assert inst.date == fhirtypes.DateTime.validate("2017-02-03")
    assert inst.description == "Optional response to a patient link notification."
    assert inst.eventCoding.code == "admin-notify"
    assert inst.eventCoding.system == "http://example.org/fhir/message-events"
    assert inst.experimental is True
    assert inst.focus[0].code == "Patient"
    assert inst.focus[0].max == "2"
    assert inst.focus[0].min == 2
    assert inst.focus[0].profile == "http://hl7.org/fhir/StructureDefinition/example"
    assert inst.id == "patient-link-response"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.15.1"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.name == "PATIENTLINKRESPONSE"
    assert inst.publisher == "Health Level Seven, Int'l"
    assert inst.purpose == (
    "Optional response message that may provide additional "
    "information on the outcome of the patient link operation."
    )
    assert inst.status == "draft"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Link Patients "
    "Response</div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Link Patients Response"
    assert inst.url == "http://hl7.org/fhir/MessageDefinition/patient-link-response"
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "positive"
    assert inst.useContext[0].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/variant-state"
    assert inst.version == "1"


def test_messagedefinition_2(base_settings):
    """No. 2 tests collection for MessageDefinition.
    Test File: messagedefinition-patient-link-response.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "messagedefinition-patient-link-response.json"
    )
    inst = messagedefinition.MessageDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MessageDefinition" == inst.resource_type

    impl_messagedefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MessageDefinition" == data["resourceType"]

    inst2 = messagedefinition.MessageDefinition(**data)
    impl_messagedefinition_2(inst2)


def impl_messagedefinition_3(inst):
    assert inst.category == "notification"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2016-11-09")
    assert inst.description == "Message definition base example"
    assert inst.eventCoding.code == "admin-notify"
    assert inst.eventCoding.system == "http://example.org/fhir/message-events"
    assert inst.experimental is True
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.15.3"
    assert inst.name == "EXAMPLE"
    assert inst.publisher == "Health Level Seven, Int'l"
    assert inst.purpose == (
    "Defines a base example for other MessageDefinition "
    "instances."
    )
    assert inst.status == "draft"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Message "
    "definition base example</div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Message definition base example"
    assert inst.url == "http://hl7.org/fhir/MessageDefinition/example"


def test_messagedefinition_3(base_settings):
    """No. 3 tests collection for MessageDefinition.
    Test File: messagedefinition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "messagedefinition-example.json"
    )
    inst = messagedefinition.MessageDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MessageDefinition" == inst.resource_type

    impl_messagedefinition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MessageDefinition" == data["resourceType"]

    inst2 = messagedefinition.MessageDefinition(**data)
    impl_messagedefinition_3(inst2)