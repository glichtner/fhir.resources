# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import bundle


def impl_bundle_1(inst):
    assert inst.entry[0].resource.id == "example"
    assert inst.entry[0].resource.meta.lastUpdated == fhirtypes.Instant.validate("2018-11-12T03:35:20.715Z")
    assert inst.entry[0].resource.meta.versionId == "1"
    assert inst.entry[0].response.etag == "W/1"
    assert inst.entry[0].response.lastModified == fhirtypes.Instant.validate("2018-11-12T03:35:20.717Z")
    assert inst.entry[0].response.status == "200"
    assert inst.entry[1].resource.id == "5bdf95d0-24a6-4024-95f5-d546fb479b"
    assert inst.entry[1].resource.meta.lastUpdated == fhirtypes.Instant.validate("2018-11-12T05:42:16.086Z")
    assert inst.entry[1].response.etag == "W/1"
    assert inst.entry[1].response.lastModified == fhirtypes.Instant.validate("2018-11-12T03:35:20.717Z")
    assert inst.entry[1].response.status == "200"
    assert inst.entry[2].resource.id == "0c11a91c-3638-4d58-8cf1-40e60f43c6"
    assert inst.entry[2].resource.meta.lastUpdated == fhirtypes.Instant.validate("2018-11-12T05:42:16.209Z")
    assert inst.entry[2].response.etag == "W/1"
    assert inst.entry[2].response.lastModified == fhirtypes.Instant.validate("2018-11-12T03:35:20.717Z")
    assert inst.entry[2].response.status == "200"
    assert inst.entry[3].resource.id == "19f0fa29-f8fe-4b07-b035-f488893f06"
    assert inst.entry[3].resource.meta.lastUpdated == fhirtypes.Instant.validate("2018-11-12T05:42:16.279Z")
    assert inst.entry[3].response.etag == "W/1"
    assert inst.entry[3].response.lastModified == fhirtypes.Instant.validate("2018-11-12T03:35:20.717Z")
    assert inst.entry[3].response.status == "200"
    assert inst.entry[4].resource.id == "dff8ab42-33f9-42ec-88c5-83d3f05323"
    assert inst.entry[4].resource.meta.lastUpdated == fhirtypes.Instant.validate("2018-11-12T05:42:16.351Z")
    assert inst.entry[4].response.etag == "W/1"
    assert inst.entry[4].response.lastModified == fhirtypes.Instant.validate("2018-11-12T03:35:20.717Z")
    assert inst.entry[4].response.status == "200"
    assert inst.id == "bundle-response-medsallergies"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.type == "batch-response"


def test_bundle_1(base_settings):
    """No. 1 tests collection for Bundle.
    Test File: bundle-response-medsallergies.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "bundle-response-medsallergies.json"
    )
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
    assert inst.entry[0].request.method == "GET"
    assert inst.entry[0].request.url == "/Patient/example"
    assert inst.entry[1].request.method == "GET"
    assert inst.entry[1].request.url == (
    "/MedicationStatement?patient=example&_list=$current-"
    "medications"
    )
    assert inst.entry[2].request.method == "GET"
    assert inst.entry[2].request.url == "/AllergyIntolerance?patient=example&_list=$current-allergies"
    assert inst.entry[3].request.method == "GET"
    assert inst.entry[3].request.url == "/Condition?patient=example&_list=$current-problems"
    assert inst.entry[4].request.method == "GET"
    assert inst.entry[4].request.url == "/MedicationStatement?patient=example&notgiven:not=true"
    assert inst.id == "bundle-request-medsallergies"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.type == "batch"


def test_bundle_2(base_settings):
    """No. 2 tests collection for Bundle.
    Test File: bundle-request-medsallergies.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "bundle-request-medsallergies.json"
    )
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
    assert inst.entry[0].fullUrl == "urn:uuid:231e7f38-2dd1-45ac-9161-d7bd87c403bd"
    assert inst.entry[0].resource.id == "231e7f38-2dd1-45ac-9161-d7bd87c403bd"
    assert inst.id == "54f808cf-d159-4c9b-accb-c33eb20f0ecc"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.timestamp == fhirtypes.Instant.validate("2020-04-17T10:24:13.1882432-05:00")
    assert inst.type == "subscription-notification"


