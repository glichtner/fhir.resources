# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import device


def impl_device_1(inst):
    assert inst.conformsTo[0].specification.coding[0].code == "528388"
    assert inst.conformsTo[0].specification.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.conformsTo[0].specification.text == "MDC_DEV_SPEC_PROFILE_PULS_OXIM: Pulse Oximeter"
    assert inst.conformsTo[0].version == "1"
    assert inst.id == "NoninBlePulseOx"
    assert inst.identifier[0].system == "urn:oid:1.2.840.10004.1.1.1.0.0.1.0.0.1.2680"
    assert inst.identifier[0].type.coding[0].code == "SYSID"
    assert inst.identifier[0].type.coding[0].display == "System Identifier"
    assert inst.identifier[0].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifi"
    "ers"
    )
    assert inst.identifier[0].value == "74-E8-FF-FE-FF-05-1C-00"
    assert inst.identifier[1].system == "http://hl7.org/fhir/sid/eui-48"
    assert inst.identifier[1].type.coding[0].code == "BTMAC"
    assert inst.identifier[1].type.coding[0].display == "Bluetooth Address"
    assert inst.identifier[1].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifi"
    "ers"
    )
    assert inst.identifier[1].value == "00-1C-05-FF-E8-74"
    assert inst.manufacturer == "Nonin_Medical_Inc."
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.modelNumber == "Model 3230"
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "Nonin3230_501900083"
    assert inst.property[0].type.coding[0].code == "532353"
    assert inst.property[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[0].type.text == (
    "MDC_REG_CERT_DATA_CONTINUA_CERT_DEV_LIST: Continua certified"
    " device list"
    )
    assert inst.property[0].valueCodeableConcept.coding[0].code == "4"
    assert inst.property[0].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/ContinuaPAN"
    assert inst.property[1].type.coding[0].code == "532354.0"
    assert inst.property[1].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[1].type.text == "regulation-status"
    assert inst.property[1].valueCodeableConcept.coding[0].code == "N"
    assert inst.property[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[1].valueCodeableConcept.text == "Device is Regulated"
    assert inst.property[2].type.coding[0].code == "68220"
    assert inst.property[2].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[2].type.text == "MDC_TIME_SYNC_PROTOCOL: Time synchronization protocol"
    assert inst.property[2].valueCodeableConcept.coding[0].code == "532224"
    assert inst.property[2].valueCodeableConcept.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[2].valueCodeableConcept.text == "MDC_TIME_SYNC_NONE: No time synchronization"
    assert inst.property[3].type.coding[0].code == "68219.0"
    assert inst.property[3].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[3].type.text == "mds-time-capab-real-time-clock"
    assert inst.property[3].valueCodeableConcept.coding[0].code == "Y"
    assert inst.property[3].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[3].valueCodeableConcept.text == "real time clock supported"
    assert inst.property[4].type.coding[0].code == "68219.1"
    assert inst.property[4].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[4].type.text == "mds-time-capab-set-clock"
    assert inst.property[4].valueCodeableConcept.coding[0].code == "Y"
    assert inst.property[4].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[4].valueCodeableConcept.text == "setting the time supported"
    assert inst.serialNumber == "501900083"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "65573"
    assert inst.type[0].coding[0].display == "MDC_MOC_VMS_MDS_SIMP"
    assert inst.type[0].coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.type[0].text == "MDC_MOC_VMS_MDS_SIMP: Personal Health Device"
    assert inst.udiCarrier[0].carrierHRF == "(01)120359741556(21)501900083"
    assert inst.udiCarrier[0].deviceIdentifier == "120359741556"
    assert inst.udiCarrier[0].entryType == "unknown"
    assert inst.udiCarrier[0].issuer == "http://hl7.org/fhir/NamingSystem/gs1-di"
    assert inst.udiCarrier[0].jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"
    assert inst.version[0].type.coding[0].code == "531976"
    assert inst.version[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[0].type.text == "MDC_ID_PROD_SPEC_FW: Firmware revision"
    assert inst.version[0].value == "r2.1"
    assert inst.version[1].type.coding[0].code == "531975"
    assert inst.version[1].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[1].type.text == "MDC_ID_PROD_SPEC_SW: Software revision"
    assert inst.version[1].value == "r1.5 9.7"
    assert inst.version[2].type.coding[0].code == "531974"
    assert inst.version[2].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[2].type.text == "MDC_ID_PROD_SPEC_HW: Hardware revision"
    assert inst.version[2].value == "r1.0"
    assert inst.version[3].type.coding[0].code == "532352"
    assert inst.version[3].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[3].type.text == "MDC_REG_CERT_DATA_CONTINUA_VERSION: Continua version"
    assert inst.version[3].value == "6.0"


def test_device_1(base_settings):
    """No. 1 tests collection for Device.
    Test File: device-example-NoninBlePulseOx.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-NoninBlePulseOx.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_1(inst2)


def impl_device_2(inst):
    assert inst.contact[0].system == "url"
    assert inst.contact[0].value == "http://acme.com"
    assert inst.id == "example-software"
    assert inst.identifier[0].system == "http://acme.com/ehr/client-ids"
    assert inst.identifier[0].value == "goodhealth"
    assert inst.manufacturer == "Acme Devices, Inc"
    assert inst.text.status == "generated"
    assert inst.type[0].text == "EHR"
    assert inst.url == "http://acme.com/goodhealth/ehr/"
    assert inst.version[0].value == "10.23-23423"


def test_device_2(base_settings):
    """No. 2 tests collection for Device.
    Test File: device-example-software.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-software.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_2(inst2)


def impl_device_3(inst):
    assert inst.conformsTo[0].specification.coding[0].code == "528391"
    assert inst.conformsTo[0].specification.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.conformsTo[0].specification.text == "MDC_DEV_SPEC_PROFILE_BP: Blood Pressure meter"
    assert inst.conformsTo[0].version == "1"
    assert inst.id == "and20601bpmonitor"
    assert inst.identifier[0].system == "urn:oid:1.2.840.10004.1.1.1.0.0.1.0.0.1.2680"
    assert inst.identifier[0].type.coding[0].code == "SYSID"
    assert inst.identifier[0].type.coding[0].display == "System Identifier"
    assert inst.identifier[0].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifi"
    "ers"
    )
    assert inst.identifier[0].value == "00-09-1F-FF-FE-80-07-3A"
    assert inst.identifier[1].system == "http://hl7.org/fhir/sid/eui-48"
    assert inst.identifier[1].type.coding[0].code == "BTMAC"
    assert inst.identifier[1].type.coding[0].display == "Bluetooth Address"
    assert inst.identifier[1].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifi"
    "ers"
    )
    assert inst.identifier[1].value == "00-09-1F-80-07-3A"
    assert inst.manufacturer == "A&D Medical"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.modelNumber == "UA-767PBT-C"
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "AND BP UA-767PBT-C"
    assert inst.property[0].type.coding[0].code == "532353"
    assert inst.property[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[0].type.text == (
    "MDC_REG_CERT_DATA_CONTINUA_CERT_DEV_LIST: Continua certified"
    " device list"
    )
    assert inst.property[0].valueCodeableConcept.coding[0].code == "7"
    assert inst.property[0].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/ContinuaPAN"
    assert inst.property[1].type.coding[0].code == "532354.0"
    assert inst.property[1].type.coding[0].display == "regulation-status"
    assert inst.property[1].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[1].valueCodeableConcept.coding[0].code == "N"
    assert inst.property[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[1].valueCodeableConcept.text == "Device is Regulated"
    assert inst.property[2].type.coding[0].code == "68220"
    assert inst.property[2].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[2].type.text == "MDC_TIME_SYNC_PROTOCOL: Time synchronization protocol"
    assert inst.property[2].valueCodeableConcept.coding[0].code == "532224"
    assert inst.property[2].valueCodeableConcept.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[2].valueCodeableConcept.text == "MDC_TIME_SYNC_NONE: No time synchronization"
    assert inst.property[3].type.coding[0].code == "68219.0"
    assert inst.property[3].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[3].type.text == "mds-time-capab-real-time-clock"
    assert inst.property[3].valueCodeableConcept.coding[0].code == "Y"
    assert inst.property[3].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[3].valueCodeableConcept.text == "real time clock supported"
    assert inst.property[4].type.coding[0].code == "68219.1"
    assert inst.property[4].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[4].type.text == "mds-time-capab-set-clock"
    assert inst.property[4].valueCodeableConcept.coding[0].code == "Y"
    assert inst.property[4].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[4].valueCodeableConcept.text == "setting the time supported"
    assert inst.property[5].type.coding[0].code == "68219.11"
    assert inst.property[5].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[5].type.text == "mds-time-mgr-set-time"
    assert inst.property[5].valueCodeableConcept.coding[0].code == "Y"
    assert inst.property[5].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[5].valueCodeableConcept.text == "manager requested to set the time"
    assert inst.serialNumber == "5091100966"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "65573"
    assert inst.type[0].coding[0].display == "MDC_MOC_VMS_MDS_SIMP"
    assert inst.type[0].coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.type[0].text == "MDC_MOC_VMS_MDS_SIMP: Personal Health Device"
    assert inst.udiCarrier[0].carrierHRF == "(01)39183189818(21)5091100966"
    assert inst.udiCarrier[0].deviceIdentifier == "39183189818"
    assert inst.udiCarrier[0].entryType == "unknown"
    assert inst.udiCarrier[0].issuer == "http://hl7.org/fhir/NamingSystem/gs1-di"
    assert inst.udiCarrier[0].jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"
    assert inst.version[0].type.coding[0].code == "532352"
    assert inst.version[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[0].type.text == "MDC_REG_CERT_DATA_CONTINUA_VERSION: Continua version"
    assert inst.version[0].value == "1.0"


def test_device_3(base_settings):
    """No. 3 tests collection for Device.
    Test File: device-example-AND20601BPMonitor.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-AND20601BPMonitor.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_3(inst2)


def impl_device_4(inst):
    assert inst.displayName == "100mL Sterile Polycup"
    assert inst.id == "device-example-specimen-container-polycup"
    assert inst.identifier[0].system == "http://acme.com/containers/id"
    assert inst.identifier[0].value == "345675"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.property[0].type.coding[0].code == "container-type"
    assert inst.property[0].type.coding[0].display == "Container Type"
    assert inst.property[0].type.coding[0].system == "http://acme.com/containers/codes"
    assert inst.property[0].valueCodeableConcept.coding[0].code == "100mlcup"
    assert inst.property[0].valueCodeableConcept.coding[0].display == "100 mL Sterile Polycup"
    assert inst.property[0].valueCodeableConcept.coding[0].system == "http://acme.com/containers/types"
    assert inst.property[1].type.coding[0].code == "amount"
    assert inst.property[1].type.coding[0].display == "Amount"
    assert inst.property[1].type.coding[0].system == "http://acme.com/containers/codes"
    assert inst.property[1].valueCodeableConcept.coding[0].code == "100mL"
    assert inst.property[1].valueCodeableConcept.coding[0].display == "100 mL"
    assert inst.property[1].valueCodeableConcept.coding[0].system == "http://acme.com/containers/capacities"
    assert inst.text.status == "generated"


def test_device_4(base_settings):
    """No. 4 tests collection for Device.
    Test File: device-example-specimen-container-polycup.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-specimen-container-polycup.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_4(inst2)


def impl_device_5(inst):
    assert inst.expirationDate == fhirtypes.DateTime.validate("2020-02-02")
    assert inst.id == "example-udi3"
    assert inst.identifier[0].type.coding[0].code == "SNO"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].value == "XYZ456789012345678"
    assert inst.lotNumber == "LOT123456789012345"
    assert inst.manufactureDate == fhirtypes.DateTime.validate("2013-02-02")
    assert inst.manufacturer == "GlobalMed, Inc"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "Ultra Implantable"
    assert inst.status == "inactive"
    assert inst.text.status == "generated"
    assert inst.udiCarrier[0].carrierHRF == (
    "+H123PARTNO1234567890120/$$420020216LOT123456789012345/SXYZ4"
    "56789012345678/16D20130202C"
    )
    assert inst.udiCarrier[0].deviceIdentifier == "007444534255003288"
    assert inst.udiCarrier[0].entryType == "manual"
    assert inst.udiCarrier[0].issuer == "http://hl7.org/fhir/NamingSystem/hibcc"
    assert inst.udiCarrier[0].jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"


def test_device_5(base_settings):
    """No. 5 tests collection for Device.
    Test File: device-example-udi3.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-udi3.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_5(inst2)


def impl_device_6(inst):
    assert inst.displayName == "device-example-specimen-container-green-gel-vacutainer"
    assert inst.id == "device-example-specimen-container-green-gel-vacutainer"
    assert inst.identifier[0].system == "http://acme.com/containers/id"
    assert inst.identifier[0].value == "345675"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.property[0].type.coding[0].code == "tube-type"
    assert inst.property[0].type.coding[0].display == "Tube Type"
    assert inst.property[0].type.coding[0].system == "http://acme.com/containers/codes"
    assert inst.property[0].valueCodeableConcept.coding[0].code == "green-gel"
    assert inst.property[0].valueCodeableConcept.coding[0].display == "Green Gel"
    assert inst.property[0].valueCodeableConcept.coding[0].system == "http://acme.com/containers/types"
    assert inst.property[1].type.coding[0].code == "amount"
    assert inst.property[1].type.coding[0].display == "Amount"
    assert inst.property[1].type.coding[0].system == "http://acme.com/containers/codes"
    assert inst.property[1].valueCodeableConcept.coding[0].code == "4.5mL"
    assert inst.property[1].valueCodeableConcept.coding[0].display == "4.5 mL"
    assert inst.property[1].valueCodeableConcept.coding[0].system == "http://acme.com/containers/capacities"
    assert inst.property[2].type.coding[0].code == "additive"
    assert inst.property[2].type.coding[0].display == "Additive"
    assert inst.property[2].type.coding[0].system == "http://acme.com/containers/codes"
    assert inst.property[2].valueCodeableConcept.coding[0].code == "lihep"
    assert inst.property[2].valueCodeableConcept.coding[0].display == "lithium heparin"
    assert inst.property[2].valueCodeableConcept.coding[0].system == "http://acme.com/containers/additive"
    assert inst.text.status == "generated"


def test_device_6(base_settings):
    """No. 6 tests collection for Device.
    Test File: device-example-specimen-container-green-gel-vacutainer.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-specimen-container-green-gel-vacutainer.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_6(inst2)


def impl_device_7(inst):
    assert inst.conformsTo[0].specification.coding[0].code == "528392"
    assert inst.conformsTo[0].specification.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.conformsTo[0].specification.text == "MDC_DEV_SPEC_PROFILE_TEMP: Thermometer"
    assert inst.conformsTo[0].version == "1"
    assert inst.id == "KinsaThermometer"
    assert inst.identifier[0].system == "urn:oid:1.2.840.10004.1.1.1.0.0.1.0.0.1.2680"
    assert inst.identifier[0].type.coding[0].code == "SYSID"
    assert inst.identifier[0].type.coding[0].display == "System Identifier"
    assert inst.identifier[0].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifi"
    "ers"
    )
    assert inst.identifier[0].value == "00-00-52-49-20-45-4C-42"
    assert inst.identifier[1].system == "http://hl7.org/fhir/sid/eui-48"
    assert inst.identifier[1].type.coding[0].code == "BTMAC"
    assert inst.identifier[1].type.coding[0].display == "Bluetooth Address"
    assert inst.identifier[1].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifi"
    "ers"
    )
    assert inst.identifier[1].value == "10-CE-A9-80-14-66"
    assert inst.manufacturer == "Kinsa"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.modelNumber == "KS_1i9JfKh"
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "KS_1i9JfKh"
    assert inst.property[0].type.coding[0].code == "68220"
    assert inst.property[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[0].type.text == "MDC_TIME_SYNC_PROTOCOL: Time synchronization protocol"
    assert inst.property[0].valueCodeableConcept.coding[0].code == "532224"
    assert inst.property[0].valueCodeableConcept.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[0].valueCodeableConcept.text == "MDC_TIME_SYNC_NONE: No time synchronization"
    assert inst.serialNumber == "1i9JfKh"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "65573"
    assert inst.type[0].coding[0].display == "MDC_MOC_VMS_MDS_SIMP"
    assert inst.type[0].coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.type[0].text == "MDC_MOC_VMS_MDS_SIMP: Personal Health Device"
    assert inst.udiCarrier[0].carrierHRF == "(01)18479793050726(21)1i9JfKh"
    assert inst.udiCarrier[0].deviceIdentifier == "18479793050726"
    assert inst.udiCarrier[0].entryType == "unknown"
    assert inst.udiCarrier[0].issuer == "http://hl7.org/fhir/NamingSystem/gs1-di"
    assert inst.udiCarrier[0].jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"
    assert inst.version[0].type.coding[0].code == "531976"
    assert inst.version[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[0].type.text == "MDC_ID_PROD_SPEC_FW: Firmware revision"
    assert inst.version[0].value == "1.00"
    assert inst.version[1].type.coding[0].code == "531975"
    assert inst.version[1].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[1].type.text == "MDC_ID_PROD_SPEC_SW: Software revision"
    assert inst.version[1].value == "V2.19"
    assert inst.version[2].type.coding[0].code == "531974"
    assert inst.version[2].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[2].type.text == "MDC_ID_PROD_SPEC_SW: Hardware revision"
    assert inst.version[2].value == "1.00"


def test_device_7(base_settings):
    """No. 7 tests collection for Device.
    Test File: device-example-KinsaThermometer.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-KinsaThermometer.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_7(inst2)


def impl_device_8(inst):
    assert inst.conformsTo[0].specification.coding[0].code == "528392"
    assert inst.conformsTo[0].specification.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.conformsTo[0].specification.text == "MDC_DEV_SPEC_PROFILE_TEMP: Thermometer"
    assert inst.conformsTo[0].version == "1"
    assert inst.id == "PhilipsThermometer"
    assert inst.identifier[0].system == "urn:oid:1.2.840.10004.1.1.1.0.0.1.0.0.1.2680"
    assert inst.identifier[0].type.coding[0].code == "SYSID"
    assert inst.identifier[0].type.coding[0].display == "System Identifier"
    assert inst.identifier[0].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifi"
    "ers"
    )
    assert inst.identifier[0].value == "1C-87-74-FF-FE-00-EC-20"
    assert inst.identifier[1].system == "http://hl7.org/fhir/sid/eui-48"
    assert inst.identifier[1].type.coding[0].code == "BTMAC"
    assert inst.identifier[1].type.coding[0].display == "Bluetooth Address"
    assert inst.identifier[1].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifi"
    "ers"
    )
    assert inst.identifier[1].value == "1C-87-74-00-EC-20"
    assert inst.manufacturer == "Philips"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.modelNumber == "DL8740"
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "Philips ear thermometer"
    assert inst.property[0].type.coding[0].code == "532353"
    assert inst.property[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[0].type.text == (
    "MDC_REG_CERT_DATA_CONTINUA_CERT_DEV_LIST: Continua certified"
    " device list"
    )
    assert inst.property[0].valueCodeableConcept.coding[0].code == "32776"
    assert inst.property[0].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/ContinuaPAN"
    assert inst.property[1].type.coding[0].code == "532354.0"
    assert inst.property[1].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[1].type.text == "regulation-status"
    assert inst.property[1].valueCodeableConcept.coding[0].code == "N"
    assert inst.property[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[1].valueCodeableConcept.text == "Device is Regulated"
    assert inst.property[2].type.coding[0].code == "68220"
    assert inst.property[2].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[2].type.text == "MDC_TIME_SYNC_PROTOCOL: Time synchronization protocol"
    assert inst.property[2].valueCodeableConcept.coding[0].code == "532224"
    assert inst.property[2].valueCodeableConcept.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[2].valueCodeableConcept.text == "MDC_TIME_SYNC_NONE: No time synchronization"
    assert inst.property[3].type.coding[0].code == "68219.0"
    assert inst.property[3].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[3].type.text == "mds-time-capab-real-time-clock"
    assert inst.property[3].valueCodeableConcept.coding[0].code == "Y"
    assert inst.property[3].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[3].valueCodeableConcept.text == "real time clock supported"
    assert inst.property[4].type.coding[0].code == "68219.1"
    assert inst.property[4].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[4].type.text == "mds-time-capab-set-clock"
    assert inst.property[4].valueCodeableConcept.coding[0].code == "Y"
    assert inst.property[4].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[4].valueCodeableConcept.text == "setting the time supported"
    assert inst.serialNumber == "162502000528"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "65573"
    assert inst.type[0].coding[0].display == "MDC_MOC_VMS_MDS_SIMP"
    assert inst.type[0].coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.type[0].text == "MDC_MOC_VMS_MDS_SIMP: Personal Health Device"
    assert inst.udiCarrier[0].carrierHRF == "(01)31368092380192(21)162502000528"
    assert inst.udiCarrier[0].deviceIdentifier == "31368092380192"
    assert inst.udiCarrier[0].entryType == "unknown"
    assert inst.udiCarrier[0].issuer == "http://hl7.org/fhir/NamingSystem/gs1-di"
    assert inst.udiCarrier[0].jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"
    assert inst.version[0].type.coding[0].code == "531976"
    assert inst.version[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[0].type.text == "MDC_ID_PROD_SPEC_FW: Firmware revision"
    assert inst.version[0].value == "1.60"
    assert inst.version[1].type.coding[0].code == "531975"
    assert inst.version[1].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[1].type.text == "MDC_ID_PROD_SPEC_SW: Software revision"
    assert inst.version[1].value == "1.50"
    assert inst.version[2].type.coding[0].code == "531974"
    assert inst.version[2].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[2].type.text == "MDC_ID_PROD_SPEC_SW: Hardware revision"
    assert inst.version[2].value == "1.40"
    assert inst.version[3].type.coding[0].code == "532352"
    assert inst.version[3].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[3].type.text == "MDC_REG_CERT_DATA_CONTINUA_VERSION: Continua version"
    assert inst.version[3].value == "5.1"


def test_device_8(base_settings):
    """No. 8 tests collection for Device.
    Test File: device-example-PhilipsThermometer.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-PhilipsThermometer.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_8(inst2)


def impl_device_9(inst):
    assert inst.conformsTo[0].specification.coding[0].code == "528388"
    assert inst.conformsTo[0].specification.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.conformsTo[0].specification.text == "MDC_DEV_SPEC_PROFILE_PULS_OXIM: Pulse Oximeter"
    assert inst.conformsTo[0].version == "1"
    assert inst.id == "Nonin20601PulseOx"
    assert inst.identifier[0].system == "urn:oid:1.2.840.10004.1.1.1.0.0.1.0.0.1.2680"
    assert inst.identifier[0].type.coding[0].code == "SYSID"
    assert inst.identifier[0].type.coding[0].display == "System Identifier"
    assert inst.identifier[0].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifi"
    "ers"
    )
    assert inst.identifier[0].value == "00-1C-05-04-00-00-78-25"
    assert inst.identifier[1].system == "http://hl7.org/fhir/sid/eui-48"
    assert inst.identifier[1].type.coding[0].code == "BTMAC"
    assert inst.identifier[1].type.coding[0].display == "Bluetooth Address"
    assert inst.identifier[1].type.coding[0].system == (
    "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifi"
    "ers"
    )
    assert inst.identifier[1].value == "00-1C-05-00-78-25"
    assert inst.manufacturer == "Nonin Medical, Inc."
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.modelNumber == "Model 3150"
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "Nonin_Medical_Inc._323552"
    assert inst.property[0].type.coding[0].code == "532353"
    assert inst.property[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[0].type.text == (
    "MDC_REG_CERT_DATA_CONTINUA_CERT_DEV_LIST: Continua certified"
    " device list"
    )
    assert inst.property[0].valueCodeableConcept.coding[0].code == "4"
    assert inst.property[0].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/ContinuaPAN"
    assert inst.property[1].type.coding[0].code == "532354.0"
    assert inst.property[1].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[1].type.text == "regulation-status"
    assert inst.property[1].valueCodeableConcept.coding[0].code == "N"
    assert inst.property[1].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[1].valueCodeableConcept.text == "Device is Regulated"
    assert inst.property[2].type.coding[0].code == "68220"
    assert inst.property[2].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[2].type.text == "MDC_TIME_SYNC_PROTOCOL: Time synchronization protocol"
    assert inst.property[2].valueCodeableConcept.coding[0].code == "532224"
    assert inst.property[2].valueCodeableConcept.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[2].valueCodeableConcept.text == "MDC_TIME_SYNC_NONE: No time synchronization"
    assert inst.property[3].type.coding[0].code == "68219.0"
    assert inst.property[3].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[3].type.text == "mds-time-capab-real-time-clock"
    assert inst.property[3].valueCodeableConcept.coding[0].code == "Y"
    assert inst.property[3].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[3].valueCodeableConcept.text == "real time clock supported"
    assert inst.property[4].type.coding[0].code == "68219.2"
    assert inst.property[4].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[4].type.text == "mds-time-capab-set-clock"
    assert inst.property[4].valueCodeableConcept.coding[0].code == "Y"
    assert inst.property[4].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[4].valueCodeableConcept.text == "setting the time supported"
    assert inst.property[5].type.coding[0].code == "68219.2"
    assert inst.property[5].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"
    assert inst.property[5].type.text == "mds-time-capab-relative-time"
    assert inst.property[5].valueCodeableConcept.coding[0].code == "Y"
    assert inst.property[5].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0136"
    assert inst.property[5].valueCodeableConcept.text == "relative time supported"
    assert inst.property[6].type.coding[0].code == "68222"
    assert inst.property[6].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[6].type.text == "MDC_TIME_RES_ABS: Resolution of absolute time clock"
    assert inst.property[6].valueQuantity.code == "us"
    assert inst.property[6].valueQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.property[6].valueQuantity.value) == float(1000000)
    assert inst.property[7].type.coding[0].code == "68222"
    assert inst.property[7].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.property[7].type.text == "MDC_TIME_RES_REL: Resolution of relative time clock"
    assert inst.property[7].valueQuantity.code == "us"
    assert inst.property[7].valueQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.property[7].valueQuantity.value) == float(1000000)
    assert inst.serialNumber == "0400007825"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "65573"
    assert inst.type[0].coding[0].display == "MDC_MOC_VMS_MDS_SIMP"
    assert inst.type[0].coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.type[0].text == "MDC_MOC_VMS_MDS_SIMP: Personal Health Device"
    assert inst.udiCarrier[0].carrierHRF == "(01)120343001125(21)0400007825"
    assert inst.udiCarrier[0].deviceIdentifier == "120343001125"
    assert inst.udiCarrier[0].entryType == "unknown"
    assert inst.udiCarrier[0].issuer == "http://hl7.org/fhir/NamingSystem/gs1-di"
    assert inst.udiCarrier[0].jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"
    assert inst.version[0].type.coding[0].code == "531976"
    assert inst.version[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[0].type.text == "MDC_ID_PROD_SPEC_FW: Firmware revision"
    assert inst.version[0].value == "0.9C"
    assert inst.version[1].type.coding[0].code == "532352"
    assert inst.version[1].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.version[1].type.text == "MDC_REG_CERT_DATA_CONTINUA_VERSION: Continua version"
    assert inst.version[1].value == "1.0"


def test_device_9(base_settings):
    """No. 9 tests collection for Device.
    Test File: device-example-Nonin20601PulseOx.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-Nonin20601PulseOx.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_9(inst2)


def impl_device_10(inst):
    assert inst.id == "example-udi4"
    assert inst.lotNumber == "RZ12345678"
    assert inst.manufacturer == "GlobalMed, Inc"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "inactive"
    assert inst.text.status == "generated"
    assert inst.udiCarrier[0].carrierHRF == "=)1TE123456A&)RZ12345678"
    assert inst.udiCarrier[0].deviceIdentifier == "A4599XQZ990T0474"
    assert inst.udiCarrier[0].issuer == "http://hl7.org/fhir/NamingSystem/iccbba-blood"
    assert inst.udiCarrier[0].jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"


def test_device_10(base_settings):
    """No. 10 tests collection for Device.
    Test File: device-example-udi4.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-udi4.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_10(inst2)