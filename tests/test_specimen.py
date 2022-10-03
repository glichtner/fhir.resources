# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Specimen
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import specimen


def impl_specimen_1(inst):
    assert inst.accessionIdentifier.system == "http://lab.acme.org/specimens/2011"
    assert inst.accessionIdentifier.value == "X352356"
    assert inst.collection.bodySite.concept.coding[0].code == "49852007"
    assert inst.collection.bodySite.concept.coding[0].display == "Structure of median cubital vein (body structure)"
    assert inst.collection.bodySite.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate("2011-05-30T06:15:00Z")
    assert inst.collection.collector.reference == "Practitioner/example"
    assert inst.collection.method.coding[0].code == "LNV"
    assert inst.collection.method.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0488"
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(6)
    assert inst.container[0].device.reference == (
    "Specimen/specimen-device-container-example-green-gel-"
    "vacutainer"
    )
    assert inst.container[0].specimenQuantity.unit == "mL"
    assert float(inst.container[0].specimenQuantity.value) == float(3)
    assert inst.id == "101"
    assert inst.identifier[0].system == "http://ehr.acme.org/identifiers/collections"
    assert inst.identifier[0].value == "23234352356"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.note[0].text == "Specimen is grossly lipemic"
    assert inst.receivedTime == fhirtypes.DateTime.validate("2011-03-04T07:03:00Z")
    assert inst.request[0].reference == "ServiceRequest/example"
    assert inst.status == "available"
    assert inst.subject.display == "Peter Patient"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_1(base_settings):
    """No. 1 tests collection for Specimen.
    Test File: specimen-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "specimen-example.json"
    )
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_1(inst2)


def impl_specimen_2(inst):
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate("2021-01-01T01:01:00Z")
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert inst.collection.method.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0488"
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "specimenFather"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/specimens"
    assert inst.identifier[0].value == "7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.receivedTime == fhirtypes.DateTime.validate("2021-01-01T01:01:01Z")
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "John Doe"
    assert inst.subject.reference == "Patient/father"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_2(base_settings):
    """No. 2 tests collection for Specimen.
    Test File: Specimen-specimenFather.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Specimen-specimenFather.json"
    )
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_2(inst2)


def impl_specimen_3(inst):
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate("2021-01-01T01:01:00Z")
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert inst.collection.method.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0488"
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "specimenMother"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/specimens"
    assert inst.identifier[0].value == "6"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.receivedTime == fhirtypes.DateTime.validate("2021-01-01T01:01:01Z")
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "Jane Doe"
    assert inst.subject.reference == "Patient/mother"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_3(base_settings):
    """No. 3 tests collection for Specimen.
    Test File: Specimen-specimenMother.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Specimen-specimenMother.json"
    )
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_3(inst2)


def impl_specimen_4(inst):
    assert inst.accessionIdentifier.system == "https://vetmed.iastate.edu/vdl"
    assert inst.accessionIdentifier.value == "20171120-1234"
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate("2017-11-14")
    assert inst.collection.collector.display == "James Herriot, FRCVS"
    assert inst.combined == "pooled"
    assert inst.container[0].device.reference == (
    "Specimen/specimen-device-container-example-red-top-"
    "vacutainer"
    )
    assert inst.id == "pooled-serum"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.note[0].text == "Pooled serum sample from 30 individuals"
    assert inst.subject.reference == "Group/herd1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "Serum sample, pooled"
    assert inst.type.coding[0].display == "Serum sample, pooled"
    assert inst.type.coding[0].system == "https://vetmed.iastate.edu/vdl"
    assert inst.type.text == "Pooled serum sample"


def test_specimen_4(base_settings):
    """No. 4 tests collection for Specimen.
    Test File: specimen-example-pooled-serum.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "specimen-example-pooled-serum.json"
    )
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_4(inst2)


