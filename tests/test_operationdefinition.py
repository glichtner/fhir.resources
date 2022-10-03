# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import operationdefinition


def impl_operationdefinition_1(inst):
    assert inst.affectsState is True
    assert inst.code == "generate"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "DocumentReference-generate"
    assert inst.instance is False
    assert inst.kind == "operation"
    assert inst.name == "Generate"
    assert inst.parameter[0].documentation == (
    "The URL to the source document. This may be a general URL or"
    " a Binary or a Composition or a Bundle."
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "url"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
    "Whether to store the document at the document end-point "
    "(/Document) or not, once it is generated (default is for the"
    " server to decide)."
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "persist"
    assert inst.parameter[1].type == "boolean"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "docRef"
    assert inst.parameter[2].type == "DocumentReference"
    assert inst.parameter[2].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "DocumentReference"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Generate a DocumentReference from a document"
    assert inst.type is True
    assert inst.url == (
    "http://hl7.org/fhir/OperationDefinition/DocumentReference-"
    "generate"
    )
    assert inst.version == "5.0.0-ballot"


def test_operationdefinition_1(base_settings):
    """No. 1 tests collection for OperationDefinition.
    Test File: operation-documentreference-generate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-documentreference-generate.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_1(inst2)


def impl_operationdefinition_2(inst):
    assert inst.affectsState is False
    assert inst.code == "data-requirements"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.description == (
    "The data-requirements operation aggregates and returns the "
    "parameters and data requirements for the measure and all its"
    " dependencies as a single module definition"
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Measure-data-requirements"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "DataRequirements"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "periodStart"
    assert inst.parameter[0].type == "date"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
    "The end of the measurement period. The period will end at "
    "the end of the period implied by the supplied timestamp. "
    "E.g. a value of 2014 would set the period end to be "
    "2014-12-31T23:59:59 inclusive"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "periodEnd"
    assert inst.parameter[1].type == "date"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
    "The result of the requirements gathering is a module-"
    "definition Library that describes the aggregate parameters, "
    "data requirements, and dependencies of the measure"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "return"
    assert inst.parameter[2].type == "Library"
    assert inst.parameter[2].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Measure"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Data Requirements"
    assert inst.type is False
    assert inst.url == (
    "http://hl7.org/fhir/OperationDefinition/Measure-data-"
    "requirements"
    )
    assert inst.version == "5.0.0-ballot"


def test_operationdefinition_2(base_settings):
    """No. 2 tests collection for OperationDefinition.
    Test File: operation-measure-data-requirements.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-measure-data-requirements.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_2(inst2)


def impl_operationdefinition_3(inst):
    assert inst.base == (
    "http://hl7.org/fhir/OperationDefinition/Questionnaire-"
    "populate"
    )
    assert inst.code == "populate"
    assert inst.comment == "Only implemented for Labs and Medications so far"
    assert inst.contact[0].name == "System Administrator"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].value == "beep@coyote.acme.com"
    assert inst.date == fhirtypes.DateTime.validate("2015-08-04")
    assert inst.description == (
    "Limited implementation of the Populate Questionnaire "
    "implementation"
    )
    assert inst.id == "example"
    assert inst.instance is True
    assert inst.jurisdiction[0].coding[0].code == "GB"
    assert inst.jurisdiction[0].coding[0].display == "United Kingdom of Great Britain and Northern Ireland (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.kind == "operation"
    assert inst.name == "Populate Questionnaire"
    assert inst.overload[0].parameterName[0] == "subject"
    assert inst.overload[0].parameterName[1] == "local"
    assert inst.overload[1].comment == "local defaults to false when not passed as a parameter"
    assert inst.overload[1].parameterName[0] == "subject"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "subject"
    assert inst.parameter[0].type == "Reference"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
    "If the *local* parameter is set to true, server information "
    "about the specified subject will be used to populate the "
    "instance."
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "local"
    assert inst.parameter[1].type == "Reference"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
    "The partially (or fully)-populated set of answers for the "
    "specified Questionnaire"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "return"
    assert inst.parameter[2].type == "QuestionnaireResponse"
    assert inst.parameter[2].use == "out"
    assert inst.publisher == "Acme Healthcare Services"
    assert inst.resource[0] == "Questionnaire"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is False
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/example"
    assert inst.useContext[0].code.code == "venue"
    assert inst.useContext[0].code.display == "Clinical Venue"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "IMP"
    assert inst.useContext[0].valueCodeableConcept.coding[0].display == "inpatient encounter"
    assert inst.useContext[0].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    assert inst.version == "B"


