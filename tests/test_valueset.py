# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import valueset


def impl_valueset_1(inst):
    assert inst.compose.include[0].system == "http://cds-hooks.hl7.org/CodeSystem/indicator"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2022-09-10T04:52:37+10:00")
    assert inst.description == (
    "This value set captures the set of indicator codes defined "
    "by the CDS Hooks specification."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "vocab"
    assert inst.id == "cdshooks-indicator"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.1065"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2022-09-10T04:52:37.223+10:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    assert inst.name == "Indicator"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CDSHooksIndicator"
    assert inst.url == "http://hl7.org/fhir/ValueSet/cdshooks-indicator"
    assert inst.version == "5.0.0-ballot"


def test_valueset_1(base_settings):
    """No. 1 tests collection for ValueSet.
    Test File: valueset-cdshooks-indicator.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-cdshooks-indicator.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_1(inst2)


def impl_valueset_2(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/ingredient-manufacturer-role"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
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
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "ingredient-manufacturer-role"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.3247"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2022-09-10T04:52:37.223+10:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    assert inst.name == "IngredientManufacturerRole"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "IngredientManufacturerRole"
    assert inst.url == "http://hl7.org/fhir/ValueSet/ingredient-manufacturer-role"
    assert inst.version == "5.0.0-ballot"


def test_valueset_2(base_settings):
    """No. 2 tests collection for ValueSet.
    Test File: valueset-ingredient-manufacturer-role.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-ingredient-manufacturer-role.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_2(inst2)


def impl_valueset_3(inst):
    assert inst.compose.include[0].system == "urn:oid:1.2.36.1.2001.1001.101.104.16592"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://www.nehta.gov.au"
    assert inst.description == (
    "Example Item Flags for the List Resource. In this case, "
    "these are the kind of flags that would be used on a "
    "medication list at the end of a consultation."
    )
    assert inst.experimental is True
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "list-item-flag"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.320"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2022-09-10T04:52:37.223+10:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    assert inst.name == "PatientMedicineChangeTypes"
    assert inst.publisher == "National E-Health Transition Authority Ltd (NEHTA)"
    assert inst.status == "draft"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\"><ul><li>Include "
    "all codes defined in <a href=\"codesystem-list-item-flag.htm"
    "l\"><code>urn:oid:1.2.36.1.2001.1001.101.104.16592</code></a"
    "></li></ul></div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Patient Medicine Change Types"
    assert inst.url == "http://hl7.org/fhir/ValueSet/list-item-flag"
    assert inst.version == "5.0.0-ballot"


def test_valueset_3(base_settings):
    """No. 3 tests collection for ValueSet.
    Test File: valueset-list-item-flag.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-list-item-flag.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_3(inst2)


def impl_valueset_4(inst):
    assert inst.compose.include[0].filter[0].op == "descendent-of"
    assert inst.compose.include[0].filter[0].property == "concept"
    assert inst.compose.include[0].filter[0].value == "research-study-phase"
    assert inst.compose.include[0].system == "http://hl7.org/fhir/research-study-classifiers"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == (
    "Codes for the stage in the progression of a therapy from "
    "initial experimental use in humans in clinical trials to "
    "post-market evaluation."
    )
    assert inst.experimental is True
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "brr"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "research-study-phase"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.821"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2022-09-10T04:52:37.223+10:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    assert inst.name == "ResearchStudyPhase"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "ResearchStudyPhase"
    assert inst.url == "http://hl7.org/fhir/ValueSet/research-study-phase"
    assert inst.version == "5.0.0-ballot"


def test_valueset_4(base_settings):
    """No. 4 tests collection for ValueSet.
    Test File: valueset-research-study-phase.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-research-study-phase.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_4(inst2)


def impl_valueset_5(inst):
    assert inst.compose.include[0].system == (
    "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpre"
    "tation"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
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
    assert inst.extension[1].valueCode == "normative"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "normative-version"
    )
    assert inst.extension[2].valueCode == "4.0.0"
    assert inst.extension[3].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[3].valueInteger == 5
    assert inst.id == "observation-interpretation"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.399"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2022-09-10T04:52:37.223+10:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    assert inst.name == "ObservationInterpretationCodes"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Observation Interpretation Codes"
    assert inst.url == "http://hl7.org/fhir/ValueSet/observation-interpretation"
    assert inst.version == "5.0.0-ballot"


def test_valueset_5(base_settings):
    """No. 5 tests collection for ValueSet.
    Test File: valueset-observation-interpretation.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-observation-interpretation.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_5(inst2)


def impl_valueset_6(inst):
    assert inst.compose.include[0].valueSet[0] == "http://hl7.org/fhir/ValueSet/substance-code"
    assert inst.compose.include[1].filter[0].op == "is-a"
    assert inst.compose.include[1].filter[0].property == "concept"
    assert inst.compose.include[1].filter[0].value == "418038007"
    assert inst.compose.include[1].system == "http://snomed.info/sct"
    assert inst.compose.include[2].filter[0].op == "is-a"
    assert inst.compose.include[2].filter[0].property == "concept"
    assert inst.compose.include[2].filter[0].value == "267425008"
    assert inst.compose.include[2].system == "http://snomed.info/sct"
    assert inst.compose.include[3].filter[0].op == "is-a"
    assert inst.compose.include[3].filter[0].property == "concept"
    assert inst.compose.include[3].filter[0].value == "29736007"
    assert inst.compose.include[3].system == "http://snomed.info/sct"
    assert inst.compose.include[4].filter[0].op == "is-a"
    assert inst.compose.include[4].filter[0].property == "concept"
    assert inst.compose.include[4].filter[0].value == "340519003"
    assert inst.compose.include[4].system == "http://snomed.info/sct"
    assert inst.compose.include[5].filter[0].op == "is-a"
    assert inst.compose.include[5].filter[0].property == "concept"
    assert inst.compose.include[5].filter[0].value == "190753003"
    assert inst.compose.include[5].system == "http://snomed.info/sct"
    assert inst.compose.include[6].filter[0].op == "is-a"
    assert inst.compose.include[6].filter[0].property == "concept"
    assert inst.compose.include[6].filter[0].value == "413427002"
    assert inst.compose.include[6].system == "http://snomed.info/sct"
    assert inst.compose.include[7].filter[0].op == "is-a"
    assert inst.compose.include[7].filter[0].property == "concept"
    assert inst.compose.include[7].filter[0].value == "716186003"
    assert inst.compose.include[7].system == "http://snomed.info/sct"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.experimental is True
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "pc"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "allergyintolerance-code"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.137"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2022-09-10T04:52:37.223+10:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    assert inst.name == (
    "AllergyIntoleranceSubstance/Product,ConditionAndNegationCode"
    "s"
    )
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == (
    "AllergyIntolerance Substance/Product, Condition and Negation"
    " Codes"
    )
    assert inst.url == "http://hl7.org/fhir/ValueSet/allergyintolerance-code"
    assert inst.version == "5.0.0-ballot"


def test_valueset_6(base_settings):
    """No. 6 tests collection for ValueSet.
    Test File: valueset-allergyintolerance-code.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-allergyintolerance-code.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_6(inst2)


def impl_valueset_7(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/codesystem-properties-mode"
    assert inst.description == "Description Needed Here"
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "vocab"
    assert inst.id == "codesystem-properties-mode"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.3129"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2022-09-10T04:52:37.223+10:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    assert inst.name == "CodeSystemPropertiesMode"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/codesystem-properties-mode"
    assert inst.version == "5.0.0-ballot"


def test_valueset_7(base_settings):
    """No. 7 tests collection for ValueSet.
    Test File: valueset-codesystem-properties-mode.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-codesystem-properties-mode.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_7(inst2)


def impl_valueset_8(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/eligibility-outcome"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == "The outcome of the processing."
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "fm"
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
    assert inst.id == "eligibility-outcome"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.3233"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2022-09-10T04:52:37.223+10:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    assert inst.name == "EligibilityOutcome"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\"><ul><li>Include "
    "all codes defined in <a href=\"codesystem-eligibility-"
    "outcome.html\"><code>http://hl7.org/fhir/eligibility-"
    "outcome</code></a></li></ul></div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "EligibilityOutcome"
    assert inst.url == "http://hl7.org/fhir/ValueSet/eligibility-outcome"
    assert inst.version == "5.0.0-ballot"


def test_valueset_8(base_settings):
    """No. 8 tests collection for ValueSet.
    Test File: valueset-eligibility-outcome.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-eligibility-outcome.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_8(inst2)


def impl_valueset_9(inst):
    assert inst.compose.include[0].system == "http://terminology.hl7.org/CodeSystem/benefit-term"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.copyright == "This is an example set."
    assert inst.description == "This value set includes a smattering of Benefit Term codes."
    assert inst.experimental is True
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "fm"
    assert inst.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "benefit-term"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.612"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2022-09-10T04:52:37.223+10:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    assert inst.name == "BenefitTermCodes"
    assert inst.publisher == "Financial Management"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Benefit Term Codes"
    assert inst.url == "http://hl7.org/fhir/ValueSet/benefit-term"
    assert inst.version == "5.0.0-ballot"


def test_valueset_9(base_settings):
    """No. 9 tests collection for ValueSet.
    Test File: valueset-benefit-term.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-benefit-term.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_9(inst2)


def impl_valueset_10(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/goal-relationship-type"
    assert inst.description == "Description Needed Here"
    assert inst.experimental is False
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
    "wg"
    )
    assert inst.extension[0].valueCode == "pc"
    assert inst.id == "goal-relationship-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.915"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2022-09-10T04:52:37.223+10:00")
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    assert inst.name == "GoalRelationshipType"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/goal-relationship-type"
    assert inst.version == "5.0.0-ballot"


def test_valueset_10(base_settings):
    """No. 10 tests collection for ValueSet.
    Test File: valueset-goal-relationship-type.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-goal-relationship-type.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_10(inst2)