# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubscriptionStatus
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import subscriptionstatus


def impl_subscriptionstatus_1(inst):
    # Don't know how to create unit test
    # for "eventsSinceSubscriptionStart",
    # which is a Integer64
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    # Don't know how to create unit test
    # for "notificationEvent[0].eventNumber",
    # which is a Integer64
    assert inst.status == "active"
    assert inst.subscription.reference == "http://example.org/FHIR/R5/Subscription/123"
    assert inst.text.status == "generated"
    assert inst.topic == "http://example.org/FHIR/R5/SubscriptionTopic/admission"
    assert inst.type == "event-notification"


def test_subscriptionstatus_1(base_settings):
    """No. 1 tests collection for SubscriptionStatus.
    Test File: subscriptionstatus-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "subscriptionstatus-example.json"
    )
    inst = subscriptionstatus.SubscriptionStatus.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubscriptionStatus" == inst.resource_type

    impl_subscriptionstatus_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubscriptionStatus" == data["resourceType"]

    inst2 = subscriptionstatus.SubscriptionStatus(**data)
    impl_subscriptionstatus_1(inst2)