def test_operationdefinition_3(base_settings):
    """No. 3 tests collection for OperationDefinition.
    Test File: operationdefinition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operationdefinition-example.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_3(inst2)


def impl_operationdefinition_4(inst):
    assert inst.affectsState is True
    assert inst.code == "get-ws-binding-token"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.description == (
    "This operation is used to get a token for a websocket client"
    " to use in order to bind to one or more subscriptions."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[0].valueInteger == 2
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Subscription-get-ws-binding-token"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "GetWsBindingToken"
    assert inst.parameter[0].max == "*"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "id"
    assert inst.parameter[0].type == "id"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
    "An access token that a client may use to show authorization "
    "during a websocket connection."
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "token"
    assert inst.parameter[1].type == "string"
    assert inst.parameter[1].use == "out"
    assert inst.parameter[2].documentation == "The date and time this token is valid until."
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "expiration"
    assert inst.parameter[2].type == "dateTime"
    assert inst.parameter[2].use == "out"
    assert inst.parameter[3].documentation == "The subscriptions this token is valid for."
    assert inst.parameter[3].max == "*"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "subscription"
    assert inst.parameter[3].type == "string"
    assert inst.parameter[3].use == "out"
    assert inst.parameter[4].documentation == "The URL the client should use to connect to Websockets."
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 1
    assert inst.parameter[4].name == "websocket-url"
    assert inst.parameter[4].type == "url"
    assert inst.parameter[4].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Subscription"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Get a binding token for use in a websocket connection"
    assert inst.type is True
    assert inst.url == (
    "http://hl7.org/fhir/OperationDefinition/Subscription-get-ws-"
    "binding-token"
    )
    assert inst.version == "5.0.0-ballot"


def test_operationdefinition_4(base_settings):
    """No. 4 tests collection for OperationDefinition.
    Test File: operation-subscription-get-ws-binding-token.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-subscription-get-ws-binding-token.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_4(inst2)


