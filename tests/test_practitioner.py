# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Practitioner
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import practitioner


def impl_practitioner_1(inst):
    assert inst.active is True
    assert inst.address[0].city == "Den helder"
    assert inst.address[0].country == "NLD"
    assert inst.address[0].line[0] == "Walvisbaai 3"
    assert inst.address[0].line[1] == "C4 - Automatisering"
    assert inst.address[0].postalCode == "2333ZA"
    assert inst.address[0].use == "work"
    assert inst.birthDate == fhirtypes.Date.validate("1960-06-12")
    assert inst.gender == "male"
    assert inst.id == "f202"
    assert inst.identifier[0].system == "urn:oid:2.16.528.1.1007.3.1"
    assert inst.identifier[0].type.text == "UZI-nummer"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345678902"
    assert inst.identifier[1].system == "https://www.bigregister.nl/"
    assert inst.identifier[1].type.text == "BIG-nummer"
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "12345678902"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Maas"
    assert inst.name[0].given[0] == "Luigi"
    assert inst.name[0].prefix[0] == "Dr."
    assert inst.name[0].text == "Luigi Maas"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "+31715269111"
    assert inst.text.status == "generated"


def test_practitioner_1(base_settings):
    """No. 1 tests collection for Practitioner.
    Test File: practitioner-example-f202-lm.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "practitioner-example-f202-lm.json"
    )
    inst = practitioner.Practitioner.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Practitioner" == inst.resource_type

    impl_practitioner_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Practitioner" == data["resourceType"]

    inst2 = practitioner.Practitioner(**data)
    impl_practitioner_1(inst2)


def impl_practitioner_2(inst):
    assert inst.address[0].city == "Den helder"
    assert inst.address[0].country == "NLD"
    assert inst.address[0].line[0] == "Walvisbaai 3"
    assert inst.address[0].postalCode == "2333ZA"
    assert inst.address[0].use == "work"
    assert inst.birthDate == fhirtypes.Date.validate("1967-11-05")
    assert inst.gender == "female"
    assert inst.id == "f204"
    assert inst.identifier[0].system == "urn:oid:2.16.528.1.1007.3.1"
    assert inst.identifier[0].type.text == "UZI-nummer"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345678904"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].text == "Carla Espinosa"
    assert inst.name[0].use == "usual"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "+31715262169"
    assert inst.text.status == "generated"


def test_practitioner_2(base_settings):
    """No. 2 tests collection for Practitioner.
    Test File: practitioner-example-f204-ce.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "practitioner-example-f204-ce.json"
    )
    inst = practitioner.Practitioner.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Practitioner" == inst.resource_type

    impl_practitioner_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Practitioner" == data["resourceType"]

    inst2 = practitioner.Practitioner(**data)
    impl_practitioner_2(inst2)


def impl_practitioner_3(inst):
    assert inst.active is True
    assert inst.id == "practitioner02"
    assert inst.identifier[0].assigner.display == "Child Hospital"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2021-01-01")
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/persons"
    assert inst.identifier[0].type.coding[0].code == "PRN"
    assert inst.identifier[0].type.coding[0].display == "Provider number"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "11116"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Doel"
    assert inst.name[0].given[0] == "Jane"
    assert inst.name[0].prefix[0] == "Dr"
    assert inst.text.status == "generated"


def test_practitioner_3(base_settings):
    """No. 3 tests collection for Practitioner.
    Test File: Practitioner-practitioner02.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Practitioner-practitioner02.json"
    )
    inst = practitioner.Practitioner.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Practitioner" == inst.resource_type

    impl_practitioner_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Practitioner" == data["resourceType"]

    inst2 = practitioner.Practitioner(**data)
    impl_practitioner_3(inst2)


def impl_practitioner_4(inst):
    assert inst.address[0].city == "Den Burg"
    assert inst.address[0].country == "NLD"
    assert inst.address[0].line[0] == "Galapagosweg 91"
    assert inst.address[0].postalCode == "9105 PZ"
    assert inst.address[0].use == "work"
    assert inst.birthDate == fhirtypes.Date.validate("1975-12-07")
    assert inst.gender == "male"
    assert inst.id == "f001"
    assert inst.identifier[0].system == "urn:oid:2.16.528.1.1007.3.1"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "938273695"
    assert inst.identifier[1].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[1].use == "usual"
    assert inst.identifier[1].value == "129IDH4OP733"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "van den broek"
    assert inst.name[0].given[0] == "Eric"
    assert inst.name[0].suffix[0] == "MD"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "0205568263"
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "E.M.vandenbroek@bmc.nl"
    assert inst.telecom[2].system == "fax"
    assert inst.telecom[2].use == "work"
    assert inst.telecom[2].value == "0205664440"
    assert inst.text.status == "generated"


def test_practitioner_4(base_settings):
    """No. 4 tests collection for Practitioner.
    Test File: practitioner-example-f001-evdb.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "practitioner-example-f001-evdb.json"
    )
    inst = practitioner.Practitioner.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Practitioner" == inst.resource_type

    impl_practitioner_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Practitioner" == data["resourceType"]

    inst2 = practitioner.Practitioner(**data)
    impl_practitioner_4(inst2)


