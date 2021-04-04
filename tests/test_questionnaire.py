# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import questionnaire


def impl_questionnaire_1(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "Library.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "Library.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "Library.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "Library.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "Library.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Library.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "Library.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "Library.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Library.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Library.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Library.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[1].valueString == "uri"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "Library.url.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == (
        "Canonical identifier for this library, represented as a URI "
        "(globally unique)"
    )
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].linkId == "Library.url"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Library"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Represents a library of quality improvement components"
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.publisher == "Health Level Seven International (Clinical Decision Support)"
    )
    assert inst.status == "draft"
    assert inst.version == "4.5.0"


def test_questionnaire_1(base_settings):
    """No. 1 tests collection for Questionnaire.
    Test File: library-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "library-questionnaire.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2013-12-03T00:00:00+00:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].type == "display"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "Provenance.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "Provenance.id"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "Provenance.meta"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].text == "Metadata about the resource"
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Provenance.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert (
        inst.item[0].item[4].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "Provenance.implicitRules"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "Provenance.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "choice"
    assert inst.item[0].item[5].linkId == "Provenance.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Provenance.text"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert (
        inst.item[0].item[6].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Provenance.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Provenance.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "Provenance.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Provenance"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Who, What, When for a set of resources"
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Health Level Seven International"
    assert inst.status == "draft"
    assert inst.version == "4.5.0"


def test_questionnaire_2(base_settings):
    """No. 2 tests collection for Questionnaire.
    Test File: provenance-relevant-history-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "provenance-relevant-history-questionnaire.json"
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
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].text == (
        "A record of a request for service such as diagnostic "
        "investigations, treatments, or operations to be performed."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "ServiceRequest.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "ServiceRequest.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "ServiceRequest.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "ServiceRequest.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "ServiceRequest.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "ServiceRequest.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "ServiceRequest.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "ServiceRequest.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "ServiceRequest.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "ServiceRequest.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "ServiceRequest.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "ServiceRequest.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "ServiceRequest.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "ServiceRequest.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "ServiceRequest.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Identifiers assigned to this order"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "ServiceRequest"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "A request for a service to be performed"
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.publisher == "Health Level Seven International (Orders and Observations)"
    )
    assert inst.status == "draft"
    assert inst.version == "4.5.0"


def test_questionnaire_3(base_settings):
    """No. 3 tests collection for Questionnaire.
    Test File: servicerequest-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-questionnaire.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T05:55:11+00:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "minOccurs"
    )
    assert inst.item[0].extension[0].valueInteger == 1
    assert inst.item[0].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].extension[1].valueInteger == 1
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].text == (
        "A group of related requests that can be used to capture "
        "intended activities that have inter-dependencies such as "
        '"give this medication after that one".'
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "RequestGroup.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "RequestGroup.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "RequestGroup.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "RequestGroup.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "RequestGroup.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "RequestGroup.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "RequestGroup.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "RequestGroup.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "RequestGroup.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "RequestGroup.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "RequestGroup.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "minOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[9].extension[1].valueInteger == 1
    assert inst.item[0].item[9].extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[2].valueString == "Identifier"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[9].item[0].text == (
        "Allows a service to provide a unique, business identifier " "for the request."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "RequestGroup.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "RequestGroup.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "RequestGroup.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "RequestGroup.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is True
    assert inst.item[0].item[9].text == "Business identifier"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "RequestGroup"
    assert inst.item[0].repeats is False
    assert inst.item[0].required is True
    assert inst.item[0].text == "A group of related requests"
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "HL7"
    assert inst.status == "draft"
    assert inst.version == "4.5.0"


def test_questionnaire_4(base_settings):
    """No. 4 tests collection for Questionnaire.
    Test File: cdshooksrequestgroup-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "cdshooksrequestgroup-questionnaire.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].text == (
        "An authorization for the provision of glasses and/or contact"
        " lenses to a patient."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "VisionPrescription.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "VisionPrescription.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "VisionPrescription.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert (
        inst.item[0].item[3].item[1].linkId == "VisionPrescription.implicitRules.value"
    )
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "VisionPrescription.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "VisionPrescription.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "VisionPrescription.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "VisionPrescription.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "VisionPrescription.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "VisionPrescription.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "VisionPrescription.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[9].item[0].text
        == "A unique identifier assigned to this vision prescription."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "VisionPrescription.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "VisionPrescription.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "VisionPrescription.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "VisionPrescription.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Business Identifier for vision prescription"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "VisionPrescription"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert (
        inst.item[0].text == "Prescription for vision correction products for a patient"
    )
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Health Level Seven International (Financial Management)"
    assert inst.status == "draft"
    assert inst.version == "4.5.0"


