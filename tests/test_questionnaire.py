# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import questionnaire


def impl_questionnaire_1(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.id == "qgen-NutritionProduct1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[0].linkId == "NutritionProduct-flyover"
    assert inst.item[0].item[0].text == "A food or supplement that is consumed by patients."
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[1].item[0].linkId == "NutritionProduct.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "NutritionProduct.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "NutritionProduct.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[2].item[0].linkId == "NutritionProduct.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
    "The metadata about the resource. This is content that is "
    "maintained by the infrastructure. Changes to the content "
    "might not always be associated with version changes to the "
    "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "NutritionProduct.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[3].item[0].linkId == "NutritionProduct.implicitRules-flyover"
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "NutritionProduct.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert inst.item[0].item[3].item[1].text == "A set of rules under which this content was created"
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "NutritionProduct.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[4].item[0].linkId == "NutritionProduct.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[4].item[1].linkId == "NutritionProduct.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "NutritionProduct.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[5].item[0].linkId == "NutritionProduct.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "NutritionProduct.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].text == "Text summary of the resource, for human interpretation"
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[6].item[0].linkId == "NutritionProduct.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "NutritionProduct.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[7].item[0].linkId == "NutritionProduct.extension-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "NutritionProduct.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[8].item[0].linkId == "NutritionProduct.modifierExtension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "NutritionProduct.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[9].extension[1].valueString == "CodeableConcept"
    assert inst.item[0].item[9].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[9].item[0].linkId == "NutritionProduct.code-flyover"
    assert inst.item[0].item[9].item[0].text == (
    "The code assigned to the product, for example a USDA NDB "
    "number, a USDA FDC ID number, or a Langual code."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[9].item[1].linkId == "NutritionProduct.code.coding"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "code:"
    assert inst.item[0].item[9].item[1].type == "coding"
    assert inst.item[0].item[9].item[2].linkId == "NutritionProduct.code.text"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "text:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].linkId == "NutritionProduct.code"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == (
    "A code that can identify the detailed nutrients and "
    "ingredients in a specific food product"
    )
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "NutritionProduct"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == (
    "A product used for nutritional purposes (i.e. food or "
    "supplement)"
    )
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Orders and Observations)"
    assert inst.status == "draft"
    assert inst.url == "http://hl7.org/fhir/Questionnaire/qgen-NutritionProduct1"
    assert inst.version == "5.0.0-ballot"


def test_questionnaire_1(base_settings):
    """No. 1 tests collection for Questionnaire.
    Test File: nutritionproduct-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "nutritionproduct-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_1(inst2)


def impl_questionnaire_2(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.id == "qgen-OperationDefinition1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[0].linkId == "OperationDefinition-flyover"
    assert inst.item[0].item[0].text == (
    "A formal computable definition of an operation (on the "
    "RESTful interface) or a named query (using the search "
    "interaction)."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[1].item[0].linkId == "OperationDefinition.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "OperationDefinition.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "OperationDefinition.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[2].item[0].linkId == "OperationDefinition.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
    "The metadata about the resource. This is content that is "
    "maintained by the infrastructure. Changes to the content "
    "might not always be associated with version changes to the "
    "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "OperationDefinition.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[3].item[0].linkId == "OperationDefinition.implicitRules-flyover"
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "OperationDefinition.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert inst.item[0].item[3].item[1].text == "A set of rules under which this content was created"
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "OperationDefinition.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[4].item[0].linkId == "OperationDefinition.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[4].item[1].linkId == "OperationDefinition.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "OperationDefinition.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[5].item[0].linkId == "OperationDefinition.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "OperationDefinition.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].text == "Text summary of the resource, for human interpretation"
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[6].item[0].linkId == "OperationDefinition.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "OperationDefinition.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[7].item[0].linkId == "OperationDefinition.extension-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "OperationDefinition.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[8].item[0].linkId == "OperationDefinition.modifierExtension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "OperationDefinition.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[9].extension[1].valueString == "uri"
    assert inst.item[0].item[9].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[9].item[0].linkId == "OperationDefinition.url-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "OperationDefinition.url.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == (
    "Canonical identifier for this operation definition, "
    "represented as a URI (globally unique)"
    )
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].linkId == "OperationDefinition.url"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "OperationDefinition"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Definition of an operation or a named query"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "active"
    assert inst.url == "http://hl7.org/fhir/Questionnaire/qgen-OperationDefinition1"
    assert inst.version == "5.0.0-ballot"


def test_questionnaire_2(base_settings):
    """No. 2 tests collection for Questionnaire.
    Test File: operationdefinition-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operationdefinition-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_2(inst2)


