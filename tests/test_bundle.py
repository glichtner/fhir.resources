# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import bundle


def impl_bundle_1(inst):
    assert inst.entry[0].fullUrl == "urn:uuid:267b18ce-3d37-4581-9baa-6fada338038b"
    assert inst.entry[0].resource.id == "267b18ce-3d37-4581-9baa-6fada338038b"
    assert inst.entry[1].fullUrl == "http://acme.com/ehr/fhir/Patient/pat1"
    assert inst.entry[1].resource.id == "pat1"
    assert inst.entry[2].fullUrl == "http://acme.com/ehr/fhir/Patient/pat12"
    assert inst.entry[2].resource.id == "pat2"
    assert inst.id == "10bb101f-a121-4264-a920-67be9cb82c74"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.timestamp == fhirtypes.Instant.validate("2015-07-14T11:15:33+10:00")
    assert inst.type == "message"


def test_bundle_1(base_settings):
    """No. 1 tests collection for Bundle.
    Test File: message-request-link.json
    """
    filename = base_settings["unittest_data_dir"] / "message-request-link.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_1(inst2)


def impl_bundle_2(inst):
    assert inst.entry[0].fullUrl == "http://hl7.org/fhir/Location/2"
    assert inst.entry[0].resource.id == "2"
    assert inst.entry[1].fullUrl == "http://hl7.org/fhir/Location/3"
    assert inst.entry[1].resource.id == "3"
    assert inst.id == "3ad0687e-f477-468c-afd5-fcc2bf897819"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.type == "collection"


def test_bundle_2(base_settings):
    """No. 2 tests collection for Bundle.
    Test File: location-examples-general.json
    """
    filename = base_settings["unittest_data_dir"] / "location-examples-general.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_2(inst2)


def impl_bundle_3(inst):
    assert inst.entry[0].fullUrl == (
        "http://fhir.healthintersections.com.au/open/Composition/180f"
        "219f-97a8-486d-99d9-ed631fe4fc57"
    )
    assert inst.entry[0].resource.id == "180f219f-97a8-486d-99d9-ed631fe4fc57"
    assert inst.entry[0].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-05-28T22:12:21Z"
    )
    assert inst.entry[1].fullUrl == (
        "http://fhir.healthintersections.com.au/open/Practitioner/exa" "mple"
    )
    assert inst.entry[1].resource.id == "example"
    assert inst.entry[1].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-05-05T16:13:03Z"
    )
    assert (
        inst.entry[2].fullUrl
        == "http://fhir.healthintersections.com.au/open/Patient/d1"
    )
    assert inst.entry[2].resource.id == "d1"
    assert inst.entry[3].fullUrl == (
        "http://fhir.healthintersections.com.au/open/Encounter/doc-" "example"
    )
    assert inst.entry[3].resource.id == "doc-example"
    assert inst.entry[3].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-05-05T16:13:03Z"
    )
    assert inst.entry[4].fullUrl == "urn:uuid:541a72a8-df75-4484-ac89-ac4923f03b81"
    assert inst.entry[4].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-05-05T16:13:03Z"
    )
    assert inst.entry[5].fullUrl == "urn:uuid:124a6916-5d84-4b8c-b250-10cefb8e6e86"
    assert inst.entry[5].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-05-05T16:13:03Z"
    )
    assert inst.entry[6].fullUrl == "urn:uuid:673f8db5-0ffd-4395-9657-6da00420bbc1"
    assert inst.entry[7].fullUrl == "urn:uuid:47600e0f-b6b5-4308-84b5-5dec157f7637"
    assert inst.entry[7].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-05-05T16:13:03Z"
    )
    assert inst.id == "father"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:uuid:0c3151bd-1cbf-4d64-b04d-cd9187a4c6e0"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2013-05-28T22:12:21Z")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.signature.onBehalfOf.reference == "Organization/example"
    assert inst.signature.sigFormat == "image/jpg"
    assert inst.signature.type[0].code == "1.2.840.10065.1.12.1.1"
    assert inst.signature.type[0].display == "Author's Signature"
    assert inst.signature.type[0].system == "urn:iso-astm:E1762-95:2013"
    assert inst.signature.when == fhirtypes.Instant.validate(
        "2015-08-31T07:42:33+10:00"
    )
    assert inst.signature.who.reference == "Device/software"
    assert inst.type == "document"


