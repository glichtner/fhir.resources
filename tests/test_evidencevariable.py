# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EvidenceVariable
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import evidencevariable


def impl_evidencevariable_1(inst):
    assert inst.actual is False
    assert inst.characteristic[0].definitionByCombination.characteristic[0].definitionCodeableConcept.coding[0].code == "718705001"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].definitionCodeableConcept.coding[0].display == "Functionally dependent (finding)"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].definitionCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].description == "functionally dependent at 90 days"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].code == "study-start"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].display == "Study Start"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].system == "http://hl7.org/fhir/evidence-variable-event"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].timeFromEvent[0].quantity.code == "d"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].timeFromEvent[0].quantity.system == "http://unitsofmeasure.org"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].timeFromEvent[0].quantity.unit == "day"
    assert float(inst.characteristic[0].definitionByCombination.characteristic[0].timeFromEvent[0].quantity.value) == float(90)
    assert inst.characteristic[0].definitionByCombination.characteristic[1].definitionCodeableConcept.coding[0].code == "419099009"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].definitionCodeableConcept.coding[0].display == "Dead (finding)"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].definitionCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].description == "dead at 90 days"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].timeFromEvent[0].quantity.code == "d"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].timeFromEvent[0].quantity.system == "http://unitsofmeasure.org"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].timeFromEvent[0].quantity.unit == "day"
    assert float(inst.characteristic[0].definitionByCombination.characteristic[1].timeFromEvent[0].quantity.value) == float(90)
    assert inst.characteristic[0].definitionByCombination.code == "any-of"
    assert inst.characteristic[0].description == "Dead or functionally dependent at 90 days"
    assert inst.description == "Dead or functionally dependent at 90 days"
    assert inst.handling == "dichotomous"
    assert inst.id == "example-dead-or-dependent-90day"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "DeadOrFunctionallyDependentAt90Days"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Dead or functionally dependent at 90 days"


def test_evidencevariable_1(base_settings):
    """No. 1 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-dead-or-dependent-90day.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-dead-or-dependent-90day.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_1(inst2)


def impl_evidencevariable_2(inst):
    assert inst.actual is False
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].code == "8410"
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].display == "alteplase"
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.characteristic[0].description == "no alteplase"
    assert inst.characteristic[0].exclude is True
    assert inst.description == "no alteplase"
    assert inst.id == "example-no-alteplase"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "NoAlteplase"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "no alteplase"


def test_evidencevariable_2(base_settings):
    """No. 2 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-no-alteplase.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-no-alteplase.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_2(inst2)


def impl_evidencevariable_3(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionExpression.description == "mRS 3-6"
    assert inst.characteristic[0].definitionExpression.expression == (
    "[\"Observation\": code in \"75859-9|LOINC\"] mRS where "
    "mRS.value between 3 and 6"
    )
    assert inst.characteristic[0].definitionExpression.language == "text/cql"
    assert inst.characteristic[0].description == "mRS 3-6 at 90 days"
    assert inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].code == "study-start"
    assert inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].display == "Study Start"
    assert inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].system == "http://hl7.org/fhir/evidence-variable-event"
    assert inst.characteristic[0].timeFromEvent[0].quantity.code == "d"
    assert inst.characteristic[0].timeFromEvent[0].quantity.system == "http://unitsofmeasure.org"
    assert inst.characteristic[0].timeFromEvent[0].quantity.unit == "day"
    assert float(inst.characteristic[0].timeFromEvent[0].quantity.value) == float(90)
    assert inst.description == "Modified Rankin Scale score 3-6 at 90 days after treatment"
    assert inst.handling == "dichotomous"
    assert inst.id == "example-mRS3-6-at-90days"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "ModifiedRankinScaleScore36At90DaysAfterTreatment"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Modified Rankin Scale score 3-6 at 90 days after treatment"


