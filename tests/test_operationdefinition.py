# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import operationdefinition


def impl_operationdefinition_1(inst):
    assert inst.affectsState is False
    assert inst.code == "data-requirements"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.description == (
        "The data-requirements operation aggregates and returns the "
        "parameters and data requirements for the measure and all its"
        " dependencies as a single module definition"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
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
    assert inst.name == "data-requirements"
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
        "http://hl7.org/fhir/OperationDefinition/Measure-data-" "requirements"
    )
    assert inst.version == "4.5.0"


def test_operationdefinition_1(base_settings):
    """No. 1 tests collection for OperationDefinition.
    Test File: operation-measure-data-requirements.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-measure-data-requirements.json"
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
    assert inst.code == "apply"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.description == (
        "The apply operation applies a PlanDefinition to a given " "context"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
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
    assert inst.name == "apply"
    assert inst.parameter[0].documentation == (
        "The plan definition to be applied. If the operation is "
        "invoked at the instance level, this parameter is not "
        "allowed; if the operation is invoked at the type level, this"
        " parameter is required"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "planDefinition"
    assert inst.parameter[0].type == "PlanDefinition"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].max == "*"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "subject"
    assert inst.parameter[1].searchType == "reference"
    assert inst.parameter[1].type == "string"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == "The encounter in context, if any"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "encounter"
    assert inst.parameter[2].searchType == "reference"
    assert inst.parameter[2].type == "string"
    assert inst.parameter[2].use == "in"
    assert (
        inst.parameter[3].documentation
        == "The practitioner applying the plan definition"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "practitioner"
    assert inst.parameter[3].searchType == "reference"
    assert inst.parameter[3].type == "string"
    assert inst.parameter[3].use == "in"
    assert (
        inst.parameter[4].documentation
        == "The organization applying the plan definition"
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "organization"
    assert inst.parameter[4].searchType == "reference"
    assert inst.parameter[4].type == "string"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
        "The type of user initiating the request, e.g. patient, "
        "healthcare provider, or specific type of healthcare provider"
        " (physician, nurse, etc.)"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "userType"
    assert inst.parameter[5].type == "CodeableConcept"
    assert inst.parameter[5].use == "in"
    assert (
        inst.parameter[6].documentation
        == "Preferred language of the person using the system"
    )
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "userLanguage"
    assert inst.parameter[6].type == "CodeableConcept"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "userTaskContext"
    assert inst.parameter[7].type == "CodeableConcept"
    assert inst.parameter[7].use == "in"
    assert inst.parameter[8].documentation == (
        "The current setting of the request (inpatient, outpatient, " "etc.)"
    )
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "setting"
    assert inst.parameter[8].type == "CodeableConcept"
    assert inst.parameter[8].use == "in"
    assert (
        inst.parameter[9].documentation
        == "Additional detail about the setting of the request, if any"
    )
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 0
    assert inst.parameter[9].name == "settingContext"
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
    assert inst.version == "4.5.0"


def test_operationdefinition_2(base_settings):
    """No. 2 tests collection for OperationDefinition.
    Test File: operation-plandefinition-apply.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-plandefinition-apply.json"
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
    assert inst.affectsState is True
    assert inst.code == "snapshot"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 5
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "StructureDefinition-snapshot"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "snapshot"
    assert inst.parameter[0].documentation == (
        "The [StructureDefinition](structuredefinition.html) is "
        "provided directly as part of the request. Servers may choose"
        " not to accept profiles in this fashion"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "definition"
    assert inst.parameter[0].type == "StructureDefinition"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The StructureDefinition's canonical URL (i.e. "
        "'StructureDefinition.url'). The server must know the "
        "structure definition, or be able to retrieve it from other "
        "known repositories."
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "url"
    assert inst.parameter[1].searchType == "token"
    assert inst.parameter[1].type == "string"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == "The structure definition with a snapshot"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "return"
    assert inst.parameter[2].type == "StructureDefinition"
    assert inst.parameter[2].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "StructureDefinition"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Generate Snapshot"
    assert inst.type is True
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/StructureDefinition-" "snapshot"
    )
    assert inst.version == "4.5.0"