def test_bundle_3(base_settings):
    """No. 3 tests collection for Bundle.
    Test File: document-example-dischargesummary.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "document-example-dischargesummary.json"
    )
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_3(inst2)


def impl_bundle_4(inst):
    assert (
        inst.entry[0].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/shareablemeasure"
    )
    assert inst.entry[0].resource.id == "shareablemeasure"
    assert (
        inst.entry[1].fullUrl == "http://hl7.org/fhir/StructureDefinition/actualgroup"
    )
    assert inst.entry[1].resource.id == "actualgroup"
    assert (
        inst.entry[2].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/groupdefinition"
    )
    assert inst.entry[2].resource.id == "groupdefinition"
    assert inst.entry[3].fullUrl == (
        "http://hl7.org/fhir/StructureDefinition/familymemberhistory-" "genetic"
    )
    assert inst.entry[3].resource.id == "familymemberhistory-genetic"
    assert inst.entry[4].fullUrl == (
        "http://hl7.org/fhir/StructureDefinition/shareableactivitydef" "inition"
    )
    assert inst.entry[4].resource.id == "shareableactivitydefinition"
    assert (
        inst.entry[5].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/cdshooksrequestgroup"
    )
    assert inst.entry[5].resource.id == "cdshooksrequestgroup"
    assert inst.entry[6].fullUrl == (
        "http://hl7.org/fhir/StructureDefinition/provenance-relevant-" "history"
    )
    assert inst.entry[6].resource.id == "provenance-relevant-history"
    assert (
        inst.entry[7].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/cqf-questionnaire"
    )
    assert inst.entry[7].resource.id == "cqf-questionnaire"
    assert (
        inst.entry[8].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.entry[8].resource.id == "shareablevalueset"
    assert (
        inst.entry[9].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/vsd-alignedvalueset"
    )
    assert inst.entry[9].resource.id == "vsd-alignedvalueset"
    assert inst.id == "profiles-others"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.type == "collection"


def test_bundle_4(base_settings):
    """No. 4 tests collection for Bundle.
    Test File: profiles-others.json
    """
    filename = base_settings["unittest_data_dir"] / "profiles-others.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_4(inst2)


def impl_bundle_5(inst):
    assert inst.entry[0].fullUrl == "https://example.com/base/DiagnosticReport/f202"
    assert inst.entry[0].resource.id == "f202"
    assert inst.entry[1].fullUrl == "https://example.com/base/ServiceRequest/req"
    assert inst.entry[1].resource.id == "req"
    assert inst.id == "f202"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.type == "collection"


def test_bundle_5(base_settings):
    """No. 5 tests collection for Bundle.
    Test File: diagnosticreport-example-f202-bloodculture.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "diagnosticreport-example-f202-bloodculture.json"
    )
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_5(inst2)


def impl_bundle_6(inst):
    assert inst.entry[0].resource.id == "example"
    assert inst.entry[0].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2018-11-12T03:35:20.715Z"
    )
    assert inst.entry[0].resource.meta.versionId == "1"
    assert inst.entry[0].response.etag == "W/1"
    assert inst.entry[0].response.lastModified == fhirtypes.Instant.validate(
        "2018-11-12T03:35:20.717Z"
    )
    assert inst.entry[0].response.status == "200"
    assert inst.entry[1].resource.id == "5bdf95d0-24a6-4024-95f5-d546fb479b"
    assert inst.entry[1].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2018-11-12T05:42:16.086Z"
    )
    assert inst.entry[1].response.etag == "W/1"
    assert inst.entry[1].response.lastModified == fhirtypes.Instant.validate(
        "2018-11-12T03:35:20.717Z"
    )
    assert inst.entry[1].response.status == "200"
    assert inst.entry[2].resource.id == "0c11a91c-3638-4d58-8cf1-40e60f43c6"
    assert inst.entry[2].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2018-11-12T05:42:16.209Z"
    )
    assert inst.entry[2].response.etag == "W/1"
    assert inst.entry[2].response.lastModified == fhirtypes.Instant.validate(
        "2018-11-12T03:35:20.717Z"
    )
    assert inst.entry[2].response.status == "200"
    assert inst.entry[3].resource.id == "19f0fa29-f8fe-4b07-b035-f488893f06"
    assert inst.entry[3].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2018-11-12T05:42:16.279Z"
    )
    assert inst.entry[3].response.etag == "W/1"
    assert inst.entry[3].response.lastModified == fhirtypes.Instant.validate(
        "2018-11-12T03:35:20.717Z"
    )
    assert inst.entry[3].response.status == "200"
    assert inst.entry[4].resource.id == "dff8ab42-33f9-42ec-88c5-83d3f05323"
    assert inst.entry[4].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2018-11-12T05:42:16.351Z"
    )
    assert inst.entry[4].response.etag == "W/1"
    assert inst.entry[4].response.lastModified == fhirtypes.Instant.validate(
        "2018-11-12T03:35:20.717Z"
    )
    assert inst.entry[4].response.status == "200"
    assert inst.id == "bundle-response-medsallergies"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.type == "batch-response"


