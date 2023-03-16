# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import codesystem


def impl_codesystem_1(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "lost"
    assert inst.concept[0].definition == "The device is lost."
    assert inst.concept[0].display == "Lost"
    assert inst.concept[1].code == "damaged"
    assert inst.concept[1].definition == "The device is damaged."
    assert inst.concept[1].display == "Damaged"
    assert inst.concept[2].code == "destroyed"
    assert inst.concept[2].definition == "The device is destroyed."
    assert inst.concept[2].display == "Destroyed"
    assert inst.concept[3].code == "available"
    assert inst.concept[3].definition == "The device is available."
    assert inst.concept[3].display == "Available"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == "The record status of the device."
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "oo"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "device-availability-status"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.2048"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-01T23:03:57.298+11:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    assert inst.name == "FHIRDeviceAvailabilityStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR Device Availability Status"
    assert inst.url == "http://hl7.org/fhir/device-availability-status"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/device-availability-status"
    assert inst.version == "5.0.0-draft-final"


def test_codesystem_1(base_settings):
    """No. 1 tests collection for CodeSystem.
    Test File: codesystem-device-availability-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-device-availability-status.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_1(inst2)


def impl_codesystem_2(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "snapshot"
    assert inst.concept[0].definition == (
    "The inventory report is a current absolute snapshot, i.e. it"
    " represents the quantities at hand."
    )
    assert inst.concept[0].display == "Snapshot"
    assert inst.concept[1].code == "difference"
    assert inst.concept[1].definition == (
    "The inventory report is about the difference between a "
    "previous count and a current count, i.e. it represents the "
    "items that have been added/subtracted from inventory."
    )
    assert inst.concept[1].display == "Difference"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == "The type of count."
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "oo"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 0
    assert inst.id == "inventoryreport-counttype"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.1926"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-01T23:03:57.298+11:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    assert inst.name == "InventoryCountType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Inventory Count Type"
    assert inst.url == "http://hl7.org/fhir/inventoryreport-counttype"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/inventoryreport-counttype"
    assert inst.version == "5.0.0-draft-final"


def test_codesystem_2(base_settings):
    """No. 2 tests collection for CodeSystem.
    Test File: codesystem-inventoryreport-counttype.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-inventoryreport-counttype.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_2(inst2)


def impl_codesystem_3(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "high"
    assert inst.concept[0].definition == "High quality evidence."
    assert inst.concept[0].display == "High quality"
    assert inst.concept[1].code == "moderate"
    assert inst.concept[1].definition == "Moderate quality evidence."
    assert inst.concept[1].display == "Moderate quality"
    assert inst.concept[2].code == "low"
    assert inst.concept[2].definition == "Low quality evidence."
    assert inst.concept[2].display == "Low quality"
    assert inst.concept[3].code == "very-low"
    assert inst.concept[3].definition == "Very low quality evidence."
    assert inst.concept[3].display == "Very low quality"
    assert inst.concept[4].code == "no-concern"
    assert inst.concept[4].definition == "no serious concern."
    assert inst.concept[4].display == "no serious concern"
    assert inst.concept[5].code == "serious-concern"
    assert inst.concept[5].definition == "serious concern."
    assert inst.concept[5].display == "serious concern"
    assert inst.concept[6].code == "very-serious-concern"
    assert inst.concept[6].definition == "very serious concern."
    assert inst.concept[6].display == "very serious concern"
    assert inst.concept[7].code == "extremely-serious-concern"
    assert inst.concept[7].definition == "extremely serious concern."
    assert inst.concept[7].display == "extremely serious concern"
    assert inst.concept[8].code == "present"
    assert inst.concept[8].definition == (
    "possible reason for increasing quality rating was checked "
    "and found to be present."
    )
    assert inst.concept[8].display == "present"
    assert inst.concept[9].code == "absent"
    assert inst.concept[9].definition == (
    "possible reason for increasing quality rating was checked "
    "and found to be absent."
    )
    assert inst.concept[9].display == "absent"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == "The assessment of quality, confidence, or certainty."
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "cds"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "certainty-rating"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.1941"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-01T23:03:57.298+11:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    assert inst.name == "EvidenceCertaintyRating"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Evidence Certainty Rating"
    assert inst.url == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/certainty-rating"
    assert inst.version == "5.0.0-draft-final"


def test_codesystem_3(base_settings):
    """No. 3 tests collection for CodeSystem.
    Test File: codesystem-certainty-rating.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-certainty-rating.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_3(inst2)


def impl_codesystem_4(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "first"
    assert inst.concept[0].definition == "Only process this rule for the first in the list."
    assert inst.concept[0].display == "First"
    assert inst.concept[1].code == "not_first"
    assert inst.concept[1].definition == "Process this rule for all but the first."
    assert inst.concept[1].display == "All but the first"
    assert inst.concept[2].code == "last"
    assert inst.concept[2].definition == "Only process this rule for the last in the list."
    assert inst.concept[2].display == "Last"
    assert inst.concept[3].code == "not_last"
    assert inst.concept[3].definition == "Process this rule for all but the last."
    assert inst.concept[3].display == "All but the last"
    assert inst.concept[4].code == "only_one"
    assert inst.concept[4].definition == "Only process this rule is there is only item."
    assert inst.concept[4].display == "Enforce only one"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == "If field is a list, how to manage the source."
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "map-source-list-mode"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.684"
    assert inst.identifier[1].system == "urn:ietf:rfc:3986"
    assert inst.identifier[1].use == "old"
    assert inst.identifier[1].value == "urn:oid:2.16.840.1.113883.4.642.1.670"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-01T23:03:57.298+11:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    assert inst.name == "StructureMapSourceListMode"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Structure Map Source List Mode"
    assert inst.url == "http://hl7.org/fhir/map-source-list-mode"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/map-source-list-mode"
    assert inst.version == "5.0.0-draft-final"


def test_codesystem_4(base_settings):
    """No. 4 tests collection for CodeSystem.
    Test File: codesystem-map-source-list-mode.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-map-source-list-mode.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_4(inst2)


def impl_codesystem_5(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "planned"
    assert inst.concept[0].definition == (
    "The patient is planned to be moved to this location at some "
    "point in the future."
    )
    assert inst.concept[0].display == "Planned"
    assert inst.concept[1].code == "active"
    assert inst.concept[1].display == "Active"
    assert inst.concept[2].code == "reserved"
    assert inst.concept[2].definition == "This location is held empty for this patient."
    assert inst.concept[2].display == "Reserved"
    assert inst.concept[3].code == "completed"
    assert inst.concept[3].display == "Completed"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == "The status of the location."
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "pa"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "encounter-location-status"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.263"
    assert inst.identifier[1].system == "urn:ietf:rfc:3986"
    assert inst.identifier[1].use == "old"
    assert inst.identifier[1].value == "urn:oid:2.16.840.1.113883.4.642.1.258"
    assert inst.identifier[2].system == "urn:ietf:rfc:3986"
    assert inst.identifier[2].use == "old"
    assert inst.identifier[2].value == "urn:oid:2.16.840.1.113883.4.642.2.147"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-01T23:03:57.298+11:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    assert inst.name == "EncounterLocationStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Encounter Location Status"
    assert inst.url == "http://hl7.org/fhir/encounter-location-status"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/encounter-location-status"
    assert inst.version == "5.0.0-draft-final"


def test_codesystem_5(base_settings):
    """No. 5 tests collection for CodeSystem.
    Test File: codesystem-encounter-location-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-encounter-location-status.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_5(inst2)


def impl_codesystem_6(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "Average"
    assert inst.concept[0].display == "Average"
    assert inst.concept[1].code == "Approximately"
    assert inst.concept[1].display == "Approximately"
    assert inst.concept[2].code == "LessThan"
    assert inst.concept[2].display == "Less Than"
    assert inst.concept[3].code == "MoreThan"
    assert inst.concept[3].display == "More Than"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == "The type of a numeric quantity measurement."
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "brr"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "substance-amount-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.2086"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-01T23:03:57.298+11:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    assert inst.name == "SubstanceAmountType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Substance Amount Type"
    assert inst.url == "http://hl7.org/fhir/substance-amount-type"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/substance-amount-type"
    assert inst.version == "5.0.0-draft-final"


def test_codesystem_6(base_settings):
    """No. 6 tests collection for CodeSystem.
    Test File: codesystem-substance-amount-type.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-substance-amount-type.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_6(inst2)


def impl_codesystem_7(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "Pregnancy"
    assert inst.concept[0].display == "Pregnancy and Lactation"
    assert inst.concept[1].code == "Overdose"
    assert inst.concept[1].display == "Overdose"
    assert inst.concept[2].code == "DriveAndMachines"
    assert inst.concept[2].display == "Effects on Ability to Drive and Use Machines"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == "ClinicalUseDefinitionCategory"
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "brr"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "clinical-use-definition-category"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.1993"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-01T23:03:57.298+11:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    assert inst.name == "ClinicalUseDefinitionCategory"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Clinical Use Definition Category"
    assert inst.url == "http://hl7.org/fhir/clinical-use-definition-category"
    assert inst.valueSet == (
    "http://hl7.org/fhir/ValueSet/clinical-use-definition-"
    "category"
    )
    assert inst.version == "5.0.0-draft-final"


def test_codesystem_7(base_settings):
    """No. 7 tests collection for CodeSystem.
    Test File: codesystem-clinical-use-definition-category.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-clinical-use-definition-category.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_7(inst2)


def impl_codesystem_8(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "continuous"
    assert inst.concept[0].definition == (
    "A continuous variable is one for which, within the limits "
    "the variable ranges, any value is possible (from STATO "
    "http://purl.obolibrary.org/obo/STATO_0000251)."
    )
    assert inst.concept[0].display == "continuous variable"
    assert inst.concept[1].code == "dichotomous"
    assert inst.concept[1].definition == (
    "A dichotomous variable is a categorical variable which is "
    "defined to have only 2 categories or possible values (from "
    "STATO http://purl.obolibrary.org/obo/STATO_0000090)."
    )
    assert inst.concept[1].display == "dichotomous variable"
    assert inst.concept[2].code == "ordinal"
    assert inst.concept[2].definition == (
    "An ordinal variable is a categorical variable where the "
    "discrete possible values are ordered or correspond to an "
    "implicit ranking (from STATO "
    "http://purl.obolibrary.org/obo/STATO_0000228)."
    )
    assert inst.concept[2].display == "ordinal variable"
    assert inst.concept[3].code == "polychotomous"
    assert inst.concept[3].display == "polychotomous variable"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == (
    "The handling of the variable in statistical analysis for "
    "exposures or outcomes (E.g. Dichotomous, Continuous, "
    "Descriptive)."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "cds"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 5
    assert inst.id == "variable-handling"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.1956"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-01T23:03:57.298+11:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    assert inst.name == "EvidenceVariableHandling"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Evidence Variable Handling"
    assert inst.url == "http://hl7.org/fhir/variable-handling"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/variable-handling"
    assert inst.version == "5.0.0-draft-final"


def test_codesystem_8(base_settings):
    """No. 8 tests collection for CodeSystem.
    Test File: codesystem-variable-handling.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-variable-handling.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_8(inst2)


def impl_codesystem_9(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "any"
    assert inst.concept[0].definition == (
    "Any number of the actions in the group may be chosen, from "
    "zero to all."
    )
    assert inst.concept[0].display == "Any"
    assert inst.concept[1].code == "all"
    assert inst.concept[1].definition == (
    "All the actions in the group must be selected as a single "
    "unit."
    )
    assert inst.concept[1].display == "All"
    assert inst.concept[2].code == "all-or-none"
    assert inst.concept[2].definition == (
    "All the actions in the group are meant to be chosen as a "
    "single unit: either all must be selected by the end user, or"
    " none may be selected."
    )
    assert inst.concept[2].display == "All Or None"
    assert inst.concept[3].code == "exactly-one"
    assert inst.concept[3].definition == (
    "The end user must choose one and only one of the selectable "
    "actions in the group. The user SHALL NOT choose none of the "
    "actions in the group."
    )
    assert inst.concept[3].display == "Exactly One"
    assert inst.concept[4].code == "at-most-one"
    assert inst.concept[4].definition == (
    "The end user may choose zero or at most one of the actions "
    "in the group."
    )
    assert inst.concept[4].display == "At Most One"
    assert inst.concept[5].code == "one-or-more"
    assert inst.concept[5].definition == (
    "The end user must choose a minimum of one, and as many "
    "additional as desired."
    )
    assert inst.concept[5].display == "One Or More"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == "Defines selection behavior of a group."
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "cds"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 3
    assert inst.id == "action-selection-behavior"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.802"
    assert inst.identifier[1].system == "urn:ietf:rfc:3986"
    assert inst.identifier[1].use == "old"
    assert inst.identifier[1].value == "urn:oid:2.16.840.1.113883.4.642.1.785"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-01T23:03:57.298+11:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    assert inst.name == "ActionSelectionBehavior"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Action Selection Behavior"
    assert inst.url == "http://hl7.org/fhir/action-selection-behavior"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/action-selection-behavior"
    assert inst.version == "5.0.0-draft-final"


def test_codesystem_9(base_settings):
    """No. 9 tests collection for CodeSystem.
    Test File: codesystem-action-selection-behavior.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-action-selection-behavior.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_9(inst2)


def impl_codesystem_10(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "pubmed-pubstatus-received"
    assert inst.concept[0].definition == "PubMed Pubstatus of Received"
    assert inst.concept[0].display == "PubMed Pubstatus of Received"
    assert inst.concept[1].code == "pubmed-pubstatus-accepted"
    assert inst.concept[1].definition == "PubMed Pubstatus of Accepted"
    assert inst.concept[1].display == "PubMed Pubstatus of Accepted"
    assert inst.concept[2].code == "pubmed-pubstatus-epublish"
    assert inst.concept[2].definition == "PubMed Pubstatus of Epublish"
    assert inst.concept[2].display == "PubMed Pubstatus of Epublish"
    assert inst.concept[3].code == "pubmed-pubstatus-ppublish"
    assert inst.concept[3].definition == "PubMed Pubstatus of Ppublish"
    assert inst.concept[3].display == "PubMed Pubstatus of Ppublish"
    assert inst.concept[4].code == "pubmed-pubstatus-revised"
    assert inst.concept[4].definition == "PubMed Pubstatus of Revised"
    assert inst.concept[4].display == "PubMed Pubstatus of Revised"
    assert inst.concept[5].code == "pubmed-pubstatus-aheadofprint"
    assert inst.concept[5].definition == "PubMed Pubstatus of aheadofprint"
    assert inst.concept[5].display == "PubMed Pubstatus of aheadofprint"
    assert inst.concept[6].code == "pubmed-pubstatus-retracted"
    assert inst.concept[6].definition == "PubMed Pubstatus of Retracted"
    assert inst.concept[6].display == "PubMed Pubstatus of Retracted"
    assert inst.concept[7].code == "pubmed-pubstatus-ecollection"
    assert inst.concept[7].definition == "PubMed Pubstatus of Ecollection"
    assert inst.concept[7].display == "PubMed Pubstatus of Ecollection"
    assert inst.concept[8].code == "pubmed-pubstatus-pmc"
    assert inst.concept[8].definition == "PubMed Pubstatus of PMC"
    assert inst.concept[8].display == "PubMed Pubstatus of PMC"
    assert inst.concept[9].code == "pubmed-pubstatus-pmcr"
    assert inst.concept[9].definition == "PubMed Pubstatus of PMCr"
    assert inst.concept[9].display == "PubMed Pubstatus of PMCr"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-03-11T10:55:11.085+11:00")
    assert inst.description == "Citation status type"
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "cds"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 0
    assert inst.id == "citation-status-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.1878"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-01T23:03:57.298+11:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    assert inst.name == "CitationStatusType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Citation Status Type"
    assert inst.url == "http://hl7.org/fhir/citation-status-type"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/citation-status-type"
    assert inst.version == "5.0.0-draft-final"


def test_codesystem_10(base_settings):
    """No. 10 tests collection for CodeSystem.
    Test File: codesystem-citation-status-type.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-citation-status-type.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_10(inst2)