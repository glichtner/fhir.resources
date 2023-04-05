# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import capabilitystatement


def impl_capabilitystatement_1(inst):
    assert inst.contact[0].name == "System Administrator"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].value == "wile@acme.org"
    assert inst.date == fhirtypes.DateTime.validate("2012-01-04")
    assert inst.description == (
    "Sample capability statement showing new MessageDefinition "
    "structure"
    )
    assert inst.experimental is True
    assert inst.fhirVersion == "5.0.0"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "messagedefinition"
    assert inst.implementation.description == "Acme Message endpoint"
    assert inst.implementation.url == "http://acem.com/fhir/message-drop"
    assert inst.kind == "instance"
    assert inst.messaging[0].documentation == "ADT A08 equivalent for external system notifications"
    assert inst.messaging[0].endpoint[0].address == "mllp:10.1.1.10:9234"
    assert inst.messaging[0].endpoint[0].protocol.code == "mllp"
    assert inst.messaging[0].endpoint[0].protocol.system == "http://hl7.org/fhir/message-transport"
    assert inst.messaging[0].reliableCache == 30
    assert inst.messaging[0].supportedMessage[0].definition == "http://hl7.org/fhir/MessageDefinition/example"
    assert inst.messaging[0].supportedMessage[0].mode == "receiver"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.publisher == "ACME Corporation"
    assert inst.software.name == "EHR"
    assert inst.status == "draft"


def test_capabilitystatement_1(base_settings):
    """No. 1 tests collection for CapabilityStatement.
    Test File: capabilitystatement-messagedefinition.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "capabilitystatement-messagedefinition.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_1(inst2)


def impl_capabilitystatement_2(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2023-03-26T15:21:02+11:00")
    assert inst.experimental is True
    assert inst.fhirVersion == "5.0.0"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "base2"
    assert inst.kind == "capability"
    assert inst.name == "Base FHIR Capability Statement (Empty)"
    assert inst.publisher == "FHIR Project Team"
    assert inst.rest[0].documentation == "An empty Capability Statement"
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.description == (
    "This is the Capability Statement to declare that the server "
    "supports SMART-on-FHIR. See the SMART-on-FHIR docs for the "
    "extension that would go with such a server"
    )
    assert inst.rest[0].security.service[0].coding[0].code == "SMART-on-FHIR"
    assert inst.rest[0].security.service[0].coding[0].display == "SMART-on-FHIR"
    assert inst.rest[0].security.service[0].coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/restful-security-"
    "service"
    )
    assert inst.rest[0].security.service[0].text == "See http://docs.smarthealthit.org/"
    assert inst.software.name == "Insert your software name here..."
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert inst.url == "http://hl7.org/fhir/CapabilityStatement/base2"
    assert inst.version == "5.0.0"


def test_capabilitystatement_2(base_settings):
    """No. 2 tests collection for CapabilityStatement.
    Test File: capabilitystatement-base2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "capabilitystatement-base2.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_2(inst2)


