# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubscriptionTopic
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import subscriptiontopic


def impl_subscriptiontopic_1(inst):
    assert inst.canFilterBy[0].description == "Filter based on the subject of an encounter."
    assert inst.canFilterBy[0].filterParameter == "subject"
    assert inst.canFilterBy[0].resource == "Encounter"
    assert inst.canFilterBy[1].description == (
    "Filter based on the group membership of the subject of an "
    "encounter."
    )
    assert inst.canFilterBy[1].filterParameter == "_in"
    assert inst.canFilterBy[1].resource == "Encounter"
    assert inst.canFilterBy[2].comparator[0] == "gt"
    assert inst.canFilterBy[2].comparator[1] == "lt"
    assert inst.canFilterBy[2].comparator[2] == "ge"
    assert inst.canFilterBy[2].comparator[3] == "le"
    assert inst.canFilterBy[2].description == "Filter based on the length of an encounter."
    assert inst.canFilterBy[2].filterParameter == "length"
    assert inst.canFilterBy[2].resource == "Encounter"
    assert inst.canFilterBy[3].description == "Filter based on the account for billing an encounter."
    assert inst.canFilterBy[3].filterParameter == "account"
    assert inst.canFilterBy[3].modifier[0] == "missing"
    assert inst.canFilterBy[3].modifier[1] == "not"
    assert inst.canFilterBy[3].modifier[2] == "identifier"
    assert inst.canFilterBy[3].resource == "Encounter"
    assert inst.date == fhirtypes.DateTime.validate("2019-01-01")
    assert inst.description == "Example topic for completed encounters"
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:uuid:1caa02ba-051b-4602-8856-65921748ae76"
    assert inst.notificationShape[0].include[0] == "Encounter:patient&iterate=Patient.link"
    assert inst.notificationShape[0].include[1] == "Encounter:practitioner"
    assert inst.notificationShape[0].include[2] == "Encounter:service-provider"
    assert inst.notificationShape[0].include[3] == "Encounter:account"
    assert inst.notificationShape[0].include[4] == "Encounter:diagnosis"
    assert inst.notificationShape[0].include[5] == "Encounter:observation"
    assert inst.notificationShape[0].include[6] == "Encounter:location"
    assert inst.notificationShape[0].resource == "Encounter"
    assert inst.resourceTrigger[0].description == "An Encounter has been completed"
    assert inst.resourceTrigger[0].fhirPathCriteria == (
    "(%previous.empty() | (%previous.status != 'completed')) and "
    "(%current.status = 'completed')"
    )
    assert inst.resourceTrigger[0].queryCriteria.current == "status=completed"
    assert inst.resourceTrigger[0].queryCriteria.previous == "status:not=completed"
    assert inst.resourceTrigger[0].queryCriteria.requireBoth is True
    assert inst.resourceTrigger[0].queryCriteria.resultForCreate == "test-passes"
    assert inst.resourceTrigger[0].queryCriteria.resultForDelete == "test-fails"
    assert inst.resourceTrigger[0].resource == "http://hl7.org/fhir/StructureDefinition/Encounter"
    assert inst.resourceTrigger[0].supportedInteraction[0] == "update"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "example"
    assert inst.url == "http://example.org/FHIR/R5/SubscriptionTopic/example"
    assert inst.version == "1.0.0-beta.1"


def test_subscriptiontopic_1(base_settings):
    """No. 1 tests collection for SubscriptionTopic.
    Test File: subscriptiontopic-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "subscriptiontopic-example.json"
    )
    inst = subscriptiontopic.SubscriptionTopic.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubscriptionTopic" == inst.resource_type

    impl_subscriptiontopic_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubscriptionTopic" == data["resourceType"]

    inst2 = subscriptiontopic.SubscriptionTopic(**data)
    impl_subscriptiontopic_1(inst2)


def impl_subscriptiontopic_2(inst):
    assert inst.canFilterBy[0].description == (
    "Matching based on the Patient (subject) of an Encounter or "
    "based on the Patient's group membership (in/not-in)."
    )
    assert inst.canFilterBy[0].filterParameter == "patient"
    assert inst.canFilterBy[0].modifier[0] == "in"
    assert inst.canFilterBy[0].modifier[1] == "not-in"
    assert inst.canFilterBy[0].resource == "Encounter"
    assert inst.description == "Example admission topic"
    assert inst.eventTrigger[0].description == "Patient admission is covered by HL7v2 ADT^A01"
    assert inst.eventTrigger[0].event.coding[0].code == "A01"
    assert inst.eventTrigger[0].event.coding[0].display == "ADT/ACK - Admit/visit notification"
    assert inst.eventTrigger[0].event.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0003"
    assert inst.eventTrigger[0].resource == "http://hl7.org/fhir/StructureDefinition/Encounter"
    assert inst.id == "admission"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:uuid:915c2040-b0a8-4935-adf8-94d6e1a74052"
    assert inst.notificationShape[0].include[0] == "Encounter:patient"
    assert inst.notificationShape[0].include[1] == "Encounter:practitioner"
    assert inst.notificationShape[0].include[2] == "Encounter:service-provider"
    assert inst.notificationShape[0].include[3] == "Encounter:account"
    assert inst.notificationShape[0].include[4] == "Encounter:diagnosis"
    assert inst.notificationShape[0].include[5] == "Encounter:observation"
    assert inst.notificationShape[0].include[6] == "Encounter:location"
    assert inst.notificationShape[0].resource == "Encounter"
    assert inst.resourceTrigger[0].description == "Encounter resource moving to state 'in-progress'"
    assert inst.resourceTrigger[0].fhirPathCriteria == (
    "%previous.status!='in-progress' and %current.status='in-"
    "progress'"
    )
    assert inst.resourceTrigger[0].queryCriteria.current == "status=in-progress"
    assert inst.resourceTrigger[0].queryCriteria.previous == "status:not=in-progress"
    assert inst.resourceTrigger[0].queryCriteria.requireBoth is True
    assert inst.resourceTrigger[0].queryCriteria.resultForCreate == "test-passes"
    assert inst.resourceTrigger[0].queryCriteria.resultForDelete == "test-fails"
    assert inst.resourceTrigger[0].resource == "http://hl7.org/fhir/StructureDefinition/Encounter"
    assert inst.resourceTrigger[0].supportedInteraction[0] == "create"
    assert inst.resourceTrigger[0].supportedInteraction[1] == "update"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "admission"
    assert inst.url == "http://example.org/FHIR/R5/SubscriptionTopic/admission"


def test_subscriptiontopic_2(base_settings):
    """No. 2 tests collection for SubscriptionTopic.
    Test File: subscriptiontopic-example-admission.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "subscriptiontopic-example-admission.json"
    )
    inst = subscriptiontopic.SubscriptionTopic.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubscriptionTopic" == inst.resource_type

    impl_subscriptiontopic_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubscriptionTopic" == data["resourceType"]

    inst2 = subscriptiontopic.SubscriptionTopic(**data)
    impl_subscriptiontopic_2(inst2)