# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentReference
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import documentreference


def impl_documentreference_1(inst):
    assert inst.author[0].display == "G.E. Medical Systems"
    assert inst.content[0].attachment.contentType == "application/dicom"
    assert inst.content[0].attachment.height == 480
    assert inst.content[0].attachment.width == 640
    assert inst.content[0].identifier.system == "urn:dicom:uid"
    assert inst.content[0].identifier.type.text == "InstanceUID"
    assert inst.content[0].identifier.use == "official"
    assert inst.content[0].identifier.value == (
        "urn:oid:1.2.840.11361907579238403408700.3.1.04.1997032715003" "3"
    )
    assert inst.event[0].coding[0].code == "US"
    assert (
        inst.event[0].coding[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.event[1].coding[0].code == "399067008"
    assert inst.event[1].coding[0].display == "Lateral projection"
    assert inst.event[1].coding[0].system == "http://snomed.info/sct"
    assert inst.extension[0].url == "http://nema.org/fhir/extensions#0002-0010"
    assert inst.extension[0].valueUri == "urn:oid:1.2.840.10008.1.2.1"
    assert inst.id == "1.2.840.11361907579238403408700.3.1.04.19970327150033"
    assert inst.identifier[0].system == "http://acme-imaging.com/accession/2012"
    assert inst.identifier[0].type.text == "accessionNo"
    assert inst.identifier[0].value == "1234567"
    assert inst.identifier[1].system == "urn:dicom:uid"
    assert inst.identifier[1].type.text == "studyId"
    assert (
        inst.identifier[1].value
        == "urn:oid:1.2.840.113619.2.21.848.34082.0.538976288.3"
    )
    assert inst.identifier[2].system == "urn:dicom:uid"
    assert inst.identifier[2].type.text == "seriesId"
    assert (
        inst.identifier[2].value
        == "urn:oid:1.2.840.113619.2.21.3408.700.0.757923840.3.0"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_documentreference_1(base_settings):
    """No. 1 tests collection for DocumentReference.
    Test File: documentreference-example-dicom.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "documentreference-example-dicom.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_1(inst2)


def impl_documentreference_2(inst):
    assert inst.content[0].attachment.contentType == "image/jpeg"
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2016-03-15"
    )
    assert inst.content[0].attachment.height == 432
    assert (
        inst.content[0].attachment.url
        == "http://someimagingcenter.org/fhir/Binary/A12345"
    )
    assert inst.content[0].attachment.width == 640
    assert inst.content[0].id == "a1"
    assert inst.encounter[0].reference == "Encounter/example"
    assert inst.encounter[1].identifier.assigner.display == "XYZ Medical Clinic"
    assert (
        inst.encounter[1].identifier.system
        == "http://someclinic.org/fhir/NamingSystem/imaging-orders"
    )
    assert inst.encounter[1].identifier.value == "111222"
    assert inst.event[0].coding[0].code == "39714003"
    assert inst.event[0].coding[0].display == "Skeletal X-ray of wrist and hand"
    assert inst.event[0].coding[0].system == "http://snomed.info/sct"
    assert inst.event[1].coding[0].code == "85151006"
    assert inst.event[1].coding[0].display == "Structure of left hand (body structure)"
    assert inst.event[1].coding[0].system == "http://snomed.info/sct"
    assert inst.id == "xray"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Xray of left '
        "hand for Patient Henry Levin (MRN 12345) 2016-03-15</div>"
    )
    assert inst.text.status == "generated"


def test_documentreference_2(base_settings):
    """No. 2 tests collection for DocumentReference.
    Test File: documentreference-example-xray.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "documentreference-example-xray.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_2(inst2)


def impl_documentreference_3(inst):
    assert inst.author[0].reference == "Practitioner/xcda-author"
    assert inst.content[0].attachment.contentType == "audio/mpeg"
    assert inst.content[0].attachment.data == bytes_validator(
        "dG9vIGJpZyB0b28gaW5jbHVkZSB0aGUgd2hvbGU="
    )
    assert float(inst.content[0].attachment.duration) == float(65)
    assert inst.id == "sound"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Sound recording '
        "of speech example for Patient Henry Levin (MRN "
        '12345):<br/><img src="#11" alt="diagram"/></div>'
    )
    assert inst.text.status == "generated"


def test_documentreference_3(base_settings):
    """No. 3 tests collection for DocumentReference.
    Test File: documentreference-example-sound.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "documentreference-example-sound.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_3(inst2)


def impl_documentreference_4(inst):
    assert inst.attester[0].mode == "official"
    assert inst.attester[0].party.reference == "Organization/f001"
    assert inst.author[0].reference == "Practitioner/xcda1"
    assert inst.author[1].reference == "#a2"
    assert inst.category[0].coding[0].code == "History and Physical"
    assert inst.category[0].coding[0].display == "History and Physical"
    assert (
        inst.category[0].coding[0].system
        == "http://ihe.net/xds/connectathon/classCodes"
    )
    assert inst.contained[0].id == "a2"
    assert inst.content[0].attachment.contentType == "application/hl7-v3+xml"
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2005-12-24T09:35:00+11:00"
    )
    assert inst.content[0].attachment.hash == bytes_validator(
        "2jmj7l5rSw0yVb/vlWAYkK/YBwk="
    )
    assert inst.content[0].attachment.language == "en-US"
    # Don't know how to create unit test
    # for "content[0].attachment.size",
    # which is a Integer64
    assert inst.content[0].attachment.title == "Physical"
    assert inst.content[0].attachment.url == (
        "http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-ed" "b665c45510"
    )
    assert inst.content[0].format.code == "urn:ihe:pcc:handp:2008"
    assert inst.content[0].format.display == "History and Physical Specification"
    assert inst.content[0].format.system == "urn:oid:1.3.6.1.4.1.19376.1.2.3"
    assert inst.content[0].identifier.system == "urn:ietf:rfc:3986"
    assert inst.content[0].identifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7"
    assert inst.custodian.reference == "Organization/f001"
    assert inst.date == fhirtypes.Instant.validate("2005-12-24T09:43:41+11:00")
    assert inst.description == "Physical"
    assert inst.docStatus == "preliminary"
    assert inst.encounter[0].reference == "Encounter/xcda"
    assert inst.event[0].coding[0].code == "T-D8200"
    assert inst.event[0].coding[0].display == "Arm"
    assert (
        inst.event[0].coding[0].system == "http://ihe.net/xds/connectathon/eventCodes"
    )
    assert inst.facilityType.coding[0].code == "Outpatient"
    assert inst.facilityType.coding[0].display == "Outpatient"
    assert inst.facilityType.coding[0].system == (
        "http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCo" "des"
    )
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2004-12-23T08:01:00+11:00")
    assert inst.period.start == fhirtypes.DateTime.validate("2004-12-23T08:00:00+11:00")
    assert inst.practiceSetting.coding[0].code == "General Medicine"
    assert inst.practiceSetting.coding[0].display == "General Medicine"
    assert (
        inst.practiceSetting.coding[0].system
        == "http://www.ihe.net/xds/connectathon/practiceSettingCodes"
    )
    assert inst.related[0].identifier.system == "urn:ietf:rfc:3986"
    assert inst.related[0].identifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.2345"
    assert inst.related[0].reference == "Patient/xcda"
    assert inst.relatesTo[0].code == "appends"
    assert inst.relatesTo[0].target.reference == "DocumentReference/example"
    assert inst.securityLabel[0].coding[0].code == "V"
    assert inst.securityLabel[0].coding[0].display == "very restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.sourcePatientInfo.reference == "Patient/xcda"
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "34108-1"
    assert inst.type.coding[0].display == "Outpatient Note"
    assert inst.type.coding[0].system == "http://loinc.org"


def test_documentreference_4(base_settings):
    """No. 4 tests collection for DocumentReference.
    Test File: documentreference-example.json
    """
    filename = base_settings["unittest_data_dir"] / "documentreference-example.json"
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_4(inst2)


def impl_documentreference_5(inst):
    assert inst.author[0].reference == "Practitioner/xcda-author"
    assert inst.author[1].display == "Acme Camera"
    assert inst.content[0].attachment.contentType == "image/gif"
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2009-09-03"
    )
    assert inst.content[0].attachment.frames == 1
    assert inst.content[0].attachment.height == 145
    assert inst.content[0].attachment.width == 126
    assert inst.content[0].id == "a1"
    assert inst.date == fhirtypes.Instant.validate("2017-12-17T14:56:18Z")
    assert inst.id == "example-diagram"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "image"
    assert inst.type.coding[0].display == "Image"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/media-type"
    )


def test_documentreference_5(base_settings):
    """No. 5 tests collection for DocumentReference.
    Test File: documentreference-example-diagram.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "documentreference-example-diagram.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_5(inst2)