def impl_practitioner_5(inst):
    assert inst.address[0].city == "Amsterdam"
    assert inst.address[0].country == "NLD"
    assert inst.address[0].line[0] == "Galapagosweg 91"
    assert inst.address[0].postalCode == "1105 AZ"
    assert inst.address[0].use == "work"
    assert inst.birthDate == fhirtypes.Date.validate("1980-02-04")
    assert inst.communication[0].coding[0].code == "nl"
    assert inst.communication[0].coding[0].display == "Netherlands"
    assert inst.communication[0].coding[0].system == "urn:ietf:bcp:47"
    assert inst.communication[0].text == "Language"
    assert inst.gender == "male"
    assert inst.id == "f004"
    assert inst.identifier[0].system == "urn:oid:2.16.528.1.1007.3.1"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "118265112"
    assert inst.identifier[1].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[1].use == "usual"
    assert inst.identifier[1].value == "523ASA1LK927"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Briet"
    assert inst.name[0].given[0] == "Ronald"
    assert inst.name[0].suffix[0] == "MD"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "0205569273"
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "r.briet@bmc.nl"
    assert inst.telecom[2].system == "fax"
    assert inst.telecom[2].use == "work"
    assert inst.telecom[2].value == "0205664440"
    assert inst.text.status == "generated"


def test_practitioner_5(base_settings):
    """No. 5 tests collection for Practitioner.
    Test File: practitioner-example-f004-rb.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "practitioner-example-f004-rb.json"
    )
    inst = practitioner.Practitioner.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Practitioner" == inst.resource_type

    impl_practitioner_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Practitioner" == data["resourceType"]

    inst2 = practitioner.Practitioner(**data)
    impl_practitioner_5(inst2)


def impl_practitioner_6(inst):
    assert inst.address[0].city == "Den Burg"
    assert inst.address[0].country == "NLD"
    assert inst.address[0].line[0] == "Galapagosweg 91"
    assert inst.address[0].postalCode == "9105 PZ"
    assert inst.address[0].use == "work"
    assert inst.birthDate == fhirtypes.Date.validate("1979-04-29")
    assert inst.gender == "male"
    assert inst.id == "f002"
    assert inst.identifier[0].system == "urn:oid:2.16.528.1.1007.3.1"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "730291637"
    assert inst.identifier[1].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[1].use == "usual"
    assert inst.identifier[1].value == "174BIP3JH438"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Voigt"
    assert inst.name[0].given[0] == "Pieter"
    assert inst.name[0].suffix[0] == "MD"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "0205569336"
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "p.voigt@bmc.nl"
    assert inst.telecom[2].system == "fax"
    assert inst.telecom[2].use == "work"
    assert inst.telecom[2].value == "0205669382"
    assert inst.text.status == "generated"


def test_practitioner_6(base_settings):
    """No. 6 tests collection for Practitioner.
    Test File: practitioner-example-f002-pv.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "practitioner-example-f002-pv.json"
    )
    inst = practitioner.Practitioner.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Practitioner" == inst.resource_type

    impl_practitioner_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Practitioner" == data["resourceType"]

    inst2 = practitioner.Practitioner(**data)
    impl_practitioner_6(inst2)


