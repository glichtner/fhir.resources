# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import conceptmap


def impl_conceptmap_1(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T05:55:11+00:00")
    assert inst.description == (
        'Canonical Mapping for "The verification status to support '
        "or decline the clinical status of the condition or "
        'diagnosis."'
    )
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "unconfirmed, provisional"
    assert inst.group[0].element[1].target[0].code == "unconfirmed"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "confirmed"
    assert inst.group[0].element[2].target[0].code == "confirmed"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "refuted"
    assert inst.group[0].element[3].target[0].code == "refuted"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].element[4].code == "differential"
    assert inst.group[0].element[4].target[0].code == "differential"
    assert inst.group[0].element[4].target[0].relationship == "equivalent"
    assert (
        inst.group[0].source
        == "http://terminology.hl7.org/CodeSystem/condition-ver-status"
    )
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-condition-ver-status"
    assert inst.name == "ConditionVerificationStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceCanonical == "http://hl7.org/fhir/ValueSet/condition-ver-status"
    assert inst.status == "draft"
    assert inst.targetCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "ConditionVerificationStatus"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-condition-ver-status"
    assert inst.version == "4.5.0"


def test_conceptmap_1(base_settings):
    """No. 1 tests collection for ConceptMap.
    Test File: sc-valueset-condition-ver-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-condition-ver-status.json"
    )
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_1(inst2)


def impl_conceptmap_2(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T05:55:11+00:00")
    assert inst.description == (
        'Canonical Mapping for "Indicates the state of the ' 'consent."'
    )
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "draft"
    assert inst.group[0].element[1].target[0].code == "draft"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "active"
    assert inst.group[0].element[2].target[0].code == "active"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "inactive"
    assert inst.group[0].element[3].target[0].code == "inactive"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].element[4].code == "unknown"
    assert inst.group[0].element[4].target[0].code == "unknown"
    assert inst.group[0].element[4].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/consent-state-codes"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-consent-state-codes"
    assert inst.name == "ConsentStateCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceCanonical == "http://hl7.org/fhir/ValueSet/consent-state-codes"
    assert inst.status == "draft"
    assert inst.targetCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "ConsentState"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-consent-state-codes"
    assert inst.version == "4.5.0"


def test_conceptmap_2(base_settings):
    """No. 2 tests collection for ConceptMap.
    Test File: sc-valueset-consent-state-codes.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-consent-state-codes.json"
    )
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_2(inst2)


def impl_conceptmap_3(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T05:55:11+00:00")
    assert inst.description == (
        'Canonical Mapping for "The Participation status of an ' 'appointment."'
    )
    assert inst.group[0].element[0].code == "tentative"
    assert inst.group[0].element[0].target[0].code == "draft"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "declined"
    assert inst.group[0].element[1].target[0].code == "declined"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "accepted"
    assert inst.group[0].element[2].target[0].code == "accepted"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "needs-action"
    assert inst.group[0].element[3].target[0].code == "failed"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/participationstatus"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-participationstatus"
    assert inst.name == "ParticipationStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceCanonical == "http://hl7.org/fhir/ValueSet/participationstatus"
    assert inst.status == "draft"
    assert inst.targetCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "ParticipationStatus"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-participationstatus"
    assert inst.version == "4.5.0"


def test_conceptmap_3(base_settings):
    """No. 3 tests collection for ConceptMap.
    Test File: sc-valueset-participationstatus.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-participationstatus.json"
    )
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_3(inst2)


def impl_conceptmap_4(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "completed"
    assert inst.group[0].element[1].target[0].code == "complete"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "not-done"
    assert inst.group[0].element[2].target[0].code == "abandoned"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/event-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-immunization-status"
    assert inst.name == "ImmunizationStatusCodesCanonicalMap"
    assert inst.publisher == "FHIR Project team"
    assert inst.sourceCanonical == "http://hl7.org/fhir/ValueSet/immunization-status"
    assert inst.status == "draft"
    assert inst.targetCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "Immunization Status Codes"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-immunization-status"
    assert inst.version == "4.5.0"


def test_conceptmap_4(base_settings):
    """No. 4 tests collection for ConceptMap.
    Test File: sc-valueset-immunization-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-immunization-status.json"
    )
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_4(inst2)


def impl_conceptmap_5(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == (
        'Canonical Mapping for "Preferred value set for Condition ' 'Clinical Status."'
    )
    assert inst.group[0].element[0].code == "active,recurrence,relapse"
    assert inst.group[0].element[0].target[0].code == "active"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "inactive,remission"
    assert inst.group[0].element[1].target[0].code == "suspended"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "resolved"
    assert inst.group[0].element[2].target[0].code == "failed"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert (
        inst.group[0].source
        == "http://terminology.hl7.org/CodeSystem/condition-clinical"
    )
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-condition-clinical"
    assert inst.name == "ConditionClinicalStatusCodesCanonicalMap"
    assert inst.publisher == "FHIR Project team"
    assert inst.sourceCanonical == "http://hl7.org/fhir/ValueSet/condition-clinical"
    assert inst.status == "draft"
    assert inst.targetCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "Condition Clinical Status Codes"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-condition-clinical"
    assert inst.version == "4.5.0"


def test_conceptmap_5(base_settings):
    """No. 5 tests collection for ConceptMap.
    Test File: sc-valueset-condition-clinical.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-condition-clinical.json"
    )
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_5(inst2)


def impl_conceptmap_6(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T05:55:11+00:00")
    assert inst.description == 'Canonical Mapping for "The status of the location."'
    assert inst.group[0].element[0].code == "planned"
    assert inst.group[0].element[0].target[0].code == "planned"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "reserved"
    assert inst.group[0].element[1].target[0].code == "accepted"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "active"
    assert inst.group[0].element[2].target[0].code == "active"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "completed"
    assert inst.group[0].element[3].target[0].code == "complete"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/encounter-location-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-encounter-location-status"
    assert inst.name == "EncounterLocationStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceCanonical == "http://hl7.org/fhir/ValueSet/encounter-location-status"
    )
    assert inst.status == "draft"
    assert inst.targetCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "EncounterLocationStatus"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-encounter-location-status"
    assert inst.version == "4.5.0"


def test_conceptmap_6(base_settings):
    """No. 6 tests collection for ConceptMap.
    Test File: sc-valueset-encounter-location-status.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "sc-valueset-encounter-location-status.json"
    )
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_6(inst2)