def test_bundle_6(base_settings):
    """No. 6 tests collection for Bundle.
    Test File: bundle-response-medsallergies.json
    """
    filename = base_settings["unittest_data_dir"] / "bundle-response-medsallergies.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_6(inst2)


def impl_bundle_7(inst):
    assert inst.entry[0].fullUrl == "http://hl7.org/fhir/StructureDefinition/Element"
    assert inst.entry[0].resource.id == "Element"
    assert inst.entry[0].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.entry[1].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/BackboneElement"
    )
    assert inst.entry[1].resource.id == "BackboneElement"
    assert inst.entry[1].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert (
        inst.entry[2].fullUrl == "http://hl7.org/fhir/StructureDefinition/base64Binary"
    )
    assert inst.entry[2].resource.id == "base64Binary"
    assert inst.entry[2].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.entry[3].fullUrl == "http://hl7.org/fhir/StructureDefinition/boolean"
    assert inst.entry[3].resource.id == "boolean"
    assert inst.entry[3].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.entry[4].fullUrl == "http://hl7.org/fhir/StructureDefinition/canonical"
    assert inst.entry[4].resource.id == "canonical"
    assert inst.entry[4].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.entry[5].fullUrl == "http://hl7.org/fhir/StructureDefinition/code"
    assert inst.entry[5].resource.id == "code"
    assert inst.entry[5].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.entry[6].fullUrl == "http://hl7.org/fhir/StructureDefinition/date"
    assert inst.entry[6].resource.id == "date"
    assert inst.entry[6].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.entry[7].fullUrl == "http://hl7.org/fhir/StructureDefinition/dateTime"
    assert inst.entry[7].resource.id == "dateTime"
    assert inst.entry[7].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.entry[8].fullUrl == "http://hl7.org/fhir/StructureDefinition/decimal"
    assert inst.entry[8].resource.id == "decimal"
    assert inst.entry[8].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.entry[9].fullUrl == "http://hl7.org/fhir/StructureDefinition/id"
    assert inst.entry[9].resource.id == "id"
    assert inst.entry[9].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.id == "types"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.type == "collection"


def test_bundle_7(base_settings):
    """No. 7 tests collection for Bundle.
    Test File: profiles-types.json
    """
    filename = base_settings["unittest_data_dir"] / "profiles-types.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_7(inst2)


def impl_bundle_8(inst):
    assert inst.entry[0].fullUrl == "http://hl7.org/fhir/NamingSystem/dicom-uid"
    assert inst.entry[0].resource.id == "dicom-uid"
    assert inst.entry[1].fullUrl == "http://hl7.org/fhir/NamingSystem/us-ssn"
    assert inst.entry[1].resource.id == "us-ssn"
    assert inst.entry[2].fullUrl == "http://hl7.org/fhir/NamingSystem/us-medicare"
    assert inst.entry[2].resource.id == "us-medicare"
    assert inst.entry[3].fullUrl == "http://hl7.org/fhir/NamingSystem/us-mbi"
    assert inst.entry[3].resource.id == "us-mbi"
    assert inst.entry[4].fullUrl == "http://hl7.org/fhir/NamingSystem/us-npi"
    assert inst.entry[4].resource.id == "us-npi"
    assert inst.entry[5].fullUrl == "http://hl7.org/fhir/NamingSystem/gtin"
    assert inst.entry[5].resource.id == "gtin"
    assert inst.entry[6].fullUrl == "http://hl7.org/fhir/NamingSystem/4.3.2"
    assert inst.entry[6].resource.id == "4.3.2"
    assert inst.entry[7].fullUrl == "http://hl7.org/fhir/NamingSystem/4.3.1"
    assert inst.entry[7].resource.id == "4.3.1"
    assert inst.entry[8].fullUrl == "http://hl7.org/fhir/NamingSystem/4.3.5"
    assert inst.entry[8].resource.id == "4.3.5"
    assert inst.entry[9].fullUrl == "http://hl7.org/fhir/NamingSystem/4.3.4"
    assert inst.entry[9].resource.id == "4.3.4"
    assert inst.id == "registry"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.type == "collection"


