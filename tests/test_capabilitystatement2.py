# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement2
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import capabilitystatement2


def impl_capabilitystatement2_1(inst):
    assert inst.contact[0].name == "FHIR Project"
    assert inst.contact[0].telecom[0].system == "other"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2016-09-16")
    assert inst.description == (
        "Basic conformance statement for a Measure Processor Service."
        " A server can support more functionality    than defined "
        "here, but this is the minimum amount"
    )
    assert inst.fhirVersion == "4.5.0"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "measure-processor"
    assert inst.kind == "capability"
    assert inst.name == "Measure Processor Service Conformance Statement"
    assert inst.publisher == "HL7, Inc"
    assert inst.rest[0].documentation == "RESTful Measure Processor Service"
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].operation[0].definition == (
        "http://hl7.org/fhir/OperationDefinition/Measure-evaluate-" "measure"
    )
    assert inst.rest[0].operation[0].name == "evaluate-measure"
    assert inst.rest[0].operation[1].definition == (
        "http://hl7.org/fhir/OperationDefinition/Measure-data-" "requirements"
    )
    assert inst.rest[0].operation[1].name == "data-requirements"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "measures"
    )
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
        "Search allows clients to filter measures based on a provided"
        " search parameter"
    )
    assert (
        inst.rest[0].resource[0].profile
        == "http://hl7.org/fhir/StructureDefinition/Measure"
    )
    assert (
        inst.rest[0].resource[0].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-identifier"
    )
    assert inst.rest[0].resource[0].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-status"
    )
    assert inst.rest[0].resource[0].searchParam[1].name == "status"
    assert inst.rest[0].resource[0].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-version"
    )
    assert inst.rest[0].resource[0].searchParam[2].name == "version"
    assert inst.rest[0].resource[0].searchParam[2].type == "string"
    assert inst.rest[0].resource[0].type == "Measure"
    assert inst.software.name == "ACME Measure Processor Service"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/measure-processor"