def test_operationdefinition_3(base_settings):
    """No. 3 tests collection for OperationDefinition.
    Test File: operation-structuredefinition-snapshot.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operation-structuredefinition-snapshot.json"
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
    assert inst.affectsState is False
    assert inst.code == "validate-code"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
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
    assert inst.name == "validate-code"
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
        "The version of the code system, if one was provided in the " "source data"
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
        "A coding to validate. The system must match the specified " "code system"
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
        "http://hl7.org/fhir/OperationDefinition/CodeSystem-validate-" "code"
    )
    assert inst.version == "4.5.0"


def test_operationdefinition_4(base_settings):
    """No. 4 tests collection for OperationDefinition.
    Test File: operation-codesystem-validate-code.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-codesystem-validate-code.json"
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
    assert inst.code == "validate"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 5
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "normative"
    assert inst.id == "Resource-validate"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "validate"
    assert (
        inst.parameter[0].documentation == 'Must be present unless the mode is "delete"'
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "resource"
    assert inst.parameter[0].type == "Resource"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].binding.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/elementdefinition-" "bindingName"
    )
    assert (
        inst.parameter[1].binding.extension[0].valueString == "ResourceValidationMode"
    )
    assert inst.parameter[1].binding.strength == "required"
    assert inst.parameter[1].binding.valueSet == (
        "http://hl7.org/fhir/ValueSet/resource-validation-" "mode|4.5.0|4.5.0"
    )
    assert (
        inst.parameter[1].documentation
        == "Default is 'no action'; (e.g. general validation)"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "mode"
    assert inst.parameter[1].type == "code"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "If this is nominated, then the resource is validated against"
        " this specific profile. If a profile is nominated, and the "
        "server cannot validate against the nominated profile, it "
        "SHALL return an error"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "profile"
    assert inst.parameter[2].type == "uri"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 1
    assert inst.parameter[3].name == "return"
    assert inst.parameter[3].type == "OperationOutcome"
    assert inst.parameter[3].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Resource"
    assert inst.status == "active"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Validate a resource"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Resource-validate"
    assert inst.version == "4.5.0"


def test_operationdefinition_5(base_settings):
    """No. 5 tests collection for OperationDefinition.
    Test File: operation-resource-validate.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-resource-validate.json"
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
    assert inst.code == "questionnaire"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
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
    assert inst.name == "questionnaire"
    assert inst.parameter[0].documentation == (
        "A logical identifier (i.e. "
        "'StructureDefinition.identifier''). The server must know the"
        " StructureDefinition or be able to retrieve it from other "
        "known repositories."
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "identifier"
    assert (
        inst.parameter[0].targetProfile[0]
        == "http://hl7.org/fhir/StructureDefinition/StructureDefinition"
    )
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
    assert inst.parameter[1].searchType == "token"
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
    assert (
        inst.parameter[2].targetProfile[0]
        == "http://hl7.org/fhir/StructureDefinition/StructureDefinition"
    )
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
        "The questionnaire form generated based on the " "StructureDefinition."
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
        "http://hl7.org/fhir/OperationDefinition/StructureDefinition-" "questionnaire"
    )
    assert inst.version == "4.5.0"


def test_operationdefinition_6(base_settings):
    """No. 6 tests collection for OperationDefinition.
    Test File: operation-structuredefinition-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operation-structuredefinition-questionnaire.json"
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
    assert inst.affectsState is False
    assert inst.code == "translate-id"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 1
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "NamingSystem-translate-id"
    assert inst.instance is False
    assert inst.kind == "operation"
    assert inst.name == "translate-id"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "id"
    assert inst.parameter[0].type == "string"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].binding.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/elementdefinition-" "bindingName"
    )
    assert (
        inst.parameter[1].binding.extension[0].valueString
        == "NamingSystemIdentifierType"
    )
    assert inst.parameter[1].binding.strength == "required"
    assert inst.parameter[1].binding.valueSet == (
        "http://hl7.org/fhir/ValueSet/namingsystem-identifier-" "type|4.5.0|4.5.0"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "sourceType"
    assert inst.parameter[1].type == "code"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].binding.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/elementdefinition-" "bindingName"
    )
    assert (
        inst.parameter[2].binding.extension[0].valueString
        == "NamingSystemIdentifierType"
    )
    assert inst.parameter[2].binding.strength == "required"
    assert inst.parameter[2].binding.valueSet == (
        "http://hl7.org/fhir/ValueSet/namingsystem-identifier-" "type|4.5.0|4.5.0"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "targetType"
    assert inst.parameter[2].type == "code"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "If preferredOnly = true then return only the preferred "
        "identifier, or if preferredOnly = false then return all "
        "available ids."
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "preferredOnly"
    assert inst.parameter[3].type == "boolean"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == (
        "If 'date' is supplied return only ids that have a validity "
        "period that includes that date."
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "date"
    assert inst.parameter[4].type == "dateTime"
    assert inst.parameter[4].use == "in"
    assert (
        inst.parameter[5].documentation
        == "True if the identifier could be translated successfully."
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 1
    assert inst.parameter[5].name == "result"
    assert inst.parameter[5].type == "boolean"
    assert inst.parameter[5].use == "out"
    assert (
        inst.parameter[6].documentation
        == "The target identifer(s) of the requested type"
    )
    assert inst.parameter[6].max == "*"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "targetIdentifier"
    assert inst.parameter[6].type == "boolean"
    assert inst.parameter[6].use == "out"
    assert (
        inst.parameter[7].documentation == "Whether the target identifier is preferred."
    )
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "targetIdentifer.preferred"
    assert inst.parameter[7].type == "boolean"
    assert inst.parameter[7].use == "out"
    assert (
        inst.parameter[8].documentation
        == "The perioid when the target identifier is valid."
    )
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "targetIdentifier.period"
    assert inst.parameter[8].type == "boolean"
    assert inst.parameter[8].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "NamingSystem"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Translate id"
    assert inst.type is True
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/NamingSystem-" "translate-id"
    )
    assert inst.version == "4.5.0"


def test_operationdefinition_7(base_settings):
    """No. 7 tests collection for OperationDefinition.
    Test File: operation-namingsystem-translate-id.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-namingsystem-translate-id.json"
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
    assert inst.code == "subsumes"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 5
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "normative"
    assert inst.id == "CodeSystem-subsumes"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "subsumes"
    assert inst.parameter[0].documentation == (
        'The "A" code that is to be tested. If a code is provided, '
        "a system must be provided"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "codeA"
    assert inst.parameter[0].type == "code"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        'The "B" code that is to be tested. If a code is provided, '
        "a system must be provided"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "codeB"
    assert inst.parameter[1].type == "code"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "The code system in which subsumption testing is to be "
        "performed. This must be provided unless the operation is "
        "invoked on a code system instance"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "system"
    assert inst.parameter[2].type == "uri"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "The version of the code system, if one was provided in the " "source data"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "version"
    assert inst.parameter[3].type == "string"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == (
        'The "A" Coding that is to be tested. The code system does '
        "not have to match the specified subsumption code system, but"
        " the relationships between the code systems must be well "
        "established"
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "codingA"
    assert inst.parameter[4].type == "Coding"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
        'The "B" Coding that is to be tested. The code system does '
        "not have to match the specified subsumption code system, but"
        " the relationships between the code systems must be well "
        "established"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "codingB"
    assert inst.parameter[5].type == "Coding"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].binding.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/elementdefinition-" "bindingName"
    )
    assert (
        inst.parameter[6].binding.extension[0].valueString
        == "ConceptSubsumptionOutcome"
    )
    assert inst.parameter[6].binding.strength == "required"
    assert inst.parameter[6].binding.valueSet == (
        "http://hl7.org/fhir/ValueSet/concept-subsumption-" "outcome|4.5.0|4.5.0"
    )
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 1
    assert inst.parameter[6].name == "outcome"
    assert inst.parameter[6].type == "code"
    assert inst.parameter[6].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "CodeSystem"
    assert inst.status == "active"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Subsumption Testing"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/CodeSystem-subsumes"
    assert inst.version == "4.5.0"


def test_operationdefinition_8(base_settings):
    """No. 8 tests collection for OperationDefinition.
    Test File: operation-codesystem-subsumes.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-codesystem-subsumes.json"
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
    assert inst.affectsState is False
    assert inst.code == "data-requirements"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.description == (
        "The data-requirements operation aggregates and returns the "
        "parameters and data requirements for a resource and all its "
        "dependencies as a single module definition"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Library-data-requirements"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "data-requirements"
    assert (
        inst.parameter[0].documentation
        == "The target of the data requirements operation"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "target"
    assert inst.parameter[0].type == "string"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == "The result of the requirements gathering"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "return"
    assert inst.parameter[1].type == "Library"
    assert inst.parameter[1].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Library"
    assert inst.status == "draft"
    assert inst.system is True
    assert inst.text.status == "extensions"
    assert inst.title == "Data Requirements"
    assert inst.type is False
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/Library-data-" "requirements"
    )
    assert inst.version == "4.5.0"


def test_operationdefinition_9(base_settings):
    """No. 9 tests collection for OperationDefinition.
    Test File: operation-library-data-requirements.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-library-data-requirements.json"
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
    assert inst.affectsState is True
    assert inst.code == "process-message"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 4
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "MessageHeader-process-message"
    assert inst.instance is False
    assert inst.kind == "operation"
    assert inst.name == "process-message"
    assert inst.parameter[0].documentation == (
        "The message to process (or, if using asynchronous messaging,"
        " it may be a response message to accept)"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "content"
    assert inst.parameter[0].type == "Bundle"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "If 'true' the message is processed using the asynchronous " "messaging pattern"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "async"
    assert inst.parameter[1].type == "boolean"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "A URL to submit response messages to, if asynchronous "
        "messaging is being used, and if the "
        "MessageHeader.source.endpoint is not the appropriate place "
        "to submit responses"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "response-url"
    assert inst.parameter[2].type == "url"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "A response message, if synchronous messaging is being used "
        "(mandatory in this case). For asynchronous messaging, there "
        "is no return value"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "return"
    assert inst.parameter[3].type == "Bundle"
    assert inst.parameter[3].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "MessageHeader"
    assert inst.status == "draft"
    assert inst.system is True
    assert inst.text.status == "extensions"
    assert inst.title == "Process Message"
    assert inst.type is False
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/MessageHeader-" "process-message"
    )
    assert inst.version == "4.5.0"


def test_operationdefinition_10(base_settings):
    """No. 10 tests collection for OperationDefinition.
    Test File: operation-messageheader-process-message.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operation-messageheader-process-message.json"
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