def test_bundle_3(base_settings):
    """No. 3 tests collection for Bundle.
    Test File: notification-handshake.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "notification-handshake.json"
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
    assert inst.entry[0].fullUrl == "urn:uuid:c2d70315-c34c-4f44-981b-6f16775477f3"
    assert inst.entry[0].resource.id == "c2d70315-c34c-4f44-981b-6f16775477f3"
    assert inst.id == "40464b74-fad0-4f45-ab60-e67f949c5e92"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.timestamp == fhirtypes.Instant.validate("2020-04-17T10:24:13.1882432-05:00")
    assert inst.type == "subscription-notification"


def test_bundle_4(base_settings):
    """No. 4 tests collection for Bundle.
    Test File: notification-query-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "notification-query-status.json"
    )
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
    assert inst.entry[0].fullUrl == "https://example.com/base/DiagnosticReport/101"
    assert inst.entry[0].resource.id == "101"
    assert inst.entry[0].resource.meta.tag[0].code == "01"
    assert inst.entry[0].resource.meta.tag[0].display == "Needs Review"
    assert inst.entry[0].resource.meta.tag[0].system == "http://example.org/fhir/CodeSystem/workflow-codes"
    assert inst.entry[1].fullUrl == "https://example.com/base/Observation/r1"
    assert inst.entry[1].resource.id == "r1"
    assert inst.entry[2].fullUrl == "https://example.com/base/Observation/r2"
    assert inst.entry[2].resource.id == "r2"
    assert inst.entry[3].fullUrl == "https://example.com/base/Observation/r3"
    assert inst.entry[3].resource.id == "r3"
    assert inst.entry[4].fullUrl == "https://example.com/base/Observation/r4"
    assert inst.entry[4].resource.id == "r4"
    assert inst.entry[5].fullUrl == "https://example.com/base/Observation/r5"
    assert inst.entry[5].resource.id == "r5"
    assert inst.entry[6].fullUrl == "https://example.com/base/Observation/r6"
    assert inst.entry[6].resource.id == "r6"
    assert inst.entry[7].fullUrl == "https://example.com/base/Observation/r7"
    assert inst.entry[7].resource.id == "r7"
    assert inst.entry[8].fullUrl == "https://example.com/base/Observation/r8"
    assert inst.entry[8].resource.id == "r8"
    assert inst.entry[9].fullUrl == "https://example.com/base/Observation/r9"
    assert inst.entry[9].resource.id == "r9"
    assert inst.id == "101"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.type == "collection"


def test_bundle_5(base_settings):
    """No. 5 tests collection for Bundle.
    Test File: diagnosticreport-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example.json"
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
    assert inst.entry[0].fullUrl == "urn:uuid:dae6bdbc-71ab-4043-b11e-59b52bda60ad"
    assert inst.entry[0].resource.id == "dae6bdbc-71ab-4043-b11e-59b52bda60ad"
    assert inst.entry[1].fullUrl == "http://example.org/FHIR/R5/Encounter/2"
    assert inst.entry[1].request.method == "PUT"
    assert inst.entry[1].request.url == "Encounter/2"
    assert inst.entry[1].response.status == "201"
    assert inst.entry[2].fullUrl == "http://example.org/FHIR/R5/Patient/ABC"
    assert inst.entry[2].request.method == "GET"
    assert inst.entry[2].request.url == "Patient/ABC"
    assert inst.entry[2].response.status == "200"
    assert inst.id == "920a46b7-045a-4773-82bd-8e90c3e15653"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.timestamp == fhirtypes.Instant.validate("2020-04-17T10:24:13.1882432-05:00")
    assert inst.type == "subscription-notification"


def test_bundle_6(base_settings):
    """No. 6 tests collection for Bundle.
    Test File: notification-id-only-with-patient.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "notification-id-only-with-patient.json"
    )
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
    assert inst.entry[0].fullUrl == "https://example.com/base/DiagnosticReport/f202"
    assert inst.entry[0].resource.id == "f202"
    assert inst.entry[1].fullUrl == "https://example.com/base/ServiceRequest/req"
    assert inst.entry[1].resource.id == "req"
    assert inst.id == "f202"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.type == "collection"


def test_bundle_7(base_settings):
    """No. 7 tests collection for Bundle.
    Test File: diagnosticreport-example-f202-bloodculture.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example-f202-bloodculture.json"
    )
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
    assert inst.entry[0].fullUrl == "https://example.com/base/DiagnosticReport/lipids"
    assert inst.entry[0].resource.id == "lipids"
    assert inst.entry[1].fullUrl == "https://example.com/base/Observation/cholesterol"
    assert inst.entry[1].resource.id == "cholesterol"
    assert inst.entry[2].fullUrl == "https://example.com/base/Observation/triglyceride"
    assert inst.entry[2].resource.id == "triglyceride"
    assert inst.entry[3].fullUrl == "https://example.com/base/Observation/hdlcholesterol"
    assert inst.entry[3].resource.id == "hdlcholesterol"
    assert inst.entry[4].fullUrl == "https://example.com/base/Observation/ldlcholesterol"
    assert inst.entry[4].resource.id == "ldlcholesterol"
    assert inst.id == "lipids"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.type == "collection"


def test_bundle_8(base_settings):
    """No. 8 tests collection for Bundle.
    Test File: bundle-lipids.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "bundle-lipids.json"
    )
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
    assert inst.entry[0].fullUrl == "urn:uuid:b21e4fae-ce73-45cb-8e37-1e203362b2ae"
    assert inst.entry[0].resource.id == "b21e4fae-ce73-45cb-8e37-1e203362b2ae"
    assert inst.id == "e2c9dc20-615e-4603-9005-74deb209cbb0"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.timestamp == fhirtypes.Instant.validate("2020-04-17T10:24:13.1882432-05:00")
    assert inst.type == "subscription-notification"


def test_bundle_9(base_settings):
    """No. 9 tests collection for Bundle.
    Test File: notification-error.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "notification-error.json"
    )
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
    assert inst.id == "externals"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2023-03-26T15:21:02.749+11:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.type == "collection"


def test_bundle_10(base_settings):
    """No. 10 tests collection for Bundle.
    Test File: external-resources.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "external-resources.json"
    )
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