def impl_specimen_5(inst):
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate("2021-01-01T01:01:00Z")
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert inst.collection.method.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0488"
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "denovo-1"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/specimens"
    assert inst.identifier[0].value == "1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.receivedTime == fhirtypes.DateTime.validate("2021-01-01T01:01:01Z")
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "Child Junior Doe"
    assert inst.subject.reference == "Patient/denovoChild"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_5(base_settings):
    """No. 5 tests collection for Specimen.
    Test File: Specimen-denovo-1.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Specimen-denovo-1.json"
    )
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_5(inst2)


def impl_specimen_6(inst):
    assert inst.accessionIdentifier.system == "http://lab.acme.org/specimens/2011"
    assert inst.accessionIdentifier.value == "X352356-ISO1"
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate("2015-08-16T07:03:00Z")
    assert inst.collection.collector.reference == "Practitioner/f202"
    assert inst.collection.method.coding[0].code == "BAP"
    assert inst.collection.method.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0488"
    assert inst.contained[0].id == "stool"
    assert inst.id == "isolate"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.note[0].text == "Patient dropped off specimen"
    assert inst.parent[0].reference == "#stool"
    assert inst.receivedTime == fhirtypes.DateTime.validate("2015-08-18T07:03:00Z")
    assert inst.role[0].coding[0].code == "p"
    assert inst.role[0].coding[0].display == "Patient"
    assert inst.status == "available"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "429951000124103"
    assert inst.type.coding[0].display == "Bacterial isolate specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_6(base_settings):
    """No. 6 tests collection for Specimen.
    Test File: specimen-example-isolate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "specimen-example-isolate.json"
    )
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_6(inst2)


def impl_specimen_7(inst):
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate("2021-01-01T01:01:00Z")
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert inst.collection.method.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0488"
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "denovo-3"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/specimens"
    assert inst.identifier[0].value == "3"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.receivedTime == fhirtypes.DateTime.validate("2021-01-01T01:01:01Z")
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "John Doe"
    assert inst.subject.reference == "Patient/denovoFather"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_7(base_settings):
    """No. 7 tests collection for Specimen.
    Test File: Specimen-denovo-3.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Specimen-denovo-3.json"
    )
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_7(inst2)


def impl_specimen_8(inst):
    assert inst.accessionIdentifier.system == "http://acme.com/labs/accession-ids"
    assert inst.accessionIdentifier.value == "20150816-00124"
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate("2015-08-16T06:40:17Z")
    assert inst.collection.collector.reference == "Practitioner/f202"
    assert inst.container[0].device.reference == "Specimen/specimen-device-container-example-sst-vacutainer"
    assert inst.id == "sst"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.request[0].reference == "ServiceRequest/ft4"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "119364003"
    assert inst.type.coding[0].display == "Serum sample"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_8(base_settings):
    """No. 8 tests collection for Specimen.
    Test File: specimen-example-serum.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "specimen-example-serum.json"
    )
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_8(inst2)


def impl_specimen_9(inst):
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate("2019-03-01T01:01:00Z")
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "129314006"
    assert inst.collection.method.coding[0].display == "Biopsy - action"
    assert inst.collection.method.coding[0].system == "http://snomed.info/sct"
    assert inst.collection.quantity.unit == "mm2"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "genomicSpecimen"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/specimens"
    assert inst.identifier[0].value == "4"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.receivedTime == fhirtypes.DateTime.validate("2019-03-01T01:01:01Z")
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "John Doe"
    assert inst.subject.reference == "Patient/genomicPatient"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122610009"
    assert inst.type.coding[0].display == "Specimen from lung obtained by biopsy (specimen) "
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_9(base_settings):
    """No. 9 tests collection for Specimen.
    Test File: Specimen-genomicSpecimen.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Specimen-genomicSpecimen.json"
    )
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_9(inst2)


def impl_specimen_10(inst):
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate("2021-01-01T01:01:00Z")
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert inst.collection.method.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0488"
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "specimenProband"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/specimens"
    assert inst.identifier[0].value == "5"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.receivedTime == fhirtypes.DateTime.validate("2021-01-01T01:01:01Z")
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "Child Junior Doe"
    assert inst.subject.reference == "Patient/proband"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_10(base_settings):
    """No. 10 tests collection for Specimen.
    Test File: Specimen-specimenProband.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Specimen-specimenProband.json"
    )
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_10(inst2)