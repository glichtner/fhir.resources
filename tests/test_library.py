# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Library
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import library


def impl_library_1(inst):
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/elm+xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.dataRequirement[0].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[0].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/opioids-indicating-end-of-" "life"
    )
    assert inst.dataRequirement[0].type == "MedicationRequest"
    assert inst.dataRequirement[1].codeFilter[0].path == "code"
    assert inst.dataRequirement[1].type == "Procedure"
    assert inst.dataRequirement[2].codeFilter[0].path == "code"
    assert inst.dataRequirement[2].type == "Procedure"
    assert inst.dataRequirement[3].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[3].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/opioids-abused-in-" "ambulatory-care"
    )
    assert inst.dataRequirement[3].type == "MedicationRequest"
    assert inst.dataRequirement[4].type == "Encounter"
    assert inst.date == fhirtypes.DateTime.validate("2018-03-25T13:49:09-06:00")
    assert inst.experimental is False
    assert inst.id == "opioidcds-recommendation-07"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OpioidCDS_REC_07"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
        "The purpose of this library is to determine whether the "
        "patient has been evaluated for benefits and harms within 1 "
        "to 4 weeks of starting opioid therapy and every 3 months or "
        "more subsequently."
    )
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
    assert (
        inst.relatedArtifact[1].resource
        == "http://example.org/fhir/Library/opioidcds-common"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Opioid CDS Logic for recommendation #7"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is used to notify the prescriber/user whether "
        "an evaluation for benefits and harms associated with opioid "
        "therapy is recommended for the patient."
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


def test_library_1(base_settings):
    """No. 1 tests collection for Library.
    Test File: library-opioidcds-recommendation-07.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-07.json"
    )
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_1(inst2)


def impl_library_2(inst):
    assert inst.content[0].contentType == "application/xml"
    assert inst.content[0].url == "http://cqlrepository.org/fhirmodel-modelinfo.xml"
    assert inst.date == fhirtypes.DateTime.validate("2016-07-08")
    assert inst.description == "Model definition for the FHIR Model"
    assert inst.id == "library-fhir-model-definition"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "FHIR"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR Model Definition"
    assert inst.topic[0].text == "FHIR"
    assert inst.type.coding[0].code == "model-definition"
    assert inst.version == "4.5.0"


def test_library_2(base_settings):
    """No. 2 tests collection for Library.
    Test File: library-fhir-model-definition.json
    """
    filename = base_settings["unittest_data_dir"] / "library-fhir-model-definition.json"
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_2(inst2)


def impl_library_3(inst):
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].url == "cql/OMTKLogic-0.1.0.cql"
    assert inst.content[1].contentType == "application/elm+xml"
    assert inst.content[1].url == "elm/OMTKLogic-0.1.0.xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.date == fhirtypes.DateTime.validate("2017-05-05")
    assert inst.description == (
        "Opioid Management Terminology Knowledge Base Logic for use "
        "in implementing CDC Opioid Prescribing Guidelines."
    )
    assert inst.experimental is True
    assert inst.id == "omtk-logic"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OMTKLogic"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert (
        inst.relatedArtifact[0].resource
        == "http://example.org/fhir/Library/omtk-modelinfo"
    )
    assert inst.relatedArtifact[0].type == "depends-on"
    assert (
        inst.relatedArtifact[1].display
        == "CDC guideline for prescribing opioids for chronic pain"
    )
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[1].url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert inst.relatedArtifact[2].display == "MME Conversion Tables"
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.relatedArtifact[2].url == (
        "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily" "_dose-a.pdf"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "OMTK Logic"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is used to gather information about an opioid "
        "prescription necessary to offer opioid management guidance "
        "for a patient."
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


def test_library_3(base_settings):
    """No. 3 tests collection for Library.
    Test File: library-omtk-logic.json
    """
    filename = base_settings["unittest_data_dir"] / "library-omtk-logic.json"
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_3(inst2)


def impl_library_4(inst):
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/elm+xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.dataRequirement[0].codeFilter[0].path == "medicationCodeableConcept"
    assert (
        inst.dataRequirement[0].codeFilter[0].valueSet
        == "http://example.org/fhir/ValueSet/naloxone"
    )
    assert inst.dataRequirement[0].type == "MedicationRequest"
    assert inst.dataRequirement[1].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[1].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/opioids-abused-in-" "ambulatory-care"
    )
    assert inst.dataRequirement[1].type == "MedicationRequest"
    assert inst.dataRequirement[2].codeFilter[0].path == "medicationCodeableConcept"
    assert (
        inst.dataRequirement[2].codeFilter[0].valueSet
        == "http://example.org/fhir/ValueSet/benzodiazepines"
    )
    assert inst.dataRequirement[2].type == "MedicationRequest"
    assert inst.dataRequirement[3].codeFilter[0].path == "code"
    assert (
        inst.dataRequirement[3].codeFilter[0].valueSet
        == "http://example.org/fhir/ValueSet/substance-abuse"
    )
    assert inst.dataRequirement[3].type == "Condition"
    assert inst.date == fhirtypes.DateTime.validate("2018-03-25T13:49:09-06:00")
    assert inst.description == (
        "Opioid decision support logic to consider offering Naloxone "
        "when factors that increase risk for opioid overdose are "
        "present."
    )
    assert inst.experimental is False
    assert inst.id == "opioidcds-recommendation-08"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OpioidCDS_REC_04"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
        "The purpose of this library is to determine whether "
        "increased risks for opioid overdose are present."
    )
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
    assert (
        inst.relatedArtifact[1].resource
        == "http://example.org/fhir/Library/opioidcds-common"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.relatedArtifact[2].display == "MME Conversion Tables"
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.relatedArtifact[2].url == (
        "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily" "_dose-a.pdf"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Opioid CDS Logic for recommendation #4"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is used to recommend the prescriber/user to "
        "consider offering Naloxone when increased risks for opioid "
        "overdose are present."
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


def test_library_4(base_settings):
    """No. 4 tests collection for Library.
    Test File: library-opioidcds-recommendation-08.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-08.json"
    )
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_4(inst2)