def impl_capabilitystatement_3(inst):
    assert inst.date == fhirtypes.DateTime.validate("2022-09-01")
    assert inst.description == (
    "Example capability statement for a Terminology Server. A "
    "server can support more fucntionality than defined here, but"
    " this is the minimum amount"
    )
    assert inst.experimental is True
    assert inst.fhirVersion == "5.0.0"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "example-terminology-server"
    assert inst.implementation.description == "The ACME FHIR Terminology Server"
    assert inst.kind == "instance"
    assert inst.name == "ACMETerminologyServiceCapabilityStatement"
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[0].interaction[0].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert inst.rest[0].resource[0].interaction[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[0].interaction[1].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[0].operation[0].definition == "http://hl7.org/fhir/OperationDefinition/CodeSystem-lookup"
    assert inst.rest[0].resource[0].operation[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[0].operation[0].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[0].operation[0].name == "expand"
    assert inst.rest[0].resource[0].operation[1].definition == (
    "http://hl7.org/fhir/OperationDefinition/CodeSystem-validate-"
    "code"
    )
    assert inst.rest[0].resource[0].operation[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[0].operation[1].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[0].operation[1].name == "expand"
    assert inst.rest[0].resource[0].operation[2].definition == "http://hl7.org/fhir/OperationDefinition/CodeSystem-subsumes"
    assert inst.rest[0].resource[0].operation[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[0].operation[2].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[0].operation[2].name == "expand"
    assert inst.rest[0].resource[0].profile == "http://hl7.org/fhir/StructureDefinition/CodeSystem"
    assert inst.rest[0].resource[0].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/CodeSystem-url"
    assert inst.rest[0].resource[0].searchParam[0].name == "url"
    assert inst.rest[0].resource[0].searchParam[0].type == "uri"
    assert inst.rest[0].resource[0].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/CodeSystem-version"
    assert inst.rest[0].resource[0].searchParam[1].name == "version"
    assert inst.rest[0].resource[0].searchParam[1].type == "token"
    assert inst.rest[0].resource[0].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/CodeSystem-name"
    assert inst.rest[0].resource[0].searchParam[2].name == "name"
    assert inst.rest[0].resource[0].searchParam[2].type == "string"
    assert inst.rest[0].resource[0].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/CodeSystem-title"
    assert inst.rest[0].resource[0].searchParam[3].name == "title"
    assert inst.rest[0].resource[0].searchParam[3].type == "string"
    assert inst.rest[0].resource[0].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/CodeSystem-status"
    assert inst.rest[0].resource[0].searchParam[4].name == "status"
    assert inst.rest[0].resource[0].searchParam[4].type == "token"
    assert inst.rest[0].resource[0].type == "CodeSystem"
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[1].interaction[0].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[1].interaction[1].code == "search-type"
    assert inst.rest[0].resource[1].interaction[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[1].interaction[1].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[1].operation[0].definition == "http://hl7.org/fhir/OperationDefinition/ValueSet-expand"
    assert inst.rest[0].resource[1].operation[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[1].operation[0].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[1].operation[0].name == "expand"
    assert inst.rest[0].resource[1].operation[1].definition == (
    "http://hl7.org/fhir/OperationDefinition/ValueSet-validate-"
    "code"
    )
    assert inst.rest[0].resource[1].operation[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[1].operation[1].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[1].operation[1].name == "expand"
    assert inst.rest[0].resource[1].profile == "http://hl7.org/fhir/StructureDefinition/ValueSet"
    assert inst.rest[0].resource[1].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/ValueSet-url"
    assert inst.rest[0].resource[1].searchParam[0].name == "url"
    assert inst.rest[0].resource[1].searchParam[0].type == "uri"
    assert inst.rest[0].resource[1].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/ValueSet-version"
    assert inst.rest[0].resource[1].searchParam[1].name == "version"
    assert inst.rest[0].resource[1].searchParam[1].type == "token"
    assert inst.rest[0].resource[1].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/ValueSet-name"
    assert inst.rest[0].resource[1].searchParam[2].name == "name"
    assert inst.rest[0].resource[1].searchParam[2].type == "string"
    assert inst.rest[0].resource[1].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/ValueSet-title"
    assert inst.rest[0].resource[1].searchParam[3].name == "title"
    assert inst.rest[0].resource[1].searchParam[3].type == "string"
    assert inst.rest[0].resource[1].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/ValueSet-status"
    assert inst.rest[0].resource[1].searchParam[4].name == "status"
    assert inst.rest[0].resource[1].searchParam[4].type == "token"
    assert inst.rest[0].resource[1].type == "ValueSet"
    assert inst.rest[0].resource[2].interaction[0].code == "read"
    assert inst.rest[0].resource[2].interaction[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[2].interaction[0].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[2].interaction[1].code == "search-type"
    assert inst.rest[0].resource[2].interaction[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[2].interaction[1].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[2].operation[0].definition == "http://hl7.org/fhir/OperationDefinition/ConceptMap-translate"
    assert inst.rest[0].resource[2].operation[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
    "expectation"
    )
    assert inst.rest[0].resource[2].operation[0].extension[0].valueCode == "SHALL"
    assert inst.rest[0].resource[2].operation[0].name == "expand"
    assert inst.rest[0].resource[2].profile == "http://hl7.org/fhir/StructureDefinition/ConceptMap"
    assert inst.rest[0].resource[2].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/ConceptMap-url"
    assert inst.rest[0].resource[2].searchParam[0].name == "url"
    assert inst.rest[0].resource[2].searchParam[0].type == "uri"
    assert inst.rest[0].resource[2].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/ConceptMap-version"
    assert inst.rest[0].resource[2].searchParam[1].name == "version"
    assert inst.rest[0].resource[2].searchParam[1].type == "token"
    assert inst.rest[0].resource[2].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/ConceptMap-name"
    assert inst.rest[0].resource[2].searchParam[2].name == "name"
    assert inst.rest[0].resource[2].searchParam[2].type == "string"
    assert inst.rest[0].resource[2].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/ConceptMap-title"
    assert inst.rest[0].resource[2].searchParam[3].name == "title"
    assert inst.rest[0].resource[2].searchParam[3].type == "string"
    assert inst.rest[0].resource[2].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/ConceptMap-status"
    assert inst.rest[0].resource[2].searchParam[4].name == "status"
    assert inst.rest[0].resource[2].searchParam[4].type == "token"
    assert inst.rest[0].resource[2].type == "ConceptMap"
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert inst.title == "ACME Terminology Service — Capability Statement"
    assert inst.url == "http://hl7.org/fhir/CapabilityStatement/terminology-server"
    assert inst.version == "5.0.0"


def test_capabilitystatement_3(base_settings):
    """No. 3 tests collection for CapabilityStatement.
    Test File: capabilitystatement-terminology-server.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "capabilitystatement-terminology-server.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_3(inst2)


def impl_capabilitystatement_4(inst):
    assert inst.contact[0].name == "FHIR Project"
    assert inst.contact[0].telecom[0].system == "other"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2016-09-16")
    assert inst.description == (
    "Basic conformance statement for a Measure Processor Service."
    " A server can support more functionality    than defined "
    "here, but this is the minimum amount"
    )
    assert inst.fhirVersion == "5.0.0"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "measure-processor"
    assert inst.kind == "capability"
    assert inst.name == "MeasureProcessorServiceConformanceStatement"
    assert inst.publisher == "HL7, Inc"
    assert inst.rest[0].documentation == "RESTful Measure Processor Service"
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].operation[0].definition == (
    "http://hl7.org/fhir/OperationDefinition/Measure-evaluate-"
    "measure"
    )
    assert inst.rest[0].operation[0].name == "evaluate-measure"
    assert inst.rest[0].operation[1].definition == (
    "http://hl7.org/fhir/OperationDefinition/Measure-data-"
    "requirements"
    )
    assert inst.rest[0].operation[1].name == "data-requirements"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
    "Read allows clients to get the logical definitions of the "
    "measures"
    )
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
    "Search allows clients to filter measures based on a provided"
    " search parameter"
    )
    assert inst.rest[0].resource[0].profile == "http://hl7.org/fhir/StructureDefinition/Measure"
    assert inst.rest[0].resource[0].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/Measure-identifier"
    assert inst.rest[0].resource[0].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[0].type == "token"
    assert inst.rest[0].resource[0].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/Measure-status"
    assert inst.rest[0].resource[0].searchParam[1].name == "status"
    assert inst.rest[0].resource[0].searchParam[1].type == "token"
    assert inst.rest[0].resource[0].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/Measure-version"
    assert inst.rest[0].resource[0].searchParam[2].name == "version"
    assert inst.rest[0].resource[0].searchParam[2].type == "token"
    assert inst.rest[0].resource[0].type == "Measure"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.service[0].coding[0].code == "Certificates"
    assert inst.rest[0].security.service[0].coding[0].system == "http://hl7.org/fhir/restful-security-service"
    assert inst.software.name == "ACME Measure Processor Service"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Measure Processor Service Conformance Statement"
    assert inst.url == "http://hl7.org/fhir/measure-processor"


def test_capabilitystatement_4(base_settings):
    """No. 4 tests collection for CapabilityStatement.
    Test File: capabilitystatement-measure-processor.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "capabilitystatement-measure-processor.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_4(inst2)


def impl_capabilitystatement_5(inst):
    assert inst.contact[0].name == "FHIR Project"
    assert inst.contact[0].telecom[0].system == "other"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2017-02-25")
    assert inst.description == (
    "Basic conformance statement for a Knowledge Repository "
    "Service. A server can support more functionality    than "
    "defined here, but this is the minimum amount"
    )
    assert inst.fhirVersion == "5.0.0"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "knowledge-repository"
    assert inst.kind == "capability"
    assert inst.name == "KnowledgeRepositoryServiceConformanceStatement"
    assert inst.publisher == "HL7, Inc"
    assert inst.rest[0].documentation == "RESTful Knowledge Repository Service"
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].operation[0].definition == (
    "http://hl7.org/fhir/OperationDefinition/Library-data-"
    "requirements"
    )
    assert inst.rest[0].operation[0].name == "data-requirements"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
    "Read allows clients to get the logical definitions of the "
    "libraries"
    )
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
    "Search allows clients to filter libraries based on a "
    "provided search parameter"
    )
    assert inst.rest[0].resource[0].profile == "http://hl7.org/fhir/StructureDefinition/Library"
    assert inst.rest[0].resource[0].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/Library-description"
    assert inst.rest[0].resource[0].searchParam[0].name == "description"
    assert inst.rest[0].resource[0].searchParam[0].type == "string"
    assert inst.rest[0].resource[0].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/Library-identifier"
    assert inst.rest[0].resource[0].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[1].type == "token"
    assert inst.rest[0].resource[0].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/Library-status"
    assert inst.rest[0].resource[0].searchParam[2].name == "status"
    assert inst.rest[0].resource[0].searchParam[2].type == "token"
    assert inst.rest[0].resource[0].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/Library-title"
    assert inst.rest[0].resource[0].searchParam[3].name == "title"
    assert inst.rest[0].resource[0].searchParam[3].type == "string"
    assert inst.rest[0].resource[0].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/Library-topic"
    assert inst.rest[0].resource[0].searchParam[4].name == "topic"
    assert inst.rest[0].resource[0].searchParam[4].type == "token"
    assert inst.rest[0].resource[0].searchParam[5].definition == "http://hl7.org/fhir/SearchParameter/Library-version"
    assert inst.rest[0].resource[0].searchParam[5].name == "version"
    assert inst.rest[0].resource[0].searchParam[5].type == "token"
    assert inst.rest[0].resource[0].searchParam[6].definition == "http://hl7.org/fhir/SearchParameter/Library-composed-of"
    assert inst.rest[0].resource[0].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[0].searchParam[6].type == "reference"
    assert inst.rest[0].resource[0].searchParam[7].definition == "http://hl7.org/fhir/SearchParameter/Library-depends-on"
    assert inst.rest[0].resource[0].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[0].searchParam[7].type == "reference"
    assert inst.rest[0].resource[0].searchParam[8].definition == "http://hl7.org/fhir/SearchParameter/Library-derived-from"
    assert inst.rest[0].resource[0].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[0].searchParam[8].type == "reference"
    assert inst.rest[0].resource[0].searchParam[9].definition == "http://hl7.org/fhir/SearchParameter/Library-predecessor"
    assert inst.rest[0].resource[0].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[0].searchParam[9].type == "reference"
    assert inst.rest[0].resource[0].type == "Library"
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[0].documentation == (
    "Read allows clients to get the logical definitions of the "
    "plan definitions"
    )
    assert inst.rest[0].resource[1].interaction[1].code == "search-type"
    assert inst.rest[0].resource[1].interaction[1].documentation == (
    "Search allows clients to filter plan definitions based on a "
    "provided search parameter"
    )
    assert inst.rest[0].resource[1].profile == "http://hl7.org/fhir/StructureDefinition/PlanDefinition"
    assert inst.rest[0].resource[1].searchParam[0].definition == (
    "http://hl7.org/fhir/SearchParameter/PlanDefinition-"
    "description"
    )
    assert inst.rest[0].resource[1].searchParam[0].name == "description"
    assert inst.rest[0].resource[1].searchParam[0].type == "string"
    assert inst.rest[0].resource[1].searchParam[1].definition == (
    "http://hl7.org/fhir/SearchParameter/PlanDefinition-"
    "identifier"
    )
    assert inst.rest[0].resource[1].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[1].searchParam[1].type == "token"
    assert inst.rest[0].resource[1].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/PlanDefinition-status"
    assert inst.rest[0].resource[1].searchParam[2].name == "status"
    assert inst.rest[0].resource[1].searchParam[2].type == "token"
    assert inst.rest[0].resource[1].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/PlanDefinition-title"
    assert inst.rest[0].resource[1].searchParam[3].name == "title"
    assert inst.rest[0].resource[1].searchParam[3].type == "string"
    assert inst.rest[0].resource[1].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/PlanDefinition-topic"
    assert inst.rest[0].resource[1].searchParam[4].name == "topic"
    assert inst.rest[0].resource[1].searchParam[4].type == "token"
    assert inst.rest[0].resource[1].searchParam[5].definition == "http://hl7.org/fhir/SearchParameter/PlanDefinition-version"
    assert inst.rest[0].resource[1].searchParam[5].name == "version"
    assert inst.rest[0].resource[1].searchParam[5].type == "token"
    assert inst.rest[0].resource[1].searchParam[6].definition == (
    "http://hl7.org/fhir/SearchParameter/PlanDefinition-composed-"
    "of"
    )
    assert inst.rest[0].resource[1].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[1].searchParam[6].type == "reference"
    assert inst.rest[0].resource[1].searchParam[7].definition == (
    "http://hl7.org/fhir/SearchParameter/PlanDefinition-depends-"
    "on"
    )
    assert inst.rest[0].resource[1].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[1].searchParam[7].type == "reference"
    assert inst.rest[0].resource[1].searchParam[8].definition == (
    "http://hl7.org/fhir/SearchParameter/PlanDefinition-derived-"
    "from"
    )
    assert inst.rest[0].resource[1].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[1].searchParam[8].type == "reference"
    assert inst.rest[0].resource[1].searchParam[9].definition == (
    "http://hl7.org/fhir/SearchParameter/PlanDefinition-"
    "predecessor"
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
    assert inst.rest[0].resource[2].profile == "http://hl7.org/fhir/StructureDefinition/ActivityDefinition"
    assert inst.rest[0].resource[2].searchParam[0].definition == (
    "http://hl7.org/fhir/SearchParameter/ActivityDefinition-"
    "description"
    )
    assert inst.rest[0].resource[2].searchParam[0].name == "description"
    assert inst.rest[0].resource[2].searchParam[0].type == "string"
    assert inst.rest[0].resource[2].searchParam[1].definition == (
    "http://hl7.org/fhir/SearchParameter/ActivityDefinition-"
    "identifier"
    )
    assert inst.rest[0].resource[2].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[2].searchParam[1].type == "token"
    assert inst.rest[0].resource[2].searchParam[2].definition == (
    "http://hl7.org/fhir/SearchParameter/ActivityDefinition-"
    "status"
    )
    assert inst.rest[0].resource[2].searchParam[2].name == "status"
    assert inst.rest[0].resource[2].searchParam[2].type == "token"
    assert inst.rest[0].resource[2].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/ActivityDefinition-title"
    assert inst.rest[0].resource[2].searchParam[3].name == "title"
    assert inst.rest[0].resource[2].searchParam[3].type == "string"
    assert inst.rest[0].resource[2].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/ActivityDefinition-topic"
    assert inst.rest[0].resource[2].searchParam[4].name == "topic"
    assert inst.rest[0].resource[2].searchParam[4].type == "token"
    assert inst.rest[0].resource[2].searchParam[5].definition == (
    "http://hl7.org/fhir/SearchParameter/ActivityDefinition-"
    "version"
    )
    assert inst.rest[0].resource[2].searchParam[5].name == "version"
    assert inst.rest[0].resource[2].searchParam[5].type == "token"
    assert inst.rest[0].resource[2].searchParam[6].definition == (
    "http://hl7.org/fhir/SearchParameter/ActivityDefinition-"
    "composed-of"
    )
    assert inst.rest[0].resource[2].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[2].searchParam[6].type == "reference"
    assert inst.rest[0].resource[2].searchParam[7].definition == (
    "http://hl7.org/fhir/SearchParameter/ActivityDefinition-"
    "depends-on"
    )
    assert inst.rest[0].resource[2].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[2].searchParam[7].type == "reference"
    assert inst.rest[0].resource[2].searchParam[8].definition == (
    "http://hl7.org/fhir/SearchParameter/ActivityDefinition-"
    "derived-from"
    )
    assert inst.rest[0].resource[2].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[2].searchParam[8].type == "reference"
    assert inst.rest[0].resource[2].searchParam[9].definition == (
    "http://hl7.org/fhir/SearchParameter/ActivityDefinition-"
    "predecessor"
    )
    assert inst.rest[0].resource[2].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[2].searchParam[9].type == "reference"
    assert inst.rest[0].resource[2].type == "ActivityDefinition"
    assert inst.rest[0].resource[3].interaction[0].code == "read"
    assert inst.rest[0].resource[3].interaction[0].documentation == (
    "Read allows clients to get the logical definitions of the "
    "measures"
    )
    assert inst.rest[0].resource[3].interaction[1].code == "search-type"
    assert inst.rest[0].resource[3].interaction[1].documentation == (
    "Search allows clients to filter measures based on a provided"
    " search parameter"
    )
    assert inst.rest[0].resource[3].profile == "http://hl7.org/fhir/StructureDefinition/Measure"
    assert inst.rest[0].resource[3].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/Measure-description"
    assert inst.rest[0].resource[3].searchParam[0].name == "description"
    assert inst.rest[0].resource[3].searchParam[0].type == "string"
    assert inst.rest[0].resource[3].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/Measure-identifier"
    assert inst.rest[0].resource[3].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[3].searchParam[1].type == "token"
    assert inst.rest[0].resource[3].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/Measure-status"
    assert inst.rest[0].resource[3].searchParam[2].name == "status"
    assert inst.rest[0].resource[3].searchParam[2].type == "token"
    assert inst.rest[0].resource[3].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/Measure-title"
    assert inst.rest[0].resource[3].searchParam[3].name == "title"
    assert inst.rest[0].resource[3].searchParam[3].type == "string"
    assert inst.rest[0].resource[3].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/Measure-topic"
    assert inst.rest[0].resource[3].searchParam[4].name == "topic"
    assert inst.rest[0].resource[3].searchParam[4].type == "token"
    assert inst.rest[0].resource[3].searchParam[5].definition == "http://hl7.org/fhir/SearchParameter/Measure-version"
    assert inst.rest[0].resource[3].searchParam[5].name == "version"
    assert inst.rest[0].resource[3].searchParam[5].type == "token"
    assert inst.rest[0].resource[3].searchParam[6].definition == "http://hl7.org/fhir/SearchParameter/Measure-composed-of"
    assert inst.rest[0].resource[3].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[3].searchParam[6].type == "reference"
    assert inst.rest[0].resource[3].searchParam[7].definition == "http://hl7.org/fhir/SearchParameter/Measure-depends-on"
    assert inst.rest[0].resource[3].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[3].searchParam[7].type == "reference"
    assert inst.rest[0].resource[3].searchParam[8].definition == "http://hl7.org/fhir/SearchParameter/Measure-derived-from"
    assert inst.rest[0].resource[3].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[3].searchParam[8].type == "reference"
    assert inst.rest[0].resource[3].searchParam[9].definition == "http://hl7.org/fhir/SearchParameter/Measure-predecessor"
    assert inst.rest[0].resource[3].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[3].searchParam[9].type == "reference"
    assert inst.rest[0].resource[3].type == "Measure"
    assert inst.rest[0].resource[4].interaction[0].code == "read"
    assert inst.rest[0].resource[4].interaction[0].documentation == (
    "Read allows clients to get the logical definitions of the "
    "measures"
    )
    assert inst.rest[0].resource[4].interaction[1].code == "search-type"
    assert inst.rest[0].resource[4].interaction[1].documentation == (
    "Search allows clients to filter measures based on a provided"
    " search parameter"
    )
    assert inst.rest[0].resource[4].profile == "http://hl7.org/fhir/StructureDefinition/Questionnaire"
    assert inst.rest[0].resource[4].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/Questionnaire-code"
    assert inst.rest[0].resource[4].searchParam[0].name == "code"
    assert inst.rest[0].resource[4].searchParam[0].type == "token"
    assert inst.rest[0].resource[4].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/Questionnaire-context"
    assert inst.rest[0].resource[4].searchParam[1].name == "context"
    assert inst.rest[0].resource[4].searchParam[1].type == "token"
    assert inst.rest[0].resource[4].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/Questionnaire-date"
    assert inst.rest[0].resource[4].searchParam[2].name == "date"
    assert inst.rest[0].resource[4].searchParam[2].type == "date"
    assert inst.rest[0].resource[4].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/Questionnaire-identifier"
    assert inst.rest[0].resource[4].searchParam[3].name == "identifier"
    assert inst.rest[0].resource[4].searchParam[3].type == "token"
    assert inst.rest[0].resource[4].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/Questionnaire-publisher"
    assert inst.rest[0].resource[4].searchParam[4].name == "publisher"
    assert inst.rest[0].resource[4].searchParam[4].type == "string"
    assert inst.rest[0].resource[4].searchParam[5].definition == "http://hl7.org/fhir/SearchParameter/Questionnaire-status"
    assert inst.rest[0].resource[4].searchParam[5].name == "status"
    assert inst.rest[0].resource[4].searchParam[5].type == "token"
    assert inst.rest[0].resource[4].searchParam[6].definition == "http://hl7.org/fhir/SearchParameter/Questionnaire-title"
    assert inst.rest[0].resource[4].searchParam[6].name == "title"
    assert inst.rest[0].resource[4].searchParam[6].type == "string"
    assert inst.rest[0].resource[4].searchParam[7].definition == "http://hl7.org/fhir/SearchParameter/Questionnaire-version"
    assert inst.rest[0].resource[4].searchParam[7].name == "version"
    assert inst.rest[0].resource[4].searchParam[7].type == "token"
    assert inst.rest[0].resource[4].type == "Questionnaire"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.service[0].coding[0].code == "Certificates"
    assert inst.rest[0].security.service[0].coding[0].system == "http://hl7.org/fhir/restful-security-service"
    assert inst.software.name == "ACME Knowledge Repository Service"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Knowledge Repository Service Conformance Statement"
    assert inst.url == "http://hl7.org/fhir/knowledge-repository"


def test_capabilitystatement_5(base_settings):
    """No. 5 tests collection for CapabilityStatement.
    Test File: capabilitystatement-knowledge-repository.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "capabilitystatement-knowledge-repository.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_5(inst2)


def impl_capabilitystatement_6(inst):
    assert inst.acceptLanguage[0] == "en"
    assert inst.acceptLanguage[1] == "es"
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
    assert inst.document[0].documentation == "Basic rules for all documents in the EHR system"
    assert inst.document[0].mode == "consumer"
    assert inst.document[0].profile == (
    "http://fhir.hl7.org/base/Profilebc054d23-75e1-4dc6-aca5-838b"
    "6b1ac81d/_history/b5fdd9fc-b021-4ea1-911a-721a60663796"
    )
    assert inst.experimental is True
    assert inst.fhirVersion == "5.0.0"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "example"
    assert inst.implementation.description == "main EHR at ACME"
    assert inst.implementation.url == "http://10.2.3.4/fhir"
    assert inst.implementationGuide[0] == "http://example.org/fhir/us/lab"
    assert inst.instantiates[0] == "http://ihe.org/fhir/CapabilityStatement/pixm-client"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.kind == "instance"
    assert inst.messaging[0].documentation == "ADT A08 equivalent for external system notifications"
    assert inst.messaging[0].endpoint[0].address == "mllp:10.1.1.10:9234"
    assert inst.messaging[0].endpoint[0].protocol.code == "mllp"
    assert inst.messaging[0].endpoint[0].protocol.system == "http://hl7.org/fhir/message-transport"
    assert inst.messaging[0].reliableCache == 30
    assert inst.messaging[0].supportedMessage[0].definition == "http://hl7.org/fhir/MessageDefinition/example"
    assert inst.messaging[0].supportedMessage[0].mode == "receiver"
    assert inst.name == "ACMEEHR"
    assert inst.patchFormat[0] == "application/xml-patch+xml"
    assert inst.patchFormat[1] == "application/json-patch+json"
    assert inst.publisher == "ACME Corporation"
    assert inst.purpose == (
    "Main EHR capability statement, published for contracting and"
    " operational support"
    )
    assert inst.rest[0].compartment[0] == "http://hl7.org/fhir/CompartmentDefinition/patient"
    assert inst.rest[0].documentation == "Main FHIR endpoint for acem health"
    assert inst.rest[0].interaction[0].code == "transaction"
    assert inst.rest[0].interaction[1].code == "history-system"
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].resource[0].conditionalCreate is True
    assert inst.rest[0].resource[0].conditionalDelete == "not-supported"
    assert inst.rest[0].resource[0].conditionalPatch is False
    assert inst.rest[0].resource[0].conditionalRead == "full-support"
    assert inst.rest[0].resource[0].conditionalUpdate is False
    assert inst.rest[0].resource[0].documentation == "This server does not let the clients create identities."
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[1].code == "vread"
    assert inst.rest[0].resource[0].interaction[1].documentation == "Only supported for patient records since 12-Dec 2012"
    assert inst.rest[0].resource[0].interaction[2].code == "update"
    assert inst.rest[0].resource[0].interaction[3].code == "history-instance"
    assert inst.rest[0].resource[0].interaction[4].code == "create"
    assert inst.rest[0].resource[0].interaction[5].code == "history-type"
    assert inst.rest[0].resource[0].profile == (
    "http://registry.fhir.org/r5/StructureDefinition/7896271d-57f"
    "6-4231-89dc-dcc91eab2416"
    )
    assert inst.rest[0].resource[0].readHistory is True
    assert inst.rest[0].resource[0].searchInclude[0] == "Patient:organization"
    assert inst.rest[0].resource[0].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/Patient-identifier"
    assert inst.rest[0].resource[0].searchParam[0].documentation == "Only supports search by institution MRN"
    assert inst.rest[0].resource[0].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[0].type == "token"
    assert inst.rest[0].resource[0].searchParam[1].definition == (
    "http://hl7.org/fhir/SearchParameter/Patient-general-"
    "practitioner"
    )
    assert inst.rest[0].resource[0].searchParam[1].name == "general-practitioner"
    assert inst.rest[0].resource[0].searchParam[1].type == "reference"
    assert inst.rest[0].resource[0].searchRevInclude[0] == "Person:patient"
    assert inst.rest[0].resource[0].supportedProfile[0] == (
    "http://registry.fhir.org/r5/StructureDefinition/00ab9e7a-06c"
    "7-4f77-9234-4154ca1e3347"
    )
    assert inst.rest[0].resource[0].type == "Patient"
    assert inst.rest[0].resource[0].updateCreate is False
    assert inst.rest[0].resource[0].versioning == "versioned-update"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.description == "See Smart on FHIR documentation"
    assert inst.rest[0].security.service[0].coding[0].code == "SMART-on-FHIR"
    assert inst.rest[0].security.service[0].coding[0].system == "http://hl7.org/fhir/restful-security-service"
    assert inst.software.name == "EHR"
    assert inst.software.releaseDate == fhirtypes.DateTime.validate("2012-01-04")
    assert inst.software.version == "0.00.020.2134"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "ACME EHR capability statement"
    assert inst.url == "urn:uuid:68d043b5-9ecf-4559-a57a-396e0d452311"
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "positive"
    assert inst.useContext[0].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/variant-state"
    assert inst.version == "20130510"


def test_capabilitystatement_6(base_settings):
    """No. 6 tests collection for CapabilityStatement.
    Test File: capabilitystatement-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "capabilitystatement-example.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_6(inst2)


def impl_capabilitystatement_7(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2013-06-18")
    assert inst.description == (
    "Prototype Capability Statement for September 2013 "
    "Connectathon"
    )
    assert inst.fhirVersion == "5.0.0"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "phr"
    assert inst.kind == "capability"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "PHRTemplate"
    assert inst.publisher == "FHIR Project"
    assert inst.rest[0].documentation == (
    "Protoype server Capability Statement for September 2013 "
    "Connectathon"
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
    assert inst.rest[0].resource[2].searchParam[0].documentation == "Standard _id parameter"
    assert inst.rest[0].resource[2].searchParam[0].name == "_id"
    assert inst.rest[0].resource[2].searchParam[0].type == "token"
    assert inst.rest[0].resource[2].type == "Condition"
    assert inst.rest[0].resource[3].interaction[0].code == "read"
    assert inst.rest[0].resource[3].interaction[1].code == "search-type"
    assert inst.rest[0].resource[3].searchParam[0].documentation == "Standard _id parameter"
    assert inst.rest[0].resource[3].searchParam[0].name == "_id"
    assert inst.rest[0].resource[3].searchParam[0].type == "token"
    assert inst.rest[0].resource[3].searchParam[1].documentation == "which diagnostic discipline/department created the report"
    assert inst.rest[0].resource[3].searchParam[1].name == "service"
    assert inst.rest[0].resource[3].searchParam[1].type == "token"
    assert inst.rest[0].resource[3].type == "DiagnosticReport"
    assert inst.rest[0].security.service[0].text == "OAuth"
    assert inst.software.name == "ACME PHR Server"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "PHR Template"


def test_capabilitystatement_7(base_settings):
    """No. 7 tests collection for CapabilityStatement.
    Test File: capabilitystatement-phr-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "capabilitystatement-phr-example.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_7(inst2)


def impl_capabilitystatement_8(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2023-03-26T15:21:02+11:00")
    assert inst.experimental is True
    assert inst.fhirVersion == "5.0.0"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "base"
    assert inst.kind == "capability"
    assert inst.name == "Base FHIR Capability Statement (Full)"
    assert inst.publisher == "FHIR Project Team"
    assert inst.rest[0].documentation == "All the functionality defined in FHIR"
    assert inst.rest[0].interaction[0].code == "transaction"
    assert inst.rest[0].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].interaction[1].code == "batch"
    assert inst.rest[0].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].interaction[2].code == "history-system"
    assert inst.rest[0].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].interaction[3].code == "search-system"
    assert inst.rest[0].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].operation[0].definition == "http://hl7.org/fhir/OperationDefinition/resource-validate"
    assert inst.rest[0].operation[0].name == "validate"
    assert inst.rest[0].operation[1].definition == "http://hl7.org/fhir/OperationDefinition/resource-meta"
    assert inst.rest[0].operation[1].name == "meta"
    assert inst.rest[0].operation[2].definition == "http://hl7.org/fhir/OperationDefinition/resource-meta-add"
    assert inst.rest[0].operation[2].name == "meta-add"
    assert inst.rest[0].operation[3].definition == "http://hl7.org/fhir/OperationDefinition/resource-meta-delete"
    assert inst.rest[0].operation[3].name == "meta-delete"
    assert inst.rest[0].operation[4].definition == "http://hl7.org/fhir/OperationDefinition/resource-convert"
    assert inst.rest[0].operation[4].name == "convert"
    assert inst.rest[0].operation[5].definition == "http://hl7.org/fhir/OperationDefinition/resource-graphql"
    assert inst.rest[0].operation[5].name == "graphql"
    assert inst.rest[0].operation[6].definition == "http://hl7.org/fhir/OperationDefinition/resource-graph"
    assert inst.rest[0].operation[6].name == "graph"
    assert inst.rest[0].operation[7].definition == "http://hl7.org/fhir/OperationDefinition/resource-add"
    assert inst.rest[0].operation[7].name == "add"
    assert inst.rest[0].operation[8].definition == "http://hl7.org/fhir/OperationDefinition/resource-remove"
    assert inst.rest[0].operation[8].name == "remove"
    assert inst.rest[0].operation[9].definition == "http://hl7.org/fhir/OperationDefinition/resource-filter"
    assert inst.rest[0].operation[9].name == "filter"
    assert inst.rest[0].resource[0].conditionalCreate is True
    assert inst.rest[0].resource[0].conditionalDelete == "multiple"
    assert inst.rest[0].resource[0].conditionalUpdate is True
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[0].interaction[1].code == "vread"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[0].interaction[2].code == "update"
    assert inst.rest[0].resource[0].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[0].interaction[3].code == "delete"
    assert inst.rest[0].resource[0].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[0].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[0].interaction[4].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[0].interaction[5].code == "history-type"
    assert inst.rest[0].resource[0].interaction[5].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[0].interaction[6].code == "create"
    assert inst.rest[0].resource[0].interaction[6].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[0].interaction[7].code == "search-type"
    assert inst.rest[0].resource[0].interaction[7].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[0].profile == "http://hl7.org/fhir/StructureDefinition/Account"
    assert inst.rest[0].resource[0].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[0].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[0].searchInclude[0] == "Account.owner"
    assert inst.rest[0].resource[0].searchInclude[1] == "Account.patient"
    assert inst.rest[0].resource[0].searchInclude[2] == "Account.subject"
    assert inst.rest[0].resource[0].searchInclude[3] == "Account.guarantor"
    assert inst.rest[0].resource[0].searchInclude[4] == "Account.relatedaccount"
    assert inst.rest[0].resource[0].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/Account-owner"
    assert inst.rest[0].resource[0].searchParam[0].documentation == "Entity managing the Account"
    assert inst.rest[0].resource[0].searchParam[0].name == "owner"
    assert inst.rest[0].resource[0].searchParam[0].type == "reference"
    assert inst.rest[0].resource[0].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/clinical-identifier"
    assert inst.rest[0].resource[0].searchParam[1].documentation == "Account number"
    assert inst.rest[0].resource[0].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[1].type == "token"
    assert inst.rest[0].resource[0].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/Account-period"
    assert inst.rest[0].resource[0].searchParam[2].documentation == "Transaction window"
    assert inst.rest[0].resource[0].searchParam[2].name == "period"
    assert inst.rest[0].resource[0].searchParam[2].type == "date"
    assert inst.rest[0].resource[0].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/clinical-patient"
    assert inst.rest[0].resource[0].searchParam[3].documentation == "The entity that caused the expenses"
    assert inst.rest[0].resource[0].searchParam[3].name == "patient"
    assert inst.rest[0].resource[0].searchParam[3].type == "reference"
    assert inst.rest[0].resource[0].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/Account-subject"
    assert inst.rest[0].resource[0].searchParam[4].documentation == "The entity that caused the expenses"
    assert inst.rest[0].resource[0].searchParam[4].name == "subject"
    assert inst.rest[0].resource[0].searchParam[4].type == "reference"
    assert inst.rest[0].resource[0].searchParam[5].definition == "http://hl7.org/fhir/SearchParameter/Account-name"
    assert inst.rest[0].resource[0].searchParam[5].documentation == "Human-readable label"
    assert inst.rest[0].resource[0].searchParam[5].name == "name"
    assert inst.rest[0].resource[0].searchParam[5].type == "string"
    assert inst.rest[0].resource[0].searchParam[6].definition == "http://hl7.org/fhir/SearchParameter/Account-guarantor"
    assert inst.rest[0].resource[0].searchParam[6].documentation == "The parties ultimately responsible for balancing the Account"
    assert inst.rest[0].resource[0].searchParam[6].name == "guarantor"
    assert inst.rest[0].resource[0].searchParam[6].type == "reference"
    assert inst.rest[0].resource[0].searchParam[7].definition == "http://hl7.org/fhir/SearchParameter/clinical-type"
    assert inst.rest[0].resource[0].searchParam[7].documentation == "E.g. patient, expense, depreciation"
    assert inst.rest[0].resource[0].searchParam[7].name == "type"
    assert inst.rest[0].resource[0].searchParam[7].type == "token"
    assert inst.rest[0].resource[0].searchParam[8].definition == "http://hl7.org/fhir/SearchParameter/Account-relatedaccount"
    assert inst.rest[0].resource[0].searchParam[8].documentation == "Parent and other related accounts"
    assert inst.rest[0].resource[0].searchParam[8].name == "relatedaccount"
    assert inst.rest[0].resource[0].searchParam[8].type == "reference"
    assert inst.rest[0].resource[0].searchParam[9].definition == "http://hl7.org/fhir/SearchParameter/Account-status"
    assert inst.rest[0].resource[0].searchParam[9].documentation == "active | inactive | entered-in-error | on-hold | unknown"
    assert inst.rest[0].resource[0].searchParam[9].name == "status"
    assert inst.rest[0].resource[0].searchParam[9].type == "token"
    assert inst.rest[0].resource[0].searchRevInclude[0] == "Account.relatedaccount"
    assert inst.rest[0].resource[0].searchRevInclude[1] == "ChargeItem.account"
    assert inst.rest[0].resource[0].searchRevInclude[2] == "Encounter.account"
    assert inst.rest[0].resource[0].searchRevInclude[3] == "Invoice.account"
    assert inst.rest[0].resource[0].searchRevInclude[4] == "PaymentReconciliation.allocation-account"
    assert inst.rest[0].resource[0].type == "Account"
    assert inst.rest[0].resource[1].conditionalCreate is True
    assert inst.rest[0].resource[1].conditionalDelete == "multiple"
    assert inst.rest[0].resource[1].conditionalUpdate is True
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[1].interaction[1].code == "vread"
    assert inst.rest[0].resource[1].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[1].interaction[2].code == "update"
    assert inst.rest[0].resource[1].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[1].interaction[3].code == "delete"
    assert inst.rest[0].resource[1].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[1].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[1].interaction[4].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[1].interaction[5].code == "history-type"
    assert inst.rest[0].resource[1].interaction[5].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[1].interaction[6].code == "create"
    assert inst.rest[0].resource[1].interaction[6].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[1].interaction[7].code == "search-type"
    assert inst.rest[0].resource[1].interaction[7].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[1].profile == "http://hl7.org/fhir/StructureDefinition/ActivityDefinition"
    assert inst.rest[0].resource[1].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[1].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[1].searchInclude[0] == "ActivityDefinition.successor"
    assert inst.rest[0].resource[1].searchInclude[1] == "ActivityDefinition.derived-from"
    assert inst.rest[0].resource[1].searchInclude[2] == "ActivityDefinition.predecessor"
    assert inst.rest[0].resource[1].searchInclude[3] == "ActivityDefinition.composed-of"
    assert inst.rest[0].resource[1].searchInclude[4] == "ActivityDefinition.depends-on"
    assert inst.rest[0].resource[1].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/CanonicalResource-date"
    assert inst.rest[0].resource[1].searchParam[0].documentation == "The activity definition publication date"
    assert inst.rest[0].resource[1].searchParam[0].name == "date"
    assert inst.rest[0].resource[1].searchParam[0].type == "date"
    assert inst.rest[0].resource[1].searchParam[1].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "identifier"
    )
    assert inst.rest[0].resource[1].searchParam[1].documentation == "External identifier for the activity definition"
    assert inst.rest[0].resource[1].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[1].searchParam[1].type == "token"
    assert inst.rest[0].resource[1].searchParam[2].definition == (
    "http://hl7.org/fhir/SearchParameter/MetadataResource-"
    "successor"
    )
    assert inst.rest[0].resource[1].searchParam[2].documentation == "What resource is being referenced"
    assert inst.rest[0].resource[1].searchParam[2].name == "successor"
    assert inst.rest[0].resource[1].searchParam[2].type == "reference"
    assert inst.rest[0].resource[1].searchParam[3].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "context-type-value"
    )
    assert inst.rest[0].resource[1].searchParam[3].documentation == (
    "A use context type and value assigned to the activity "
    "definition"
    )
    assert inst.rest[0].resource[1].searchParam[3].name == "context-type-value"
    assert inst.rest[0].resource[1].searchParam[3].type == "composite"
    assert inst.rest[0].resource[1].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/ActivityDefinition-kind"
    assert inst.rest[0].resource[1].searchParam[4].documentation == "The kind of activity definition"
    assert inst.rest[0].resource[1].searchParam[4].name == "kind"
    assert inst.rest[0].resource[1].searchParam[4].type == "token"
    assert inst.rest[0].resource[1].searchParam[5].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "jurisdiction"
    )
    assert inst.rest[0].resource[1].searchParam[5].documentation == "Intended jurisdiction for the activity definition"
    assert inst.rest[0].resource[1].searchParam[5].name == "jurisdiction"
    assert inst.rest[0].resource[1].searchParam[5].type == "token"
    assert inst.rest[0].resource[1].searchParam[6].definition == (
    "http://hl7.org/fhir/SearchParameter/MetadataResource-"
    "derived-from"
    )
    assert inst.rest[0].resource[1].searchParam[6].documentation == "What resource is being referenced"
    assert inst.rest[0].resource[1].searchParam[6].name == "derived-from"
    assert inst.rest[0].resource[1].searchParam[6].type == "reference"
    assert inst.rest[0].resource[1].searchParam[7].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "description"
    )
    assert inst.rest[0].resource[1].searchParam[7].documentation == "The description of the activity definition"
    assert inst.rest[0].resource[1].searchParam[7].name == "description"
    assert inst.rest[0].resource[1].searchParam[7].type == "string"
    assert inst.rest[0].resource[1].searchParam[8].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "context-type"
    )
    assert inst.rest[0].resource[1].searchParam[8].documentation == "A type of use context assigned to the activity definition"
    assert inst.rest[0].resource[1].searchParam[8].name == "context-type"
    assert inst.rest[0].resource[1].searchParam[8].type == "token"
    assert inst.rest[0].resource[1].searchParam[9].definition == (
    "http://hl7.org/fhir/SearchParameter/MetadataResource-"
    "predecessor"
    )
    assert inst.rest[0].resource[1].searchParam[9].documentation == "What resource is being referenced"
    assert inst.rest[0].resource[1].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[1].searchParam[9].type == "reference"
    assert inst.rest[0].resource[1].searchRevInclude[0] == "CarePlan.instantiates-canonical"
    assert inst.rest[0].resource[1].searchRevInclude[1] == "ClinicalUseDefinition.product"
    assert inst.rest[0].resource[1].searchRevInclude[2] == "ClinicalUseDefinition.subject"
    assert inst.rest[0].resource[1].searchRevInclude[3] == "Communication.instantiates-canonical"
    assert inst.rest[0].resource[1].searchRevInclude[4] == "DeviceRequest.instantiates-canonical"
    assert inst.rest[0].resource[1].searchRevInclude[5] == "FamilyMemberHistory.instantiates-canonical"
    assert inst.rest[0].resource[1].searchRevInclude[6] == "MessageDefinition.parent"
    assert inst.rest[0].resource[1].searchRevInclude[7] == "PlanDefinition.definition"
    assert inst.rest[0].resource[1].searchRevInclude[8] == "Procedure.instantiates-canonical"
    assert inst.rest[0].resource[1].searchRevInclude[9] == "RegulatedAuthorization.subject"
    assert inst.rest[0].resource[1].type == "ActivityDefinition"
    assert inst.rest[0].resource[2].conditionalCreate is True
    assert inst.rest[0].resource[2].conditionalDelete == "multiple"
    assert inst.rest[0].resource[2].conditionalUpdate is True
    assert inst.rest[0].resource[2].interaction[0].code == "read"
    assert inst.rest[0].resource[2].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[2].interaction[1].code == "vread"
    assert inst.rest[0].resource[2].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[2].interaction[2].code == "update"
    assert inst.rest[0].resource[2].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[2].interaction[3].code == "delete"
    assert inst.rest[0].resource[2].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[2].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[2].interaction[4].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[2].interaction[5].code == "history-type"
    assert inst.rest[0].resource[2].interaction[5].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[2].interaction[6].code == "create"
    assert inst.rest[0].resource[2].interaction[6].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[2].interaction[7].code == "search-type"
    assert inst.rest[0].resource[2].interaction[7].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[2].profile == "http://hl7.org/fhir/StructureDefinition/ActorDefinition"
    assert inst.rest[0].resource[2].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[2].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[2].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/CanonicalResource-date"
    assert inst.rest[0].resource[2].searchParam[0].documentation == "The Actor Definition publication date"
    assert inst.rest[0].resource[2].searchParam[0].name == "date"
    assert inst.rest[0].resource[2].searchParam[0].type == "date"
    assert inst.rest[0].resource[2].searchParam[1].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "identifier"
    )
    assert inst.rest[0].resource[2].searchParam[1].documentation == "External identifier for the Actor Definition"
    assert inst.rest[0].resource[2].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[2].searchParam[1].type == "token"
    assert inst.rest[0].resource[2].searchParam[2].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "context-type-value"
    )
    assert inst.rest[0].resource[2].searchParam[2].documentation == (
    "A use context type and value assigned to the Actor "
    "Definition"
    )
    assert inst.rest[0].resource[2].searchParam[2].name == "context-type-value"
    assert inst.rest[0].resource[2].searchParam[2].type == "composite"
    assert inst.rest[0].resource[2].searchParam[3].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "jurisdiction"
    )
    assert inst.rest[0].resource[2].searchParam[3].documentation == "Intended jurisdiction for the Actor Definition"
    assert inst.rest[0].resource[2].searchParam[3].name == "jurisdiction"
    assert inst.rest[0].resource[2].searchParam[3].type == "token"
    assert inst.rest[0].resource[2].searchParam[4].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "description"
    )
    assert inst.rest[0].resource[2].searchParam[4].documentation == "The description of the Actor Definition"
    assert inst.rest[0].resource[2].searchParam[4].name == "description"
    assert inst.rest[0].resource[2].searchParam[4].type == "string"
    assert inst.rest[0].resource[2].searchParam[5].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "context-type"
    )
    assert inst.rest[0].resource[2].searchParam[5].documentation == "A type of use context assigned to the Actor Definition"
    assert inst.rest[0].resource[2].searchParam[5].name == "context-type"
    assert inst.rest[0].resource[2].searchParam[5].type == "token"
    assert inst.rest[0].resource[2].searchParam[6].definition == "http://hl7.org/fhir/SearchParameter/CanonicalResource-title"
    assert inst.rest[0].resource[2].searchParam[6].documentation == "The human-friendly name of the Actor Definition"
    assert inst.rest[0].resource[2].searchParam[6].name == "title"
    assert inst.rest[0].resource[2].searchParam[6].type == "string"
    assert inst.rest[0].resource[2].searchParam[7].definition == "http://hl7.org/fhir/SearchParameter/ActorDefinition-type"
    assert inst.rest[0].resource[2].searchParam[7].documentation == "The type of actor"
    assert inst.rest[0].resource[2].searchParam[7].name == "type"
    assert inst.rest[0].resource[2].searchParam[7].type == "token"
    assert inst.rest[0].resource[2].searchParam[8].definition == (
    "http://hl7.org/fhir/SearchParameter/CanonicalResource-"
    "version"
    )
    assert inst.rest[0].resource[2].searchParam[8].documentation == "The business version of the Actor Definition"
    assert inst.rest[0].resource[2].searchParam[8].name == "version"
    assert inst.rest[0].resource[2].searchParam[8].type == "token"
    assert inst.rest[0].resource[2].searchParam[9].definition == "http://hl7.org/fhir/SearchParameter/CanonicalResource-url"
    assert inst.rest[0].resource[2].searchParam[9].documentation == "The uri that identifies the Actor Definition"
    assert inst.rest[0].resource[2].searchParam[9].name == "url"
    assert inst.rest[0].resource[2].searchParam[9].type == "uri"
    assert inst.rest[0].resource[2].searchRevInclude[0] == "Requirements.actor"
    assert inst.rest[0].resource[2].type == "ActorDefinition"
    assert inst.rest[0].resource[3].conditionalCreate is True
    assert inst.rest[0].resource[3].conditionalDelete == "multiple"
    assert inst.rest[0].resource[3].conditionalUpdate is True
    assert inst.rest[0].resource[3].interaction[0].code == "read"
    assert inst.rest[0].resource[3].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[3].interaction[1].code == "vread"
    assert inst.rest[0].resource[3].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[3].interaction[2].code == "update"
    assert inst.rest[0].resource[3].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[3].interaction[3].code == "delete"
    assert inst.rest[0].resource[3].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[3].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[3].interaction[4].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[3].interaction[5].code == "history-type"
    assert inst.rest[0].resource[3].interaction[5].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[3].interaction[6].code == "create"
    assert inst.rest[0].resource[3].interaction[6].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[3].interaction[7].code == "search-type"
    assert inst.rest[0].resource[3].interaction[7].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[3].profile == (
    "http://hl7.org/fhir/StructureDefinition/AdministrableProduct"
    "Definition"
    )
    assert inst.rest[0].resource[3].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[3].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[3].searchInclude[0] == "AdministrableProductDefinition.manufactured-item"
    assert inst.rest[0].resource[3].searchInclude[1] == "AdministrableProductDefinition.device"
    assert inst.rest[0].resource[3].searchInclude[2] == "AdministrableProductDefinition.form-of"
    assert inst.rest[0].resource[3].searchParam[0].definition == (
    "http://hl7.org/fhir/SearchParameter/AdministrableProductDefi"
    "nition-identifier"
    )
    assert inst.rest[0].resource[3].searchParam[0].documentation == "An identifier for the administrable product"
    assert inst.rest[0].resource[3].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[3].searchParam[0].type == "token"
    assert inst.rest[0].resource[3].searchParam[1].definition == (
    "http://hl7.org/fhir/SearchParameter/AdministrableProductDefi"
    "nition-manufactured-item"
    )
    assert inst.rest[0].resource[3].searchParam[1].name == "manufactured-item"
    assert inst.rest[0].resource[3].searchParam[1].type == "reference"
    assert inst.rest[0].resource[3].searchParam[2].definition == (
    "http://hl7.org/fhir/SearchParameter/AdministrableProductDefi"
    "nition-ingredient"
    )
    assert inst.rest[0].resource[3].searchParam[2].documentation == "The ingredients of this administrable medicinal product"
    assert inst.rest[0].resource[3].searchParam[2].name == "ingredient"
    assert inst.rest[0].resource[3].searchParam[2].type == "token"
    assert inst.rest[0].resource[3].searchParam[3].definition == (
    "http://hl7.org/fhir/SearchParameter/AdministrableProductDefi"
    "nition-route"
    )
    assert inst.rest[0].resource[3].searchParam[3].documentation == "Coded expression for the route"
    assert inst.rest[0].resource[3].searchParam[3].name == "route"
    assert inst.rest[0].resource[3].searchParam[3].type == "token"
    assert inst.rest[0].resource[3].searchParam[4].definition == (
    "http://hl7.org/fhir/SearchParameter/AdministrableProductDefi"
    "nition-dose-form"
    )
    assert inst.rest[0].resource[3].searchParam[4].documentation == (
    "The administrable dose form, i.e. the dose form of the final"
    " product after necessary reconstitution or processing"
    )
    assert inst.rest[0].resource[3].searchParam[4].name == "dose-form"
    assert inst.rest[0].resource[3].searchParam[4].type == "token"
    assert inst.rest[0].resource[3].searchParam[5].definition == (
    "http://hl7.org/fhir/SearchParameter/AdministrableProductDefi"
    "nition-device"
    )
    assert inst.rest[0].resource[3].searchParam[5].documentation == (
    "A device that is integral to the medicinal product, in "
    "effect being considered as an \"ingredient\" of the "
    "medicinal product. This is not intended for devices that are"
    " just co-packaged"
    )
    assert inst.rest[0].resource[3].searchParam[5].name == "device"
    assert inst.rest[0].resource[3].searchParam[5].type == "reference"
    assert inst.rest[0].resource[3].searchParam[6].definition == (
    "http://hl7.org/fhir/SearchParameter/AdministrableProductDefi"
    "nition-form-of"
    )
    assert inst.rest[0].resource[3].searchParam[6].documentation == (
    "The medicinal product that this is an administrable form of."
    " This is not a reference to the item(s) that make up this "
    "administrable form - it is the whole product"
    )
    assert inst.rest[0].resource[3].searchParam[6].name == "form-of"
    assert inst.rest[0].resource[3].searchParam[6].type == "reference"
    assert inst.rest[0].resource[3].searchParam[7].definition == (
    "http://hl7.org/fhir/SearchParameter/AdministrableProductDefi"
    "nition-target-species"
    )
    assert inst.rest[0].resource[3].searchParam[7].documentation == "Coded expression for the species"
    assert inst.rest[0].resource[3].searchParam[7].name == "target-species"
    assert inst.rest[0].resource[3].searchParam[7].type == "token"
    assert inst.rest[0].resource[3].searchParam[8].definition == (
    "http://hl7.org/fhir/SearchParameter/AdministrableProductDefi"
    "nition-status"
    )
    assert inst.rest[0].resource[3].searchParam[8].documentation == (
    "The status of this administrable product. Enables tracking "
    "the life-cycle of the content."
    )
    assert inst.rest[0].resource[3].searchParam[8].name == "status"
    assert inst.rest[0].resource[3].searchParam[8].type == "token"
    assert inst.rest[0].resource[3].searchRevInclude[0] == "Ingredient.for"
    assert inst.rest[0].resource[3].type == "AdministrableProductDefinition"
    assert inst.rest[0].resource[4].conditionalCreate is True
    assert inst.rest[0].resource[4].conditionalDelete == "multiple"
    assert inst.rest[0].resource[4].conditionalUpdate is True
    assert inst.rest[0].resource[4].interaction[0].code == "read"
    assert inst.rest[0].resource[4].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[4].interaction[1].code == "vread"
    assert inst.rest[0].resource[4].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[4].interaction[2].code == "update"
    assert inst.rest[0].resource[4].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[4].interaction[3].code == "delete"
    assert inst.rest[0].resource[4].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[4].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[4].interaction[4].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[4].interaction[5].code == "history-type"
    assert inst.rest[0].resource[4].interaction[5].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[4].interaction[6].code == "create"
    assert inst.rest[0].resource[4].interaction[6].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[4].interaction[7].code == "search-type"
    assert inst.rest[0].resource[4].interaction[7].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[4].profile == "http://hl7.org/fhir/StructureDefinition/AdverseEvent"
    assert inst.rest[0].resource[4].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[4].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[4].searchInclude[0] == "AdverseEvent.recorder"
    assert inst.rest[0].resource[4].searchInclude[1] == "AdverseEvent.study"
    assert inst.rest[0].resource[4].searchInclude[2] == "AdverseEvent.subject"
    assert inst.rest[0].resource[4].searchInclude[3] == "AdverseEvent.substance"
    assert inst.rest[0].resource[4].searchInclude[4] == "AdverseEvent.patient"
    assert inst.rest[0].resource[4].searchInclude[5] == "AdverseEvent.resultingeffect"
    assert inst.rest[0].resource[4].searchInclude[6] == "AdverseEvent.location"
    assert inst.rest[0].resource[4].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/clinical-date"
    assert inst.rest[0].resource[4].searchParam[0].documentation == "When the event occurred"
    assert inst.rest[0].resource[4].searchParam[0].name == "date"
    assert inst.rest[0].resource[4].searchParam[0].type == "date"
    assert inst.rest[0].resource[4].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/clinical-identifier"
    assert inst.rest[0].resource[4].searchParam[1].documentation == "Business identifier for the event"
    assert inst.rest[0].resource[4].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[4].searchParam[1].type == "token"
    assert inst.rest[0].resource[4].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/AdverseEvent-recorder"
    assert inst.rest[0].resource[4].searchParam[2].documentation == "Who recorded the adverse event"
    assert inst.rest[0].resource[4].searchParam[2].name == "recorder"
    assert inst.rest[0].resource[4].searchParam[2].type == "reference"
    assert inst.rest[0].resource[4].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/AdverseEvent-study"
    assert inst.rest[0].resource[4].searchParam[3].documentation == "Research study that the subject is enrolled in"
    assert inst.rest[0].resource[4].searchParam[3].name == "study"
    assert inst.rest[0].resource[4].searchParam[3].type == "reference"
    assert inst.rest[0].resource[4].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/clinical-code"
    assert inst.rest[0].resource[4].searchParam[4].documentation == "Event or incident that occurred or was averted"
    assert inst.rest[0].resource[4].searchParam[4].name == "code"
    assert inst.rest[0].resource[4].searchParam[4].type == "token"
    assert inst.rest[0].resource[4].searchParam[5].definition == "http://hl7.org/fhir/SearchParameter/AdverseEvent-actuality"
    assert inst.rest[0].resource[4].searchParam[5].documentation == "actual | potential"
    assert inst.rest[0].resource[4].searchParam[5].name == "actuality"
    assert inst.rest[0].resource[4].searchParam[5].type == "token"
    assert inst.rest[0].resource[4].searchParam[6].definition == "http://hl7.org/fhir/SearchParameter/AdverseEvent-subject"
    assert inst.rest[0].resource[4].searchParam[6].documentation == "Subject impacted by event"
    assert inst.rest[0].resource[4].searchParam[6].name == "subject"
    assert inst.rest[0].resource[4].searchParam[6].type == "reference"
    assert inst.rest[0].resource[4].searchParam[7].definition == "http://hl7.org/fhir/SearchParameter/AdverseEvent-substance"
    assert inst.rest[0].resource[4].searchParam[7].documentation == "Refers to the specific entity that caused the adverse event"
    assert inst.rest[0].resource[4].searchParam[7].name == "substance"
    assert inst.rest[0].resource[4].searchParam[7].type == "reference"
    assert inst.rest[0].resource[4].searchParam[8].definition == "http://hl7.org/fhir/SearchParameter/clinical-patient"
    assert inst.rest[0].resource[4].searchParam[8].documentation == "Subject impacted by event"
    assert inst.rest[0].resource[4].searchParam[8].name == "patient"
    assert inst.rest[0].resource[4].searchParam[8].type == "reference"
    assert inst.rest[0].resource[4].searchParam[9].definition == (
    "http://hl7.org/fhir/SearchParameter/AdverseEvent-"
    "resultingeffect"
    )
    assert inst.rest[0].resource[4].searchParam[9].documentation == "Effect on the subject due to this event"
    assert inst.rest[0].resource[4].searchParam[9].name == "resultingeffect"
    assert inst.rest[0].resource[4].searchParam[9].type == "reference"
    assert inst.rest[0].resource[4].type == "AdverseEvent"
    assert inst.rest[0].resource[5].conditionalCreate is True
    assert inst.rest[0].resource[5].conditionalDelete == "multiple"
    assert inst.rest[0].resource[5].conditionalUpdate is True
    assert inst.rest[0].resource[5].interaction[0].code == "read"
    assert inst.rest[0].resource[5].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[5].interaction[1].code == "vread"
    assert inst.rest[0].resource[5].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[5].interaction[2].code == "update"
    assert inst.rest[0].resource[5].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[5].interaction[3].code == "delete"
    assert inst.rest[0].resource[5].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[5].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[5].interaction[4].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[5].interaction[5].code == "history-type"
    assert inst.rest[0].resource[5].interaction[5].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[5].interaction[6].code == "create"
    assert inst.rest[0].resource[5].interaction[6].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[5].interaction[7].code == "search-type"
    assert inst.rest[0].resource[5].interaction[7].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[5].profile == "http://hl7.org/fhir/StructureDefinition/AllergyIntolerance"
    assert inst.rest[0].resource[5].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[5].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[5].searchInclude[0] == "AllergyIntolerance.manifestation-reference"
    assert inst.rest[0].resource[5].searchInclude[1] == "AllergyIntolerance.participant"
    assert inst.rest[0].resource[5].searchInclude[2] == "AllergyIntolerance.patient"
    assert inst.rest[0].resource[5].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/clinical-date"
    assert inst.rest[0].resource[5].searchParam[0].documentation == "Date first version of the resource instance was recorded"
    assert inst.rest[0].resource[5].searchParam[0].name == "date"
    assert inst.rest[0].resource[5].searchParam[0].type == "date"
    assert inst.rest[0].resource[5].searchParam[1].definition == (
    "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-"
    "severity"
    )
    assert inst.rest[0].resource[5].searchParam[1].documentation == "mild | moderate | severe (of event as a whole)"
    assert inst.rest[0].resource[5].searchParam[1].name == "severity"
    assert inst.rest[0].resource[5].searchParam[1].type == "token"
    assert inst.rest[0].resource[5].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/clinical-identifier"
    assert inst.rest[0].resource[5].searchParam[2].documentation == "External ids for this item"
    assert inst.rest[0].resource[5].searchParam[2].name == "identifier"
    assert inst.rest[0].resource[5].searchParam[2].type == "token"
    assert inst.rest[0].resource[5].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/clinical-code"
    assert inst.rest[0].resource[5].searchParam[3].documentation == "Code that identifies the allergy or intolerance"
    assert inst.rest[0].resource[5].searchParam[3].name == "code"
    assert inst.rest[0].resource[5].searchParam[3].type == "token"
    assert inst.rest[0].resource[5].searchParam[4].definition == (
    "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-"
    "verification-status"
    )
    assert inst.rest[0].resource[5].searchParam[4].documentation == (
    "unconfirmed | presumed | confirmed | refuted | entered-in-"
    "error"
    )
    assert inst.rest[0].resource[5].searchParam[4].name == "verification-status"
    assert inst.rest[0].resource[5].searchParam[4].type == "token"
    assert inst.rest[0].resource[5].searchParam[5].definition == (
    "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-"
    "criticality"
    )
    assert inst.rest[0].resource[5].searchParam[5].documentation == "low | high | unable-to-assess"
    assert inst.rest[0].resource[5].searchParam[5].name == "criticality"
    assert inst.rest[0].resource[5].searchParam[5].type == "token"
    assert inst.rest[0].resource[5].searchParam[6].definition == (
    "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-"
    "manifestation-reference"
    )
    assert inst.rest[0].resource[5].searchParam[6].documentation == "Clinical symptoms/signs associated with the Event"
    assert inst.rest[0].resource[5].searchParam[6].name == "manifestation-reference"
    assert inst.rest[0].resource[5].searchParam[6].type == "reference"
    assert inst.rest[0].resource[5].searchParam[7].definition == (
    "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-"
    "clinical-status"
    )
    assert inst.rest[0].resource[5].searchParam[7].documentation == "active | inactive | resolved"
    assert inst.rest[0].resource[5].searchParam[7].name == "clinical-status"
    assert inst.rest[0].resource[5].searchParam[7].type == "token"
    assert inst.rest[0].resource[5].searchParam[8].definition == "http://hl7.org/fhir/SearchParameter/clinical-type"
    assert inst.rest[0].resource[5].searchParam[8].documentation == "allergy | intolerance - Underlying mechanism (if known)"
    assert inst.rest[0].resource[5].searchParam[8].name == "type"
    assert inst.rest[0].resource[5].searchParam[8].type == "token"
    assert inst.rest[0].resource[5].searchParam[9].definition == (
    "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-"
    "participant"
    )
    assert inst.rest[0].resource[5].searchParam[9].documentation == (
    "Who or what participated in the activities related to the "
    "allergy or intolerance"
    )
    assert inst.rest[0].resource[5].searchParam[9].name == "participant"
    assert inst.rest[0].resource[5].searchParam[9].type == "reference"
    assert inst.rest[0].resource[5].searchRevInclude[0] == "ClinicalImpression.problem"
    assert inst.rest[0].resource[5].type == "AllergyIntolerance"
    assert inst.rest[0].resource[6].conditionalCreate is True
    assert inst.rest[0].resource[6].conditionalDelete == "multiple"
    assert inst.rest[0].resource[6].conditionalUpdate is True
    assert inst.rest[0].resource[6].interaction[0].code == "read"
    assert inst.rest[0].resource[6].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[6].interaction[1].code == "vread"
    assert inst.rest[0].resource[6].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[6].interaction[2].code == "update"
    assert inst.rest[0].resource[6].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[6].interaction[3].code == "delete"
    assert inst.rest[0].resource[6].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[6].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[6].interaction[4].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[6].interaction[5].code == "history-type"
    assert inst.rest[0].resource[6].interaction[5].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[6].interaction[6].code == "create"
    assert inst.rest[0].resource[6].interaction[6].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[6].interaction[7].code == "search-type"
    assert inst.rest[0].resource[6].interaction[7].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[6].profile == "http://hl7.org/fhir/StructureDefinition/Appointment"
    assert inst.rest[0].resource[6].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[6].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[6].searchInclude[0] == "Appointment.practitioner"
    assert inst.rest[0].resource[6].searchInclude[1] == "Appointment.subject"
    assert inst.rest[0].resource[6].searchInclude[2] == "Appointment.slot"
    assert inst.rest[0].resource[6].searchInclude[3] == "Appointment.actor"
    assert inst.rest[0].resource[6].searchInclude[4] == "Appointment.based-on"
    assert inst.rest[0].resource[6].searchInclude[5] == "Appointment.patient"
    assert inst.rest[0].resource[6].searchInclude[6] == "Appointment.reason-reference"
    assert inst.rest[0].resource[6].searchInclude[7] == "Appointment.supporting-info"
    assert inst.rest[0].resource[6].searchInclude[8] == "Appointment.location"
    assert inst.rest[0].resource[6].searchInclude[9] == "Appointment.group"
    assert inst.rest[0].resource[6].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/clinical-date"
    assert inst.rest[0].resource[6].searchParam[0].documentation == "Appointment date/time."
    assert inst.rest[0].resource[6].searchParam[0].name == "date"
    assert inst.rest[0].resource[6].searchParam[0].type == "date"
    assert inst.rest[0].resource[6].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/clinical-identifier"
    assert inst.rest[0].resource[6].searchParam[1].documentation == "An Identifier of the Appointment"
    assert inst.rest[0].resource[6].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[6].searchParam[1].type == "token"
    assert inst.rest[0].resource[6].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/Appointment-specialty"
    assert inst.rest[0].resource[6].searchParam[2].documentation == (
    "The specialty of a practitioner that would be required to "
    "perform the service requested in this appointment"
    )
    assert inst.rest[0].resource[6].searchParam[2].name == "specialty"
    assert inst.rest[0].resource[6].searchParam[2].type == "token"
    assert inst.rest[0].resource[6].searchParam[3].definition == (
    "http://hl7.org/fhir/SearchParameter/Appointment-service-"
    "category"
    )
    assert inst.rest[0].resource[6].searchParam[3].documentation == (
    "A broad categorization of the service that is to be "
    "performed during this appointment"
    )
    assert inst.rest[0].resource[6].searchParam[3].name == "service-category"
    assert inst.rest[0].resource[6].searchParam[3].type == "token"
    assert inst.rest[0].resource[6].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/Appointment-practitioner"
    assert inst.rest[0].resource[6].searchParam[4].documentation == (
    "One of the individuals of the appointment is this "
    "practitioner"
    )
    assert inst.rest[0].resource[6].searchParam[4].name == "practitioner"
    assert inst.rest[0].resource[6].searchParam[4].type == "reference"
    assert inst.rest[0].resource[6].searchParam[5].definition == (
    "http://hl7.org/fhir/SearchParameter/Appointment-appointment-"
    "type"
    )
    assert inst.rest[0].resource[6].searchParam[5].documentation == (
    "The style of appointment or patient that has been booked in "
    "the slot (not service type)"
    )
    assert inst.rest[0].resource[6].searchParam[5].name == "appointment-type"
    assert inst.rest[0].resource[6].searchParam[5].type == "token"
    assert inst.rest[0].resource[6].searchParam[6].definition == "http://hl7.org/fhir/SearchParameter/Appointment-part-status"
    assert inst.rest[0].resource[6].searchParam[6].documentation == (
    "The Participation status of the subject, or other "
    "participant on the appointment. Can be used to locate "
    "participants that have not responded to meeting requests."
    )
    assert inst.rest[0].resource[6].searchParam[6].name == "part-status"
    assert inst.rest[0].resource[6].searchParam[6].type == "token"
    assert inst.rest[0].resource[6].searchParam[7].definition == "http://hl7.org/fhir/SearchParameter/Appointment-subject"
    assert inst.rest[0].resource[6].searchParam[7].documentation == "One of the individuals of the appointment is this patient"
    assert inst.rest[0].resource[6].searchParam[7].name == "subject"
    assert inst.rest[0].resource[6].searchParam[7].type == "reference"
    assert inst.rest[0].resource[6].searchParam[8].definition == "http://hl7.org/fhir/SearchParameter/Appointment-service-type"
    assert inst.rest[0].resource[6].searchParam[8].documentation == (
    "The specific service (by coding) that is to be performed "
    "during this appointment"
    )
    assert inst.rest[0].resource[6].searchParam[8].name == "service-type"
    assert inst.rest[0].resource[6].searchParam[8].type == "token"
    assert inst.rest[0].resource[6].searchParam[9].definition == "http://hl7.org/fhir/SearchParameter/Appointment-slot"
    assert inst.rest[0].resource[6].searchParam[9].documentation == "The slots that this appointment is filling"
    assert inst.rest[0].resource[6].searchParam[9].name == "slot"
    assert inst.rest[0].resource[6].searchParam[9].type == "reference"
    assert inst.rest[0].resource[6].searchRevInclude[0] == "AppointmentResponse.appointment"
    assert inst.rest[0].resource[6].searchRevInclude[1] == "CarePlan.activity-reference"
    assert inst.rest[0].resource[6].searchRevInclude[2] == "DocumentReference.based-on"
    assert inst.rest[0].resource[6].searchRevInclude[3] == "DocumentReference.context"
    assert inst.rest[0].resource[6].searchRevInclude[4] == "Encounter.appointment"
    assert inst.rest[0].resource[6].searchRevInclude[5] == "ImagingSelection.based-on"
    assert inst.rest[0].resource[6].searchRevInclude[6] == "ImagingStudy.based-on"
    assert inst.rest[0].resource[6].type == "Appointment"
    assert inst.rest[0].resource[7].conditionalCreate is True
    assert inst.rest[0].resource[7].conditionalDelete == "multiple"
    assert inst.rest[0].resource[7].conditionalUpdate is True
    assert inst.rest[0].resource[7].interaction[0].code == "read"
    assert inst.rest[0].resource[7].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[7].interaction[1].code == "vread"
    assert inst.rest[0].resource[7].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[7].interaction[2].code == "update"
    assert inst.rest[0].resource[7].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[7].interaction[3].code == "delete"
    assert inst.rest[0].resource[7].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[7].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[7].interaction[4].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[7].interaction[5].code == "history-type"
    assert inst.rest[0].resource[7].interaction[5].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[7].interaction[6].code == "create"
    assert inst.rest[0].resource[7].interaction[6].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[7].interaction[7].code == "search-type"
    assert inst.rest[0].resource[7].interaction[7].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[7].profile == "http://hl7.org/fhir/StructureDefinition/AppointmentResponse"
    assert inst.rest[0].resource[7].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[7].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[7].searchInclude[0] == "AppointmentResponse.actor"
    assert inst.rest[0].resource[7].searchInclude[1] == "AppointmentResponse.practitioner"
    assert inst.rest[0].resource[7].searchInclude[2] == "AppointmentResponse.patient"
    assert inst.rest[0].resource[7].searchInclude[3] == "AppointmentResponse.appointment"
    assert inst.rest[0].resource[7].searchInclude[4] == "AppointmentResponse.location"
    assert inst.rest[0].resource[7].searchInclude[5] == "AppointmentResponse.group"
    assert inst.rest[0].resource[7].searchParam[0].definition == (
    "http://hl7.org/fhir/SearchParameter/AppointmentResponse-"
    "actor"
    )
    assert inst.rest[0].resource[7].searchParam[0].documentation == (
    "The Person, Location/HealthcareService or Device that this "
    "appointment response replies for"
    )
    assert inst.rest[0].resource[7].searchParam[0].name == "actor"
    assert inst.rest[0].resource[7].searchParam[0].type == "reference"
    assert inst.rest[0].resource[7].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/clinical-identifier"
    assert inst.rest[0].resource[7].searchParam[1].documentation == "An Identifier in this appointment response"
    assert inst.rest[0].resource[7].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[7].searchParam[1].type == "token"
    assert inst.rest[0].resource[7].searchParam[2].definition == (
    "http://hl7.org/fhir/SearchParameter/AppointmentResponse-"
    "practitioner"
    )
    assert inst.rest[0].resource[7].searchParam[2].documentation == "This Response is for this Practitioner"
    assert inst.rest[0].resource[7].searchParam[2].name == "practitioner"
    assert inst.rest[0].resource[7].searchParam[2].type == "reference"
    assert inst.rest[0].resource[7].searchParam[3].definition == (
    "http://hl7.org/fhir/SearchParameter/AppointmentResponse-"
    "part-status"
    )
    assert inst.rest[0].resource[7].searchParam[3].documentation == "The participants acceptance status for this appointment"
    assert inst.rest[0].resource[7].searchParam[3].name == "part-status"
    assert inst.rest[0].resource[7].searchParam[3].type == "token"
    assert inst.rest[0].resource[7].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/clinical-patient"
    assert inst.rest[0].resource[7].searchParam[4].documentation == "This Response is for this Patient"
    assert inst.rest[0].resource[7].searchParam[4].name == "patient"
    assert inst.rest[0].resource[7].searchParam[4].type == "reference"
    assert inst.rest[0].resource[7].searchParam[5].definition == (
    "http://hl7.org/fhir/SearchParameter/AppointmentResponse-"
    "appointment"
    )
    assert inst.rest[0].resource[7].searchParam[5].documentation == "The appointment that the response is attached to"
    assert inst.rest[0].resource[7].searchParam[5].name == "appointment"
    assert inst.rest[0].resource[7].searchParam[5].type == "reference"
    assert inst.rest[0].resource[7].searchParam[6].definition == (
    "http://hl7.org/fhir/SearchParameter/AppointmentResponse-"
    "location"
    )
    assert inst.rest[0].resource[7].searchParam[6].documentation == "This Response is for this Location"
    assert inst.rest[0].resource[7].searchParam[6].name == "location"
    assert inst.rest[0].resource[7].searchParam[6].type == "reference"
    assert inst.rest[0].resource[7].searchParam[7].definition == (
    "http://hl7.org/fhir/SearchParameter/AppointmentResponse-"
    "group"
    )
    assert inst.rest[0].resource[7].searchParam[7].documentation == "This Response is for this Group"
    assert inst.rest[0].resource[7].searchParam[7].name == "group"
    assert inst.rest[0].resource[7].searchParam[7].type == "reference"
    assert inst.rest[0].resource[7].searchRevInclude[0] == "DocumentReference.based-on"
    assert inst.rest[0].resource[7].searchRevInclude[1] == "ImagingSelection.based-on"
    assert inst.rest[0].resource[7].searchRevInclude[2] == "ImagingStudy.based-on"
    assert inst.rest[0].resource[7].type == "AppointmentResponse"
    assert inst.rest[0].resource[8].conditionalCreate is True
    assert inst.rest[0].resource[8].conditionalDelete == "multiple"
    assert inst.rest[0].resource[8].conditionalUpdate is True
    assert inst.rest[0].resource[8].interaction[0].code == "read"
    assert inst.rest[0].resource[8].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[8].interaction[1].code == "vread"
    assert inst.rest[0].resource[8].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[8].interaction[2].code == "update"
    assert inst.rest[0].resource[8].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[8].interaction[3].code == "delete"
    assert inst.rest[0].resource[8].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[8].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[8].interaction[4].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[8].interaction[5].code == "history-type"
    assert inst.rest[0].resource[8].interaction[5].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[8].interaction[6].code == "create"
    assert inst.rest[0].resource[8].interaction[6].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[8].interaction[7].code == "search-type"
    assert inst.rest[0].resource[8].interaction[7].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[8].profile == "http://hl7.org/fhir/StructureDefinition/ArtifactAssessment"
    assert inst.rest[0].resource[8].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[8].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[8].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/ArtifactAssessment-date"
    assert inst.rest[0].resource[8].searchParam[0].documentation == "The artifact assessment publication date"
    assert inst.rest[0].resource[8].searchParam[0].name == "date"
    assert inst.rest[0].resource[8].searchParam[0].type == "date"
    assert inst.rest[0].resource[8].searchParam[1].definition == (
    "http://hl7.org/fhir/SearchParameter/ArtifactAssessment-"
    "identifier"
    )
    assert inst.rest[0].resource[8].searchParam[1].documentation == "The artifact assessment identifier"
    assert inst.rest[0].resource[8].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[8].searchParam[1].type == "token"
    assert inst.rest[0].resource[8].type == "ArtifactAssessment"
    assert inst.rest[0].resource[9].conditionalCreate is True
    assert inst.rest[0].resource[9].conditionalDelete == "multiple"
    assert inst.rest[0].resource[9].conditionalUpdate is True
    assert inst.rest[0].resource[9].interaction[0].code == "read"
    assert inst.rest[0].resource[9].interaction[0].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[9].interaction[1].code == "vread"
    assert inst.rest[0].resource[9].interaction[1].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[9].interaction[2].code == "update"
    assert inst.rest[0].resource[9].interaction[2].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[9].interaction[3].code == "delete"
    assert inst.rest[0].resource[9].interaction[3].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[9].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[9].interaction[4].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[9].interaction[5].code == "history-type"
    assert inst.rest[0].resource[9].interaction[5].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[9].interaction[6].code == "create"
    assert inst.rest[0].resource[9].interaction[6].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[9].interaction[7].code == "search-type"
    assert inst.rest[0].resource[9].interaction[7].documentation == (
    "Implemented per the specification (or Insert other doco "
    "here)"
    )
    assert inst.rest[0].resource[9].profile == "http://hl7.org/fhir/StructureDefinition/AuditEvent"
    assert inst.rest[0].resource[9].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[9].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[9].searchInclude[0] == "AuditEvent.agent"
    assert inst.rest[0].resource[9].searchInclude[1] == "AuditEvent.encounter"
    assert inst.rest[0].resource[9].searchInclude[2] == "AuditEvent.source"
    assert inst.rest[0].resource[9].searchInclude[3] == "AuditEvent.based-on"
    assert inst.rest[0].resource[9].searchInclude[4] == "AuditEvent.patient"
    assert inst.rest[0].resource[9].searchInclude[5] == "AuditEvent.entity"
    assert inst.rest[0].resource[9].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/clinical-date"
    assert inst.rest[0].resource[9].searchParam[0].documentation == "Time when the event was recorded"
    assert inst.rest[0].resource[9].searchParam[0].name == "date"
    assert inst.rest[0].resource[9].searchParam[0].type == "date"
    assert inst.rest[0].resource[9].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/AuditEvent-agent"
    assert inst.rest[0].resource[9].searchParam[1].documentation == "Identifier of who"
    assert inst.rest[0].resource[9].searchParam[1].name == "agent"
    assert inst.rest[0].resource[9].searchParam[1].type == "reference"
    assert inst.rest[0].resource[9].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/AuditEvent-entity-role"
    assert inst.rest[0].resource[9].searchParam[2].documentation == "What role the entity played"
    assert inst.rest[0].resource[9].searchParam[2].name == "entity-role"
    assert inst.rest[0].resource[9].searchParam[2].type == "token"
    assert inst.rest[0].resource[9].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/clinical-code"
    assert inst.rest[0].resource[9].searchParam[3].documentation == "More specific code for the event"
    assert inst.rest[0].resource[9].searchParam[3].name == "code"
    assert inst.rest[0].resource[9].searchParam[3].type == "token"
    assert inst.rest[0].resource[9].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/AuditEvent-purpose"
    assert inst.rest[0].resource[9].searchParam[4].documentation == "The authorization (purposeOfUse) of the event"
    assert inst.rest[0].resource[9].searchParam[4].name == "purpose"
    assert inst.rest[0].resource[9].searchParam[4].type == "token"
    assert inst.rest[0].resource[9].searchParam[5].definition == "http://hl7.org/fhir/SearchParameter/clinical-encounter"
    assert inst.rest[0].resource[9].searchParam[5].documentation == "Encounter related to the activity recorded in the AuditEvent"
    assert inst.rest[0].resource[9].searchParam[5].name == "encounter"
    assert inst.rest[0].resource[9].searchParam[5].type == "reference"
    assert inst.rest[0].resource[9].searchParam[6].definition == "http://hl7.org/fhir/SearchParameter/AuditEvent-source"
    assert inst.rest[0].resource[9].searchParam[6].documentation == "The identity of source detecting the event"
    assert inst.rest[0].resource[9].searchParam[6].name == "source"
    assert inst.rest[0].resource[9].searchParam[6].type == "reference"
    assert inst.rest[0].resource[9].searchParam[7].definition == "http://hl7.org/fhir/SearchParameter/AuditEvent-based-on"
    assert inst.rest[0].resource[9].searchParam[7].documentation == "Reference to the service request."
    assert inst.rest[0].resource[9].searchParam[7].name == "based-on"
    assert inst.rest[0].resource[9].searchParam[7].type == "reference"
    assert inst.rest[0].resource[9].searchParam[8].definition == "http://hl7.org/fhir/SearchParameter/clinical-patient"
    assert inst.rest[0].resource[9].searchParam[8].documentation == "Where the activity involved patient data"
    assert inst.rest[0].resource[9].searchParam[8].name == "patient"
    assert inst.rest[0].resource[9].searchParam[8].type == "reference"
    assert inst.rest[0].resource[9].searchParam[9].definition == "http://hl7.org/fhir/SearchParameter/AuditEvent-action"
    assert inst.rest[0].resource[9].searchParam[9].documentation == "Type of action performed during the event"
    assert inst.rest[0].resource[9].searchParam[9].name == "action"
    assert inst.rest[0].resource[9].searchParam[9].type == "token"
    assert inst.rest[0].resource[9].type == "AuditEvent"
    assert inst.rest[0].searchParam[0].definition == "http://hl7.org/fhir/SearchParameter/DomainResource-text"
    assert inst.rest[0].searchParam[0].documentation == "Search on the narrative of the resource"
    assert inst.rest[0].searchParam[0].name == "_text"
    assert inst.rest[0].searchParam[0].type == "special"
    assert inst.rest[0].searchParam[1].definition == "http://hl7.org/fhir/SearchParameter/id"
    assert inst.rest[0].searchParam[1].documentation == "some doco"
    assert inst.rest[0].searchParam[1].name == "_id"
    assert inst.rest[0].searchParam[1].type == "string"
    assert inst.rest[0].searchParam[2].definition == "http://hl7.org/fhir/SearchParameter/Resource-list"
    assert inst.rest[0].searchParam[2].documentation == (
    "Retrieval of resources that are referenced by a List "
    "resource"
    )
    assert inst.rest[0].searchParam[2].name == "_list"
    assert inst.rest[0].searchParam[2].type == "token"
    assert inst.rest[0].searchParam[3].definition == "http://hl7.org/fhir/SearchParameter/Resource-has"
    assert inst.rest[0].searchParam[3].documentation == "Provides support for reverse chaining"
    assert inst.rest[0].searchParam[3].name == "_has"
    assert inst.rest[0].searchParam[3].type == "composite"
    assert inst.rest[0].searchParam[4].definition == "http://hl7.org/fhir/SearchParameter/Resource-type"
    assert inst.rest[0].searchParam[4].documentation == "Type of resource (when doing cross-resource search"
    assert inst.rest[0].searchParam[4].name == "_type"
    assert inst.rest[0].searchParam[4].type == "token"
    assert inst.rest[0].searchParam[5].definition == "http://hl7.org/fhir/SearchParameter/Resource-source"
    assert inst.rest[0].searchParam[5].documentation == "How to sort the resources when returning"
    assert inst.rest[0].searchParam[5].name == "_sort"
    assert inst.rest[0].searchParam[5].type == "token"
    assert inst.rest[0].searchParam[6].definition == "http://hl7.org/fhir/SearchParameter/Resource-count"
    assert inst.rest[0].searchParam[6].documentation == "How many resources to return"
    assert inst.rest[0].searchParam[6].name == "_count"
    assert inst.rest[0].searchParam[6].type == "number"
    assert inst.rest[0].searchParam[7].definition == "http://hl7.org/fhir/SearchParameter/Resource-include"
    assert inst.rest[0].searchParam[7].documentation == "Control over returning additional resources (see spec)"
    assert inst.rest[0].searchParam[7].name == "_include"
    assert inst.rest[0].searchParam[7].type == "token"
    assert inst.rest[0].searchParam[8].definition == "http://hl7.org/fhir/SearchParameter/Resource-revinclude"
    assert inst.rest[0].searchParam[8].documentation == "Control over returning additional resources (see spec)"
    assert inst.rest[0].searchParam[8].name == "_revinclude"
    assert inst.rest[0].searchParam[8].type == "token"
    assert inst.rest[0].searchParam[9].definition == "http://hl7.org/fhir/SearchParameter/Resource-summary"
    assert inst.rest[0].searchParam[9].documentation == "What kind of information to return"
    assert inst.rest[0].searchParam[9].name == "_summary"
    assert inst.rest[0].searchParam[9].type == "token"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.description == (
    "This is the Capability Statement to declare that the server "
    "supports SMART-on-FHIR. See the SMART-on-FHIR docs for the "
    "extension that would go with such a server"
    )
    assert inst.rest[0].security.service[0].coding[0].code == "SMART-on-FHIR"
    assert inst.rest[0].security.service[0].coding[0].display == "SMART-on-FHIR"
    assert inst.rest[0].security.service[0].coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/restful-security-"
    "service"
    )
    assert inst.rest[0].security.service[0].text == "See http://docs.smarthealthit.org/"
    assert inst.software.name == "Insert your software name here..."
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert inst.url == "http://hl7.org/fhir/CapabilityStatement/base"
    assert inst.version == "5.0.0"


def test_capabilitystatement_8(base_settings):
    """No. 8 tests collection for CapabilityStatement.
    Test File: capabilitystatement-base.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "capabilitystatement-base.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_8(inst2)