def test_questionnaire_5(base_settings):
    """No. 5 tests collection for Questionnaire.
    Test File: visionprescription-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "visionprescription-questionnaire.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].text == (
        "A medicinal product in the final form which is suitable for "
        "administering to a patient (after any mixing of multiple "
        "components, dissolution etc. has been performed)."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].item[0].type == "display"
    assert (
        inst.item[0].item[1].item[1].linkId == "AdministrableProductDefinition.id.value"
    )
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "AdministrableProductDefinition.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "AdministrableProductDefinition.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert (
        inst.item[0].item[3].item[1].linkId
        == "AdministrableProductDefinition.implicitRules.value"
    )
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "AdministrableProductDefinition.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert (
        inst.item[0].item[4].item[1].linkId
        == "AdministrableProductDefinition.language.value"
    )
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "AdministrableProductDefinition.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "AdministrableProductDefinition.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "AdministrableProductDefinition.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "AdministrableProductDefinition.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert (
        inst.item[0].item[8].linkId
        == "AdministrableProductDefinition.modifierExtension"
    )
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[9].item[0].text
        == "An identifier for the administrable product."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert (
        inst.item[0].item[9].item[1].linkId
        == "AdministrableProductDefinition.identifier.label"
    )
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert (
        inst.item[0].item[9].item[2].linkId
        == "AdministrableProductDefinition.identifier.system"
    )
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert (
        inst.item[0].item[9].item[3].linkId
        == "AdministrableProductDefinition.identifier.value"
    )
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "AdministrableProductDefinition.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "An identifier for the administrable product"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "AdministrableProductDefinition"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == (
        "A medicinal product in the final form which is suitable for "
        "administering to a patient (after any mixing of multiple "
        "components, dissolution etc. has been performed)"
    )
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == (
        "Health Level Seven International (Biomedical Research and " "Regulation)"
    )
    assert inst.status == "draft"
    assert inst.version == "4.5.0"


def test_questionnaire_6(base_settings):
    """No. 6 tests collection for Questionnaire.
    Test File: administrableproductdefinition-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "administrableproductdefinition-questionnaire.json"
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
    assert inst.contained[1].id == "vs3"
    assert inst.date == fhirtypes.DateTime.validate("2021-02-15T00:00:00+00:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "minOccurs"
    )
    assert inst.item[0].extension[0].valueInteger == 1
    assert inst.item[0].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].extension[1].valueInteger == 1
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
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
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
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
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "ValueSet.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "ValueSet.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "ValueSet.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "ValueSet.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "ValueSet.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "ValueSet.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].text == "An Extension"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "ValueSet.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Extension"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "ValueSet.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "minOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[9].extension[1].valueInteger == 1
    assert inst.item[0].item[9].extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[2].valueString == "uri"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
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
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "HL7"
    assert inst.status == "draft"
    assert inst.version == "4.5.0"