def impl_library_5(inst):
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].title == "Zika Virus Intervention Logic"
    assert inst.content[0].url == "library-zika-virus-intervention-logic-content.cql"
    assert inst.dataRequirement[0].codeFilter[0].path == "code"
    assert inst.dataRequirement[0].codeFilter[0].valueSet == "urn:oid:X.Y.Z"
    assert inst.dataRequirement[0].type == "Condition"
    assert inst.dataRequirement[1].codeFilter[0].path == "code"
    assert inst.dataRequirement[1].codeFilter[0].valueSet == "urn:oid:X.Y.Z"
    assert inst.dataRequirement[1].type == "Observation"
    assert inst.dataRequirement[2].codeFilter[0].path == "code"
    assert (
        inst.dataRequirement[2].codeFilter[0].valueSet
        == "urn:oid:2.16.840.1.114222.4.11.7459"
    )
    assert inst.dataRequirement[2].type == "Condition"
    assert inst.date == fhirtypes.DateTime.validate("2016-11-14")
    assert (
        inst.description == "Decision support logic for managing zika virus infection"
    )
    assert inst.experimental is True
    assert inst.id == "zika-virus-intervention-logic"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "zika-virus-intervention-logic"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.parameter[0].name == "Patient"
    assert inst.parameter[0].type == "Patient"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].name == "Current Encounter"
    assert inst.parameter[1].type == "Encounter"
    assert inst.parameter[1].use == "in"
    assert (
        inst.relatedArtifact[0].resource
        == "http://example.org/fhir/Library/fhir-model-definition"
    )
    assert inst.relatedArtifact[0].type == "depends-on"
    assert (
        inst.relatedArtifact[1].resource
        == "http://hl7.org/fhir/ValueSet/zika-affected-area"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Zika Virus '
        "Intervention Logic</div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Zika Virus Intervention Logic"
    assert inst.topic[0].text == "Zika Virus Management"
    assert inst.type.coding[0].code == "logic-library"
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
    assert inst.version == "1.0.0"


def test_library_5(base_settings):
    """No. 5 tests collection for Library.
    Test File: library-zika-virus-intervention-logic.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "library-zika-virus-intervention-logic.json"
    )
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_5(inst2)


def impl_library_6(inst):
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/elm+xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.dataRequirement[0].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[0].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/opioids-abused-in-" "ambulatory-care"
    )
    assert inst.dataRequirement[0].type == "MedicationRequest"
    assert inst.dataRequirement[1].type == "Encounter"
    assert inst.date == fhirtypes.DateTime.validate("2018-03-25T13:49:09-06:00")
    assert inst.description == (
        "Opioid decision support logic for prescribing extended-"
        "release/long-acting (ER/LA) opioids when starting a patient "
        "on opioids."
    )
    assert inst.experimental is False
    assert inst.id == "opioidcds-recommendation-04"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OpioidCDS_REC_04"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
        "The purpose of this library is to determine the "
        "appropriateness of extended-release opioids with ambulatory "
        "abuse potential for the patient."
    )
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
    assert (
        inst.relatedArtifact[1].resource
        == "http://example.org/fhir/Library/opioidcds-common"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Opioid CDS Logic for recommendation #4"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is used to notify the prescriber/user that "
        "immediate-release opioids are recommended when starting a "
        "patient on opioids."
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


def test_library_6(base_settings):
    """No. 6 tests collection for Library.
    Test File: library-opioidcds-recommendation-04.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-04.json"
    )
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_6(inst2)


