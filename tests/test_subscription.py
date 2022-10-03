# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Subscription
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import subscription


def impl_subscription_1(inst):
    assert inst.channelType.code == "rest-hook"
    assert inst.content == "id-only"
    assert inst.contentType == "application/fhir+json"
    assert inst.end == fhirtypes.Instant.validate("2019-08-07T11:15:18Z")
    assert inst.endpoint == "https://example.org/Endpoints/P123"
    assert inst.filterBy[0].filterParameter == "patient"
    assert inst.filterBy[0].value == "Patient/123"
    assert inst.header[0] == "Authorization: Bearer secret-token-abc-123"
    assert inst.heartbeatPeriod == 60
    assert inst.id == "admission"
    assert inst.maxCount == 100
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "AdmissionExample"
    assert inst.reason == (
    "subscription for beginning of a clinical encounter for "
    "patient 123"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.timeout == 5
    assert inst.topic == "http://example.org/R5/SubscriptionTopic/admission"


def test_subscription_1(base_settings):
    """No. 1 tests collection for Subscription.
    Test File: subscription-admission.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "subscription-admission.json"
    )
    inst = subscription.Subscription.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Subscription" == inst.resource_type

    impl_subscription_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Subscription" == data["resourceType"]

    inst2 = subscription.Subscription(**data)
    impl_subscription_1(inst2)