def test_capabilitystatement2_1(base_settings):
    """No. 1 tests collection for CapabilityStatement2.
    Test File: capabilitystatement2-measure-processor.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "capabilitystatement2-measure-processor.json"
    )
    inst = capabilitystatement2.CapabilityStatement2.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement2" == inst.resource_type

    impl_capabilitystatement2_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement2" == data["resourceType"]

    inst2 = capabilitystatement2.CapabilityStatement2(**data)
    impl_capabilitystatement2_1(inst2)


def impl_capabilitystatement2_2(inst):
    assert inst.contact[0].name == "FHIR Project"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2015-07-05")
    assert inst.description == (
        "Basic capability statement for a Terminology Server. A "
        "server can support more fucntionality than defined here, but"
        " this is the minimum amount"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement2"
        "-supported-system"
    )
    assert inst.extension[0].valueUri == "http://loinc.org"
    assert inst.fhirVersion == "4.5.0"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "terminology-server"
    assert inst.kind == "capability"
    assert inst.name == "Terminology Service Capability Statement"
    assert inst.publisher == "HL7, Inc"
    assert inst.rest[0].documentation == "RESTful Terminology Server"
    assert inst.rest[0].mode == "server"
    assert (
        inst.rest[0].operation[0].definition
        == "http://hl7.org/fhir/OperationDefinition/ValueSet-expand"
    )
    assert inst.rest[0].operation[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement2" "-expectation"
    )
    assert inst.rest[0].operation[0].extension[0].valueCode == "SHALL"
    assert inst.rest[0].operation[0].name == "expand"
    assert (
        inst.rest[0].operation[1].definition
        == "http://hl7.org/fhir/OperationDefinition/CodeSystem-lookup"
    )
    assert inst.rest[0].operation[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement2" "-expectation"
    )
    assert inst.rest[0].operation[1].extension[0].valueCode == "SHALL"
    assert inst.rest[0].operation[1].name == "lookup"
    assert inst.rest[0].operation[2].definition == (
        "http://hl7.org/fhir/OperationDefinition/ValueSet-validate-" "code"
    )
    assert inst.rest[0].operation[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement2" "-expectation"
    )
    assert inst.rest[0].operation[2].extension[0].valueCode == "SHALL"
    assert inst.rest[0].operation[2].name == "validate-code"
    assert (
        inst.rest[0].operation[3].definition
        == "http://hl7.org/fhir/OperationDefinition/ConceptMap-translate"
    )
    assert inst.rest[0].operation[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement2" "-expectation"
    )
    assert inst.rest[0].operation[3].extension[0].valueCode == "SHALL"
    assert inst.rest[0].operation[3].name == "translate"
    assert (
        inst.rest[0].operation[4].definition
        == "http://hl7.org/fhir/OperationDefinition/ConceptMap-closure"
    )
    assert inst.rest[0].operation[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement2" "-expectation"
    )
    assert inst.rest[0].operation[4].extension[0].valueCode == "SHOULD"
    assert inst.rest[0].operation[4].name == "closure"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "value sets"
    )
    assert inst.rest[0].resource[0].interaction[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement2" "-expectation"
    )
    assert inst.rest[0].resource[0].interaction[0].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert (
        inst.rest[0].resource[0].interaction[1].documentation
        == "Search allows clients to find value sets on the server"
    )
    assert inst.rest[0].resource[0].interaction[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement2" "-expectation"
    )
    assert inst.rest[0].resource[0].interaction[1].extension[0].valueCode == "SHALL"
    assert (
        inst.rest[0].resource[0].profile
        == "http://hl7.org/fhir/StructureDefinition/ValueSet"
    )
    assert (
        inst.rest[0].resource[0].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-date"
    )
    assert inst.rest[0].resource[0].searchParam[0].name == "date"
    assert inst.rest[0].resource[0].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[0].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-name"
    )
    assert inst.rest[0].resource[0].searchParam[1].name == "name"
    assert inst.rest[0].resource[0].searchParam[1].type == "string"
    assert (
        inst.rest[0].resource[0].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-reference"
    )
    assert inst.rest[0].resource[0].searchParam[2].name == "reference"
    assert inst.rest[0].resource[0].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-status"
    )
    assert inst.rest[0].resource[0].searchParam[3].name == "status"
    assert inst.rest[0].resource[0].searchParam[3].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-url"
    )
    assert inst.rest[0].resource[0].searchParam[4].name == "url"
    assert inst.rest[0].resource[0].searchParam[4].type == "uri"
    assert (
        inst.rest[0].resource[0].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-version"
    )
    assert inst.rest[0].resource[0].searchParam[5].name == "version"
    assert inst.rest[0].resource[0].searchParam[5].type == "token"
    assert inst.rest[0].resource[0].type == "ValueSet"
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "concept maps"
    )
    assert inst.rest[0].resource[1].interaction[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement2" "-expectation"
    )
    assert inst.rest[0].resource[1].interaction[0].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[1].interaction[1].code == "search-type"
    assert (
        inst.rest[0].resource[1].interaction[1].documentation
        == "Search allows clients to find concept maps on the server"
    )
    assert inst.rest[0].resource[1].interaction[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement2" "-expectation"
    )
    assert inst.rest[0].resource[1].interaction[1].extension[0].valueCode == "SHALL"
    assert (
        inst.rest[0].resource[1].profile
        == "http://hl7.org/fhir/StructureDefinition/ConceptMap"
    )
    assert (
        inst.rest[0].resource[1].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-date"
    )
    assert inst.rest[0].resource[1].searchParam[0].name == "date"
    assert inst.rest[0].resource[1].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[1].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-name"
    )
    assert inst.rest[0].resource[1].searchParam[1].name == "name"
    assert inst.rest[0].resource[1].searchParam[1].type == "string"
    assert (
        inst.rest[0].resource[1].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-status"
    )
    assert inst.rest[0].resource[1].searchParam[2].name == "status"
    assert inst.rest[0].resource[1].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[1].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-source"
    )
    assert inst.rest[0].resource[1].searchParam[3].name == "source"
    assert inst.rest[0].resource[1].searchParam[3].type == "uri"
    assert (
        inst.rest[0].resource[1].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-target"
    )
    assert inst.rest[0].resource[1].searchParam[4].name == "target"
    assert inst.rest[0].resource[1].searchParam[4].type == "uri"
    assert (
        inst.rest[0].resource[1].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-url"
    )
    assert inst.rest[0].resource[1].searchParam[5].name == "url"
    assert inst.rest[0].resource[1].searchParam[5].type == "uri"
    assert (
        inst.rest[0].resource[1].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-version"
    )
    assert inst.rest[0].resource[1].searchParam[6].name == "version"
    assert inst.rest[0].resource[1].searchParam[6].type == "token"
    assert inst.rest[0].resource[1].type == "ConceptMap"
    assert inst.software.name == "ACME Terminology Server"
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert inst.url == "http://hl7.org/fhir/terminology-server"


def test_capabilitystatement2_2(base_settings):
    """No. 2 tests collection for CapabilityStatement2.
    Test File: capabilitystatement2-terminology-server.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "capabilitystatement2-terminology-server.json"
    )
    inst = capabilitystatement2.CapabilityStatement2.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement2" == inst.resource_type

    impl_capabilitystatement2_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement2" == data["resourceType"]

    inst2 = capabilitystatement2.CapabilityStatement2(**data)
    impl_capabilitystatement2_2(inst2)


