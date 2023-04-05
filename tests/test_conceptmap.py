# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import conceptmap


def impl_conceptmap_1(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == "Canonical Mapping for \"The status of the episode of care.\""
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "planned"
    assert inst.group[0].element[1].target[0].code == "planned"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "waitlist"
    assert inst.group[0].element[2].target[0].code == "draft"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "active"
    assert inst.group[0].element[3].target[0].code == "active"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].element[4].code == "onhold"
    assert inst.group[0].element[4].target[0].code == "suspended"
    assert inst.group[0].element[4].target[0].relationship == "equivalent"
    assert inst.group[0].element[5].code == "finished"
    assert inst.group[0].element[5].target[0].code == "complete"
    assert inst.group[0].element[5].target[0].relationship == "equivalent"
    assert inst.group[0].element[6].code == "cancelled"
    assert inst.group[0].element[6].target[0].code == "abandoned"
    assert inst.group[0].element[6].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/episode-of-care-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-episode-of-care-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.name == "EpisodeOfCareStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/episode-of-care-status"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == "Canonical Mapping for \"Episode Of Care Status\""
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-episode-of-care-status"
    assert inst.version == "5.0.0"


def test_conceptmap_1(base_settings):
    """No. 1 tests collection for ConceptMap.
    Test File: sc-valueset-episode-of-care-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-episode-of-care-status.json"
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
    assert inst.description == "Canonical Mapping for \"Medication Status Codes\""
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "active"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "inactive"
    assert inst.group[0].element[2].target[0].code == "inactive"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/CodeSystem/medication-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-medication-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.name == "MedicationStatusCodesCanonicalMap"
    assert inst.publisher == "FHIR Project team"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/medication-status"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == "Canonical Mapping for \"Medication Status Codes\""
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-medication-status"
    assert inst.version == "5.0.0"


def test_conceptmap_2(base_settings):
    """No. 2 tests collection for ConceptMap.
    Test File: sc-valueset-medication-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-medication-status.json"
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
    assert inst.description == (
    "Canonical Mapping for \"BiologicallyDerivedProductDispense "
    "Status Codes\""
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "preparation"
    assert inst.group[0].element[1].target[0].code == "planned"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "in-progress"
    assert inst.group[0].element[2].target[0].code == "active"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "unfulfilled"
    assert inst.group[0].element[3].target[0].code == "failed"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].element[4].code == "issued"
    assert inst.group[0].element[4].target[0].code == "complete"
    assert inst.group[0].element[4].target[0].relationship == "equivalent"
    assert inst.group[0].element[5].code == "returned"
    assert inst.group[0].element[5].target[0].code == "abandoned"
    assert inst.group[0].element[5].target[0].relationship == "equivalent"
    assert inst.group[0].element[6].code == "unknown"
    assert inst.group[0].element[6].target[0].code == "unknown"
    assert inst.group[0].element[6].target[0].relationship == "equivalent"
    assert inst.group[0].element[7].code == "allocated"
    assert inst.group[0].element[7].target[0].code == "confirmed"
    assert inst.group[0].element[7].target[0].relationship == "equivalent"
    assert inst.group[0].source == (
    "http://hl7.org/fhir/biologicallyderivedproductdispense-"
    "status"
    )
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-biologicallyderivedproductdispense-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.name == "BiologicallyDerivedProductDispenseCodesCanonicalMap"
    assert inst.publisher == "FHIR Project team"
    assert inst.sourceScopeCanonical == (
    "http://hl7.org/fhir/ValueSet/biologicallyderivedproductdispe"
    "nse-status"
    )
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == (
    "Canonical Mapping for \"BiologicallyDerivedProductDispense "
    "Status Codes\""
    )
    assert inst.url == (
    "http://hl7.org/fhir/ConceptMap/sc-"
    "biologicallyderivedproductdispense-status"
    )
    assert inst.version == "5.0.0"