def test_evidencevariable_3(base_settings):
    """No. 3 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-mRS3-6-at-90days.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-mRS3-6-at-90days.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_3(inst2)


def impl_evidencevariable_4(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].code == "1386000"
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].display == "Intracranial hemorrhage (disorder)"
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[0].description == "intracranial hemorrhage within 7 days"
    assert inst.characteristic[0].timeFromEvent[0].description == "within 7 days"
    assert inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].code == "study-start"
    assert inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].display == "Study Start"
    assert inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].system == "http://hl7.org/fhir/evidence-variable-event"
    assert inst.characteristic[0].timeFromEvent[0].range.high.code == "d"
    assert inst.characteristic[0].timeFromEvent[0].range.high.system == "http://unitsofmeasure.org"
    assert inst.characteristic[0].timeFromEvent[0].range.high.unit == "day"
    assert float(inst.characteristic[0].timeFromEvent[0].range.high.value) == float(7)
    assert inst.characteristic[0].timeFromEvent[0].range.low.code == "d"
    assert inst.characteristic[0].timeFromEvent[0].range.low.system == "http://unitsofmeasure.org"
    assert inst.characteristic[0].timeFromEvent[0].range.low.unit == "day"
    assert float(inst.characteristic[0].timeFromEvent[0].range.low.value) == float(0)
    assert inst.characteristic[1].definitionCodeableConcept.coding[0].code == "419620001"
    assert inst.characteristic[1].definitionCodeableConcept.coding[0].display == "Death (event)"
    assert inst.characteristic[1].definitionCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[1].description == "death within 7 days"
    assert inst.characteristic[1].timeFromEvent[0].description == "within 7 days"
    assert inst.characteristic[1].timeFromEvent[0].range.high.code == "d"
    assert inst.characteristic[1].timeFromEvent[0].range.high.system == "http://unitsofmeasure.org"
    assert inst.characteristic[1].timeFromEvent[0].range.high.unit == "day"
    assert float(inst.characteristic[1].timeFromEvent[0].range.high.value) == float(7)
    assert inst.characteristic[1].timeFromEvent[0].range.low.code == "d"
    assert inst.characteristic[1].timeFromEvent[0].range.low.system == "http://unitsofmeasure.org"
    assert inst.characteristic[1].timeFromEvent[0].range.low.unit == "day"
    assert float(inst.characteristic[1].timeFromEvent[0].range.low.value) == float(0)
    assert inst.description == "Fatal Intracranial Hemorrhage Within Seven Days"
    assert inst.handling == "dichotomous"
    assert inst.id == "example-fatal-ICH-in-7-days"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "FatalIntracranialHemorrhageWithinSevenDays"
    assert inst.note[0].text == "Death must be due to intracranial hemorrhage"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Fatal Intracranial Hemorrhage Within Seven Days"


def test_evidencevariable_4(base_settings):
    """No. 4 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-fatal-ICH-in-7-days.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-fatal-ICH-in-7-days.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_4(inst2)