def impl_questionnaire_3(inst):
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.id == "qgen-DeviceMetric1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "DeviceMetric-display"
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[1].linkId == "DeviceMetric-flyover"
    assert inst.item[0].item[1].text == (
    "Describes a measurement, calculation or setting capability "
    "of a medical device."
    )
    assert inst.item[0].item[1].type == "display"
    assert inst.item[0].item[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[2].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[2].item[0].linkId == "DeviceMetric.id-flyover"
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "DeviceMetric.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "DeviceMetric.id"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[3].item[0].linkId == "DeviceMetric.meta-flyover"
    assert inst.item[0].item[3].item[0].text == (
    "The metadata about the resource. This is content that is "
    "maintained by the infrastructure. Changes to the content "
    "might not always be associated with version changes to the "
    "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "DeviceMetric.meta"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].text == "Metadata about the resource"
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert inst.item[0].item[4].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[4].item[0].linkId == "DeviceMetric.implicitRules-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "DeviceMetric.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "A set of rules under which this content was created"
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "DeviceMetric.implicitRules"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert inst.item[0].item[5].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[5].item[0].linkId == "DeviceMetric.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[5].item[1].linkId == "DeviceMetric.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "coding"
    assert inst.item[0].item[5].linkId == "DeviceMetric.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[6].item[0].linkId == "DeviceMetric.text-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "DeviceMetric.text"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Text summary of the resource, for human interpretation"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[7].item[0].linkId == "DeviceMetric.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "DeviceMetric.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[8].item[0].linkId == "DeviceMetric.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "DeviceMetric.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[9].item[0].linkId == "DeviceMetric.modifierExtension-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "DeviceMetric.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "DeviceMetric"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == (
    "Measurement, calculation or setting capability of a medical "
    "device"
    )
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Health Care Devices)"
    assert inst.status == "draft"
    assert inst.url == "http://hl7.org/fhir/Questionnaire/qgen-DeviceMetric1"
    assert inst.version == "5.0.0-ballot"