def impl_capabilitystatement2_3(inst):
    assert inst.contact[0].name == "FHIR Project"
    assert inst.contact[0].telecom[0].system == "other"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2017-02-25")
    assert inst.description == (
        "Basic conformance statement for a Knowledge Repository "
        "Service. A server can support more functionality    than "
        "defined here, but this is the minimum amount"
    )
    assert inst.fhirVersion == "4.5.0"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "knowledge-repository"
    assert inst.kind == "capability"
    assert inst.name == "Knowledge Repository Service Conformance Statement"
    assert inst.publisher == "HL7, Inc"
    assert inst.rest[0].documentation == "RESTful Knowledge Repository Service"
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].operation[0].definition == (
        "http://hl7.org/fhir/OperationDefinition/Library-data-" "requirements"
    )
    assert inst.rest[0].operation[0].name == "data-requirements"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "libraries"
    )
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
        "Search allows clients to filter libraries based on a "
        "provided search parameter"
    )
    assert (
        inst.rest[0].resource[0].profile
        == "http://hl7.org/fhir/StructureDefinition/Library"
    )
    assert (
        inst.rest[0].resource[0].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Library-description"
    )
    assert inst.rest[0].resource[0].searchParam[0].name == "description"
    assert inst.rest[0].resource[0].searchParam[0].type == "string"
    assert (
        inst.rest[0].resource[0].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Library-identifier"
    )
    assert inst.rest[0].resource[0].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Library-status"
    )
    assert inst.rest[0].resource[0].searchParam[2].name == "status"
    assert inst.rest[0].resource[0].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/Library-title"
    )
    assert inst.rest[0].resource[0].searchParam[3].name == "title"
    assert inst.rest[0].resource[0].searchParam[3].type == "string"
    assert (
        inst.rest[0].resource[0].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/Library-topic"
    )
    assert inst.rest[0].resource[0].searchParam[4].name == "topic"
    assert inst.rest[0].resource[0].searchParam[4].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/Library-version"
    )
    assert inst.rest[0].resource[0].searchParam[5].name == "version"
    assert inst.rest[0].resource[0].searchParam[5].type == "string"
    assert (
        inst.rest[0].resource[0].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/Library-composed-of"
    )
    assert inst.rest[0].resource[0].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[0].searchParam[6].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/Library-depends-on"
    )
    assert inst.rest[0].resource[0].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[0].searchParam[7].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[8].definition
        == "http://hl7.org/fhir/SearchParameter/Library-derived-from"
    )
    assert inst.rest[0].resource[0].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[0].searchParam[8].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[9].definition
        == "http://hl7.org/fhir/SearchParameter/Library-predecessor"
    )
    assert inst.rest[0].resource[0].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[0].searchParam[9].type == "reference"
    assert inst.rest[0].resource[0].type == "Library"
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "plan definitions"
    )
    assert inst.rest[0].resource[1].interaction[1].code == "search-type"
    assert inst.rest[0].resource[1].interaction[1].documentation == (
        "Search allows clients to filter plan definitions based on a "
        "provided search parameter"
    )
    assert (
        inst.rest[0].resource[1].profile
        == "http://hl7.org/fhir/StructureDefinition/PlanDefinition"
    )
    assert inst.rest[0].resource[1].searchParam[0].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-" "description"
    )
    assert inst.rest[0].resource[1].searchParam[0].name == "description"
    assert inst.rest[0].resource[1].searchParam[0].type == "string"
    assert inst.rest[0].resource[1].searchParam[1].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-" "identifier"
    )
    assert inst.rest[0].resource[1].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[1].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[1].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/PlanDefinition-status"
    )
    assert inst.rest[0].resource[1].searchParam[2].name == "status"
    assert inst.rest[0].resource[1].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[1].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/PlanDefinition-title"
    )
    assert inst.rest[0].resource[1].searchParam[3].name == "title"
    assert inst.rest[0].resource[1].searchParam[3].type == "string"
    assert (
        inst.rest[0].resource[1].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/PlanDefinition-topic"
    )
    assert inst.rest[0].resource[1].searchParam[4].name == "topic"
    assert inst.rest[0].resource[1].searchParam[4].type == "token"
    assert (
        inst.rest[0].resource[1].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/PlanDefinition-version"
    )
    assert inst.rest[0].resource[1].searchParam[5].name == "version"
    assert inst.rest[0].resource[1].searchParam[5].type == "string"
    assert inst.rest[0].resource[1].searchParam[6].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-composed-" "of"
    )
    assert inst.rest[0].resource[1].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[1].searchParam[6].type == "reference"
    assert inst.rest[0].resource[1].searchParam[7].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-depends-" "on"
    )
    assert inst.rest[0].resource[1].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[1].searchParam[7].type == "reference"
    assert inst.rest[0].resource[1].searchParam[8].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-derived-" "from"
    )
    assert inst.rest[0].resource[1].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[1].searchParam[8].type == "reference"
    assert inst.rest[0].resource[1].searchParam[9].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-" "predecessor"
    )
    assert inst.rest[0].resource[1].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[1].searchParam[9].type == "reference"
    assert inst.rest[0].resource[1].type == "PlanDefinition"
    assert inst.rest[0].resource[2].interaction[0].code == "read"
    assert inst.rest[0].resource[2].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the "
        "activity definitions"
    )
    assert inst.rest[0].resource[2].interaction[1].code == "search-type"
    assert inst.rest[0].resource[2].interaction[1].documentation == (
        "Search allows clients to filter activity definitions based "
        "on a provided search parameter"
    )
    assert (
        inst.rest[0].resource[2].profile
        == "http://hl7.org/fhir/StructureDefinition/ActivityDefinition"
    )
    assert inst.rest[0].resource[2].searchParam[0].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "description"
    )
    assert inst.rest[0].resource[2].searchParam[0].name == "description"
    assert inst.rest[0].resource[2].searchParam[0].type == "string"
    assert inst.rest[0].resource[2].searchParam[1].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "identifier"
    )
    assert inst.rest[0].resource[2].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[2].searchParam[1].type == "token"
    assert inst.rest[0].resource[2].searchParam[2].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "status"
    )
    assert inst.rest[0].resource[2].searchParam[2].name == "status"
    assert inst.rest[0].resource[2].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[2].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/ActivityDefinition-title"
    )
    assert inst.rest[0].resource[2].searchParam[3].name == "title"
    assert inst.rest[0].resource[2].searchParam[3].type == "string"
    assert (
        inst.rest[0].resource[2].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/ActivityDefinition-topic"
    )
    assert inst.rest[0].resource[2].searchParam[4].name == "topic"
    assert inst.rest[0].resource[2].searchParam[4].type == "token"
    assert inst.rest[0].resource[2].searchParam[5].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "version"
    )
    assert inst.rest[0].resource[2].searchParam[5].name == "version"
    assert inst.rest[0].resource[2].searchParam[5].type == "string"
    assert inst.rest[0].resource[2].searchParam[6].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "composed-of"
    )
    assert inst.rest[0].resource[2].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[2].searchParam[6].type == "reference"
    assert inst.rest[0].resource[2].searchParam[7].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "depends-on"
    )
    assert inst.rest[0].resource[2].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[2].searchParam[7].type == "reference"
    assert inst.rest[0].resource[2].searchParam[8].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "derived-from"
    )
    assert inst.rest[0].resource[2].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[2].searchParam[8].type == "reference"
    assert inst.rest[0].resource[2].searchParam[9].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "predecessor"
    )
    assert inst.rest[0].resource[2].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[2].searchParam[9].type == "reference"
    assert inst.rest[0].resource[2].type == "ActivityDefinition"
    assert inst.rest[0].resource[3].interaction[0].code == "read"
    assert inst.rest[0].resource[3].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "measures"
    )
    assert inst.rest[0].resource[3].interaction[1].code == "search-type"
    assert inst.rest[0].resource[3].interaction[1].documentation == (
        "Search allows clients to filter measures based on a provided"
        " search parameter"
    )
    assert (
        inst.rest[0].resource[3].profile
        == "http://hl7.org/fhir/StructureDefinition/Measure"
    )
    assert (
        inst.rest[0].resource[3].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-description"
    )
    assert inst.rest[0].resource[3].searchParam[0].name == "description"
    assert inst.rest[0].resource[3].searchParam[0].type == "string"
    assert (
        inst.rest[0].resource[3].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-identifier"
    )
    assert inst.rest[0].resource[3].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[3].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-status"
    )
    assert inst.rest[0].resource[3].searchParam[2].name == "status"
    assert inst.rest[0].resource[3].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-title"
    )
    assert inst.rest[0].resource[3].searchParam[3].name == "title"
    assert inst.rest[0].resource[3].searchParam[3].type == "string"
    assert (
        inst.rest[0].resource[3].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-topic"
    )
    assert inst.rest[0].resource[3].searchParam[4].name == "topic"
    assert inst.rest[0].resource[3].searchParam[4].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-version"
    )
    assert inst.rest[0].resource[3].searchParam[5].name == "version"
    assert inst.rest[0].resource[3].searchParam[5].type == "string"
    assert (
        inst.rest[0].resource[3].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-composed-of"
    )
    assert inst.rest[0].resource[3].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[3].searchParam[6].type == "reference"
    assert (
        inst.rest[0].resource[3].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-depends-on"
    )
    assert inst.rest[0].resource[3].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[3].searchParam[7].type == "reference"
    assert (
        inst.rest[0].resource[3].searchParam[8].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-derived-from"
    )
    assert inst.rest[0].resource[3].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[3].searchParam[8].type == "reference"
    assert (
        inst.rest[0].resource[3].searchParam[9].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-predecessor"
    )
    assert inst.rest[0].resource[3].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[3].searchParam[9].type == "reference"
    assert inst.rest[0].resource[3].type == "Measure"
    assert inst.rest[0].resource[4].interaction[0].code == "read"
    assert inst.rest[0].resource[4].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "measures"
    )
    assert inst.rest[0].resource[4].interaction[1].code == "search-type"
    assert inst.rest[0].resource[4].interaction[1].documentation == (
        "Search allows clients to filter measures based on a provided"
        " search parameter"
    )
    assert (
        inst.rest[0].resource[4].profile
        == "http://hl7.org/fhir/StructureDefinition/Questionnaire"
    )
    assert (
        inst.rest[0].resource[4].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-code"
    )
    assert inst.rest[0].resource[4].searchParam[0].name == "code"
    assert inst.rest[0].resource[4].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-context"
    )
    assert inst.rest[0].resource[4].searchParam[1].name == "context"
    assert inst.rest[0].resource[4].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-date"
    )
    assert inst.rest[0].resource[4].searchParam[2].name == "date"
    assert inst.rest[0].resource[4].searchParam[2].type == "date"
    assert (
        inst.rest[0].resource[4].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-identifier"
    )
    assert inst.rest[0].resource[4].searchParam[3].name == "identifier"
    assert inst.rest[0].resource[4].searchParam[3].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-publisher"
    )
    assert inst.rest[0].resource[4].searchParam[4].name == "publisher"
    assert inst.rest[0].resource[4].searchParam[4].type == "string"
    assert (
        inst.rest[0].resource[4].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-status"
    )
    assert inst.rest[0].resource[4].searchParam[5].name == "status"
    assert inst.rest[0].resource[4].searchParam[5].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-title"
    )
    assert inst.rest[0].resource[4].searchParam[6].name == "title"
    assert inst.rest[0].resource[4].searchParam[6].type == "string"
    assert (
        inst.rest[0].resource[4].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-version"
    )
    assert inst.rest[0].resource[4].searchParam[7].name == "version"
    assert inst.rest[0].resource[4].searchParam[7].type == "string"
    assert inst.rest[0].resource[4].type == "Questionnaire"
    assert inst.software.name == "ACME Knowledge Repository Service"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/knowledge-repository"