def impl_operationdefinition_5(inst):
    assert inst.affectsState is False
    assert inst.code == "questionnaire"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[0].valueInteger == 5
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "StructureDefinition-questionnaire"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Questionnaire"
    assert inst.parameter[0].documentation == (
    "A logical identifier (i.e. "
    "'StructureDefinition.identifier''). The server must know the"
    " StructureDefinition or be able to retrieve it from other "
    "known repositories."
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "identifier"
    assert inst.parameter[0].targetProfile[0] == "http://hl7.org/fhir/StructureDefinition/StructureDefinition"
    assert inst.parameter[0].type == "Identifier"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
    "The [StructureDefinition](structuredefinition.html) is "
    "provided directly as part of the request. Servers may choose"
    " not to accept profiles in this fashion"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "profile"
    assert inst.parameter[1].type == "StructureDefinition"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
    "The StructureDefinition's official URL (i.e. "
    "'StructureDefinition.url'). The server must know the "
    "StructureDefinition or be able to retrieve it from other "
    "known repositories."
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "url"
    assert inst.parameter[2].targetProfile[0] == "http://hl7.org/fhir/StructureDefinition/StructureDefinition"
    assert inst.parameter[2].type == "canonical"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
    "If true, the questionnaire will only include those elements "
    "marked as \"mustSupport='true'\" in the StructureDefinition."
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "supportedOnly"
    assert inst.parameter[3].type == "boolean"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == (
    "The questionnaire form generated based on the "
    "StructureDefinition."
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 1
    assert inst.parameter[4].name == "return"
    assert inst.parameter[4].type == "Questionnaire"
    assert inst.parameter[4].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "StructureDefinition"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Build Questionnaire"
    assert inst.type is True
    assert inst.url == (
    "http://hl7.org/fhir/OperationDefinition/StructureDefinition-"
    "questionnaire"
    )
    assert inst.version == "5.0.0-ballot"


def test_operationdefinition_5(base_settings):
    """No. 5 tests collection for OperationDefinition.
    Test File: operation-structuredefinition-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-structuredefinition-questionnaire.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_5(inst2)


def impl_operationdefinition_6(inst):
    assert inst.affectsState is False
    assert inst.code == "validate-code"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[0].valueInteger == 5
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "normative"
    assert inst.id == "CodeSystem-validate-code"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "ValidateCode"
    assert inst.parameter[0].documentation == (
    "CodeSystem URL. The server must know the code system (e.g. "
    "it is defined explicitly in the server'scode systems, or it "
    "is known implicitly by the server"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "url"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "codeSystem"
    assert inst.parameter[1].type == "CodeSystem"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == "The code that is to be validated"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "code"
    assert inst.parameter[2].type == "code"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
    "The version of the code system, if one was provided in the "
    "source data"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "version"
    assert inst.parameter[3].type == "string"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "display"
    assert inst.parameter[4].type == "string"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
    "A coding to validate. The system must match the specified "
    "code system"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "coding"
    assert inst.parameter[5].type == "Coding"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "codeableConcept"
    assert inst.parameter[6].type == "CodeableConcept"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "date"
    assert inst.parameter[7].type == "dateTime"
    assert inst.parameter[7].use == "in"
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "abstract"
    assert inst.parameter[8].type == "boolean"
    assert inst.parameter[8].use == "in"
    assert inst.parameter[9].documentation == (
    "Specifies the language to be used for description when "
    "validating the display property"
    )
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 0
    assert inst.parameter[9].name == "displayLanguage"
    assert inst.parameter[9].type == "code"
    assert inst.parameter[9].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "CodeSystem"
    assert inst.status == "active"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Code System based Validation"
    assert inst.type is True
    assert inst.url == (
    "http://hl7.org/fhir/OperationDefinition/CodeSystem-validate-"
    "code"
    )
    assert inst.version == "5.0.0-ballot"


def test_operationdefinition_6(base_settings):
    """No. 6 tests collection for OperationDefinition.
    Test File: operation-codesystem-validate-code.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-codesystem-validate-code.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_6(inst2)


def impl_operationdefinition_7(inst):
    assert inst.affectsState is True
    assert inst.code == "filter"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.description == (
    "Filter content from an array in a large resource such as "
    "List or Group. See [Operations for Large "
    "Resources](operations-for-large-resources.html)."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[0].valueInteger == 0
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Resource-filter"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Filter"
    assert inst.parameter[0].documentation == (
    "Resource containing content that acts as a filter. See "
    "[Operations for Large Resources](operations-for-large-"
    "resources.html)."
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "probes"
    assert inst.parameter[0].type == "Resource"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
    "Resource containing content matching the filter. See "
    "[Operations for Large Resources](operations-for-large-"
    "resources.html)."
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "return"
    assert inst.parameter[1].type == "Resource"
    assert inst.parameter[1].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Resource"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Filter an array in a large resource"
    assert inst.type is False
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Resource-filter"
    assert inst.version == "5.0.0-ballot"


def test_operationdefinition_7(base_settings):
    """No. 7 tests collection for OperationDefinition.
    Test File: operation-resource-filter.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-resource-filter.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_7(inst2)


def impl_operationdefinition_8(inst):
    assert inst.affectsState is False
    assert inst.code == "apply"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.description == (
    "The apply operation applies a PlanDefinition to a given "
    "subject"
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "PlanDefinition-apply"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Apply"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "planDefinition"
    assert inst.parameter[0].type == "PlanDefinition"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "url"
    assert inst.parameter[1].searchType == "reference"
    assert inst.parameter[1].targetProfile[0] == "http://hl7.org/fhir/StructureDefinition/PlanDefinition"
    assert inst.parameter[1].type == "canonical"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "version"
    assert inst.parameter[2].type == "string"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].max == "*"
    assert inst.parameter[3].min == 1
    assert inst.parameter[3].name == "subject"
    assert inst.parameter[3].searchType == "reference"
    assert inst.parameter[3].type == "string"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == "The encounter in context, if any"
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "encounter"
    assert inst.parameter[4].searchType == "reference"
    assert inst.parameter[4].type == "string"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == "The practitioner applying the plan definition"
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "practitioner"
    assert inst.parameter[5].searchType == "reference"
    assert inst.parameter[5].type == "string"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].documentation == "The organization applying the plan definition"
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "organization"
    assert inst.parameter[6].searchType == "reference"
    assert inst.parameter[6].type == "string"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].documentation == (
    "The type of user initiating the request, e.g. patient, "
    "healthcare provider, or specific type of healthcare provider"
    " (physician, nurse, etc.)"
    )
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "userType"
    assert inst.parameter[7].type == "CodeableConcept"
    assert inst.parameter[7].use == "in"
    assert inst.parameter[8].documentation == "Preferred language of the person using the system"
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "userLanguage"
    assert inst.parameter[8].type == "CodeableConcept"
    assert inst.parameter[8].use == "in"
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 0
    assert inst.parameter[9].name == "userTaskContext"
    assert inst.parameter[9].type == "CodeableConcept"
    assert inst.parameter[9].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "PlanDefinition"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Apply"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/PlanDefinition-apply"
    assert inst.version == "5.0.0-ballot"


def test_operationdefinition_8(base_settings):
    """No. 8 tests collection for OperationDefinition.
    Test File: operation-plandefinition-apply.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-plandefinition-apply.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_8(inst2)


def impl_operationdefinition_9(inst):
    assert inst.affectsState is True
    assert inst.code == "submit"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[0].valueInteger == 2
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "CoverageEligibilityRequest-submit"
    assert inst.instance is False
    assert inst.kind == "operation"
    assert inst.name == "Submit"
    assert inst.parameter[0].documentation == (
    "An EligibilityRequest resource or Bundle of "
    "EligibilityRequests, either as individual EligibilityRequest"
    " resources or as Bundles each containing a single "
    "EligibilityRequest plus referenced resources."
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "resource"
    assert inst.parameter[0].type == "Resource"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "return"
    assert inst.parameter[1].type == "Resource"
    assert inst.parameter[1].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "CoverageEligibilityRequest"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Submit an EligibilityRequest resource for assessment"
    assert inst.type is True
    assert inst.url == (
    "http://hl7.org/fhir/OperationDefinition/CoverageEligibilityR"
    "equest-submit"
    )
    assert inst.version == "5.0.0-ballot"


def test_operationdefinition_9(base_settings):
    """No. 9 tests collection for OperationDefinition.
    Test File: operation-coverageeligibilityrequest-submit.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-coverageeligibilityrequest-submit.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_9(inst2)


def impl_operationdefinition_10(inst):
    assert inst.affectsState is False
    assert inst.code == "submit-data"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Measure-submit-data"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "SubmitData"
    assert inst.parameter[0].documentation == "The measure report being submitted"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "measureReport"
    assert inst.parameter[0].type == "MeasureReport"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
    "The individual resources that make up the data-of-interest "
    "being submitted"
    )
    assert inst.parameter[1].max == "*"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "resource"
    assert inst.parameter[1].type == "Resource"
    assert inst.parameter[1].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Measure"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Submit Data"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Measure-submit-data"
    assert inst.version == "5.0.0-ballot"


def test_operationdefinition_10(base_settings):
    """No. 10 tests collection for OperationDefinition.
    Test File: operation-measure-submit-data.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-measure-submit-data.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_10(inst2)