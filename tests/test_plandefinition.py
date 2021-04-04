# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import plandefinition


def impl_plandefinition_1(inst):
    assert inst.action[0].action[0].description == "Will revise"
    assert inst.action[0].action[1].description == (
        "Risk of overdose carefully considered and outweighed by "
        "benefit; snooze 3 mo"
    )
    assert inst.action[0].action[2].description == "N/A - see comment; snooze 3 mo"
    assert inst.action[0].condition[0].expression.description == (
        "Check whether the existing patient is using opioids "
        "concurrently with benzodiazepines."
    )
    assert inst.action[0].condition[0].expression.expression == "Inclusion Criteria"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].description == (
        "Checking if the trigger prescription meets the inclusion "
        "criteria for recommendation #11 workflow."
    )
    assert inst.action[0].documentation[0].document.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/cqf-" "strengthOfRecommendation"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "strong"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Strong"
    )
    assert inst.action[0].documentation[0].document.extension[
        0
    ].valueCodeableConcept.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/recommendation-" "strength"
    )
    assert inst.action[0].documentation[0].document.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/cqf-" "qualityOfEvidence"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .code
        == "low"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .display
        == "Low quality"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .system
        == "http://terminology.hl7.org/CodeSystem/evidence-quality"
    )
    assert inst.action[0].documentation[0].type == "documentation"
    assert inst.action[0].dynamicValue[0].expression.expression == "Get Detail"
    assert inst.action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[0].path == "action.description"
    assert inst.action[0].dynamicValue[1].expression.expression == "Get Summary"
    assert inst.action[0].dynamicValue[1].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[1].path == "action.title"
    assert inst.action[0].dynamicValue[2].expression.expression == "Get Indicator"
    assert inst.action[0].dynamicValue[2].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[2].path == "action.extension"
    assert inst.action[0].groupingBehavior == "visual-group"
    assert inst.action[0].selectionBehavior == "exactly-one"
    assert inst.action[0].title == (
        "Existing patient has concurrent opioid and benzodiazepine " "prescriptions."
    )
    assert inst.action[0].trigger[0].name == "medication-prescribe"
    assert inst.action[0].trigger[0].type == "named-event"
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.copyright == "© CDC 2016+."
    assert inst.date == fhirtypes.DateTime.validate("2018-03-19")
    assert inst.description == (
        "Concurrently prescribing opioid medications with "
        "benzodiazepines increases the risk of harm for the patient."
    )
    assert inst.id == "opioidcds-11"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "cdc-opioid-guidance"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert (
        inst.library[0] == "http://example.org/fhir/Library/opioidcds-recommendation-11"
    )
    assert inst.name == "cdc-opioid-11"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert (
        inst.relatedArtifact[0].display
        == "CDC guideline for prescribing opioids for chronic pain"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[0].url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert inst.relatedArtifact[1].display == "MME Conversion Tables"
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[1].url == (
        "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily" "_dose-a.pdf"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CDC Opioid Prescribing Guideline Recommendation #11"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "eca-rule"
    assert inst.type.coding[0].display == "ECA Rule"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/plan-definition-type"
    )
    assert inst.url == (
        "http://hl7.org/fhir/ig/opioid-" "cds/PlanDefinition/opioidcds-11"
    )
    assert inst.usage == (
        "Clinicians should avoid prescribing opioid pain medication "
        "and benzodiazepines concurrently whenever possible."
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Medication requested (situation)"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].display
        == "Chronic pain (finding)"
    )
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "0.1.0"


def test_plandefinition_1(base_settings):
    """No. 1 tests collection for PlanDefinition.
    Test File: plandefinition-opioidcds-11.json
    """
    filename = base_settings["unittest_data_dir"] / "plandefinition-opioidcds-11.json"
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_1(inst2)


def impl_plandefinition_2(inst):
    assert inst.action[0].action[0].description == "Will precribe immediate release"
    assert inst.action[0].action[1].description == (
        "Risk of overdose carefully considered and outweighed by "
        "benefit; snooze 3 mo"
    )
    assert inst.action[0].action[2].description == "N/A - see comment; snooze 3 mo"
    assert inst.action[0].condition[0].expression.description == (
        "Check whether the opioid prescription for the existing "
        "patient is extended-release without any opioids-with-abuse-"
        "potential prescribed in the past 90 days."
    )
    assert inst.action[0].condition[0].expression.expression == "Inclusion Criteria"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].description == (
        "Checking if the trigger prescription meets the inclusion "
        "criteria for recommendation #4 workflow."
    )
    assert inst.action[0].documentation[0].document.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/cqf-" "strengthOfRecommendation"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "strong"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Strong"
    )
    assert inst.action[0].documentation[0].document.extension[
        0
    ].valueCodeableConcept.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/recommendation-" "strength"
    )
    assert inst.action[0].documentation[0].document.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/cqf-" "qualityOfEvidence"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .code
        == "low"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .display
        == "Low quality"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .system
        == "http://terminology.hl7.org/CodeSystem/evidence-quality"
    )
    assert inst.action[0].documentation[0].type == "documentation"
    assert inst.action[0].dynamicValue[0].expression.expression == "Get Summary"
    assert inst.action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[0].path == "action.title"
    assert inst.action[0].dynamicValue[1].expression.expression == "Get Detail"
    assert inst.action[0].dynamicValue[1].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[1].path == "action.description"
    assert inst.action[0].dynamicValue[2].expression.expression == "Get Indicator"
    assert inst.action[0].dynamicValue[2].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[2].path == "activity.extension"
    assert inst.action[0].groupingBehavior == "visual-group"
    assert inst.action[0].selectionBehavior == "exactly-one"
    assert inst.action[0].title == "Extended-release opioid prescription triggered."
    assert inst.action[0].trigger[0].name == "medication-prescribe"
    assert inst.action[0].trigger[0].type == "named-event"
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.copyright == "© CDC 2016+."
    assert inst.date == fhirtypes.DateTime.validate("2018-03-19")
    assert inst.description == (
        "When starting opioid therapy for chronic pain, clinicians "
        "should prescribe immediate-release opioids instead of "
        "extended-release/long-acting (ER/LA) opioids."
    )
    assert inst.id == "opioidcds-04"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "cdc-opioid-guidance"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert (
        inst.library[0] == "http://example.org/fhir/Library/opioidcds-recommendation-04"
    )
    assert inst.name == "cdc-opioid-04"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert (
        inst.relatedArtifact[0].display
        == "CDC guideline for prescribing opioids for chronic pain"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[0].url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert inst.relatedArtifact[1].display == "MME Conversion Tables"
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[1].url == (
        "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily" "_dose-a.pdf"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CDC Opioid Prescribing Guideline Recommendation #4"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "eca-rule"
    assert inst.type.coding[0].display == "ECA Rule"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/plan-definition-type"
    )
    assert inst.url == (
        "http://hl7.org/fhir/ig/opioid-" "cds/PlanDefinition/opioidcds-04"
    )
    assert inst.usage == (
        "Providers should use caution when prescribing extended-"
        "release/long-acting (ER/LA) opioids as they carry a higher "
        "risk and negligible benefit compared to immediate-release "
        "opioids."
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Medication requested (situation)"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].display
        == "Chronic pain (finding)"
    )
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "0.1.0"


def test_plandefinition_2(base_settings):
    """No. 2 tests collection for PlanDefinition.
    Test File: plandefinition-opioidcds-04.json
    """
    filename = base_settings["unittest_data_dir"] / "plandefinition-opioidcds-04.json"
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_2(inst2)


def impl_plandefinition_3(inst):
    assert inst.action[0].action[0].description == "Will reduce dosage"
    assert inst.action[0].action[1].description == (
        "Risk of overdose carefully considered and outweighed by "
        "benefit; snooze 3 mo"
    )
    assert inst.action[0].action[2].description == "Acute pain; snooze 1 mo"
    assert inst.action[0].action[3].description == (
        "N/A - see comment (will be reviewed by medical director); " "snooze 3 mo"
    )
    assert inst.action[0].condition[0].expression.description == "Is total MME >= 50?"
    assert inst.action[0].condition[0].expression.expression == "Is MME 50 Or More?"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].description == (
        "Total morphine milligram equivalent (MME) exceeds "
        "recommended amount. Taper to less than 50."
    )
    assert inst.action[0].documentation[0].document.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/cqf-" "strengthOfRecommendation"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "strong"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Strong"
    )
    assert inst.action[0].documentation[0].document.extension[
        0
    ].valueCodeableConcept.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/recommendation-" "strength"
    )
    assert inst.action[0].documentation[0].document.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/cqf-" "qualityOfEvidence"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .code
        == "low"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .display
        == "Low quality"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .system
        == "http://terminology.hl7.org/CodeSystem/evidence-quality"
    )
    assert inst.action[0].documentation[0].type == "documentation"
    assert inst.action[0].dynamicValue[0].expression.expression == "getSummary"
    assert inst.action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[0].path == "action.title"
    assert inst.action[0].dynamicValue[1].expression.expression == "getDetail"
    assert inst.action[0].dynamicValue[1].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[1].path == "action.description"
    assert inst.action[0].dynamicValue[2].expression.expression == "getIndicator"
    assert inst.action[0].dynamicValue[2].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[2].path == "activity.extension"
    assert inst.action[0].groupingBehavior == "visual-group"
    assert inst.action[0].selectionBehavior == "exactly-one"
    assert inst.action[0].title == "High risk for opioid overdose."
    assert inst.action[0].trigger[0].name == "medication-prescribe"
    assert inst.action[0].trigger[0].type == "named-event"
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.copyright == "© CDC 2016+."
    assert inst.date == fhirtypes.DateTime.validate("2017-04-23")
    assert inst.description == (
        "When opioids are started, providers should prescribe the "
        "lowest effective dosage."
    )
    assert inst.id == "opioidcds-05"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "cdc-opioid-guidance"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert (
        inst.library[0] == "http://example.org/fhir/Library/opioidcds-recommendation-05"
    )
    assert inst.name == "cdc-opioid-05"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert (
        inst.relatedArtifact[0].display
        == "CDC guideline for prescribing opioids for chronic pain"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[0].url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert inst.relatedArtifact[1].display == "MME Conversion Tables"
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[1].url == (
        "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily" "_dose-a.pdf"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CDC Opioid Prescribing Guideline Recommendation #5"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "eca-rule"
    assert inst.type.coding[0].display == "ECA Rule"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/plan-definition-type"
    )
    assert inst.url == (
        "http://hl7.org/fhir/ig/opioid-" "cds/PlanDefinition/opioidcds-05"
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Medication requested (situation)"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].display
        == "Chronic pain (finding)"
    )
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "0.1.0"


def test_plandefinition_3(base_settings):
    """No. 3 tests collection for PlanDefinition.
    Test File: plandefinition-opioidcds-05.json
    """
    filename = base_settings["unittest_data_dir"] / "plandefinition-opioidcds-05.json"
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_3(inst2)


def impl_plandefinition_4(inst):
    assert (
        inst.action[0].action[0].definitionCanonical
        == "#activitydefinition-medicationrequest-1"
    )
    assert inst.action[0].action[0].id == "medication-action-1"
    assert inst.action[0].action[0].title == "Administer Medication 1"
    assert (
        inst.action[0].action[1].definitionCanonical
        == "#activitydefinition-medicationrequest-2"
    )
    assert inst.action[0].action[1].id == "medication-action-2"
    assert inst.action[0].action[1].relatedAction[0].actionId == "medication-action-1"
    assert inst.action[0].action[1].relatedAction[0].offsetDuration.unit == "h"
    assert float(
        inst.action[0].action[1].relatedAction[0].offsetDuration.value
    ) == float(1)
    assert inst.action[0].action[1].relatedAction[0].relationship == "after-end"
    assert inst.action[0].action[1].title == "Administer Medication 2"
    assert inst.action[0].groupingBehavior == "logical-group"
    assert inst.action[0].selectionBehavior == "all"
    assert inst.contained[0].id == "activitydefinition-medicationrequest-1"
    assert inst.contained[1].id == "activitydefinition-medicationrequest-2"
    assert inst.id == "options-example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "This example illustrates relationships between actions."


def test_plandefinition_4(base_settings):
    """No. 4 tests collection for PlanDefinition.
    Test File: plandefinition-options-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-options-example.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_4(inst2)


def impl_plandefinition_5(inst):
    assert (
        inst.action[0].action[0].condition[0].expression.expression
        == "Should Administer Zika Virus Exposure Assessment"
    )
    assert inst.action[0].action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].action[0].condition[0].kind == "applicability"
    assert inst.action[0].action[0].definitionCanonical == (
        "http://example.org/fhir/ActivityDefinition/administer-zika-"
        "virus-exposure-assessment"
    )
    assert (
        inst.action[0].action[1].condition[0].expression.expression
        == "Should Order Serum + Urine rRT-PCR Test"
    )
    assert inst.action[0].action[1].condition[0].expression.language == "text/cql"
    assert inst.action[0].action[1].condition[0].kind == "applicability"
    assert inst.action[0].action[1].definitionCanonical == (
        "http://example.org/fhir/ActivityDefinition/order-serum-" "urine-rrt-pcr-test"
    )
    assert (
        inst.action[0].action[2].condition[0].expression.expression
        == "Should Order Serum Zika Virus IgM + Dengue Virus IgM"
    )
    assert inst.action[0].action[2].condition[0].expression.language == "text/cql"
    assert inst.action[0].action[2].condition[0].kind == "applicability"
    assert inst.action[0].action[2].definitionCanonical == (
        "http://example.org/fhir/ActivityDefinition/order-serum-zika-"
        "dengue-virus-igm"
    )
    assert (
        inst.action[0].action[3].condition[0].expression.expression
        == "Should Consider IgM Antibody Testing"
    )
    assert inst.action[0].action[3].condition[0].expression.language == "text/cql"
    assert inst.action[0].action[3].condition[0].kind == "applicability"
    assert inst.action[0].action[3].definitionCanonical == (
        "http://example.org/fhir/ActivityDefinition/consider-igm-" "antibody-testing"
    )
    assert inst.action[0].action[4].action[0].definitionCanonical == (
        "http://example.org/fhir/ActivityDefinition/provide-mosquito-"
        "prevention-advice"
    )
    assert inst.action[0].action[4].action[1].definitionCanonical == (
        "http://example.org/fhir/ActivityDefinition/provide-" "contraception-advice"
    )
    assert (
        inst.action[0].action[4].condition[0].expression.expression
        == "Should Provide Mosquito Prevention and Contraception Advice"
    )
    assert inst.action[0].action[4].condition[0].expression.language == "text/cql"
    assert inst.action[0].action[4].condition[0].kind == "applicability"
    assert inst.action[0].condition[0].expression.expression == "Is Patient Pregnant"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == "Zika Virus Assessment"
    assert inst.action[0].trigger[0].name == "patient-view"
    assert inst.action[0].trigger[0].type == "named-event"
    assert inst.date == fhirtypes.DateTime.validate("2017-01-12")
    assert inst.description == (
        "Zika Virus Management intervention describing the CDC "
        "Guidelines for Zika Virus Reporting and Management."
    )
    assert inst.id == "zika-virus-intervention"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "zika-virus-intervention"
    assert inst.library[0] == (
        "http://example.org/fhir/Library/zika-virus-intervention-" "logic"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.relatedArtifact[0].url == (
        "https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm" "6539e1_w"
    )
    assert inst.relatedArtifact[1].resource == (
        "http://example.org/fhir/PlanDefinition/zika-virus-" "intervention-initial"
    )
    assert inst.relatedArtifact[1].type == "predecessor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Example Zika Virus Intervention"
    assert inst.topic[0].text == "Zika Virus Management"
    assert inst.url == "http://example.org/PlanDefinition/zika-virus-intervention"
    assert inst.useContext[0].code.code == "age"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueRange.low.unit == "a"
    assert float(inst.useContext[0].valueRange.low.value) == float(12)
    assert inst.useContext[1].code.code == "user"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "309343006"
    assert inst.useContext[1].valueCodeableConcept.coding[0].display == "Physician"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "2.0.0"


def test_plandefinition_5(base_settings):
    """No. 5 tests collection for PlanDefinition.
    Test File: plandefinition-zika-virus-intervention.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-zika-virus-intervention.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_5(inst2)


def impl_plandefinition_6(inst):
    assert (
        inst.action[0].action[0].dynamicValue[0].expression.expression
        == "Communication Request to Provider"
    )
    assert inst.action[0].action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[0].dynamicValue[0].path == "/"
    assert inst.action[0].action[0].textEquivalent == (
        "A Breastfeeding Readiness Assessment is recommended, please "
        "authorize or reject the order."
    )
    assert inst.action[0].action[0].title == "Notify the provider to sign the order."
    assert inst.action[0].action[0].type.coding[0].code == "create"
    assert (
        inst.action[0].condition[0].expression.expression
        == "Should Notify Provider to Sign Assessment Order"
    )
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == (
        "Mother should be administered a breastfeeding readiness " "assessment."
    )
    assert inst.action[0].trigger[0].name == "Admission"
    assert inst.action[0].trigger[0].type == "named-event"
    assert inst.action[0].trigger[1].name == "Birth"
    assert inst.action[0].trigger[1].type == "named-event"
    assert inst.action[0].trigger[2].name == "Infant Transfer to Recovery"
    assert inst.action[0].trigger[2].type == "named-event"
    assert inst.action[0].trigger[3].name == "Transfer to Post-Partum"
    assert inst.action[0].trigger[3].type == "named-event"
    assert inst.date == fhirtypes.DateTime.validate("2015-03-08")
    assert inst.id == "exclusive-breastfeeding-intervention-02"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-intervention-02"
    assert inst.library[0] == (
        "http://example.org/fhir/Library/library-exclusive-" "breastfeeding-cds-logic"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.relatedArtifact[0].resource == (
        "http://example.org/fhir/Measure/measure-exclusive-" "breastfeeding"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Intervention-02"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.version == "1.0.0"


def test_plandefinition_6(base_settings):
    """No. 6 tests collection for PlanDefinition.
    Test File: plandefinition-exclusive-breastfeeding-intervention-02.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-exclusive-breastfeeding-intervention-02.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_6(inst2)


def impl_plandefinition_7(inst):
    assert inst.action[0].action[0].description == "Will offer Naloxone instead"
    assert inst.action[0].action[1].description == (
        "Risk of overdose carefully considered and outweighed by "
        "benefit; snooze 3 mo"
    )
    assert inst.action[0].action[2].description == "N/A - see comment; snooze 3 mo"
    assert inst.action[0].condition[0].expression.expression == "Inclusion Criteria"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].description == (
        "Checking if the trigger prescription meets the inclusion "
        "criteria for recommendation #8 workflow."
    )
    assert inst.action[0].documentation[0].document.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/cqf-" "strengthOfRecommendation"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "strong"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Strong"
    )
    assert inst.action[0].documentation[0].document.extension[
        0
    ].valueCodeableConcept.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/recommendation-" "strength"
    )
    assert inst.action[0].documentation[0].document.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/cqf-" "qualityOfEvidence"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .code
        == "low"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .display
        == "Low quality"
    )
    assert (
        inst.action[0]
        .documentation[0]
        .document.extension[1]
        .valueCodeableConcept.coding[0]
        .system
        == "http://terminology.hl7.org/CodeSystem/evidence-quality"
    )
    assert inst.action[0].documentation[0].type == "documentation"
    assert inst.action[0].dynamicValue[0].expression.expression == "Get Detail"
    assert inst.action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[0].path == "action.description"
    assert inst.action[0].dynamicValue[1].expression.expression == "Get Summary"
    assert inst.action[0].dynamicValue[1].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[1].path == "action.title"
    assert inst.action[0].dynamicValue[2].expression.expression == "Get Indicator"
    assert inst.action[0].dynamicValue[2].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[2].path == "action.extension"
    assert inst.action[0].groupingBehavior == "visual-group"
    assert inst.action[0].selectionBehavior == "exactly-one"
    assert inst.action[0].title == (
        "Existing patient exhibits risk factors for opioid-related " "harms."
    )
    assert inst.action[0].trigger[0].name == "medication-prescribe"
    assert inst.action[0].trigger[0].type == "named-event"
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.copyright == "© CDC 2016+."
    assert inst.date == fhirtypes.DateTime.validate("2018-03-19")
    assert inst.id == "opioidcds-08"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "cdc-opioid-guidance"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert (
        inst.library[0] == "http://example.org/fhir/Library/opioidcds-recommendation-08"
    )
    assert inst.name == "cdc-opioid-08"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert (
        inst.relatedArtifact[0].display
        == "CDC guideline for prescribing opioids for chronic pain"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[0].url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert inst.relatedArtifact[1].display == "MME Conversion Tables"
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[1].url == (
        "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily" "_dose-a.pdf"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CDC Opioid Prescribing Guideline Recommendation #8"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "eca-rule"
    assert inst.type.coding[0].display == "ECA Rule"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/plan-definition-type"
    )
    assert inst.url == (
        "http://hl7.org/fhir/ig/opioid-" "cds/PlanDefinition/opioidcds-08"
    )
    assert inst.usage == (
        "Before starting and periodically during continuation of "
        "opioid therapy, clinicians should evaluate risk factors for "
        "opioid-related harms."
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Medication requested (situation)"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].display
        == "Chronic pain (finding)"
    )
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "0.1.0"


def test_plandefinition_7(base_settings):
    """No. 7 tests collection for PlanDefinition.
    Test File: plandefinition-opioidcds-08.json
    """
    filename = base_settings["unittest_data_dir"] / "plandefinition-opioidcds-08.json"
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_7(inst2)


def impl_plandefinition_8(inst):
    assert inst.action[0].condition[0].expression.expression == "NoScreening"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert (
        inst.action[0].dynamicValue[0].expression.expression
        == "ChlamydiaScreeningRequest"
    )
    assert inst.action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[0].path == "$this"
    assert inst.action[0].title == (
        "Patient has not had chlamydia screening within the " "recommended timeframe..."
    )
    assert inst.date == fhirtypes.DateTime.validate("2015-07-22")
    assert inst.description == "Chlamydia Screening CDS Example Using Common"
    assert inst.id == "chlamydia-screening-intervention"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "ChlamydiaScreening_CDS_UsingCommon"
    assert inst.library[0] == "http://example.org/fhir/Library/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Chalmydia Screening CDS Example Using Common"
    assert inst.topic[0].text == "Chlamydia Screening"
    assert inst.version == "2.0.0"


def test_plandefinition_8(base_settings):
    """No. 8 tests collection for PlanDefinition.
    Test File: plandefinition-chlamydia-screening-intervention.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-chlamydia-screening-intervention.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_8(inst2)


def impl_plandefinition_9(inst):
    assert (
        inst.action[0].action[0].dynamicValue[0].expression.expression
        == "Communication Request to Charge Nurse"
    )
    assert inst.action[0].action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[0].dynamicValue[0].path == "/"
    assert inst.action[0].action[0].textEquivalent == (
        "A Breastfeeding Readiness Assessment is recommended, please "
        "administer the assessment."
    )
    assert (
        inst.action[0].action[0].title
        == "Notify the charge nurse to perform the assessment."
    )
    assert inst.action[0].action[0].type.coding[0].code == "create"
    assert (
        inst.action[0].action[1].dynamicValue[0].expression.expression
        == "Communication Request to Bedside Nurse"
    )
    assert inst.action[0].action[1].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[1].dynamicValue[0].path == "/"
    assert inst.action[0].action[1].textEquivalent == (
        "A Breastfeeding Readiness Assessment is recommended, please "
        "administer the assessment."
    )
    assert (
        inst.action[0].action[1].title
        == "Notify the bedside nurse to perform the assessment."
    )
    assert inst.action[0].action[1].type.coding[0].code == "create"
    assert (
        inst.action[0].condition[0].expression.expression
        == "Should Notify Nurse to Perform Assessment"
    )
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == (
        "Mother should be administered a breastfeeding readiness " "assessment."
    )
    assert inst.action[0].trigger[0].name == "Admission"
    assert inst.action[0].trigger[0].type == "named-event"
    assert inst.action[0].trigger[1].name == "Birth"
    assert inst.action[0].trigger[1].type == "named-event"
    assert inst.action[0].trigger[2].name == "Infant Transfer to Recovery"
    assert inst.action[0].trigger[2].type == "named-event"
    assert inst.action[0].trigger[3].name == "Transfer to Post-Partum"
    assert inst.action[0].trigger[3].type == "named-event"
    assert inst.date == fhirtypes.DateTime.validate("2015-03-08")
    assert inst.id == "exclusive-breastfeeding-intervention-03"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-intervention-03"
    assert inst.library[0] == (
        "http://example.org/fhir/Library/library-exclusive-" "breastfeeding-cds-logic"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.relatedArtifact[0].resource == (
        "http://example.org/fhir/Measure/measure-exclusive-" "breastfeeding"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Intervention-03"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.version == "1.0.0"


def test_plandefinition_9(base_settings):
    """No. 9 tests collection for PlanDefinition.
    Test File: plandefinition-exclusive-breastfeeding-intervention-03.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-exclusive-breastfeeding-intervention-03.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_9(inst2)


def impl_plandefinition_10(inst):
    assert (
        inst.action[0].action[0].dynamicValue[0].expression.expression
        == "Create Breastfeeding Risk Assessment"
    )
    assert inst.action[0].action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[0].dynamicValue[0].path == "/"
    assert (
        inst.action[0].action[0].textEquivalent
        == "Administer a breastfeeding readiness assessment."
    )
    assert (
        inst.action[0].action[0].title
        == "Create the breastfeeding readiness assessment order."
    )
    assert inst.action[0].action[0].type.coding[0].code == "create"
    assert (
        inst.action[0].action[1].dynamicValue[0].expression.expression
        == "Communication Request to Provider"
    )
    assert inst.action[0].action[1].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[1].dynamicValue[0].path == "/"
    assert inst.action[0].action[1].textEquivalent == (
        "A Breastfeeding Readiness Assessment is recommended, please "
        "authorize or reject the order."
    )
    assert inst.action[0].action[1].title == "Notify the provider to sign the order."
    assert inst.action[0].action[1].type.coding[0].code == "create"
    assert (
        inst.action[0].condition[0].expression.expression
        == "Should Create Assessment Order"
    )
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == (
        "Mother should be administered a breastfeeding readiness " "assessment."
    )
    assert inst.action[0].trigger[0].name == "Admission"
    assert inst.action[0].trigger[0].type == "named-event"
    assert inst.action[0].trigger[1].name == "Birth"
    assert inst.action[0].trigger[1].type == "named-event"
    assert inst.action[0].trigger[2].name == "Infant Transfer to Recovery"
    assert inst.action[0].trigger[2].type == "named-event"
    assert inst.action[0].trigger[3].name == "Transfer to Post-Partum"
    assert inst.action[0].trigger[3].type == "named-event"
    assert inst.date == fhirtypes.DateTime.validate("2015-03-08")
    assert inst.id == "exclusive-breastfeeding-intervention-01"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-intervention-01"
    assert inst.library[0] == (
        "http://example.org/fhir/Library/library-exclusive-" "breastfeeding-cds-logic"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.relatedArtifact[0].resource == (
        "http://example.org/fhir/Measure/measure-exclusive-" "breastfeeding"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Intervention-01"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.version == "1.0.0"


def test_plandefinition_10(base_settings):
    """No. 10 tests collection for PlanDefinition.
    Test File: plandefinition-exclusive-breastfeeding-intervention-01.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-exclusive-breastfeeding-intervention-01.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_10(inst2)