def test_questionnaire_7(base_settings):
    """No. 7 tests collection for Questionnaire.
    Test File: vsd-alignedvalueset-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "vsd-alignedvalueset-questionnaire.json"
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
    assert inst.code[0].code == "VL 1-1, 18-65_1.2.2"
    assert inst.code[0].display == "Lifelines Questionnaire 1 part 1"
    assert inst.code[0].system == "http://example.org/system/code/lifelines/nl"
    assert inst.date == fhirtypes.DateTime.validate("2010")
    assert inst.id == "f201"
    assert inst.item[0].linkId == "1"
    assert inst.item[0].text == "Do you have allergies?"
    assert inst.item[0].type == "boolean"
    assert inst.item[1].item[0].linkId == "2.1"
    assert inst.item[1].item[0].text == "What is your gender?"
    assert inst.item[1].item[0].type == "string"
    assert inst.item[1].item[1].linkId == "2.2"
    assert inst.item[1].item[1].text == "What is your date of birth?"
    assert inst.item[1].item[1].type == "date"
    assert inst.item[1].item[2].linkId == "2.3"
    assert inst.item[1].item[2].text == "What is your country of birth?"
    assert inst.item[1].item[2].type == "string"
    assert inst.item[1].item[3].linkId == "2.4"
    assert inst.item[1].item[3].text == "What is your marital status?"
    assert inst.item[1].item[3].type == "string"
    assert inst.item[1].linkId == "2"
    assert inst.item[1].text == "General questions"
    assert inst.item[1].type == "group"
    assert inst.item[2].item[0].linkId == "3.1"
    assert inst.item[2].item[0].text == "Do you smoke?"
    assert inst.item[2].item[0].type == "boolean"
    assert inst.item[2].item[1].linkId == "3.2"
    assert inst.item[2].item[1].text == "Do you drink alchohol?"
    assert inst.item[2].item[1].type == "boolean"
    assert inst.item[2].linkId == "3"
    assert inst.item[2].text == "Intoxications"
    assert inst.item[2].type == "group"
    assert inst.status == "active"
    assert inst.subjectType[0] == "Patient"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/Questionnaire/f201"


def test_questionnaire_8(base_settings):
    """No. 8 tests collection for Questionnaire.
    Test File: questionnaire-example-f201-lifelines.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "questionnaire-example-f201-lifelines.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].text == (
        "This resource provides the status of the payment for goods "
        "and services rendered, and the request and response resource"
        " references."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "PaymentNotice.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "PaymentNotice.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "PaymentNotice.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "PaymentNotice.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "PaymentNotice.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "PaymentNotice.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "PaymentNotice.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "PaymentNotice.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "PaymentNotice.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "PaymentNotice.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "PaymentNotice.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[9].item[0].text
        == "A unique identifier assigned to this payment notice."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "PaymentNotice.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "PaymentNotice.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "PaymentNotice.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "PaymentNotice.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Business Identifier for the payment noctice"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "PaymentNotice"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "PaymentNotice request"
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Health Level Seven International (Financial Management)"
    assert inst.status == "draft"
    assert inst.version == "4.5.0"


def test_questionnaire_9(base_settings):
    """No. 9 tests collection for Questionnaire.
    Test File: paymentnotice-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "paymentnotice-questionnaire.json"
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
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.date == fhirtypes.DateTime.validate("2015-05-30T00:00:00+00:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "Questionnaire.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "Questionnaire.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "Questionnaire.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "Questionnaire.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "Questionnaire.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Questionnaire.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "Questionnaire.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "Questionnaire.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Questionnaire.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].text == "An Extension"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Questionnaire.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Extension"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Questionnaire.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[1].valueString == "uri"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "Questionnaire.url.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == (
        "Canonical identifier for this questionnaire, represented as "
        "a URI (globally unique)"
    )
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].linkId == "Questionnaire.url"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Questionnaire"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == (
        "A questionnaire with the ability to specify behavior "
        "associated with questions or groups of questions"
    )
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Health Level Seven, Inc. - CDS WG"
    assert inst.status == "draft"
    assert inst.version == "4.5.0"


def test_questionnaire_10(base_settings):
    """No. 10 tests collection for Questionnaire.
    Test File: cqf-questionnaire-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "cqf-questionnaire-questionnaire.json"
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
