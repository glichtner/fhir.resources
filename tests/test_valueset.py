# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import valueset


def impl_valueset_1(inst):
    assert inst.compose.include[0].filter[0].op == "is-a"
    assert inst.compose.include[0].filter[0].property == "concept"
    assert inst.compose.include[0].filter[0].value == "_ActDetectedIssueManagementCode"
    assert (
        inst.compose.include[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == (
        "Kinds of mitigating actions and observations that can be "
        "associated with a detected issue or contraindication, such "
        "as 'added concurrent therapy', 'prior therapy documented', "
        "etc."
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "cds"
    assert inst.id == "detectedissue-mitigation-action"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.205"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "DetectedIssueMitigationAction"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Detected Issue Mitigation Action"
    assert inst.url == "http://hl7.org/fhir/ValueSet/detectedissue-mitigation-action"
    assert inst.version == "4.5.0"


def test_valueset_1(base_settings):
    """No. 1 tests collection for ValueSet.
    Test File: valueset-detectedissue-mitigation-action.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-detectedissue-mitigation-action.json"
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
    assert inst.compose.include[0].filter[0].op == "is-a"
    assert inst.compose.include[0].filter[0].property == "concept"
    assert inst.compose.include[0].filter[0].value == "91723000"
    assert inst.compose.include[0].system == "http://snomed.info/sct"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == (
        "This value set includes Anatomical Structure codes from "
        "SNOMED CT - provided as an exemplar."
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "approach-site-codes"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.346"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "SNOMEDCTAnatomicalStructureForAdministrationSiteCodes"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "SNOMED CT Anatomical Structure for Administration Site Codes"
    assert inst.url == "http://hl7.org/fhir/ValueSet/approach-site-codes"
    assert inst.version == "4.5.0"


def test_valueset_2(base_settings):
    """No. 2 tests collection for ValueSet.
    Test File: valueset-approach-site-codes.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-approach-site-codes.json"
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
    assert inst.compose.include[0].system == "http://hl7.org/fhir/trigger-type"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.description == "The type of trigger."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 5
    assert inst.id == "trigger-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.103"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "TriggerType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><ul><li>Include '
        'all codes defined in <a href="codesystem-trigger-'
        'type.html"><code>http://hl7.org/fhir/trigger-'
        "type</code></a></li></ul></div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "TriggerType"
    assert inst.url == "http://hl7.org/fhir/ValueSet/trigger-type"
    assert inst.version == "4.5.0"


def test_valueset_3(base_settings):
    """No. 3 tests collection for ValueSet.
    Test File: valueset-trigger-type.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-trigger-type.json"
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
    assert inst.compose.include[0].concept[0].code == "proposal"
    assert inst.compose.include[0].concept[1].code == "plan"
    assert inst.compose.include[0].concept[2].code == "order"
    assert inst.compose.include[0].concept[3].code == "option"
    assert inst.compose.include[0].concept[4].code == "directive"
    assert inst.compose.include[0].system == "http://hl7.org/fhir/request-intent"
    assert inst.contact[0].telecom[0].system == "url"
    assert (
        inst.contact[0].telecom[0].value
        == "http://www.hl7.org/Special/committees/patientcare/"
    )
    assert inst.description == (
        "Codes indicating the degree of authority/intentionality "
        "associated with a care plan."
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "pc"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "care-plan-intent"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.150"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "CarePlanIntent"
    assert inst.publisher == "HL7 International - Patient Care WG"
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert inst.title == "Care Plan Intent"
    assert inst.url == "http://hl7.org/fhir/ValueSet/care-plan-intent"
    assert inst.version == "4.5.0"


def test_valueset_4(base_settings):
    """No. 4 tests collection for ValueSet.
    Test File: valueset-care-plan-intent.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-care-plan-intent.json"
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
    assert inst.compose.include[0].system == "http://snomed.info/sct"
    assert inst.compose.include[1].system == "http://loinc.org"
    assert (
        inst.compose.include[2].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://healthit.gov"
    assert inst.date == fhirtypes.DateTime.validate("2021-04-03T00:34:11+00:00")
    assert inst.description == (
        "The allowed codes for identifying the ISO 11179 ObjectClass "
        "for a particular data element if intended for "
        "registration/use within the U.S. Structured Data Capture "
        "(SDC) project."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.id == "dataelement-sdcobjectclass"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.910"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "DataElementSDCObjectClass"
    assert inst.publisher == "Office of the National Coordinator for Health IT"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "DataElement SDC Object Class"
    assert inst.url == "http://hl7.org/fhir/ValueSet/dataelement-sdcobjectclass"
    assert inst.version == "4.5.0"


def test_valueset_5(base_settings):
    """No. 5 tests collection for ValueSet.
    Test File: valueset-dataelement-sdcobjectclass.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-dataelement-sdcobjectclass.json"
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
    assert (
        inst.compose.include[0].system
        == "http://terminology.hl7.org/CodeSystem/communication-category"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == (
        "Codes for general categories of communications such as "
        "alerts, instructions, etc."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "pc"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "communication-category"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.172"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T11:34:11.075+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "CommunicationCategory"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CommunicationCategory"
    assert inst.url == "http://hl7.org/fhir/ValueSet/communication-category"
    assert inst.version == "4.5.0"


def test_valueset_6(base_settings):
    """No. 6 tests collection for ValueSet.
    Test File: valueset-communication-category.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-communication-category.json"
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
    assert inst.compose.include[0].system == (
        "http://terminology.hl7.org/CodeSystem/cited-artifact-" "classification-type"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-03-11T10:55:11.085+11:00")
    assert inst.description == "Cited Artifact Classification Type"
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "cds"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-classification"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 0
    assert inst.extension[3].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[3].valueCode == "trial-use"
    assert inst.id == "cited-artifact-classification-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.0"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T11:34:11.075+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "CitedArtifactClassificationType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CitedArtifactClassificationType"
    assert inst.url == (
        "http://hl7.org/fhir/ValueSet/cited-artifact-classification-" "type"
    )
    assert inst.version == "4.5.0"


def test_valueset_7(base_settings):
    """No. 7 tests collection for ValueSet.
    Test File: valueset-cited-artifact-classification-type.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-cited-artifact-classification-type.json"
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
    assert (
        inst.compose.include[0].system
        == "http://terminology.hl7.org/CodeSystem/paymentstatus"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.copyright == "This is an example set."
    assert inst.description == (
        "This value set includes a sample set of Payment Status " "codes."
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fm"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "payment-status"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.643"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "PaymentStatusCodes"
    assert inst.publisher == "Financial Management"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Payment Status Codes"
    assert inst.url == "http://hl7.org/fhir/ValueSet/payment-status"
    assert inst.version == "4.5.0"


def test_valueset_8(base_settings):
    """No. 8 tests collection for ValueSet.
    Test File: valueset-payment-status.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-payment-status.json"
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
    assert inst.compose.include[0].system == "http://www.ensembl.org"
    assert inst.compose.include[1].system == "http://www.ncbi.nlm.nih.gov/nuccore"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == "This value set includes all Reference codes"
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "cg"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "sequence-referenceSeq"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.221"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "ENSEMBL"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/sequence-referenceSeq"
    assert inst.version == "4.5.0"


def test_valueset_9(base_settings):
    """No. 9 tests collection for ValueSet.
    Test File: valueset-sequence-referenceSeq.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-sequence-referenceSeq.json"
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
    assert inst.compose.include[0].concept[0].code == "47545007"
    assert inst.compose.include[0].concept[0].designation[0].value == "CPAP"
    assert inst.compose.include[0].concept[0].display == (
        "Continuous positive airway pressure ventilation treatment " "(regime/therapy)"
    )
    assert inst.compose.include[0].concept[1].code == "286812008"
    assert inst.compose.include[0].concept[1].designation[0].value == "PCV"
    assert (
        inst.compose.include[0].concept[1].display
        == "Pressure controlled ventilation (procedure)"
    )
    assert inst.compose.include[0].concept[2].code == "243144002"
    assert inst.compose.include[0].concept[2].designation[0].value == "IPPB "
    assert (
        inst.compose.include[0].concept[2].display
        == "Patient triggered inspiratory assistance (procedure)"
    )
    assert inst.compose.include[0].concept[3].code == "243150007"
    assert inst.compose.include[0].concept[3].designation[0].value == "ACV"
    assert (
        inst.compose.include[0].concept[3].display
        == "Assisted controlled mandatory ventilation (procedure)"
    )
    assert inst.compose.include[0].concept[4].code == "59427005"
    assert inst.compose.include[0].concept[4].designation[0].value == "SIMV"
    assert (
        inst.compose.include[0].concept[4].display
        == "Synchronized intermittent mandatory ventilation (procedure)"
    )
    assert inst.compose.include[0].system == "http://snomed.info/sct"
    assert inst.contact[0].telecom[0].system == "url"
    assert (
        inst.contact[0].telecom[0].value
        == "http://www.hl7.org/Special/committees/orders/index.cfm"
    )
    assert inst.description == (
        "An example value set of Codified order entry details "
        "concepts.  These concepts only make sense in the context of "
        "what is being ordered.  This example is for a patient "
        "ventilation order"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "oo"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "servicerequest-orderdetail"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.435"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "ServiceRequestOrderDetailsCodes"
    assert inst.publisher == "Orders and Observations Workgroup"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Service Request Order Details Codes"
    assert inst.url == "http://hl7.org/fhir/ValueSet/servicerequest-orderdetail"
    assert inst.version == "4.5.0"


def test_valueset_10(base_settings):
    """No. 10 tests collection for ValueSet.
    Test File: valueset-servicerequest-orderdetail.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-servicerequest-orderdetail.json"
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
