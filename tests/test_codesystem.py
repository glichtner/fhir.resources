# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import codesystem


def impl_codesystem_1(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "policy"
    assert inst.concept[0].definition == "To be completed"
    assert inst.concept[0].display == "Policy"
    assert inst.contact[0].name == "FHIR project team"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2017-02-13")
    assert inst.description == (
        "This CodeSystem contains FHIR-defined contract security "
        "classification types."
    )
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fm"
    assert inst.id == "contract-security-classification"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.1219"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "ContractSecurityClassification"
    assert inst.publisher == "HL7 International"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/contract-security-classification"
    assert inst.version == "4.5.0"


def test_codesystem_1(base_settings):
    """No. 1 tests collection for CodeSystem.
    Test File: codesystem-contract-security-classification.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-contract-security-classification.json"
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
    assert inst.concept[0].code == "Patient"
    assert (
        inst.concept[0].definition
        == "The compartment definition is for the patient compartment."
    )
    assert inst.concept[0].display == "Patient"
    assert inst.concept[1].code == "Encounter"
    assert (
        inst.concept[1].definition
        == "The compartment definition is for the encounter compartment."
    )
    assert inst.concept[1].display == "Encounter"
    assert inst.concept[2].code == "RelatedPerson"
    assert inst.concept[2].definition == (
        "The compartment definition is for the related-person " "compartment."
    )
    assert inst.concept[2].display == "RelatedPerson"
    assert inst.concept[3].code == "Practitioner"
    assert inst.concept[3].definition == (
        "The compartment definition is for the practitioner " "compartment."
    )
    assert inst.concept[3].display == "Practitioner"
    assert inst.concept[4].code == "Device"
    assert (
        inst.concept[4].definition
        == "The compartment definition is for the device compartment."
    )
    assert inst.concept[4].display == "Device"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == "Which type a compartment definition describes."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "compartment-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.787"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T11:34:11.075+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "CompartmentType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CompartmentType"
    assert inst.url == "http://hl7.org/fhir/compartment-type"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/compartment-type"
    assert inst.version == "4.5.0"


def test_codesystem_2(base_settings):
    """No. 2 tests collection for CodeSystem.
    Test File: codesystem-compartment-type.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-compartment-type.json"
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
    assert inst.concept[0].code == "usual"
    assert inst.concept[0].definition == (
        "The identifier recommended for display and use in real-world" " interactions."
    )
    assert inst.concept[0].display == "Usual"
    assert inst.concept[1].code == "official"
    assert inst.concept[1].display == "Official"
    assert inst.concept[2].code == "temp"
    assert inst.concept[2].definition == "A temporary identifier."
    assert inst.concept[2].display == "Temp"
    assert inst.concept[3].code == "secondary"
    assert inst.concept[3].definition == (
        "An identifier that was assigned in secondary use - it serves"
        " to identify the object in a relative context, but cannot be"
        " consistently assigned to the same object again in a "
        "different context."
    )
    assert inst.concept[3].display == "Secondary"
    assert inst.concept[4].code == "old"
    assert inst.concept[4].definition == (
        "The identifier id no longer considered valid, but may be "
        "relevant for search purposes.  E.g. Changes to identifier "
        "schemes, account merges, etc."
    )
    assert inst.concept[4].display == "Old"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.description == "Identifies the purpose for this identifier, if known ."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "normative"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "normative-version"
    )
    assert inst.extension[2].valueCode == "4.0.0"
    assert inst.extension[3].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[3].valueInteger == 5
    assert inst.id == "identifier-use"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.58"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.name == "IdentifierUse"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "IdentifierUse"
    assert inst.url == "http://hl7.org/fhir/identifier-use"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/identifier-use"
    assert inst.version == "4.5.0"