def test_capabilitystatement2_3(base_settings):
    """No. 3 tests collection for CapabilityStatement2.
    Test File: capabilitystatement2-knowledge-repository.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "capabilitystatement2-knowledge-repository.json"
    )
    inst = capabilitystatement2.CapabilityStatement2.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement2" == inst.resource_type

    impl_capabilitystatement2_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement2" == data["resourceType"]

    inst2 = capabilitystatement2.CapabilityStatement2(**data)
    impl_capabilitystatement2_3(inst2)


def impl_capabilitystatement2_4(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2013-06-18")
    assert inst.description == (
        "Prototype Capability Statement for September 2013 " "Connectathon"
    )
    assert inst.fhirVersion == "4.5.0"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "phr"
    assert inst.kind == "capability"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "PHR Template"
    assert inst.publisher == "FHIR Project"
    assert inst.rest[0].documentation == (
        "Protoype server Capability Statement for September 2013 " "Connectathon"
    )
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
        "When a client searches patients with no search criteria, "
        "they get a list of all patients they have access too. "
        "Servers may elect to offer additional search parameters, but"
        " this is not required"
    )
    assert inst.rest[0].resource[0].type == "Patient"
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[1].code == "search-type"
    assert inst.rest[0].resource[1].searchParam[0].documentation == (
        "_id parameter always supported. For the connectathon, "
        "servers may elect which search parameters are supported"
    )
    assert inst.rest[0].resource[1].searchParam[0].name == "_id"
    assert inst.rest[0].resource[1].searchParam[0].type == "token"
    assert inst.rest[0].resource[1].type == "DocumentReference"
    assert inst.rest[0].resource[2].interaction[0].code == "read"
    assert inst.rest[0].resource[2].interaction[1].code == "search-type"
    assert (
        inst.rest[0].resource[2].searchParam[0].documentation
        == "Standard _id parameter"
    )
    assert inst.rest[0].resource[2].searchParam[0].name == "_id"
    assert inst.rest[0].resource[2].searchParam[0].type == "token"
    assert inst.rest[0].resource[2].type == "Condition"
    assert inst.rest[0].resource[3].interaction[0].code == "read"
    assert inst.rest[0].resource[3].interaction[1].code == "search-type"
    assert (
        inst.rest[0].resource[3].searchParam[0].documentation
        == "Standard _id parameter"
    )
    assert inst.rest[0].resource[3].searchParam[0].name == "_id"
    assert inst.rest[0].resource[3].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[1].documentation
        == "which diagnostic discipline/department created the report"
    )
    assert inst.rest[0].resource[3].searchParam[1].name == "service"
    assert inst.rest[0].resource[3].searchParam[1].type == "token"
    assert inst.rest[0].resource[3].type == "DiagnosticReport"
    assert inst.software.name == "ACME PHR Server"
    assert inst.status == "draft"
    assert inst.text.status == "generated"


def test_capabilitystatement2_4(base_settings):
    """No. 4 tests collection for CapabilityStatement2.
    Test File: capabilitystatement2-phr-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "capabilitystatement2-phr-example.json"
    )
    inst = capabilitystatement2.CapabilityStatement2.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement2" == inst.resource_type

    impl_capabilitystatement2_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement2" == data["resourceType"]

    inst2 = capabilitystatement2.CapabilityStatement2(**data)
    impl_capabilitystatement2_4(inst2)