def test_conceptmap_3(base_settings):
    """No. 3 tests collection for ConceptMap.
    Test File: sc-valueset-biologicallyderivedproductdispense-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-biologicallyderivedproductdispense-status.json"
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
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == "Canonical Mapping for \"The status of the Device record.\""
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "active"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "inactive"
    assert inst.group[0].element[2].target[0].code == "inactive"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/device-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-device-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.name == "FHIRDeviceStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/device-status"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == "Canonical Mapping for \"FHIR Device Status\""
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-device-status"
    assert inst.version == "5.0.0"


def test_conceptmap_4(base_settings):
    """No. 4 tests collection for ConceptMap.
    Test File: sc-valueset-device-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-device-status.json"
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
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == (
    "Canonical Mapping for \"Indicates the status of a detected "
    "issue\""
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "preliminary"
    assert inst.group[0].element[1].target[0].code == "draft"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "final"
    assert inst.group[0].element[2].target[0].code == "complete"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "mitigated"
    assert inst.group[0].element[3].target[0].code == "inactive"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/observation-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-detectedissue-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.name == "DetectedIssueStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/detectedissue-status"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == "Canonical Mapping for \"Detected Issue Status\""
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-detectedissue-status"
    assert inst.version == "5.0.0"


def test_conceptmap_5(base_settings):
    """No. 5 tests collection for ConceptMap.
    Test File: sc-valueset-detectedissue-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-detectedissue-status.json"
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
    assert inst.contact[0].telecom[0].value == "http://www.hl7.org/Special/committees/patientcare/"
    assert inst.description == (
    "Canonical Mapping for \"Codes identifying the lifecycle "
    "stage of an adverse event.\""
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "in-progress"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "completed"
    assert inst.group[0].element[2].target[0].code == "complete"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "unknown"
    assert inst.group[0].element[3].target[0].code == "unknown"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/event-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-adverse-event-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.name == "AdverseEventStatusCanonicalMap"
    assert inst.publisher == "HL7 International - Patient Care WG"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/adverse-event-status"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == "Canonical Mapping for \"Adverse Event Status\""
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-adverse-event-status"
    assert inst.version == "5.0.0"


def test_conceptmap_6(base_settings):
    """No. 6 tests collection for ConceptMap.
    Test File: sc-valueset-adverse-event-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-adverse-event-status.json"
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
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == (
    "Canonical Mapping for \"MedicationAdministration Status "
    "Codes\""
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "in-progress"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "on-hold"
    assert inst.group[0].element[2].target[0].code == "suspended"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "stopped"
    assert inst.group[0].element[3].target[0].code == "failed"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].element[4].code == "completed"
    assert inst.group[0].element[4].target[0].code == "complete"
    assert inst.group[0].element[4].target[0].relationship == "equivalent"
    assert inst.group[0].element[5].code == "unknown"
    assert inst.group[0].element[5].target[0].code == "unknown"
    assert inst.group[0].element[5].target[0].relationship == "equivalent"
    assert inst.group[0].element[6].code == "not-done"
    assert inst.group[0].element[6].target[0].code == "not-done"
    assert inst.group[0].element[6].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/CodeSystem/medication-admin-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-medication-admin-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.name == "MedicationAdministrationStatusCodesCanonicalMap"
    assert inst.publisher == "FHIR Project team"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/medication-admin-status"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == (
    "Canonical Mapping for \"MedicationAdministration Status "
    "Codes\""
    )
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-medication-admin-status"
    assert inst.version == "5.0.0"


def test_conceptmap_7(base_settings):
    """No. 7 tests collection for ConceptMap.
    Test File: sc-valueset-medication-admin-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-medication-admin-status.json"
    )
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
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == (
    "Canonical Mapping for \"Indicates the state of the "
    "consent.\""
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "draft"
    assert inst.group[0].element[1].target[0].code == "draft"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "active"
    assert inst.group[0].element[2].target[0].code == "active"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "not-done"
    assert inst.group[0].element[3].target[0].code == "failed"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].element[4].code == "inactive"
    assert inst.group[0].element[4].target[0].code == "inactive"
    assert inst.group[0].element[4].target[0].relationship == "equivalent"
    assert inst.group[0].element[5].code == "unknown"
    assert inst.group[0].element[5].target[0].code == "unknown"
    assert inst.group[0].element[5].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/consent-state-codes"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-consent-state-codes"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.name == "ConsentStateCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/consent-state-codes"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == "Canonical Mapping for \"Consent State\""
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-consent-state-codes"
    assert inst.version == "5.0.0"


def test_conceptmap_8(base_settings):
    """No. 8 tests collection for ConceptMap.
    Test File: sc-valueset-consent-state-codes.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-consent-state-codes.json"
    )
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
    assert inst.date == fhirtypes.DateTime.validate("2023-03-26T15:21:02+11:00")
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "home"
    assert inst.group[0].element[0].target[0].code == "H"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "work"
    assert inst.group[0].element[1].target[0].code == "O"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "temp"
    assert inst.group[0].element[2].target[0].code == "C"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "old"
    assert inst.group[0].element[3].target[0].code == "BA"
    assert inst.group[0].element[3].target[0].comment == "unclear about old addresses"
    assert inst.group[0].element[3].target[0].relationship == "source-is-broader-than-target"
    assert inst.group[0].element[4].code == "billing"
    assert inst.group[0].element[4].target[0].code == "BI"
    assert inst.group[0].element[4].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/address-use"
    assert inst.group[0].target == "http://terminology.hl7.org/CodeSystem/v2-0190"
    assert inst.id == "cm-address-use-v2"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.name == "v2.AddressUse"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/address-use"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://terminology.hl7.org/ValueSet/v2-0190"
    assert inst.text.status == "extensions"
    assert inst.title == "v2 map for AddressUse"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-address-use-v2"
    assert inst.version == "5.0.0"


def test_conceptmap_9(base_settings):
    """No. 9 tests collection for ConceptMap.
    Test File: cm-address-use-v2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "cm-address-use-v2.json"
    )
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
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == (
    "Canonical Mapping for \"The current status of the test "
    "report.\""
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "in-progress"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "waiting"
    assert inst.group[0].element[2].target[0].code == "suspended"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "stopped"
    assert inst.group[0].element[3].target[0].code == "failed"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].element[4].code == "completed"
    assert inst.group[0].element[4].target[0].code == "complete"
    assert inst.group[0].element[4].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/report-status-codes"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-report-status-codes"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert inst.jurisdiction[0].coding[0].system == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    assert inst.name == "TestReportStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/report-status-codes"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == "Canonical Mapping for \"Test Report Status\""
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-report-status-codes"
    assert inst.version == "5.0.0"


def test_conceptmap_10(base_settings):
    """No. 10 tests collection for ConceptMap.
    Test File: sc-valueset-report-status-codes.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-report-status-codes.json"
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