def test_codesystem_3(base_settings):
    """No. 3 tests collection for CodeSystem.
    Test File: codesystem-identifier-use.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-identifier-use.json"
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
    assert inst.concept[0].code == "std-MA"
    assert inst.concept[0].definition == (
        "A meta-analysis of the summary data of estimates from "
        "individual studies or data sets."
    )
    assert inst.concept[0].display == "summary data meta-analysis"
    assert inst.concept[1].code == "IPD-MA"
    assert inst.concept[1].definition == (
        "A meta-analysis of the individual participant data from "
        "individual studies or data sets."
    )
    assert inst.concept[1].display == "individual patient data meta-analysis"
    assert inst.concept[2].code == "indirect-NMA"
    assert inst.concept[2].definition == (
        "An indirect meta-analysis derived from 2 or more direct "
        "comparisons in a network meta-analysis."
    )
    assert inst.concept[2].display == "indirect network meta-analysis"
    assert inst.concept[3].code == "combined-NMA"
    assert inst.concept[3].definition == (
        "An composite meta-analysis derived from direct comparisons "
        "and indirect comparisons in a network meta-analysis."
    )
    assert (
        inst.concept[3].display == "combined direct plus indirect network meta-analysis"
    )
    assert inst.concept[4].code == "range"
    assert inst.concept[4].definition == "A range of results across a body of evidence."
    assert inst.concept[4].display == "range of results"
    assert inst.concept[5].code == "classification"
    assert inst.concept[5].definition == (
        "An approach describing a body of evidence by categorically "
        "classifying individual studies (eg 3 studies showed beneft "
        "and 2 studied found no effect)."
    )
    assert inst.concept[5].display == "classifcation of results"
    assert inst.concept[6].code == "NotApplicable"
    assert inst.concept[6].definition == (
        "Not applicable because the evidence is not from a synthesis "
        "but from a single study. Used fo explicitly state that it's "
        "not a synthesis."
    )
    assert inst.concept[6].display == "not applicable"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == (
        "Types of combining results from a body of evidence (eg. "
        "summary data meta-analysis)."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "cds"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "synthesis-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.1348"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T11:34:11.075+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "SynthesisType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "SynthesisType"
    assert inst.url == "http://terminology.hl7.org/CodeSystem/synthesis-type"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/synthesis-type"
    assert inst.version == "4.5.0"


def test_codesystem_4(base_settings):
    """No. 4 tests collection for CodeSystem.
    Test File: codesystem-synthesis-type.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-synthesis-type.json"
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
    assert inst.concept[0].code == "classification"
    assert inst.concept[0].definition == (
        "The report is primarily a listing of classifiers about the " "report subject."
    )
    assert inst.concept[0].display == "Classification"
    assert inst.concept[1].code == "search-results"
    assert inst.concept[1].definition == (
        "The report is a composition of results generated in response"
        " to a search query."
    )
    assert inst.concept[1].display == "Search Results"
    assert inst.concept[2].code == "resources-compiled"
    assert inst.concept[2].definition == (
        "The report is a composition containing one or more FHIR "
        "resources in the content."
    )
    assert inst.concept[2].display == "Resource Compilation"
    assert inst.concept[3].code == "text-structured"
    assert (
        inst.concept[3].definition
        == "The report is a structured representation of text."
    )
    assert inst.concept[3].display == "Structured Text"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == (
        "The kind of report, such as grouping of classifiers, search "
        "results, or human-compiled expression."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "cds"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "evidence-report-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.0"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T11:34:11.075+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "EvidenceReportType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "EvidenceReportType"
    assert inst.url == "http://terminology.hl7.org/CodeSystem/evidence-report-type"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/evidence-report-type"
    assert inst.version == "4.5.0"


def test_codesystem_5(base_settings):
    """No. 5 tests collection for CodeSystem.
    Test File: codesystem-evidence-report-type.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-evidence-report-type.json"
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
    assert inst.concept[0].code == "NL1"
    assert inst.concept[0].display == "Own Name"
    assert inst.concept[1].code == "NL2"
    assert inst.concept[1].display == "Partner Name"
    assert inst.concept[2].code == "NL3"
    assert inst.concept[2].display == "Partner Name followed by Maiden Name"
    assert inst.concept[3].code == "NL4"
    assert inst.concept[3].display == "Own Name followed by Partner Name"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.description == (
        "A code that represents the preferred display order of the "
        "components of a human name."
    )
    assert inst.experimental is False
    assert inst.id == "name-assembly-order"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.1266"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.name == "HumanNameAssemblyOrder"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "HumanNameAssemblyOrder"
    assert inst.url == "http://terminology.hl7.org/CodeSystem/name-assembly-order"
    assert inst.version == "4.5.0"


def test_codesystem_6(base_settings):
    """No. 6 tests collection for CodeSystem.
    Test File: codesystem-name-assembly-order.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-name-assembly-order.json"
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
    assert inst.concept[0].code == "active"
    assert inst.concept[0].definition == "Study is opened for accrual."
    assert inst.concept[0].display == "Active"
    assert inst.concept[1].code == "administratively-completed"
    assert inst.concept[1].definition == (
        "Study is completed prematurely and will not resume; patients"
        " are no longer examined nor treated."
    )
    assert inst.concept[1].display == "Administratively Completed"
    assert inst.concept[2].code == "approved"
    assert inst.concept[2].definition == "Protocol is approved by the review board."
    assert inst.concept[2].display == "Approved"
    assert inst.concept[3].code == "closed-to-accrual"
    assert inst.concept[3].definition == (
        "Study is closed for accrual; patients can be examined and " "treated."
    )
    assert inst.concept[3].display == "Closed to Accrual"
    assert inst.concept[4].code == "closed-to-accrual-and-intervention"
    assert inst.concept[4].display == "Closed to Accrual and Intervention"
    assert inst.concept[5].code == "completed"
    assert inst.concept[5].display == "Completed"
    assert inst.concept[6].code == "disapproved"
    assert inst.concept[6].definition == "Protocol was disapproved by the review board."
    assert inst.concept[6].display == "Disapproved"
    assert inst.concept[7].code == "in-review"
    assert (
        inst.concept[7].definition
        == "Protocol is submitted to the review board for approval."
    )
    assert inst.concept[7].display == "In Review"
    assert inst.concept[8].code == "temporarily-closed-to-accrual"
    assert inst.concept[8].definition == (
        "Study is temporarily closed for accrual; can be potentially "
        "resumed in the future; patients can be examined and treated."
    )
    assert inst.concept[8].display == "Temporarily Closed to Accrual"
    assert inst.concept[9].code == "temporarily-closed-to-accrual-and-intervention"
    assert inst.concept[9].definition == (
        "Study is temporarily closed for accrual and intervention and"
        " potentially can be resumed in the future."
    )
    assert inst.concept[9].display == "Temporarily Closed to Accrual and Intervention"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert (
        inst.description
        == "Codes that convey the current status of the research study."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "brr"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 0
    assert inst.id == "research-study-status"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.820"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T11:34:11.075+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "ResearchStudyStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "ResearchStudyStatus"
    assert inst.url == "http://hl7.org/fhir/research-study-status"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/research-study-status"
    assert inst.version == "4.5.0"


def test_codesystem_7(base_settings):
    """No. 7 tests collection for CodeSystem.
    Test File: codesystem-research-study-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-research-study-status.json"
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
    assert inst.concept[0].code == "codesystem"
    assert inst.concept[0].definition == (
        "The naming system is used to define concepts and symbols to "
        "represent those concepts; e.g. UCUM, LOINC, NDC code, local "
        "lab codes, etc."
    )
    assert inst.concept[0].display == "Code System"
    assert inst.concept[1].code == "identifier"
    assert inst.concept[1].definition == (
        "The naming system is used to manage identifiers (e.g. "
        "license numbers, order numbers, etc.)."
    )
    assert inst.concept[1].display == "Identifier"
    assert inst.concept[2].code == "root"
    assert inst.concept[2].definition == (
        "The naming system is used as the root for other identifiers "
        "and naming systems."
    )
    assert inst.concept[2].display == "Root"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == "Identifies the purpose of the naming system."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "namingsystem-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.491"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T11:34:11.075+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "NamingSystemType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "NamingSystemType"
    assert inst.url == "http://hl7.org/fhir/namingsystem-type"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/namingsystem-type"
    assert inst.version == "4.5.0"


def test_codesystem_8(base_settings):
    """No. 8 tests collection for CodeSystem.
    Test File: codesystem-namingsystem-type.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-namingsystem-type.json"
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
    assert inst.concept[0].code == "food"
    assert inst.concept[0].definition == (
        "Any substance consumed to provide nutritional support for " "the body."
    )
    assert inst.concept[0].display == "Food"
    assert inst.concept[1].code == "medication"
    assert (
        inst.concept[1].definition
        == "Substances administered to achieve a physiological effect."
    )
    assert inst.concept[1].display == "Medication"
    assert inst.concept[2].code == "environment"
    assert inst.concept[2].definition == (
        "Any substances that are encountered in the environment, "
        "including any substance not already classified as food, "
        "medication, or biologic."
    )
    assert inst.concept[2].display == "Environment"
    assert inst.concept[3].code == "biologic"
    assert inst.concept[3].display == "Biologic"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == (
        "Category of an identified substance associated with "
        "allergies or intolerances."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "pc"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 3
    assert inst.id == "allergy-intolerance-category"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.134"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T11:34:11.075+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "AllergyIntoleranceCategory"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "AllergyIntoleranceCategory"
    assert inst.url == "http://hl7.org/fhir/allergy-intolerance-category"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/allergy-intolerance-category"
    assert inst.version == "4.5.0"


def test_codesystem_9(base_settings):
    """No. 9 tests collection for CodeSystem.
    Test File: codesystem-allergy-intolerance-category.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-allergy-intolerance-category.json"
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
    assert inst.concept[0].code == "mon"
    assert inst.concept[0].definition == "Monday."
    assert inst.concept[0].display == "Monday"
    assert inst.concept[1].code == "tue"
    assert inst.concept[1].definition == "Tuesday."
    assert inst.concept[1].display == "Tuesday"
    assert inst.concept[2].code == "wed"
    assert inst.concept[2].definition == "Wednesday."
    assert inst.concept[2].display == "Wednesday"
    assert inst.concept[3].code == "thu"
    assert inst.concept[3].definition == "Thursday."
    assert inst.concept[3].display == "Thursday"
    assert inst.concept[4].code == "fri"
    assert inst.concept[4].definition == "Friday."
    assert inst.concept[4].display == "Friday"
    assert inst.concept[5].code == "sat"
    assert inst.concept[5].definition == "Saturday."
    assert inst.concept[5].display == "Saturday"
    assert inst.concept[6].code == "sun"
    assert inst.concept[6].definition == "Sunday."
    assert inst.concept[6].display == "Sunday"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == "The days of the week."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "pa"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "normative"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "normative-version"
    )
    assert inst.extension[2].valueCode == "4.0.0"
    assert inst.extension[3].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[3].valueInteger == 5
    assert inst.id == "days-of-week"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.513"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T11:34:11.075+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "DaysOfWeek"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "DaysOfWeek"
    assert inst.url == "http://hl7.org/fhir/days-of-week"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/days-of-week"
    assert inst.version == "4.5.0"


def test_codesystem_10(base_settings):
    """No. 10 tests collection for CodeSystem.
    Test File: codesystem-days-of-week.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-days-of-week.json"
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