def test_questionnaire_3(base_settings):
    """No. 3 tests collection for Questionnaire.
    Test File: devicemetric-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "devicemetric-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_3(inst2)


def impl_questionnaire_4(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.id == "qgen-RegulatedAuthorization1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[0].linkId == "RegulatedAuthorization-flyover"
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[1].item[0].linkId == "RegulatedAuthorization.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "RegulatedAuthorization.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "RegulatedAuthorization.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[2].item[0].linkId == "RegulatedAuthorization.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
    "The metadata about the resource. This is content that is "
    "maintained by the infrastructure. Changes to the content "
    "might not always be associated with version changes to the "
    "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "RegulatedAuthorization.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[3].item[0].linkId == "RegulatedAuthorization.implicitRules-flyover"
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "RegulatedAuthorization.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert inst.item[0].item[3].item[1].text == "A set of rules under which this content was created"
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "RegulatedAuthorization.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[4].item[0].linkId == "RegulatedAuthorization.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[4].item[1].linkId == "RegulatedAuthorization.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "RegulatedAuthorization.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[5].item[0].linkId == "RegulatedAuthorization.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "RegulatedAuthorization.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].text == "Text summary of the resource, for human interpretation"
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[6].item[0].linkId == "RegulatedAuthorization.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "RegulatedAuthorization.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[7].item[0].linkId == "RegulatedAuthorization.extension-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "RegulatedAuthorization.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[8].item[0].linkId == "RegulatedAuthorization.modifierExtension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "RegulatedAuthorization.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert inst.item[0].item[9].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[9].item[0].linkId == "RegulatedAuthorization.identifier-flyover"
    assert inst.item[0].item[9].item[0].text == (
    "Business identifier for the authorization, typically "
    "assigned by the authorizing body."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "RegulatedAuthorization.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "RegulatedAuthorization.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "RegulatedAuthorization.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "RegulatedAuthorization.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == (
    "Business identifier for the authorization, typically "
    "assigned by the authorizing body"
    )
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "RegulatedAuthorization"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == (
    "Regulatory approval, clearance or licencing related to a "
    "regulated product, treatment, facility or activity e.g. "
    "Market Authorization for a Medicinal Product"
    )
    assert inst.item[0].type == "group"
    assert inst.publisher == (
    "Health Level Seven International (Biomedical Research and "
    "Regulation)"
    )
    assert inst.status == "draft"
    assert inst.url == (
    "http://hl7.org/fhir/Questionnaire/qgen-"
    "RegulatedAuthorization1"
    )
    assert inst.version == "5.0.0-ballot"


def test_questionnaire_4(base_settings):
    """No. 4 tests collection for Questionnaire.
    Test File: regulatedauthorization-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "regulatedauthorization-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_4(inst2)


