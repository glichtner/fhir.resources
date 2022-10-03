# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Library
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
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
    "http://example.org/fhir/ValueSet/opioids-indicating-end-of-"
    "life"
    )
    assert inst.dataRequirement[0].type == "MedicationRequest"
    assert inst.dataRequirement[1].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[1].codeFilter[0].valueSet == (
    "http://example.org/fhir/ValueSet/opioids-abused-in-"
    "ambulatory-care"
    )
    assert inst.dataRequirement[1].type == "MedicationRequest"
    assert inst.dataRequirement[2].codeFilter[0].path == "combo-code"
    assert inst.dataRequirement[2].codeFilter[0].valueSet == (
    "http://example.org/fhir/ValueSet/illicit-drug-urine-"
    "screening"
    )
    assert inst.dataRequirement[2].type == "Observation"
    assert inst.dataRequirement[3].codeFilter[0].path == "combo-code"
    assert inst.dataRequirement[3].codeFilter[0].valueSet == "http://example.org/fhir/ValueSet/opioid-urine-screening"
    assert inst.dataRequirement[3].type == "Observation"
    assert inst.date == fhirtypes.DateTime.validate("2018-03-25T13:49:09-06:00")
    assert inst.description == (
    "Opioid decision support logic to evaluate whether the "
    "patient has had a urine screening in the past 12 months and "
    "provide analysis."
    )
    assert inst.experimental is False
    assert inst.id == "opioidcds-recommendation-10"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OpioidCDS_REC_10"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.relatedArtifact[0].display == "CDC guideline for prescribing opioids for chronic pain"
    assert inst.relatedArtifact[0].document.url == (
    "https://guidelines.gov/summaries/summary/50153/cdc-"
    "guideline-for-prescribing-opioids-for-chronic-pain---united-"
    "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].resource == "http://example.org/fhir/Library/opioidcds-common"
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Opioid CDS Logic for recommendation #10"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/library-type"
    assert inst.usage == (
    "This library is used to notify the prescriber/user whether "
    "the patient has had a urine screening in the past 12 months "
    "and to provide analysis if true."
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


def test_library_1(base_settings):
    """No. 1 tests collection for Library.
    Test File: library-opioidcds-recommendation-10.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-10.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2017-03-10")
    assert inst.description == (
    "Artifacts required for implementation of Zika Virus "
    "Management"
    )
    assert inst.id == "composition-example"
    assert inst.identifier[0].system == "http://example.org"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "Zika Artifacts"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.relatedArtifact[0].resource == (
    "http://example.org/fhir/ActivityDefinition/administer-zika-"
    "virus-exposure-assessment"
    )
    assert inst.relatedArtifact[0].type == "composed-of"
    assert inst.relatedArtifact[1].resource == (
    "http://example.org/fhir/ActivityDefinition/order-serum-zika-"
    "dengue-virus-igm"
    )
    assert inst.relatedArtifact[1].type == "composed-of"
    assert inst.relatedArtifact[2].resource == (
    "http://example.org/fhir/ActivityDefinition/provide-mosquito-"
    "prevention-advice"
    )
    assert inst.relatedArtifact[2].type == "composed-of"
    assert inst.relatedArtifact[3].resource == (
    "http://example.org/fhir/Library/zika-virus-intervention-"
    "logic"
    )
    assert inst.relatedArtifact[3].type == "composed-of"
    assert inst.relatedArtifact[4].resource == (
    "http://example.org/fhir/PlanDefinition/zika-virus-"
    "intervention"
    )
    assert inst.relatedArtifact[4].type == "composed-of"
    assert inst.relatedArtifact[5].resource == (
    "http://hl7.org/fhir/Questionnaire/zika-virus-exposure-"
    "assessment"
    )
    assert inst.relatedArtifact[5].type == "composed-of"
    assert inst.relatedArtifact[6].document.url == (
    "https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm"
    "6539e1_w"
    )
    assert inst.relatedArtifact[6].type == "derived-from"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Zika Artifacts"
    assert inst.topic[0].text == "Zika Virus Management"
    assert inst.type.coding[0].code == "asset-collection"
    assert inst.version == "1.0.0"


def test_library_2(base_settings):
    """No. 2 tests collection for Library.
    Test File: library-composition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-composition-example.json"
    )
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
    assert inst.content[0].contentType == "application/xml"
    assert inst.content[0].url == "http://cqlrepository.org/fhirmodel-modelinfo.xml"
    assert inst.date == fhirtypes.DateTime.validate("2016-07-08")
    assert inst.description == "Model definition for the FHIR Model"
    assert inst.id == "library-fhir-model-definition"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "FHIR"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR Model Definition"
    assert inst.topic[0].text == "FHIR"
    assert inst.type.coding[0].code == "model-definition"
    assert inst.version == "5.0.0"


def test_library_3(base_settings):
    """No. 3 tests collection for Library.
    Test File: library-fhir-model-definition.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-fhir-model-definition.json"
    )
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
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].title == "FHIR Helpers"
    assert inst.content[0].url == "library-fhir-helpers-content.cql"
    assert inst.date == fhirtypes.DateTime.validate("2016-11-14")
    assert inst.description == "FHIR Helpers"
    assert inst.experimental is True
    assert inst.id == "library-fhir-helpers-predecessor"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "FHIRHelpers"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.relatedArtifact[0].resource == "http://example.org/fhir/Library/fhir-model-definition"
    assert inst.relatedArtifact[0].type == "depends-on"
    assert inst.relatedArtifact[1].resource == "http://example.org/fhir/Library/library-fhir-helpers"
    assert inst.relatedArtifact[1].type == "successor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR Helpers"
    assert inst.topic[0].text == "FHIR Helpers"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.version == "1.6"


def test_library_4(base_settings):
    """No. 4 tests collection for Library.
    Test File: library-predecessor-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-predecessor-example.json"
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
    assert inst.dataRequirement[0].codeFilter[0].valueSet == "urn:oid:2.999.0.1.2.3"
    assert inst.dataRequirement[0].type == "Condition"
    assert inst.dataRequirement[1].codeFilter[0].path == "code"
    assert inst.dataRequirement[1].codeFilter[0].valueSet == "urn:oid:2.999.0.1.2.3"
    assert inst.dataRequirement[1].type == "Observation"
    assert inst.dataRequirement[2].codeFilter[0].path == "code"
    assert inst.dataRequirement[2].codeFilter[0].valueSet == "urn:oid:2.16.840.1.114222.4.11.7459"
    assert inst.dataRequirement[2].type == "Condition"
    assert inst.date == fhirtypes.DateTime.validate("2016-11-14")
    assert inst.description == "Decision support logic for managing zika virus infection"
    assert inst.experimental is True
    assert inst.id == "zika-virus-intervention-logic"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "zika-virus-intervention-logic"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.parameter[0].name == "Patient"
    assert inst.parameter[0].type == "Patient"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].name == "Current Encounter"
    assert inst.parameter[1].type == "Encounter"
    assert inst.parameter[1].use == "in"
    assert inst.relatedArtifact[0].resource == "http://example.org/fhir/Library/fhir-model-definition"
    assert inst.relatedArtifact[0].type == "depends-on"
    assert inst.relatedArtifact[1].resource == "http://hl7.org/fhir/ValueSet/zika-affected-area"
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "active"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Zika Virus "
    "Intervention Logic</div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Zika Virus Intervention Logic"
    assert inst.topic[0].text == "Zika Virus Management"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.useContext[0].code.code == "age"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueRange.low.unit == "a"
    assert float(inst.useContext[0].valueRange.low.value) == float(12)
    assert inst.useContext[1].code.code == "user"
    assert inst.useContext[1].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "309343006"
    assert inst.useContext[1].valueCodeableConcept.coding[0].display == "Physician"
    assert inst.useContext[1].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.version == "1.0.0"


