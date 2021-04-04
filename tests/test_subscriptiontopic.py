# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubscriptionTopic
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import subscriptiontopic


def impl_subscriptiontopic_1(inst):
    assert inst.id == "admission"
    assert inst.resourceTrigger[0].canFilterBy[0].documentation == (
        "Matching based on the Patient (subject) of an Encounter or "
        "based on the Patient's group membership (in/not-in)."
    )
    assert inst.resourceTrigger[0].canFilterBy[0].searchModifier[0] == "="
    assert inst.resourceTrigger[0].canFilterBy[0].searchModifier[1] == "in"
    assert inst.resourceTrigger[0].canFilterBy[0].searchModifier[2] == "not-in"
    assert inst.resourceTrigger[0].canFilterBy[0].searchParamName == "patient"
    assert inst.resourceTrigger[0].description == "Beginning of a clinical encounter"
    assert inst.resourceTrigger[0].fhirPathCriteria[0] == (
        "%previous.status!='in-progress' and %current.status='in-" "progress'"
    )
    assert inst.resourceTrigger[0].queryCriteria.current == "status=in-progress"
    assert inst.resourceTrigger[0].queryCriteria.previous == "status:not=in-progress"
    assert inst.resourceTrigger[0].queryCriteria.requireBoth is True
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "admission"
    assert inst.url == (
        "http://argonautproject.org/subscription-" "ig/SubscriptionTopic/admission"
    )


def test_subscriptiontopic_1(base_settings):
    """No. 1 tests collection for SubscriptionTopic.
    Test File: subscriptiontopic-example-admission.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "subscriptiontopic-example-admission.json"
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