def impl_conceptmap_7(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert (
        inst.contact[0].telecom[0].value
        == "http://www.hl7.org/Special/committees/patientcare/"
    )
    assert inst.description == (
        'Canonical Mapping for "Describes the progression, or lack '
        'thereof, towards the goal against the target."'
    )
    assert (
        inst.group[0].element[0].code
        == "in-progress, sustaining, improving, worsening, no-change"
    )
    assert inst.group[0].element[0].target[0].code == "active"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "achieved"
    assert inst.group[0].element[1].target[0].code == "complete"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "not-attainable"
    assert inst.group[0].element[2].target[0].code == "abandoned"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "no-progress, not-achieved"
    assert inst.group[0].element[3].target[0].code == "not-done"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert (
        inst.group[0].source == "http://terminology.hl7.org/CodeSystem/goal-achievement"
    )
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-goal-achievement"
    assert inst.name == "GoalAchievementStatusCanonicalMap"
    assert inst.publisher == "HL7 International - Patient Care WG"
    assert inst.sourceCanonical == "http://hl7.org/fhir/ValueSet/goal-achievement"
    assert inst.status == "draft"
    assert inst.targetCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "GoalAchievementStatus"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-goal-achievement"
    assert inst.version == "4.5.0"


def test_conceptmap_7(base_settings):
    """No. 7 tests collection for ConceptMap.
    Test File: sc-valueset-goal-achievement.json
    """
    filename = base_settings["unittest_data_dir"] / "sc-valueset-goal-achievement.json"
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_7(inst2)


def impl_conceptmap_8(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T05:55:11+00:00")
    assert inst.description == (
        'Canonical Mapping for "Indicates the status of the care ' 'team."'
    )
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "proposed"
    assert inst.group[0].element[1].target[0].code == "proposed"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "active"
    assert inst.group[0].element[2].target[0].code == "active"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "suspended"
    assert inst.group[0].element[3].target[0].code == "suspended"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].element[4].code == "inactive"
    assert inst.group[0].element[4].target[0].code == "inactive"
    assert inst.group[0].element[4].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/care-team-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-care-team-status"
    assert inst.name == "CareTeamStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceCanonical == "http://hl7.org/fhir/ValueSet/care-team-status"
    assert inst.status == "draft"
    assert inst.targetCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "CareTeamStatus"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-care-team-status"
    assert inst.version == "4.5.0"


def test_conceptmap_8(base_settings):
    """No. 8 tests collection for ConceptMap.
    Test File: sc-valueset-care-team-status.json
    """
    filename = base_settings["unittest_data_dir"] / "sc-valueset-care-team-status.json"
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_8(inst2)


def impl_conceptmap_9(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T05:55:11+00:00")
    assert inst.description == (
        'Canonical Mapping for "Indicates whether this flag is '
        "active and needs to be displayed to a user, or whether it is"
        ' no longer needed or was entered in error."'
    )
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "active"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "inactive"
    assert inst.group[0].element[2].target[0].code == "inactive"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/flag-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-flag-status"
    assert inst.name == "FlagStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceCanonical == "http://hl7.org/fhir/ValueSet/flag-status"
    assert inst.status == "draft"
    assert inst.targetCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "FlagStatus"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-flag-status"
    assert inst.version == "4.5.0"


def test_conceptmap_9(base_settings):
    """No. 9 tests collection for ConceptMap.
    Test File: sc-valueset-flag-status.json
    """
    filename = base_settings["unittest_data_dir"] / "sc-valueset-flag-status.json"
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_9(inst2)


def impl_conceptmap_10(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "completed"
    assert inst.group[0].element[1].target[0].code == "complete"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert (
        inst.group[0].source == "http://hl7.org/fhir/CodeSystem/medication-admin-status"
    )
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-immunization-evaluation-status"
    assert inst.name == "ImmunizationEvaluationStatusCodesCanonicalMap"
    assert inst.publisher == "FHIR Project team"
    assert (
        inst.sourceCanonical
        == "http://hl7.org/fhir/ValueSet/immunization-evaluation-status"
    )
    assert inst.status == "draft"
    assert inst.targetCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == (
        'Canonical Mapping for "Immunization Evaluation Status ' 'Codes"'
    )
    assert inst.url == (
        "http://hl7.org/fhir/ConceptMap/sc-immunization-evaluation-" "status"
    )
    assert inst.version == "4.5.0"


def test_conceptmap_10(base_settings):
    """No. 10 tests collection for ConceptMap.
    Test File: sc-valueset-immunization-evaluation-status.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "sc-valueset-immunization-evaluation-status.json"
    )
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_10(inst2)