def impl_questionnaire_5(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.experimental is False
    assert inst.id == "qgen-actualgroup1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "minOccurs"
    )
    assert inst.item[0].extension[0].valueInteger == 1
    assert inst.item[0].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].extension[1].valueInteger == 1
    assert inst.item[0].item[0].linkId == "Group-display"
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[1].linkId == "Group-flyover"
    assert inst.item[0].item[1].type == "display"
    assert inst.item[0].item[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[2].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[2].item[0].linkId == "Group.id-flyover"
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "Group.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "Group.id"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[3].item[0].linkId == "Group.meta-flyover"
    assert inst.item[0].item[3].item[0].text == (
    "The metadata about the resource. This is content that is "
    "maintained by the infrastructure. Changes to the content "
    "might not always be associated with version changes to the "
    "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "Group.meta"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].text == "Metadata about the resource"
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert inst.item[0].item[4].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[4].item[0].linkId == "Group.implicitRules-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Group.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "A set of rules under which this content was created"
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "Group.implicitRules"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert inst.item[0].item[5].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[5].item[0].linkId == "Group.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[5].item[1].linkId == "Group.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "coding"
    assert inst.item[0].item[5].linkId == "Group.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[6].item[0].linkId == "Group.text-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Group.text"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Text summary of the resource, for human interpretation"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[7].item[0].linkId == "Group.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Group.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[8].item[0].linkId == "Group.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Group.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[9].item[0].linkId == "Group.modifierExtension-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "Group.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Group"
    assert inst.item[0].repeats is False
    assert inst.item[0].required is True
    assert inst.item[0].text == "Group of multiple entities"
    assert inst.item[0].type == "group"
    assert inst.publisher == "HL7"
    assert inst.status == "draft"
    assert inst.url == "http://hl7.org/fhir/Questionnaire/qgen-actualgroup1"
    assert inst.version == "5.0.0-ballot"


def test_questionnaire_5(base_settings):
    """No. 5 tests collection for Questionnaire.
    Test File: actualgroup-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "actualgroup-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_5(inst2)


def impl_questionnaire_6(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.contained[3].id == "vs5"
    assert inst.contained[4].id == "vs6"
    assert inst.contained[5].id == "vs7"
    assert inst.contained[6].id == "vs8"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.experimental is False
    assert inst.id == "qgen-shareableplandefinition1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "minOccurs"
    )
    assert inst.item[0].extension[0].valueInteger == 1
    assert inst.item[0].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].extension[1].valueInteger == 1
    assert inst.item[0].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[0].linkId == "PlanDefinition-flyover"
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[1].item[0].linkId == "PlanDefinition.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "PlanDefinition.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "PlanDefinition.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[2].item[0].linkId == "PlanDefinition.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
    "The metadata about the resource. This is content that is "
    "maintained by the infrastructure. Changes to the content "
    "might not always be associated with version changes to the "
    "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "PlanDefinition.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[3].item[0].linkId == "PlanDefinition.implicitRules-flyover"
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "PlanDefinition.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert inst.item[0].item[3].item[1].text == "A set of rules under which this content was created"
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "PlanDefinition.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[4].item[0].linkId == "PlanDefinition.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[4].item[1].linkId == "PlanDefinition.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "PlanDefinition.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[5].item[0].linkId == "PlanDefinition.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "PlanDefinition.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].text == "Text summary of the resource, for human interpretation"
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[6].item[0].linkId == "PlanDefinition.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "PlanDefinition.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[7].item[0].linkId == "PlanDefinition.extension-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "PlanDefinition.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[8].item[0].linkId == "PlanDefinition.modifierExtension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "PlanDefinition.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "minOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[9].extension[1].valueInteger == 1
    assert inst.item[0].item[9].extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[9].extension[2].valueString == "uri"
    assert inst.item[0].item[9].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[9].item[0].linkId == "PlanDefinition.url-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "PlanDefinition.url.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == (
    "Canonical identifier for this plan definition, represented "
    "as a URI (globally unique)"
    )
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].linkId == "PlanDefinition.url"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is True
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "PlanDefinition"
    assert inst.item[0].repeats is False
    assert inst.item[0].required is True
    assert inst.item[0].text == (
    "The definition of a plan for a series of actions, "
    "independent of any specific patient or context"
    )
    assert inst.item[0].type == "group"
    assert inst.publisher == "HL7"
    assert inst.status == "draft"
    assert inst.url == (
    "http://hl7.org/fhir/Questionnaire/qgen-"
    "shareableplandefinition1"
    )
    assert inst.version == "5.0.0-ballot"


def test_questionnaire_6(base_settings):
    """No. 6 tests collection for Questionnaire.
    Test File: shareableplandefinition-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "shareableplandefinition-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_6(inst2)


def impl_questionnaire_7(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.id == "qgen-AllergyIntolerance1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "AllergyIntolerance-display"
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[1].linkId == "AllergyIntolerance-flyover"
    assert inst.item[0].item[1].text == (
    "Risk of harmful or undesirable physiological response which "
    "is specific to an individual and associated with exposure to"
    " a substance."
    )
    assert inst.item[0].item[1].type == "display"
    assert inst.item[0].item[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[2].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[2].item[0].linkId == "AllergyIntolerance.id-flyover"
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "AllergyIntolerance.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "AllergyIntolerance.id"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[3].item[0].linkId == "AllergyIntolerance.meta-flyover"
    assert inst.item[0].item[3].item[0].text == (
    "The metadata about the resource. This is content that is "
    "maintained by the infrastructure. Changes to the content "
    "might not always be associated with version changes to the "
    "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "AllergyIntolerance.meta"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].text == "Metadata about the resource"
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert inst.item[0].item[4].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[4].item[0].linkId == "AllergyIntolerance.implicitRules-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "AllergyIntolerance.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "A set of rules under which this content was created"
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "AllergyIntolerance.implicitRules"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert inst.item[0].item[5].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[5].item[0].linkId == "AllergyIntolerance.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[5].item[1].linkId == "AllergyIntolerance.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "coding"
    assert inst.item[0].item[5].linkId == "AllergyIntolerance.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[6].item[0].linkId == "AllergyIntolerance.text-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "AllergyIntolerance.text"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Text summary of the resource, for human interpretation"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[7].item[0].linkId == "AllergyIntolerance.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "AllergyIntolerance.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[8].item[0].linkId == "AllergyIntolerance.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "AllergyIntolerance.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[9].item[0].linkId == "AllergyIntolerance.modifierExtension-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "AllergyIntolerance.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "AllergyIntolerance"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == (
    "Allergy or Intolerance (generally: Risk of adverse reaction "
    "to a substance)"
    )
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Patient Care)"
    assert inst.status == "draft"
    assert inst.url == "http://hl7.org/fhir/Questionnaire/qgen-AllergyIntolerance1"
    assert inst.version == "5.0.0-ballot"


def test_questionnaire_7(base_settings):
    """No. 7 tests collection for Questionnaire.
    Test File: allergyintolerance-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "allergyintolerance-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_7(inst2)


def impl_questionnaire_8(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.date == fhirtypes.DateTime.validate("2018-08-11T00:00:00+10:00")
    assert inst.experimental is False
    assert inst.id == "qgen-bodytemp1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "Observation-display"
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[1].linkId == "Observation-flyover"
    assert inst.item[0].item[1].text == (
    "This profile defines  how to represent Body Temperature "
    "observations in FHIR using a standard LOINC code and UCUM "
    "units of measure."
    )
    assert inst.item[0].item[1].type == "display"
    assert inst.item[0].item[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[2].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[2].item[0].linkId == "Observation.id-flyover"
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "Observation.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "Observation.id"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[3].item[0].linkId == "Observation.meta-flyover"
    assert inst.item[0].item[3].item[0].text == (
    "The metadata about the resource. This is content that is "
    "maintained by the infrastructure. Changes to the content "
    "might not always be associated with version changes to the "
    "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "Observation.meta"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].text == "Metadata about the resource"
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert inst.item[0].item[4].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[4].item[0].linkId == "Observation.implicitRules-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Observation.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "A set of rules under which this content was created"
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "Observation.implicitRules"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert inst.item[0].item[5].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[5].item[0].linkId == "Observation.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[5].item[1].linkId == "Observation.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "coding"
    assert inst.item[0].item[5].linkId == "Observation.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[6].item[0].linkId == "Observation.text-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Observation.text"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Text summary of the resource, for human interpretation"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[7].item[0].linkId == "Observation.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Observation.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[8].item[0].linkId == "Observation.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Observation.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[9].item[0].linkId == "Observation.modifierExtension-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "Observation.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Observation"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "FHIR Body Temperature Profile"
    assert inst.item[0].type == "group"
    assert inst.publisher == (
    "Health Level Seven International (Orders and Observations "
    "Workgroup)"
    )
    assert inst.status == "draft"
    assert inst.url == "http://hl7.org/fhir/Questionnaire/qgen-bodytemp1"
    assert inst.version == "5.0.0-ballot"


def test_questionnaire_8(base_settings):
    """No. 8 tests collection for Questionnaire.
    Test File: bodytemp-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "bodytemp-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_8(inst2)


def impl_questionnaire_9(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.date == fhirtypes.DateTime.validate("2021-02-15T00:00:00+10:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "minOccurs"
    )
    assert inst.item[0].extension[0].valueInteger == 1
    assert inst.item[0].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].extension[1].valueInteger == 1
    assert inst.item[0].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[0].linkId == "ValueSet-flyover"
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[1].item[0].linkId == "ValueSet.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "ValueSet.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "ValueSet.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[2].item[0].linkId == "ValueSet.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
    "The metadata about the resource. This is content that is "
    "maintained by the infrastructure. Changes to the content "
    "might not always be associated with version changes to the "
    "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "ValueSet.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[3].item[0].linkId == "ValueSet.implicitRules-flyover"
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "ValueSet.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert inst.item[0].item[3].item[1].text == "A set of rules under which this content was created"
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "ValueSet.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[4].item[0].linkId == "ValueSet.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[4].item[1].linkId == "ValueSet.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "ValueSet.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[5].item[0].linkId == "ValueSet.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "ValueSet.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].text == "Text summary of the resource, for human interpretation"
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[6].item[0].linkId == "ValueSet.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "ValueSet.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[7].item[0].linkId == "ValueSet.extension-flyover"
    assert inst.item[0].item[7].item[0].text == "An Extension"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "ValueSet.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Extension"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[8].item[0].linkId == "ValueSet.modifierExtension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "ValueSet.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "minOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[9].extension[1].valueInteger == 1
    assert inst.item[0].item[9].extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[9].extension[2].valueString == "uri"
    assert inst.item[0].item[9].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[9].item[0].linkId == "ValueSet.url-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "ValueSet.url.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == (
    "Canonical identifier for this value set, represented as a "
    "URI (globally unique)"
    )
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].linkId == "ValueSet.url"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is True
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "ValueSet"
    assert inst.item[0].repeats is False
    assert inst.item[0].required is True
    assert inst.item[0].text == "A set of codes drawn from one or more code systems"
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.publisher == "HL7"
    assert inst.status == "draft"
    assert inst.version == "5.0.0-cibuild"


def test_questionnaire_9(base_settings):
    """No. 9 tests collection for Questionnaire.
    Test File: vsd-alignedvalueset-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "vsd-alignedvalueset-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_9(inst2)


def impl_questionnaire_10(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.experimental is False
    assert inst.id == "qgen-DocumentReference1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "DocumentReference-display"
    assert inst.item[0].item[0].text == (
    "Usually, this is used for documents other than those defined"
    " by FHIR."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[1].linkId == "DocumentReference-flyover"
    assert inst.item[0].item[1].type == "display"
    assert inst.item[0].item[2].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[2].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[2].item[0].linkId == "DocumentReference.id-flyover"
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "DocumentReference.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "DocumentReference.id"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[3].item[0].linkId == "DocumentReference.meta-flyover"
    assert inst.item[0].item[3].item[0].text == (
    "The metadata about the resource. This is content that is "
    "maintained by the infrastructure. Changes to the content "
    "might not always be associated with version changes to the "
    "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "DocumentReference.meta"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].text == "Metadata about the resource"
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert inst.item[0].item[4].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[4].item[0].linkId == "DocumentReference.implicitRules-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "DocumentReference.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "A set of rules under which this content was created"
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "DocumentReference.implicitRules"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "fhirType"
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert inst.item[0].item[5].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[5].item[0].linkId == "DocumentReference.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].answerConstraint == "optionsOnly"
    assert inst.item[0].item[5].item[1].linkId == "DocumentReference.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "coding"
    assert inst.item[0].item[5].linkId == "DocumentReference.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[6].item[0].linkId == "DocumentReference.text-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "DocumentReference.text"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Text summary of the resource, for human interpretation"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[7].item[0].linkId == "DocumentReference.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "DocumentReference.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[8].item[0].linkId == "DocumentReference.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "DocumentReference.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/questionnaire-"
    "itemControl"
    )
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code == "flyover"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display == "Fly-over"
    assert inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/questionnaire-item-control"
    assert inst.item[0].item[9].item[0].linkId == "DocumentReference.modifierExtension-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "DocumentReference.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "DocumentReference"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "A reference to a document"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Orders and Observations)"
    assert inst.status == "draft"
    assert inst.url == "http://hl7.org/fhir/Questionnaire/qgen-DocumentReference1"
    assert inst.version == "5.0.0-ballot"


def test_questionnaire_10(base_settings):
    """No. 10 tests collection for Questionnaire.
    Test File: documentreference-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "documentreference-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_10(inst2)