def test_bundle_8(base_settings):
    """No. 8 tests collection for Bundle.
    Test File: namingsystem-registry.json
    """
    filename = base_settings["unittest_data_dir"] / "namingsystem-registry.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_8(inst2)


def impl_bundle_9(inst):
    assert (
        inst.entry[0].fullUrl
        == "http://hl7.org/fhir/ConceptMap/cm-administrative-gender-v2"
    )
    assert inst.entry[0].resource.id == "cm-administrative-gender-v2"
    assert (
        inst.entry[1].fullUrl
        == "http://hl7.org/fhir/ConceptMap/cm-administrative-gender-v3"
    )
    assert inst.entry[1].resource.id == "cm-administrative-gender-v3"
    assert (
        inst.entry[2].fullUrl
        == "http://hl7.org/fhir/ConceptMap/cm-data-absent-reason-v3"
    )
    assert inst.entry[2].resource.id == "cm-data-absent-reason-v3"
    assert inst.entry[3].fullUrl == (
        "http://hl7.org/fhir/ConceptMap/cm-document-reference-" "status-v3"
    )
    assert inst.entry[3].resource.id == "cm-document-reference-status-v3"
    assert inst.entry[4].fullUrl == "http://hl7.org/fhir/ConceptMap/cm-name-use-v2"
    assert inst.entry[4].resource.id == "cm-name-use-v2"
    assert inst.entry[5].fullUrl == "http://hl7.org/fhir/ConceptMap/cm-name-use-v3"
    assert inst.entry[5].resource.id == "cm-name-use-v3"
    assert inst.entry[6].fullUrl == "http://hl7.org/fhir/ConceptMap/cm-address-use-v2"
    assert inst.entry[6].resource.id == "cm-address-use-v2"
    assert inst.entry[7].fullUrl == "http://hl7.org/fhir/ConceptMap/cm-address-use-v3"
    assert inst.entry[7].resource.id == "cm-address-use-v3"
    assert inst.entry[8].fullUrl == "http://hl7.org/fhir/ConceptMap/cm-address-type-v3"
    assert inst.entry[8].resource.id == "cm-address-type-v3"
    assert (
        inst.entry[9].fullUrl
        == "http://hl7.org/fhir/ConceptMap/cm-contact-point-system-v2"
    )
    assert inst.entry[9].resource.id == "cm-contact-point-system-v2"
    assert inst.id == "conceptmaps"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2021-04-03T00:34:11.075+00:00"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.type == "collection"


def test_bundle_9(base_settings):
    """No. 9 tests collection for Bundle.
    Test File: conceptmaps.json
    """
    filename = base_settings["unittest_data_dir"] / "conceptmaps.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_9(inst2)


def impl_bundle_10(inst):
    assert inst.entry[0].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-sct"
    assert inst.entry[0].resource.id == "tx-sct"
    assert inst.entry[1].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-rxnorm"
    assert inst.entry[1].resource.id == "tx-rxnorm"
    assert inst.entry[2].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-loinc"
    assert inst.entry[2].resource.id == "tx-loinc"
    assert inst.entry[3].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-ucum"
    assert inst.entry[3].resource.id == "tx-ucum"
    assert inst.entry[4].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-nci"
    assert inst.entry[4].resource.id == "tx-nci"
    assert inst.entry[5].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-cpt"
    assert inst.entry[5].resource.id == "tx-cpt"
    assert inst.entry[6].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-ndf-rt"
    assert inst.entry[6].resource.id == "tx-ndf-rt"
    assert inst.entry[7].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-unii"
    assert inst.entry[7].resource.id == "tx-unii"
    assert inst.entry[8].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-ndc"
    assert inst.entry[8].resource.id == "tx-ndc"
    assert inst.entry[9].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-cvx"
    assert inst.entry[9].resource.id == "tx-cvx"
    assert inst.id == "terminologies"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.type == "collection"


def test_bundle_10(base_settings):
    """No. 10 tests collection for Bundle.
    Test File: namingsystem-terminologies.json
    """
    filename = base_settings["unittest_data_dir"] / "namingsystem-terminologies.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_10(inst2)