def impl_library_7(inst):
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].title == "FHIR Helpers"
    assert inst.content[0].url == "library-fhir-helpers-content.cql"
    assert inst.date == fhirtypes.DateTime.validate("2018-11-10")
    assert inst.description == "FHIR Helpers"
    assert inst.experimental is True
    assert inst.id == "library-fhir-helpers"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "FHIRHelpers"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.relatedArtifact[0].resource
        == "http://example.org/fhir/Library/fhir-model-definition"
    )
    assert inst.relatedArtifact[0].type == "depends-on"
    assert inst.relatedArtifact[1].resource == (
        "http://example.org/fhir/Library/library-fhir-helpers-" "predecessor"
    )
    assert inst.relatedArtifact[1].type == "predecessor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR Helpers"
    assert inst.topic[0].text == "FHIR Helpers"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.version == "4.5.0"


def test_library_7(base_settings):
    """No. 7 tests collection for Library.
    Test File: library-fhir-helpers.json
    """
    filename = base_settings["unittest_data_dir"] / "library-fhir-helpers.json"
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_7(inst2)


def impl_library_8(inst):
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/elm+xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.dataRequirement[0].codeFilter[0].path == "medicationCodeableConcept"
    assert (
        inst.dataRequirement[0].codeFilter[0].valueSet
        == "http://example.org/fhir/ValueSet/benzodiazepines"
    )
    assert inst.dataRequirement[0].type == "MedicationRequest"
    assert inst.dataRequirement[1].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[1].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/opioids-abused-in-" "ambulatory-care"
    )
    assert inst.dataRequirement[1].type == "MedicationRequest"
    assert inst.date == fhirtypes.DateTime.validate("2018-03-25T13:49:09-06:00")
    assert inst.description == (
        "Opioid decision support logic to avoid prescribing opioid "
        "pain medication and benzodiazepines concurrently whenever "
        "possible."
    )
    assert inst.experimental is False
    assert inst.id == "opioidcds-recommendation-11"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OpioidCDS_REC_11"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
        "The purpose of this library is to determine whether opioid "
        "pain medication and benzodiazepines have been prescribed "
        "concurrently."
    )
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
    assert (
        inst.relatedArtifact[1].resource
        == "http://example.org/fhir/Library/opioidcds-common"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Opioid CDS Logic for recommendation #11"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is used to notify the prescriber/user to avoid "
        "prescribing opioid pain medication and benzodiazepines "
        "concurrently."
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


def test_library_8(base_settings):
    """No. 8 tests collection for Library.
    Test File: library-opioidcds-recommendation-11.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-11.json"
    )
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_8(inst2)


def impl_library_9(inst):
    assert inst.content[0].contentType == "application/xml"
    assert inst.content[0].url == "http://cqlrepository.org/quick-modelinfo.xml"
    assert inst.date == fhirtypes.DateTime.validate("2016-07-08")
    assert inst.description == "Model definition for the QUICK Logical Model"
    assert inst.id == "library-quick-model-definition"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "QUICK"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "QUICK Model Definition"
    assert inst.topic[0].text == "QUICK"
    assert inst.type.coding[0].code == "model-definition"
    assert inst.version == "1.0.0"


def test_library_9(base_settings):
    """No. 9 tests collection for Library.
    Test File: library-quick-model-definition.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-quick-model-definition.json"
    )
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_9(inst2)


def impl_library_10(inst):
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/elm+xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.date == fhirtypes.DateTime.validate("2018-03-25T13:49:09-06:00")
    assert inst.description == (
        "Common Opioid Decision Support Logic for use in implementing"
        " CDC Opioid Prescribing Guidelines."
    )
    assert inst.experimental is False
    assert inst.id == "opioidcds-common"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OpioidCDS_Common"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
        "This library contains common logic across recommendations "
        "including MME calculations, conversions, and looking up "
        "codes in valuesets."
    )
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
    assert (
        inst.relatedArtifact[1].resource == "http://example.org/fhir/Library/omtk-logic"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.relatedArtifact[2].display == "MME Conversion Tables"
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.relatedArtifact[2].url == (
        "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily" "_dose-a.pdf"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Opioid CDS Common Logic"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is used for decision support for opioid "
        "guideline recommendations when applying PlanDefinitions."
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


def test_library_10(base_settings):
    """No. 10 tests collection for Library.
    Test File: library-opioidcds-common.json
    """
    filename = base_settings["unittest_data_dir"] / "library-opioidcds-common.json"
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_10(inst2)