def test_library_5(base_settings):
    """No. 5 tests collection for Library.
    Test File: library-zika-virus-intervention-logic.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-zika-virus-intervention-logic.json"
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
    assert inst.content[0].contentType == "text/cql"
    assert inst.dataRequirement[0].codeFilter[0].path == "code"
    assert inst.dataRequirement[0].codeFilter[0].valueSet == "urn:oid:2.16.840.1.113883.3.464.1003.111.12.1006"
    assert inst.dataRequirement[0].type == "Condition"
    assert inst.date == fhirtypes.DateTime.validate("2015-07-22")
    assert inst.description == "Common Logic for adherence to Chlamydia Screening guidelines"
    assert inst.id == "example"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "ChalmydiaScreening_Common"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.relatedArtifact[0].resource == "http://hl7.org/fhir/Library/library-quick-model-definition"
    assert inst.relatedArtifact[0].type == "depends-on"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Chlamydia Screening Common Library"
    assert inst.topic[0].text == "Chlamydia Screening"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.version == "2.0.0"


def test_library_6(base_settings):
    """No. 6 tests collection for Library.
    Test File: library-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-example.json"
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
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/elm+xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.dataRequirement[0].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[0].codeFilter[0].valueSet == (
    "http://example.org/fhir/ValueSet/opioids-abused-in-"
    "ambulatory-care"
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
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
    "The purpose of this library is to determine the "
    "appropriateness of extended-release opioids with ambulatory "
    "abuse potential for the patient."
    )
    assert inst.relatedArtifact[0].display == "CDC guideline for prescribing opioids for chronic pain"
    assert inst.relatedArtifact[0].document.url == (
    "https://guidelines.gov/summaries/summary/50153/cdc-"
    "guideline-for-prescribing-opioids-for-chronic-pain---united-"
    "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].resource == "http://example.org/fhir/Library/opioidcds-common"
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Opioid CDS Logic for recommendation #4"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/library-type"
    assert inst.usage == (
    "This library is used to notify the prescriber/user that "
    "immediate-release opioids are recommended when starting a "
    "patient on opioids."
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


def test_library_7(base_settings):
    """No. 7 tests collection for Library.
    Test File: library-opioidcds-recommendation-04.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-04.json"
    )
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
    assert inst.dataRequirement[0].codeFilter[0].valueSet == "http://example.org/fhir/ValueSet/naloxone"
    assert inst.dataRequirement[0].type == "MedicationRequest"
    assert inst.dataRequirement[1].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[1].codeFilter[0].valueSet == (
    "http://example.org/fhir/ValueSet/opioids-abused-in-"
    "ambulatory-care"
    )
    assert inst.dataRequirement[1].type == "MedicationRequest"
    assert inst.dataRequirement[2].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[2].codeFilter[0].valueSet == "http://example.org/fhir/ValueSet/benzodiazepines"
    assert inst.dataRequirement[2].type == "MedicationRequest"
    assert inst.dataRequirement[3].codeFilter[0].path == "code"
    assert inst.dataRequirement[3].codeFilter[0].valueSet == "http://example.org/fhir/ValueSet/substance-abuse"
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
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
    "The purpose of this library is to determine whether "
    "increased risks for opioid overdose are present."
    )
    assert inst.relatedArtifact[0].display == "CDC guideline for prescribing opioids for chronic pain"
    assert inst.relatedArtifact[0].document.url == (
    "https://guidelines.gov/summaries/summary/50153/cdc-"
    "guideline-for-prescribing-opioids-for-chronic-pain---united-"
    "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].resource == "http://example.org/fhir/Library/opioidcds-common"
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.relatedArtifact[2].display == "MME Conversion Tables"
    assert inst.relatedArtifact[2].document.url == (
    "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily"
    "_dose-a.pdf"
    )
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Opioid CDS Logic for recommendation #4"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/library-type"
    assert inst.usage == (
    "This library is used to recommend the prescriber/user to "
    "consider offering Naloxone when increased risks for opioid "
    "overdose are present."
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


def test_library_8(base_settings):
    """No. 8 tests collection for Library.
    Test File: library-opioidcds-recommendation-08.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-08.json"
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
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
    "This library contains common logic across recommendations "
    "including MME calculations, conversions, and looking up "
    "codes in valuesets."
    )
    assert inst.relatedArtifact[0].display == "CDC guideline for prescribing opioids for chronic pain"
    assert inst.relatedArtifact[0].document.url == (
    "https://guidelines.gov/summaries/summary/50153/cdc-"
    "guideline-for-prescribing-opioids-for-chronic-pain---united-"
    "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].resource == "http://example.org/fhir/Library/omtk-logic"
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.relatedArtifact[2].display == "MME Conversion Tables"
    assert inst.relatedArtifact[2].document.url == (
    "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily"
    "_dose-a.pdf"
    )
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Opioid CDS Common Logic"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/library-type"
    assert inst.usage == (
    "This library is used for decision support for opioid "
    "guideline recommendations when applying PlanDefinitions."
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


def test_library_9(base_settings):
    """No. 9 tests collection for Library.
    Test File: library-opioidcds-common.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-common.json"
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
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.relatedArtifact[0].resource == "http://example.org/fhir/Library/omtk-modelinfo"
    assert inst.relatedArtifact[0].type == "depends-on"
    assert inst.relatedArtifact[1].display == "CDC guideline for prescribing opioids for chronic pain"
    assert inst.relatedArtifact[1].document.url == (
    "https://guidelines.gov/summaries/summary/50153/cdc-"
    "guideline-for-prescribing-opioids-for-chronic-pain---united-"
    "states-2016#420"
    )
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[2].display == "MME Conversion Tables"
    assert inst.relatedArtifact[2].document.url == (
    "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily"
    "_dose-a.pdf"
    )
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "OMTK Logic"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/library-type"
    assert inst.usage == (
    "This library is used to gather information about an opioid "
    "prescription necessary to offer opioid management guidance "
    "for a patient."
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


def test_library_10(base_settings):
    """No. 10 tests collection for Library.
    Test File: library-omtk-logic.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-omtk-logic.json"
    )
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