def impl_practitioner_7(inst):
    assert inst.address[0].city == "Den Burg"
    assert inst.address[0].country == "NLD"
    assert inst.address[0].line[0] == "Galapagosweg 91"
    assert inst.address[0].postalCode == "9105 PZ"
    assert inst.address[0].use == "work"
    assert inst.birthDate == fhirtypes.Date.validate("1975-12-07")
    assert inst.gender == "male"
    assert inst.id == "f006"
    assert inst.identifier[0].system == "urn:oid:2.16.528.1.1007.3.1"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "937223645"
    assert inst.identifier[1].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[1].use == "usual"
    assert inst.identifier[1].value == "134IDY41W988"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "van den Berk"
    assert inst.name[0].given[0] == "Rob"
    assert inst.name[0].suffix[0] == "MD"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "0205569288"
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "R.A.vandenberk@bmc.nl"
    assert inst.telecom[2].system == "fax"
    assert inst.telecom[2].use == "work"
    assert inst.telecom[2].value == "0205664987"
    assert inst.text.status == "generated"


def test_practitioner_7(base_settings):
    """No. 7 tests collection for Practitioner.
    Test File: practitioner-example-f006-rvdb.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "practitioner-example-f006-rvdb.json"
    )
    inst = practitioner.Practitioner.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Practitioner" == inst.resource_type

    impl_practitioner_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Practitioner" == data["resourceType"]

    inst2 = practitioner.Practitioner(**data)
    impl_practitioner_7(inst2)


def impl_practitioner_8(inst):
    assert inst.active is True
    assert inst.id == "practitioner01"
    assert inst.identifier[0].assigner.display == "Child Hospital"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2021-01-01")
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/persons"
    assert inst.identifier[0].type.coding[0].code == "PRN"
    assert inst.identifier[0].type.coding[0].display == "Provider number"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "11115"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Doel"
    assert inst.name[0].given[0] == "John"
    assert inst.name[0].prefix[0] == "Dr"
    assert inst.text.status == "generated"


def test_practitioner_8(base_settings):
    """No. 8 tests collection for Practitioner.
    Test File: Practitioner-practitioner01.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "Practitioner-practitioner01.json"
    )
    inst = practitioner.Practitioner.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Practitioner" == inst.resource_type

    impl_practitioner_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Practitioner" == data["resourceType"]

    inst2 = practitioner.Practitioner(**data)
    impl_practitioner_8(inst2)


def impl_practitioner_9(inst):
    assert inst.address[0].city == "Amsterdam"
    assert inst.address[0].country == "NLD"
    assert inst.address[0].line[0] == "Galapagosweg 91"
    assert inst.address[0].postalCode == "1105 AZ"
    assert inst.address[0].use == "work"
    assert inst.birthDate == fhirtypes.Date.validate("1963-07-01")
    assert inst.communication[0].coding[0].code == "nl"
    assert inst.communication[0].coding[0].display == "Dutch"
    assert inst.communication[0].coding[0].system == "urn:ietf:bcp:47"
    assert inst.gender == "male"
    assert inst.id == "f003"
    assert inst.identifier[0].system == "urn:oid:2.16.528.1.1007.3.1"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "846100293"
    assert inst.identifier[1].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[1].use == "usual"
    assert inst.identifier[1].value == "243HID3RT938"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Versteegh"
    assert inst.name[0].given[0] == "Marc"
    assert inst.name[0].suffix[0] == "MD"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "0205562431"
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "m.versteegh@bmc.nl"
    assert inst.telecom[2].system == "fax"
    assert inst.telecom[2].use == "work"
    assert inst.telecom[2].value == "0205662948"
    assert inst.text.status == "generated"


def test_practitioner_9(base_settings):
    """No. 9 tests collection for Practitioner.
    Test File: practitioner-example-f003-mv.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "practitioner-example-f003-mv.json"
    )
    inst = practitioner.Practitioner.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Practitioner" == inst.resource_type

    impl_practitioner_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Practitioner" == data["resourceType"]

    inst2 = practitioner.Practitioner(**data)
    impl_practitioner_9(inst2)


def impl_practitioner_10(inst):
    assert inst.id == "xcda-author"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name[0].family == "Hippocrates"
    assert inst.name[0].given[0] == "Harold"
    assert inst.name[0].suffix[0] == "MD"
    assert inst.text.status == "generated"


def test_practitioner_10(base_settings):
    """No. 10 tests collection for Practitioner.
    Test File: practitioner-example-xcda-author.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "practitioner-example-xcda-author.json"
    )
    inst = practitioner.Practitioner.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Practitioner" == inst.resource_type

    impl_practitioner_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Practitioner" == data["resourceType"]

    inst2 = practitioner.Practitioner(**data)
    impl_practitioner_10(inst2)