def impl_evidencevariable_5(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionByCombination.characteristic[0].definitionReference.display == "ECASS III Trial Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].definitionReference.reference == "Group/ECASSIII-Trial-Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].definitionReference.type == "Group"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].definitionReference.display == "IST3 Trial Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].definitionReference.reference == "Group/IST3-Trial-Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].definitionReference.type == "Group"
    assert inst.characteristic[0].definitionByCombination.characteristic[2].definitionReference.display == "ECASS Trial Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[2].definitionReference.reference == "Group/ECASS-Trial-Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[2].definitionReference.type == "Group"
    assert inst.characteristic[0].definitionByCombination.characteristic[3].definitionReference.display == "ECASSII Trial Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[3].definitionReference.reference == "Group/ECASSII-Trial-Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[3].definitionReference.type == "Group"
    assert inst.characteristic[0].definitionByCombination.characteristic[4].definitionReference.display == "EPITHET Trial Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[4].definitionReference.reference == "Group/EPITHET-Trial-Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[4].definitionReference.type == "Group"
    assert inst.characteristic[0].definitionByCombination.characteristic[5].definitionReference.display == "ATLANTIS Trial Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[5].definitionReference.reference == "Group/ATLANTIS-Trial-Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[5].definitionReference.type == "Group"
    assert inst.characteristic[0].definitionByCombination.characteristic[6].definitionReference.display == "NINDS Trial Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[6].definitionReference.reference == "Group/NINDS-Trial-Cohort"
    assert inst.characteristic[0].definitionByCombination.characteristic[6].definitionReference.type == "Group"
    assert inst.characteristic[0].definitionByCombination.code == "any-of"
    assert inst.characteristic[0].description == (
    "Stroke Thrombolysis Trialists’ Collaborators Group "
    "collection used for individual patient data meta-analysis"
    )
    assert inst.description == (
    "Stroke Thrombolysis Trialists’ Collaborators Group "
    "collection used for individual patient data meta-analysis"
    )
    assert inst.id == (
    "example-Stroke-Thrombolysis-Trialists-2014-2016-IPD-MA-"
    "Cohort"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "StrokeThrombolysisTrialists20142016IPDMACohort"
    assert inst.relatedArtifact[0].document.url == "https://doi.org/10.1016/S0140-6736(14)60584-5"
    assert inst.relatedArtifact[0].label == "Emberson 2014"
    assert inst.relatedArtifact[0].type == "citation"
    assert inst.relatedArtifact[1].display == "Figure 2 Lees 2016"
    assert inst.relatedArtifact[1].document.url == "https://doi.org/10.1161/STROKEAHA.116.013644"
    assert inst.relatedArtifact[1].label == "Lees 2016"
    assert inst.relatedArtifact[1].type == "citation"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == (
    "Stroke Thrombolysis Trialists’ Collaborators Group "
    "collection used for individual patient data meta-analysis"
    )


def test_evidencevariable_5(base_settings):
    """No. 5 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-Stroke-Thrombolysis-Trialists-2014-2016-IPD-MA-Cohort.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-Stroke-Thrombolysis-Trialists-2014-2016-IPD-MA-Cohort.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_5(inst2)


def impl_evidencevariable_6(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionExpression.description == "mRS 0-2"
    assert inst.characteristic[0].definitionExpression.expression == (
    "[\"Observation\": code in \"75859-9|LOINC\"] mRS where "
    "mRS.value between 0 and 2"
    )
    assert inst.characteristic[0].definitionExpression.language == "text/cql"
    assert inst.characteristic[0].description == "mRS 0-2 at 90 days"
    assert inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].code == "study-start"
    assert inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].display == "Study Start"
    assert inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].system == "http://hl7.org/fhir/evidence-variable-event"
    assert inst.characteristic[0].timeFromEvent[0].quantity.code == "d"
    assert inst.characteristic[0].timeFromEvent[0].quantity.system == "http://unitsofmeasure.org"
    assert inst.characteristic[0].timeFromEvent[0].quantity.unit == "day"
    assert float(inst.characteristic[0].timeFromEvent[0].quantity.value) == float(90)
    assert inst.description == "Modified Rankin Scale score 0-2 at 90 days after treatment"
    assert inst.handling == "dichotomous"
    assert inst.id == "example-mRS0-2-at-90days"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "ModifiedRankinScaleScore02At90DaysAfterTreatment"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Modified Rankin Scale score 0-2 at 90 days after treatment"


def test_evidencevariable_6(base_settings):
    """No. 6 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-mRS0-2-at-90days.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-mRS0-2-at-90days.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_6(inst2)


def impl_evidencevariable_7(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionByCombination.characteristic[0].definitionReference.display == "NINDS 1995"
    assert inst.characteristic[0].definitionByCombination.characteristic[0].definitionReference.type == "Evidence"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].definitionReference.display == "ECASS 1995"
    assert inst.characteristic[0].definitionByCombination.characteristic[1].definitionReference.type == "Evidence"
    assert inst.characteristic[0].definitionByCombination.characteristic[2].definitionReference.display == "ECASS II 1998"
    assert inst.characteristic[0].definitionByCombination.characteristic[2].definitionReference.type == "Evidence"
    assert inst.characteristic[0].definitionByCombination.characteristic[3].definitionReference.display == "ATLANTIS B 1999"
    assert inst.characteristic[0].definitionByCombination.characteristic[3].definitionReference.type == "Evidence"
    assert inst.characteristic[0].definitionByCombination.characteristic[4].definitionReference.display == "ATLANTIS A 2000"
    assert inst.characteristic[0].definitionByCombination.characteristic[4].definitionReference.type == "Evidence"
    assert inst.characteristic[0].definitionByCombination.characteristic[5].definitionReference.display == "IST3 2012"
    assert inst.characteristic[0].definitionByCombination.characteristic[5].definitionReference.type == "Evidence"
    assert inst.characteristic[0].definitionByCombination.code == "any-of"
    assert inst.characteristic[0].description == (
    "'Wardlaw 2014 Analysis 1.16.3 Evidence set' is a grouping of"
    " six Evidence results used in a meta-analysis."
    )
    assert inst.description == "Wardlaw 2014  Analysis 1.16.3  Evidence set"
    assert inst.handling == "dichotomous"
    assert inst.id == "example-Wardlaw2014Analysis1.16.3EvidenceSet"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Wardlaw2014Analysis1163EvidenceSet"
    assert inst.note[0].text == (
    "Short names for Evidence sources are detailed in 'References"
    " to studies included in this review'"
    )
    assert inst.relatedArtifact[0].citation == (
    "Wardlaw JM, Murray V, Berge E, del Zoppo GJ. Thrombolysis "
    "for acute ischaemic stroke. Cochrane Database Syst Rev. 2014"
    " Jul 29(7):CD000213. PMID 25072528"
    )
    assert inst.relatedArtifact[0].display == "Analysis 1.16.3 from Wardlaw 2014"
    assert inst.relatedArtifact[0].document.url == "https://doi.org/10.1002/14651858.CD000213.pub3"
    assert inst.relatedArtifact[0].label == "Wardlaw 2014"
    assert inst.relatedArtifact[0].type == "citation"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Wardlaw 2014  Analysis 1.16.3  Evidence set"


def test_evidencevariable_7(base_settings):
    """No. 7 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-Wardlaw2014Analysis1.16.3EvidenceSet.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-Wardlaw2014Analysis1.16.3EvidenceSet.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_7(inst2)


def impl_evidencevariable_8(inst):
    assert inst.actual is True
    assert inst.author[0].name == "Brian S. Alper"
    assert inst.characteristic[0].definitionByTypeAndValue.type.coding[0].code == "397669002"
    assert inst.characteristic[0].definitionByTypeAndValue.type.coding[0].display == "Age"
    assert inst.characteristic[0].definitionByTypeAndValue.type.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[0].definitionByTypeAndValue.valueRange.high.code == "a"
    assert inst.characteristic[0].definitionByTypeAndValue.valueRange.high.system == "http://unitsofmeasure.org"
    assert inst.characteristic[0].definitionByTypeAndValue.valueRange.high.unit == "years"
    assert float(inst.characteristic[0].definitionByTypeAndValue.valueRange.high.value) == float(67)
    assert inst.characteristic[0].definitionByTypeAndValue.valueRange.low.code == "a"
    assert inst.characteristic[0].definitionByTypeAndValue.valueRange.low.system == "http://unitsofmeasure.org"
    assert inst.characteristic[0].definitionByTypeAndValue.valueRange.low.unit == "years"
    assert float(inst.characteristic[0].definitionByTypeAndValue.valueRange.low.value) == float(30)
    assert inst.characteristic[0].description == "Age 30 to 67 years at eligibility visit."
    assert inst.characteristic[0].exclude is False
    assert inst.characteristic[0].timeFromEvent[0].description == "at eligibility visit"
    assert inst.characteristic[0].timeFromEvent[0].eventId == "EligibilityVisit"
    assert float(inst.characteristic[0].timeFromEvent[0].quantity.value) == float(0)
    assert inst.characteristic[1].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[0].code == "64572001"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[0].display == "Disease (disorder)"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[1].code == "Condition"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[1].display == "Condition"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[1].system == "http://hl7.org/fhir/resource-types"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].definitionByTypeAndValue.valueCodeableConcept.coding[0].code == "44054006"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].definitionByTypeAndValue.valueCodeableConcept.coding[0].display == "Diabetes mellitus type 2 (disorder)"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].definitionByTypeAndValue.valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].description == "Diagnosed with T2DM at least 6 months prior to enrollment"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].exclude is False
    assert inst.characteristic[1].definitionByCombination.characteristic[0].timeFromEvent[0].description == "at least 6 months prior to enrollment"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].timeFromEvent[0].eventId == "EligibilityVisit"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].timeFromEvent[0].quantity.code == "mo"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].timeFromEvent[0].quantity.comparator == "<="
    assert inst.characteristic[1].definitionByCombination.characteristic[0].timeFromEvent[0].quantity.system == "http://unitsofmeasure.org"
    assert inst.characteristic[1].definitionByCombination.characteristic[0].timeFromEvent[0].quantity.unit == "months"
    assert float(inst.characteristic[1].definitionByCombination.characteristic[0].timeFromEvent[0].quantity.value) == float(-6)
    assert inst.characteristic[1].definitionByCombination.characteristic[1].definitionCodeableConcept.coding[0].code == "305450004"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].definitionCodeableConcept.coding[0].display == "Under care of doctor (finding)"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].definitionCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].definitionCodeableConcept.text == "under the active care of a doctor"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].description == (
    "under the active care of a doctor for at least the six "
    "months prior to enrollment"
    )
    assert inst.characteristic[1].definitionByCombination.characteristic[1].exclude is False
    assert inst.characteristic[1].definitionByCombination.characteristic[1].note[0].text == (
    "assumption that active care means active care of type 2 "
    "diabetes mellitus"
    )
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].description == "for at least the six months prior to enrollment"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].eventCodeableConcept.coding[0].code == "450332002"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].eventCodeableConcept.coding[0].display == "Assessment of eligibility for clinical trial"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].eventCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].note[0].text == (
    "presence throughout the range is equivalent to 'for at least"
    " the six months prior to'"
    )
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].range.high.code == "mo"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].range.high.system == "http://unitsofmeasure.org"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].range.high.unit == "months"
    assert float(inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].range.high.value) == float(0)
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].range.low.code == "mo"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].range.low.system == "http://unitsofmeasure.org"
    assert inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].range.low.unit == "months"
    assert float(inst.characteristic[1].definitionByCombination.characteristic[1].timeFromEvent[0].range.low.value) == float(-6)
    assert inst.characteristic[1].definitionByCombination.characteristic[2].definitionByTypeAndValue.type.coding[0].code == "59261-8"
    assert inst.characteristic[1].definitionByCombination.characteristic[2].definitionByTypeAndValue.type.coding[0].display == "Hemoglobin A1c/Hemoglobin.total in Blood"
    assert inst.characteristic[1].definitionByCombination.characteristic[2].definitionByTypeAndValue.type.coding[0].system == "http://loinc.org"
    assert inst.characteristic[1].definitionByCombination.characteristic[2].definitionByTypeAndValue.valueQuantity.code == "%"
    assert inst.characteristic[1].definitionByCombination.characteristic[2].definitionByTypeAndValue.valueQuantity.comparator == ">="
    assert inst.characteristic[1].definitionByCombination.characteristic[2].definitionByTypeAndValue.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.characteristic[1].definitionByCombination.characteristic[2].definitionByTypeAndValue.valueQuantity.unit == "%"
    assert float(inst.characteristic[1].definitionByCombination.characteristic[2].definitionByTypeAndValue.valueQuantity.value) == float(8)
    assert inst.characteristic[1].definitionByCombination.characteristic[2].description == "HbA1c ≥ 8.0%"
    assert inst.characteristic[1].definitionByCombination.characteristic[2].exclude is False
    assert inst.characteristic[1].definitionByCombination.characteristic[2].note[0].text == (
    "assumption that this is the last recorded HbA1c before the "
    "enrollment visit, but not explicitly stated in the short-"
    "phrase Eligibility Criteria"
    )
    assert inst.characteristic[1].definitionByCombination.code == "all-of"
    assert inst.characteristic[1].description == (
    "Diagnosed with T2DM at least 6 months prior to enrollment, "
    "under the active care of a doctor for at least the six "
    "months prior to enrollment, and HbA1c ≥ 8.0%."
    )
    assert inst.characteristic[1].exclude is False
    assert inst.characteristic[2].definitionByTypeAndValue.type.coding[0].code == "39156-5"
    assert inst.characteristic[2].definitionByTypeAndValue.type.coding[0].display == "Body mass index (BMI) [Ratio]"
    assert inst.characteristic[2].definitionByTypeAndValue.type.coding[0].system == "http://loinc.org"
    assert inst.characteristic[2].definitionByTypeAndValue.valueRange.high.code == "kg/m2"
    assert inst.characteristic[2].definitionByTypeAndValue.valueRange.high.system == "http://unitsofmeasure.org"
    assert inst.characteristic[2].definitionByTypeAndValue.valueRange.high.unit == "kg/m2"
    assert float(inst.characteristic[2].definitionByTypeAndValue.valueRange.high.value) == float(39.9)
    assert inst.characteristic[2].definitionByTypeAndValue.valueRange.low.code == "kg/m2"
    assert inst.characteristic[2].definitionByTypeAndValue.valueRange.low.system == "http://unitsofmeasure.org"
    assert inst.characteristic[2].definitionByTypeAndValue.valueRange.low.unit == "kg/m2"
    assert float(inst.characteristic[2].definitionByTypeAndValue.valueRange.low.value) == float(30)
    assert inst.characteristic[2].description == (
    "Body Mass Index (BMI) ≥ 30.0 kg/m2 and ≤ 39.9 kg/m2 at "
    "eligibility visit."
    )
    assert inst.characteristic[2].exclude is False
    assert inst.characteristic[2].timeFromEvent[0].description == "at eligibility visit"
    assert inst.characteristic[2].timeFromEvent[0].eventId == "EligibilityVisit"
    assert float(inst.characteristic[2].timeFromEvent[0].quantity.value) == float(0)
    assert inst.characteristic[3].description == (
    "Willingness to accept random assignment to either treatment "
    "group."
    )
    assert inst.characteristic[3].exclude is False
    assert inst.characteristic[4].description == (
    "Expect to live or work within approximately one hour's "
    "traveling time from the study clinic for the duration of the"
    " two-year trial."
    )
    assert inst.characteristic[4].exclude is False
    assert inst.characteristic[5].description == (
    "Willingness to comply with the follow-up protocol and "
    "successful completion of the run-in."
    )
    assert inst.characteristic[5].exclude is False
    assert inst.characteristic[6].description == "Written informed consent."
    assert inst.characteristic[6].exclude is False
    assert inst.characteristic[6].linkId == "EligibilityVisit"
    assert inst.characteristic[6].timeFromEvent[0].eventCodeableConcept.coding[0].code == "450332002"
    assert inst.characteristic[6].timeFromEvent[0].eventCodeableConcept.coding[0].display == "Assessment of eligibility for clinical trial (procedure)"
    assert inst.characteristic[6].timeFromEvent[0].eventCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[7].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[0].code == "64572001"
    assert inst.characteristic[7].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[0].display == "Disease (disorder)"
    assert inst.characteristic[7].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[7].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[1].code == "Condition"
    assert inst.characteristic[7].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[1].display == "Condition"
    assert inst.characteristic[7].definitionByCombination.characteristic[0].definitionByTypeAndValue.type.coding[1].system == "http://hl7.org/fhir/resource-types"
    assert inst.characteristic[7].definitionByCombination.characteristic[0].definitionByTypeAndValue.valueCodeableConcept.coding[0].code == "22298006"
    assert inst.characteristic[7].definitionByCombination.characteristic[0].definitionByTypeAndValue.valueCodeableConcept.coding[0].display == "Myocardial infarction (disorder)"
    assert inst.characteristic[7].definitionByCombination.characteristic[0].definitionByTypeAndValue.valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[7].definitionByCombination.characteristic[0].description == "myocardial infarction"
    assert inst.characteristic[7].definitionByCombination.characteristic[1].definitionByTypeAndValue.type.coding[0].code == "64572001"
    assert inst.characteristic[7].definitionByCombination.characteristic[1].definitionByTypeAndValue.type.coding[0].display == "Disease (disorder)"
    assert inst.characteristic[7].definitionByCombination.characteristic[1].definitionByTypeAndValue.type.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[7].definitionByCombination.characteristic[1].definitionByTypeAndValue.type.coding[1].code == "Condition"
    assert inst.characteristic[7].definitionByCombination.characteristic[1].definitionByTypeAndValue.type.coding[1].display == "Condition"
    assert inst.characteristic[7].definitionByCombination.characteristic[1].definitionByTypeAndValue.type.coding[1].system == "http://hl7.org/fhir/resource-types"
    assert inst.characteristic[7].definitionByCombination.characteristic[1].definitionByTypeAndValue.valueCodeableConcept.coding[0].code == "394659003"
    assert inst.characteristic[7].definitionByCombination.characteristic[1].definitionByTypeAndValue.valueCodeableConcept.coding[0].display == "Acute coronary syndrome (disorder)"
    assert inst.characteristic[7].definitionByCombination.characteristic[1].definitionByTypeAndValue.valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[7].definitionByCombination.characteristic[1].description == "acute coronary syndrome"
    assert inst.characteristic[7].definitionByCombination.characteristic[2].definitionByTypeAndValue.type.coding[0].code == "71388002"
    assert inst.characteristic[7].definitionByCombination.characteristic[2].definitionByTypeAndValue.type.coding[0].display == "Procedure (procedure)"
    assert inst.characteristic[7].definitionByCombination.characteristic[2].definitionByTypeAndValue.type.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[7].definitionByCombination.characteristic[2].definitionByTypeAndValue.valueCodeableConcept.coding[0].code == "81266008"
    assert inst.characteristic[7].definitionByCombination.characteristic[2].definitionByTypeAndValue.valueCodeableConcept.coding[0].display == "Heart revascularization (procedure)"
    assert inst.characteristic[7].definitionByCombination.characteristic[2].definitionByTypeAndValue.valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[7].definitionByCombination.characteristic[2].description == "coronary artery angioplasty or bypass"
    assert inst.characteristic[7].definitionByCombination.characteristic[3].definitionByTypeAndValue.type.coding[0].code == "64572001"
    assert inst.characteristic[7].definitionByCombination.characteristic[3].definitionByTypeAndValue.type.coding[0].display == "Disease (disorder)"
    assert inst.characteristic[7].definitionByCombination.characteristic[3].definitionByTypeAndValue.type.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[7].definitionByCombination.characteristic[3].definitionByTypeAndValue.type.coding[1].code == "Condition"
    assert inst.characteristic[7].definitionByCombination.characteristic[3].definitionByTypeAndValue.type.coding[1].display == "Condition"
    assert inst.characteristic[7].definitionByCombination.characteristic[3].definitionByTypeAndValue.type.coding[1].system == "http://hl7.org/fhir/resource-types"
    assert inst.characteristic[7].definitionByCombination.characteristic[3].definitionByTypeAndValue.valueCodeableConcept.coding[0].code == "230690007"
    assert inst.characteristic[7].definitionByCombination.characteristic[3].definitionByTypeAndValue.valueCodeableConcept.coding[0].display == "Cerebrovascular accident (disorder)"
    assert inst.characteristic[7].definitionByCombination.characteristic[3].definitionByTypeAndValue.valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[7].definitionByCombination.characteristic[3].description == "stroke"
    assert inst.characteristic[7].definitionByCombination.code == "any-of"
    assert inst.characteristic[7].description == (
    "Cardiovascular event (myocardial infarction, acute coronary "
    "syndrome, coronary artery angioplasty or bypass, stroke) in "
    "the past six months."
    )
    assert inst.characteristic[7].exclude is True
    assert inst.characteristic[7].timeFromEvent[0].description == "in the past six months"
    assert inst.characteristic[7].timeFromEvent[0].eventId == "EligibilityVisit"
    assert inst.characteristic[7].timeFromEvent[0].note[0].text == (
    "occurrence within the range is equivalent to 'in the past "
    "six months'"
    )
    assert inst.characteristic[7].timeFromEvent[0].range.high.code == "mo"
    assert inst.characteristic[7].timeFromEvent[0].range.high.system == "http://unitsofmeasure.org"
    assert inst.characteristic[7].timeFromEvent[0].range.high.unit == "months"
    assert float(inst.characteristic[7].timeFromEvent[0].range.high.value) == float(0)
    assert inst.characteristic[7].timeFromEvent[0].range.low.code == "mo"
    assert inst.characteristic[7].timeFromEvent[0].range.low.system == "http://unitsofmeasure.org"
    assert inst.characteristic[7].timeFromEvent[0].range.low.unit == "months"
    assert float(inst.characteristic[7].timeFromEvent[0].range.low.value) == float(-6)
    assert inst.characteristic[8].description == (
    "Current evidence of congestive heart failure, angina "
    "pectoris, or symptomatic peripheral vascular disease."
    )
    assert inst.characteristic[8].exclude is True
    assert inst.characteristic[8].note[0].text == (
    "This may be possible to encode as presence of "
    "Disease(disorder) without 'in remission'"
    )
    assert inst.characteristic[9].description == (
    "Cardiac stress test indicating that surgery or IMM would not"
    " be safe."
    )
    assert inst.characteristic[9].exclude is True
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].value == "support@computablepublishing.com"
    assert inst.copyright == "https://creativecommons.org/licenses/by-nc-sa/4.0/"
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate("2016-12")
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate("2008-02")
    assert inst.id == "example-eligibility-criteria-diabetes-surgery"
    assert inst.identifier[0].assigner.display == "Computable Publishing LLC"
    assert inst.identifier[0].system == "https://fevir.net"
    assert inst.identifier[0].type.text == "FEvIR Object Identifier"
    assert inst.identifier[0].value == "32120"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == (
    "StudyEligibilityCriteriaEligibilityCriteriaForBariatricSurge"
    "ryRandomizedTrialDiabetesSurgeryStudy"
    )
    assert inst.publisher == "Computable Publishing LLC"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == (
    "StudyEligibilityCriteria: Eligibility Criteria for Bariatric"
    " Surgery Randomized Trial (Diabetes Surgery Study)"
    )


def test_evidencevariable_8(base_settings):
    """No. 8 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-eligibility-criteria-diabetes-surgery.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-eligibility-criteria-diabetes-surgery.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_8(inst2)


def impl_evidencevariable_9(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionCanonical == (
    "http://example.org/fhir/ActivityDefinition/example-"
    "alteplase-dosing"
    )
    assert inst.characteristic[0].description == (
    "IV alteplase 0.9 mg/kg (maximum 90 mg) as 10% of dose over 1"
    " minute and 90% over 1 hour"
    )
    assert inst.description == "Alteplase for Stroke"
    assert inst.id == "example-alteplase-for-stroke"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "AlteplaseForStroke"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Alteplase for Stroke"


def test_evidencevariable_9(base_settings):
    """No. 9 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-alteplase-for-stroke.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-alteplase-for-stroke.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_9(inst2)


def impl_evidencevariable_10(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].code == "182886004"
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].display == "Placebo given (situation)"
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.characteristic[0].description == "placebo"
    assert inst.description == "placebo"
    assert inst.id == "example-placebo"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Placebo"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "placebo"


def test_evidencevariable_10(base_settings):
    """No. 10 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-placebo.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-placebo.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_10(inst2)