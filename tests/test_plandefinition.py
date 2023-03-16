# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import plandefinition


def impl_plandefinition_1(inst):
    assert inst.action[0].action[0].action[0].action[0].action[0].definitionCanonical == "#1111"
    assert inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[0].url == "day"
    assert inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[0].valueInteger == 1
    assert inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[1].url == "day"
    assert inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[1].valueInteger == 8
    assert inst.action[0].action[0].action[0].action[0].action[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"
    assert inst.action[0].action[0].action[0].action[0].action[0].id == "action-1"
    assert inst.action[0].action[0].action[0].action[0].action[0].textEquivalent == "Gemcitabine 1250 mg/m² IV over 30 minutes on days 1 and 8"
    assert inst.action[0].action[0].action[0].action[0].action[1].definitionCanonical == "#2222"
    assert inst.action[0].action[0].action[0].action[0].action[1].extension[0].extension[0].url == "day"
    assert inst.action[0].action[0].action[0].action[0].action[1].extension[0].extension[0].valueInteger == 1
    assert inst.action[0].action[0].action[0].action[0].action[1].extension[0].url == "http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"
    assert inst.action[0].action[0].action[0].action[0].action[1].id == "action-2"
    assert inst.action[0].action[0].action[0].action[0].action[1].relatedAction[0].relationship == "concurrent-with-start"
    assert inst.action[0].action[0].action[0].action[0].action[1].relatedAction[0].targetId == "action-1"
    assert inst.action[0].action[0].action[0].action[0].action[1].textEquivalent == "CARBOplatin AUC 5 IV over 30 minutes on Day 1"
    assert inst.action[0].action[0].action[0].action[0].id == "cycle-definition-1"
    assert inst.action[0].action[0].action[0].action[0].textEquivalent == "21-day cycle for 6 cycles"
    assert inst.action[0].action[0].action[0].action[0].timingTiming.repeat.count == 6
    assert float(inst.action[0].action[0].action[0].action[0].timingTiming.repeat.duration) == float(21)
    assert inst.action[0].action[0].action[0].action[0].timingTiming.repeat.durationUnit == "d"
    assert inst.action[0].action[0].action[0].groupingBehavior == "sentence-group"
    assert inst.action[0].action[0].action[0].selectionBehavior == "exactly-one"
    assert inst.action[0].action[0].selectionBehavior == "all"
    assert inst.action[0].selectionBehavior == "exactly-one"
    assert inst.approvalDate == fhirtypes.Date.validate("2016-07-27")
    assert inst.author[0].name == "Lee Surprenant"
    assert inst.contained[0].id == "1111"
    assert inst.contained[1].id == "2222"
    assert inst.copyright == "All rights reserved."
    assert inst.description == "Gemcitabine/CARBOplatin"
    assert inst.experimental is True
    assert inst.id == "KDN5"
    assert inst.identifier[0].system == "http://example.org/ordertemplates"
    assert inst.identifier[0].value == "KDN5"
    assert inst.lastReviewDate == fhirtypes.Date.validate("2016-07-27")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "GemcitabineCARBOplatin"
    assert inst.publisher == "National Comprehensive Cancer Network, Inc."
    assert inst.relatedArtifact[0].display == "NCCN Guidelines for Kidney Cancer. V.2.2016"
    assert inst.relatedArtifact[0].document.url == (
    "http://www.example.org/professionals/physician_gls/PDF/kidne"
    "y.pdf"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.relatedArtifact[1].citation == "Oudard S, et al. J Urol. 2007;177(5):1698-702"
    assert inst.relatedArtifact[1].document.url == "http://www.ncbi.nlm.nih.gov/pubmed/17437788"
    assert inst.relatedArtifact[1].type == "citation"
    assert inst.status == "draft"
    assert inst.text.status == "additional"
    assert inst.title == "Gemcitabine/CARBOplatin"
    assert inst.type.text == "Chemotherapy Order Template"
    assert inst.useContext[0].code.code == "treamentSetting-or-diseaseStatus"
    assert inst.useContext[0].code.system == "http://example.org/fhir/CodeSystem/indications"
    assert inst.useContext[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    assert inst.useContext[0].extension[0].valueString == "A"
    assert inst.useContext[0].valueCodeableConcept.text == "Metastatic"
    assert inst.useContext[1].code.code == "disease-or-histology"
    assert inst.useContext[1].code.system == "http://example.org/fhir/CodeSystem/indications"
    assert inst.useContext[1].extension[0].url == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    assert inst.useContext[1].extension[0].valueString == "A"
    assert inst.useContext[1].valueCodeableConcept.text == "Collecting Duct/Medullary Subtypes"
    assert inst.useContext[2].code.code == "focus"
    assert inst.useContext[2].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[2].extension[0].url == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    assert inst.useContext[2].extension[0].valueString == "A"
    assert inst.useContext[2].valueCodeableConcept.text == "Kidney Cancer"
    assert inst.useContext[3].code.code == "treatmentSetting-or-diseaseStatus"
    assert inst.useContext[3].code.system == "http://example.org/fhir/CodeSystem/indications"
    assert inst.useContext[3].extension[0].url == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    assert inst.useContext[3].extension[0].valueString == "B"
    assert inst.useContext[3].valueCodeableConcept.text == "Relapsed"
    assert inst.useContext[4].code.code == "disease-or-histology"
    assert inst.useContext[4].code.system == "http://example.org/fhir/CodeSystem/indications"
    assert inst.useContext[4].extension[0].url == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    assert inst.useContext[4].extension[0].valueString == "B"
    assert inst.useContext[4].valueCodeableConcept.text == "Collecting Duct/Medullary Subtypes"
    assert inst.useContext[5].code.code == "focus"
    assert inst.useContext[5].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[5].extension[0].url == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    assert inst.useContext[5].extension[0].valueString == "B"
    assert inst.useContext[5].valueCodeableConcept.text == (
    "Kidney Cancer – Collecting Duct/Medullary Subtypes - "
    "Metastatic"
    )
    assert inst.version == "1"


def test_plandefinition_1(base_settings):
    """No. 1 tests collection for PlanDefinition.
    Test File: plandefinition-example-kdn5-simplified.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-example-kdn5-simplified.json"
    )
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
    assert inst.action[0].action[0].description == (
    "Will schedule assessment of risk for opioid use for the "
    "patient"
    )
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
    "criteria for recommendation #7 workflow."
    )
    assert inst.action[0].documentation[0].document.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "strengthOfRecommendation"
    )
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].code == "strong"
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].display == "Strong"
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/recommendation-"
    "strength"
    )
    assert inst.action[0].documentation[0].document.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "qualityOfEvidence"
    )
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].code == "low"
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].display == "Low quality"
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/evidence-quality"
    assert inst.action[0].documentation[0].type == "documentation"
    assert inst.action[0].dynamicValue[0].expression.expression == "Get Summary"
    assert inst.action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[0].path == "action.title"
    assert inst.action[0].dynamicValue[1].expression.expression == "Get Detail"
    assert inst.action[0].dynamicValue[1].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[1].path == "action.description"
    assert inst.action[0].dynamicValue[2].expression.expression == "Get Indicator"
    assert inst.action[0].dynamicValue[2].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[2].path == "action.extension"
    assert inst.action[0].groupingBehavior == "visual-group"
    assert inst.action[0].selectionBehavior == "exactly-one"
    assert inst.action[0].title == (
    "Existing patient should be evaluated for risk of continued "
    "opioid therapy."
    )
    assert inst.action[0].trigger[0].name == "medication-prescribe"
    assert inst.action[0].trigger[0].type == "named-event"
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.copyright == "© CDC 2016+."
    assert inst.date == fhirtypes.DateTime.validate("2018-03-19")
    assert inst.id == "opioidcds-07"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.11.6"
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "cdc-opioid-guidance"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.library[0] == "http://example.org/fhir/Library/opioidcds-recommendation-07"
    assert inst.name == "Cdcopioid07"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.relatedArtifact[0].display == "CDC guideline for prescribing opioids for chronic pain"
    assert inst.relatedArtifact[0].document.url == (
    "https://guidelines.gov/summaries/summary/50153/cdc-"
    "guideline-for-prescribing-opioids-for-chronic-pain---united-"
    "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].display == "MME Conversion Tables"
    assert inst.relatedArtifact[1].document.url == (
    "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily"
    "_dose-a.pdf"
    )
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CDC Opioid Prescribing Guideline Recommendation #7"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "eca-rule"
    assert inst.type.coding[0].display == "ECA Rule"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/plan-definition-type"
    assert inst.url == (
    "http://hl7.org/fhir/ig/opioid-"
    "cds/PlanDefinition/opioidcds-07"
    )
    assert inst.usage == (
    "If benefits do not outweigh harms of continued opioid "
    "therapy, clinicians should optimize other therapies and work"
    " with patients to taper opioids to lower dosages or to taper"
    " and discontinue opioids."
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert inst.useContext[0].valueCodeableConcept.coding[0].display == "Medication requested (situation)"
    assert inst.useContext[0].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert inst.useContext[1].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert inst.useContext[1].valueCodeableConcept.coding[0].display == "Chronic pain (finding)"
    assert inst.useContext[1].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.version == "0.1.0"


def test_plandefinition_2(base_settings):
    """No. 2 tests collection for PlanDefinition.
    Test File: plandefinition-opioidcds-07.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-opioidcds-07.json"
    )
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
    assert inst.action[0].action[0].dynamicValue[0].expression.expression == "Create Breastfeeding Risk Assessment"
    assert inst.action[0].action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[0].dynamicValue[0].path == "/"
    assert inst.action[0].action[0].textEquivalent == "Administer a breastfeeding readiness assessment."
    assert inst.action[0].action[0].title == "Create the breastfeeding readiness assessment order."
    assert inst.action[0].action[0].type.coding[0].code == "create"
    assert inst.action[0].action[1].dynamicValue[0].expression.expression == "Communication Request to Provider"
    assert inst.action[0].action[1].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[1].dynamicValue[0].path == "/"
    assert inst.action[0].action[1].textEquivalent == (
    "A Breastfeeding Readiness Assessment is recommended, please "
    "authorize or reject the order."
    )
    assert inst.action[0].action[1].title == "Notify the provider to sign the order."
    assert inst.action[0].action[1].type.coding[0].code == "create"
    assert inst.action[0].condition[0].expression.expression == "Should Create Assessment Order"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == (
    "Mother should be administered a breastfeeding readiness "
    "assessment."
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
    "http://example.org/fhir/Library/library-exclusive-"
    "breastfeeding-cds-logic"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "ExclusiveBreastfeedingIntervention01"
    assert inst.relatedArtifact[0].resource == (
    "http://example.org/fhir/Measure/measure-exclusive-"
    "breastfeeding"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Intervention-01"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.version == "1.0.0"


def test_plandefinition_3(base_settings):
    """No. 3 tests collection for PlanDefinition.
    Test File: plandefinition-exclusive-breastfeeding-intervention-01.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-exclusive-breastfeeding-intervention-01.json"
    )
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
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "strengthOfRecommendation"
    )
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].code == "strong"
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].display == "Strong"
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/recommendation-"
    "strength"
    )
    assert inst.action[0].documentation[0].document.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "qualityOfEvidence"
    )
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].code == "low"
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].display == "Low quality"
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/evidence-quality"
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
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.11.4"
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "cdc-opioid-guidance"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.library[0] == "http://example.org/fhir/Library/opioidcds-recommendation-04"
    assert inst.name == "Cdcopioid04"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.relatedArtifact[0].display == "CDC guideline for prescribing opioids for chronic pain"
    assert inst.relatedArtifact[0].document.url == (
    "https://guidelines.gov/summaries/summary/50153/cdc-"
    "guideline-for-prescribing-opioids-for-chronic-pain---united-"
    "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].display == "MME Conversion Tables"
    assert inst.relatedArtifact[1].document.url == (
    "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily"
    "_dose-a.pdf"
    )
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CDC Opioid Prescribing Guideline Recommendation #4"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "eca-rule"
    assert inst.type.coding[0].display == "ECA Rule"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/plan-definition-type"
    assert inst.url == (
    "http://hl7.org/fhir/ig/opioid-"
    "cds/PlanDefinition/opioidcds-04"
    )
    assert inst.usage == (
    "Providers should use caution when prescribing extended-"
    "release/long-acting (ER/LA) opioids as they carry a higher "
    "risk and negligible benefit compared to immediate-release "
    "opioids."
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert inst.useContext[0].valueCodeableConcept.coding[0].display == "Medication requested (situation)"
    assert inst.useContext[0].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert inst.useContext[1].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert inst.useContext[1].valueCodeableConcept.coding[0].display == "Chronic pain (finding)"
    assert inst.useContext[1].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.version == "0.1.0"


def test_plandefinition_4(base_settings):
    """No. 4 tests collection for PlanDefinition.
    Test File: plandefinition-opioidcds-04.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-opioidcds-04.json"
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
    assert inst.action[0].action[0].description == "Will perform urine screening"
    assert inst.action[0].action[1].description == "Not for chronic pain management. Snooze 3 months"
    assert inst.action[0].condition[0].expression.description == "Patient has not had a urine screening in the past 12 months"
    assert inst.action[0].condition[0].expression.expression == "No Screenings in Past Year"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].description == "Patient has not had a urine screening in the past 12 months"
    assert inst.action[0].documentation[0].document.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "strengthOfRecommendation"
    )
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].code == "strong"
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].display == "Strong"
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/recommendation-"
    "strength"
    )
    assert inst.action[0].documentation[0].document.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "qualityOfEvidence"
    )
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].code == "low"
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].display == "Low quality"
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/evidence-quality"
    assert inst.action[0].documentation[0].type == "documentation"
    assert inst.action[0].dynamicValue[0].expression.expression == "Get Indicator"
    assert inst.action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].dynamicValue[0].path == "activity.extension"
    assert inst.action[0].title == "Annual Urine Screening Check"
    assert inst.action[0].trigger[0].name == "medication-prescribe"
    assert inst.action[0].trigger[0].type == "named-event"
    assert inst.action[1].action[0].action[0].description == "Not for chronic pain management. Snooze 3 months"
    assert inst.action[1].action[0].condition[0].expression.description == (
    "Patient has a positive urine screening in the past 12 months"
    " for opioid(s), which is not prescribed"
    )
    assert inst.action[1].action[0].condition[0].expression.expression == "Has Unprescribed Opioids?"
    assert inst.action[1].action[0].condition[0].expression.language == "text/cql"
    assert inst.action[1].action[0].condition[0].kind == "applicability"
    assert inst.action[1].action[0].description == (
    "Patient has a positive urine screening in the past 12 months"
    " for opioid(s), which is not prescribed"
    )
    assert inst.action[1].action[0].documentation[0].document.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "strengthOfRecommendation"
    )
    assert inst.action[1].action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].code == "strong"
    assert inst.action[1].action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].display == "Strong"
    assert inst.action[1].action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/recommendation-"
    "strength"
    )
    assert inst.action[1].action[0].documentation[0].document.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "qualityOfEvidence"
    )
    assert inst.action[1].action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].code == "low"
    assert inst.action[1].action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].display == "Low quality"
    assert inst.action[1].action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/evidence-quality"
    assert inst.action[1].action[0].documentation[0].type == "documentation"
    assert inst.action[1].action[0].dynamicValue[0].expression.expression == "Get Indicator"
    assert inst.action[1].action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[1].action[0].dynamicValue[0].path == "activity.extension"
    assert inst.action[1].action[0].dynamicValue[1].expression.expression == "Inconsistent Unprescribed Opioids"
    assert inst.action[1].action[0].dynamicValue[1].expression.language == "text/cql"
    assert inst.action[1].action[0].dynamicValue[1].path == "action.description"
    assert inst.action[1].action[0].title == "Unprescribed Opioids Found In Urine Screening"
    assert inst.action[1].action[1].condition[0].expression.description == (
    "Patient has a positive urine screening in the past 12 "
    "months, which does not include prescribed opioids"
    )
    assert inst.action[1].action[1].condition[0].expression.expression == "Has Missing Opioids?"
    assert inst.action[1].action[1].condition[0].expression.language == "text/cql"
    assert inst.action[1].action[1].condition[0].kind == "applicability"
    assert inst.action[1].action[1].description == (
    "Patient has a positive urine screening in the past 12 "
    "months, which does not include prescribed opioids"
    )
    assert inst.action[1].action[1].documentation[0].document.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "strengthOfRecommendation"
    )
    assert inst.action[1].action[1].documentation[0].document.extension[0].valueCodeableConcept.coding[0].code == "strong"
    assert inst.action[1].action[1].documentation[0].document.extension[0].valueCodeableConcept.coding[0].display == "Strong"
    assert inst.action[1].action[1].documentation[0].document.extension[0].valueCodeableConcept.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/recommendation-"
    "strength"
    )
    assert inst.action[1].action[1].documentation[0].document.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "qualityOfEvidence"
    )
    assert inst.action[1].action[1].documentation[0].document.extension[1].valueCodeableConcept.coding[0].code == "low"
    assert inst.action[1].action[1].documentation[0].document.extension[1].valueCodeableConcept.coding[0].display == "Low quality"
    assert inst.action[1].action[1].documentation[0].document.extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/evidence-quality"
    assert inst.action[1].action[1].documentation[0].type == "documentation"
    assert inst.action[1].action[1].dynamicValue[0].expression.expression == "Get Indicator"
    assert inst.action[1].action[1].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[1].action[1].dynamicValue[0].path == "activity.extension"
    assert inst.action[1].action[1].dynamicValue[1].expression.expression == "Inconsistent Missing Opioids"
    assert inst.action[1].action[1].dynamicValue[1].expression.language == "text/cql"
    assert inst.action[1].action[1].dynamicValue[1].path == "action.description"
    assert inst.action[1].action[1].title == "Prescribed Opioids Not Found In Urine Screening"
    assert inst.action[1].action[2].action[0].description == "Not for chronic pain management. Snooze 3 months"
    assert inst.action[1].action[2].condition[0].expression.description == (
    "Patient has a positive urine screening in the past 12 months"
    " for illicit drugs"
    )
    assert inst.action[1].action[2].condition[0].expression.expression == "Has Illicit Drugs in Screening?"
    assert inst.action[1].action[2].condition[0].expression.language == "text/cql"
    assert inst.action[1].action[2].condition[0].kind == "applicability"
    assert inst.action[1].action[2].description == (
    "Patient has a positive urine screening in the past 12 months"
    " for illicit drugs"
    )
    assert inst.action[1].action[2].documentation[0].document.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "strengthOfRecommendation"
    )
    assert inst.action[1].action[2].documentation[0].document.extension[0].valueCodeableConcept.coding[0].code == "strong"
    assert inst.action[1].action[2].documentation[0].document.extension[0].valueCodeableConcept.coding[0].display == "Strong"
    assert inst.action[1].action[2].documentation[0].document.extension[0].valueCodeableConcept.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/recommendation-"
    "strength"
    )
    assert inst.action[1].action[2].documentation[0].document.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "qualityOfEvidence"
    )
    assert inst.action[1].action[2].documentation[0].document.extension[1].valueCodeableConcept.coding[0].code == "low"
    assert inst.action[1].action[2].documentation[0].document.extension[1].valueCodeableConcept.coding[0].display == "Low quality"
    assert inst.action[1].action[2].documentation[0].document.extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/evidence-quality"
    assert inst.action[1].action[2].documentation[0].type == "documentation"
    assert inst.action[1].action[2].dynamicValue[0].expression.expression == "Get Indicator"
    assert inst.action[1].action[2].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[1].action[2].dynamicValue[0].path == "activity.extension"
    assert inst.action[1].action[2].dynamicValue[1].expression.expression == "Inconsistent Illicit Drugs"
    assert inst.action[1].action[2].dynamicValue[1].expression.language == "text/cql"
    assert inst.action[1].action[2].dynamicValue[1].path == "action.description"
    assert inst.action[1].action[2].title == "Illicit Drugs Found In Urine Screening"
    assert inst.action[1].condition[0].expression.description == "Patient has a positive urine screening in the past 12 months"
    assert inst.action[1].condition[0].expression.expression == "Has Positive Screening?"
    assert inst.action[1].condition[0].expression.language == "text/cql"
    assert inst.action[1].condition[0].kind == "applicability"
    assert inst.action[1].description == (
    "Patient has a urine screening testing positive for either "
    "unprescribed opioids or illicit drugs in the past 12 months"
    )
    assert inst.action[1].documentation[0].document.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "strengthOfRecommendation"
    )
    assert inst.action[1].documentation[0].document.extension[0].valueCodeableConcept.coding[0].code == "strong"
    assert inst.action[1].documentation[0].document.extension[0].valueCodeableConcept.coding[0].display == "Strong"
    assert inst.action[1].documentation[0].document.extension[0].valueCodeableConcept.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/recommendation-"
    "strength"
    )
    assert inst.action[1].documentation[0].document.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "qualityOfEvidence"
    )
    assert inst.action[1].documentation[0].document.extension[1].valueCodeableConcept.coding[0].code == "low"
    assert inst.action[1].documentation[0].document.extension[1].valueCodeableConcept.coding[0].display == "Low quality"
    assert inst.action[1].documentation[0].document.extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/evidence-quality"
    assert inst.action[1].documentation[0].type == "documentation"
    assert inst.action[1].title == "Positive Urine Screening Check"
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.copyright == "© CDC 2016+."
    assert inst.date == fhirtypes.DateTime.validate("2017-04-23")
    assert inst.id == "opioidcds-10"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.11.3"
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "cdc-opioid-guidance"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.library[0] == "http://example.org/fhir/Library/opioidcds-recommendation-10"
    assert inst.name == "Cdcopioid10"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.relatedArtifact[0].display == "CDC guideline for prescribing opioids for chronic pain"
    assert inst.relatedArtifact[0].document.url == (
    "https://guidelines.gov/summaries/summary/50153/cdc-"
    "guideline-for-prescribing-opioids-for-chronic-pain---united-"
    "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CDC Opioid Prescribing Guideline Recommendation #10"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "eca-rule"
    assert inst.type.coding[0].display == "ECA Rule"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/plan-definition-type"
    assert inst.url == (
    "http://hl7.org/fhir/ig/opioid-"
    "cds/PlanDefinition/opioidcds-10"
    )
    assert inst.usage == (
    "Providers should be aware if patients are taking other "
    "prescription drugs or illicit drugs that might increase "
    "their risk of an overdose."
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert inst.useContext[0].valueCodeableConcept.coding[0].display == "Medication requested (situation)"
    assert inst.useContext[0].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert inst.useContext[1].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert inst.useContext[1].valueCodeableConcept.coding[0].display == "Chronic pain (finding)"
    assert inst.useContext[1].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.version == "0.1.0"


def test_plandefinition_5(base_settings):
    """No. 5 tests collection for PlanDefinition.
    Test File: plandefinition-opioidcds-10.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-opioidcds-10.json"
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
    assert inst.action[0].action[0].dynamicValue[0].expression.expression == "Create Lactation Consult Request"
    assert inst.action[0].action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[0].dynamicValue[0].path == "/"
    assert inst.action[0].action[0].textEquivalent == "Create a lactation consult request"
    assert inst.action[0].action[0].title == "Create a lactation consult request."
    assert inst.action[0].action[0].type.coding[0].code == "create"
    assert inst.action[0].condition[0].expression.expression == "Should Create Lactation Consult"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == (
    "Mother should be referred to a lactation specialist for "
    "consultation."
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
    assert inst.description == (
    "Exclusive breastfeeding intervention intended to improve "
    "outcomes for exclusive breastmilk feeding of newborns by "
    "creating a lactation consult for the mother if appropriate."
    )
    assert inst.id == "exclusive-breastfeeding-intervention-04"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-intervention-04"
    assert inst.library[0] == (
    "http://example.org/fhir/Library/library-exclusive-"
    "breastfeeding-cds-logic"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "ExclusiveBreastfeedingIntervention04"
    assert inst.relatedArtifact[0].resource == (
    "http://example.org/fhir/Measure/measure-exclusive-"
    "breastfeeding"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Intervention-04"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.version == "1.0.0"


def test_plandefinition_6(base_settings):
    """No. 6 tests collection for PlanDefinition.
    Test File: plandefinition-exclusive-breastfeeding-intervention-04.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-exclusive-breastfeeding-intervention-04.json"
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
    assert inst.action[0].action[0].dynamicValue[0].expression.expression == "Communication Request to Provider"
    assert inst.action[0].action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[0].dynamicValue[0].path == "/"
    assert inst.action[0].action[0].textEquivalent == (
    "A Breastfeeding Readiness Assessment is recommended, please "
    "authorize or reject the order."
    )
    assert inst.action[0].action[0].title == "Notify the provider to sign the order."
    assert inst.action[0].action[0].type.coding[0].code == "create"
    assert inst.action[0].condition[0].expression.expression == "Should Notify Provider to Sign Assessment Order"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == (
    "Mother should be administered a breastfeeding readiness "
    "assessment."
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
    "http://example.org/fhir/Library/library-exclusive-"
    "breastfeeding-cds-logic"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "ExclusiveBreastfeedingIntervention02"
    assert inst.relatedArtifact[0].resource == (
    "http://example.org/fhir/Measure/measure-exclusive-"
    "breastfeeding"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Intervention-02"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.version == "1.0.0"


def test_plandefinition_7(base_settings):
    """No. 7 tests collection for PlanDefinition.
    Test File: plandefinition-exclusive-breastfeeding-intervention-02.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-exclusive-breastfeeding-intervention-02.json"
    )
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
    assert inst.action[0].action[0].condition[0].expression.expression == "Should Administer Zika Virus Exposure Assessment"
    assert inst.action[0].action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].action[0].condition[0].kind == "applicability"
    assert inst.action[0].action[0].definitionCanonical == (
    "http://example.org/fhir/ActivityDefinition/administer-zika-"
    "virus-exposure-assessment"
    )
    assert inst.action[0].action[1].condition[0].expression.expression == "Should Order Serum + Urine rRT-PCR Test"
    assert inst.action[0].action[1].condition[0].expression.language == "text/cql"
    assert inst.action[0].action[1].condition[0].kind == "applicability"
    assert inst.action[0].action[1].definitionCanonical == (
    "http://example.org/fhir/ActivityDefinition/order-serum-"
    "urine-rrt-pcr-test"
    )
    assert inst.action[0].action[2].condition[0].expression.expression == "Should Order Serum Zika Virus IgM + Dengue Virus IgM"
    assert inst.action[0].action[2].condition[0].expression.language == "text/cql"
    assert inst.action[0].action[2].condition[0].kind == "applicability"
    assert inst.action[0].action[2].definitionCanonical == (
    "http://example.org/fhir/ActivityDefinition/order-serum-zika-"
    "dengue-virus-igm"
    )
    assert inst.action[0].action[3].condition[0].expression.expression == "Should Consider IgM Antibody Testing"
    assert inst.action[0].action[3].condition[0].expression.language == "text/cql"
    assert inst.action[0].action[3].condition[0].kind == "applicability"
    assert inst.action[0].action[3].definitionCanonical == (
    "http://example.org/fhir/ActivityDefinition/consider-igm-"
    "antibody-testing"
    )
    assert inst.action[0].action[4].action[0].definitionCanonical == (
    "http://example.org/fhir/ActivityDefinition/provide-mosquito-"
    "prevention-advice"
    )
    assert inst.action[0].action[4].action[1].definitionCanonical == (
    "http://example.org/fhir/ActivityDefinition/provide-"
    "contraception-advice"
    )
    assert inst.action[0].action[4].condition[0].expression.expression == "Should Provide Mosquito Prevention and Contraception Advice"
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
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.11.5"
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "zika-virus-intervention"
    assert inst.library[0] == (
    "http://example.org/fhir/Library/zika-virus-intervention-"
    "logic"
    )
    assert inst.name == "ExampleZikaVirusIntervention"
    assert inst.relatedArtifact[0].document.url == (
    "https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm"
    "6539e1_w"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.relatedArtifact[1].resource == (
    "http://example.org/fhir/PlanDefinition/zika-virus-"
    "intervention-initial"
    )
    assert inst.relatedArtifact[1].type == "predecessor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Example Zika Virus Intervention"
    assert inst.topic[0].text == "Zika Virus Management"
    assert inst.url == "http://example.org/PlanDefinition/zika-virus-intervention"
    assert inst.useContext[0].code.code == "age"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueRange.low.unit == "a"
    assert float(inst.useContext[0].valueRange.low.value) == float(12)
    assert inst.useContext[1].code.code == "user"
    assert inst.useContext[1].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "309343006"
    assert inst.useContext[1].valueCodeableConcept.coding[0].display == "Physician"
    assert inst.useContext[1].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.version == "2.0.0"


def test_plandefinition_8(base_settings):
    """No. 8 tests collection for PlanDefinition.
    Test File: plandefinition-zika-virus-intervention.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-zika-virus-intervention.json"
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
    assert inst.action[0].action[0].dynamicValue[0].expression.expression == "Communication Request to Charge Nurse"
    assert inst.action[0].action[0].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[0].dynamicValue[0].path == "/"
    assert inst.action[0].action[0].textEquivalent == (
    "A Breastfeeding Readiness Assessment is recommended, please "
    "administer the assessment."
    )
    assert inst.action[0].action[0].title == "Notify the charge nurse to perform the assessment."
    assert inst.action[0].action[0].type.coding[0].code == "create"
    assert inst.action[0].action[1].dynamicValue[0].expression.expression == "Communication Request to Bedside Nurse"
    assert inst.action[0].action[1].dynamicValue[0].expression.language == "text/cql"
    assert inst.action[0].action[1].dynamicValue[0].path == "/"
    assert inst.action[0].action[1].textEquivalent == (
    "A Breastfeeding Readiness Assessment is recommended, please "
    "administer the assessment."
    )
    assert inst.action[0].action[1].title == "Notify the bedside nurse to perform the assessment."
    assert inst.action[0].action[1].type.coding[0].code == "create"
    assert inst.action[0].condition[0].expression.expression == "Should Notify Nurse to Perform Assessment"
    assert inst.action[0].condition[0].expression.language == "text/cql"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == (
    "Mother should be administered a breastfeeding readiness "
    "assessment."
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
    "http://example.org/fhir/Library/library-exclusive-"
    "breastfeeding-cds-logic"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "ExclusiveBreastfeedingIntervention03"
    assert inst.relatedArtifact[0].resource == (
    "http://example.org/fhir/Measure/measure-exclusive-"
    "breastfeeding"
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
        base_settings["unittest_data_dir"] / "plandefinition-exclusive-breastfeeding-intervention-03.json"
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
    assert inst.action[0].action[0].description == "Will reduce dosage"
    assert inst.action[0].action[1].description == (
    "Risk of overdose carefully considered and outweighed by "
    "benefit; snooze 3 mo"
    )
    assert inst.action[0].action[2].description == "Acute pain; snooze 1 mo"
    assert inst.action[0].action[3].description == (
    "N/A - see comment (will be reviewed by medical director); "
    "snooze 3 mo"
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
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "strengthOfRecommendation"
    )
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].code == "strong"
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].display == "Strong"
    assert inst.action[0].documentation[0].document.extension[0].valueCodeableConcept.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/recommendation-"
    "strength"
    )
    assert inst.action[0].documentation[0].document.extension[1].url == (
    "http://hl7.org/fhir/StructureDefinition/cqf-"
    "qualityOfEvidence"
    )
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].code == "low"
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].display == "Low quality"
    assert inst.action[0].documentation[0].document.extension[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/evidence-quality"
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
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.11.1"
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "cdc-opioid-guidance"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.library[0] == "http://example.org/fhir/Library/opioidcds-recommendation-05"
    assert inst.name == "Cdcopioid05"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.relatedArtifact[0].display == "CDC guideline for prescribing opioids for chronic pain"
    assert inst.relatedArtifact[0].document.url == (
    "https://guidelines.gov/summaries/summary/50153/cdc-"
    "guideline-for-prescribing-opioids-for-chronic-pain---united-"
    "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].display == "MME Conversion Tables"
    assert inst.relatedArtifact[1].document.url == (
    "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily"
    "_dose-a.pdf"
    )
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CDC Opioid Prescribing Guideline Recommendation #5"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "eca-rule"
    assert inst.type.coding[0].display == "ECA Rule"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/plan-definition-type"
    assert inst.url == (
    "http://hl7.org/fhir/ig/opioid-"
    "cds/PlanDefinition/opioidcds-05"
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert inst.useContext[0].valueCodeableConcept.coding[0].display == "Medication requested (situation)"
    assert inst.useContext[0].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert inst.useContext[1].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert inst.useContext[1].valueCodeableConcept.coding[0].display == "Chronic pain (finding)"
    assert inst.useContext[1].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.version == "0.1.0"


def test_plandefinition_10(base_settings):
    """No. 10 tests collection for PlanDefinition.
    Test File: plandefinition-opioidcds-05.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-opioidcds-05.json"
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