def impl_capabilitystatement2_5(inst):
    assert inst.contact[0].name == "System Administrator"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].value == "wile@acme.org"
    assert inst.copyright == "Copyright © Acme Healthcare and GoodCorp EHR Systems"
    assert inst.date == fhirtypes.DateTime.validate("2012-01-04")
    assert inst.description == (
        "This is the FHIR capability statement for the main EHR at "
        "ACME for the private interface - it does not describe the "
        "public interface"
    )
    assert inst.experimental is True
    assert inst.fhirVersion == "4.5.0"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "example"
    assert inst.implementation.description == "main EHR at ACME"
    assert inst.implementation.url == "http://10.2.3.4/fhir"
    assert inst.implementationGuide[0] == "http://hl7.org/fhir/us/lab"
    assert (
        inst.instantiates[0] == "http://ihe.org/fhir/CapabilityStatement2/pixm-client"
    )
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.kind == "instance"
    assert inst.name == "ACME-EHR"
    assert inst.patchFormat[0] == "application/xml-patch+xml"
    assert inst.patchFormat[1] == "application/json-patch+json"
    assert inst.publisher == "ACME Corporation"
    assert inst.purpose == (
        "Main EHR capability statement, published for contracting and"
        " operational support"
    )
    assert (
        inst.rest[0].compartment[0]
        == "http://hl7.org/fhir/CompartmentDefinition/patient"
    )
    assert inst.rest[0].documentation == "Main FHIR endpoint for acem health"
    assert inst.rest[0].interaction[0].code == "transaction"
    assert inst.rest[0].interaction[1].code == "history-system"
    assert inst.rest[0].mode == "server"
    assert (
        inst.rest[0].resource[0].documentation
        == "This server does not let the clients create identities."
    )
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[1].code == "vread"
    assert (
        inst.rest[0].resource[0].interaction[1].documentation
        == "Only supported for patient records since 12-Dec 2012"
    )
    assert inst.rest[0].resource[0].interaction[2].code == "update"
    assert inst.rest[0].resource[0].interaction[3].code == "history-instance"
    assert inst.rest[0].resource[0].interaction[4].code == "create"
    assert inst.rest[0].resource[0].interaction[5].code == "history-type"
    assert inst.rest[0].resource[0].profile == (
        "http://registry.fhir.org/r4/StructureDefinition/7896271d-57f"
        "6-4231-89dc-dcc91eab2416"
    )
    assert (
        inst.rest[0].resource[0].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Patient-identifier"
    )
    assert (
        inst.rest[0].resource[0].searchParam[0].documentation
        == "Only supports search by institution MRN"
    )
    assert inst.rest[0].resource[0].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[0].type == "token"
    assert inst.rest[0].resource[0].searchParam[1].definition == (
        "http://hl7.org/fhir/SearchParameter/Patient-general-" "practitioner"
    )
    assert inst.rest[0].resource[0].searchParam[1].name == "general-practitioner"
    assert inst.rest[0].resource[0].searchParam[1].type == "reference"
    assert inst.rest[0].resource[0].supportedProfile[0] == (
        "http://registry.fhir.org/r4/StructureDefinition/00ab9e7a-06c"
        "7-4f77-9234-4154ca1e3347"
    )
    assert inst.rest[0].resource[0].type == "Patient"
    assert inst.software.name == "EHR"
    assert inst.software.releaseDate == fhirtypes.DateTime.validate("2012-01-04")
    assert inst.software.version == "0.00.020.2134"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "ACME EHR capability statement"
    assert inst.url == "urn:uuid:68D043B5-9ECF-4559-A57A-396E0D452311"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "positive"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variant-state"
    )
    assert inst.version == "20130510"


def test_capabilitystatement2_5(base_settings):
    """No. 5 tests collection for CapabilityStatement2.
    Test File: capabilitystatement2-example.json
    """
    filename = base_settings["unittest_data_dir"] / "capabilitystatement2-example.json"
    inst = capabilitystatement2.CapabilityStatement2.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement2" == inst.resource_type

    impl_capabilitystatement2_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement2" == data["resourceType"]

    inst2 = capabilitystatement2.CapabilityStatement2(**data)
    impl_capabilitystatement2_5(inst2)
