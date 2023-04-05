# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Organization
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import organization


def impl_organization_1(inst):
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "022-655 2300"
    assert inst.contact[1].address.city == "Den Burg"
    assert inst.contact[1].address.country == "NLD"
    assert inst.contact[1].address.line[0] == "Galapagosweg 91"
    assert inst.contact[1].address.postalCode == "9105 PZ"
    assert inst.contact[1].address.use == "work"
    assert inst.contact[2].address.city == "Den Burg"
    assert inst.contact[2].address.country == "NLD"
    assert inst.contact[2].address.line[0] == "PO Box 2311"
    assert inst.contact[2].address.postalCode == "9100 AA"
    assert inst.contact[2].address.use == "work"
    assert inst.contact[3].purpose.coding[0].code == "PRESS"
    assert inst.contact[3].purpose.coding[0].system == "http://terminology.hl7.org/CodeSystem/contactentity-type"
    assert inst.contact[3].telecom[0].system == "phone"
    assert inst.contact[3].telecom[0].value == "022-655 2334"
    assert inst.contact[4].purpose.coding[0].code == "PATINF"
    assert inst.contact[4].purpose.coding[0].system == "http://terminology.hl7.org/CodeSystem/contactentity-type"
    assert inst.contact[4].telecom[0].system == "phone"
    assert inst.contact[4].telecom[0].value == "022-655 2335"
    assert inst.id == "f001"
    assert inst.identifier[0].system == "urn:oid:2.16.528.1"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "91654"
    assert inst.identifier[1].system == "urn:oid:2.16.840.1.113883.2.4.6.1"
    assert inst.identifier[1].use == "usual"
    assert inst.identifier[1].value == "17-0112278"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Burgers University Medical Center"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "V6"
    assert inst.type[0].coding[0].display == "University Medical Hospital"
    assert inst.type[0].coding[0].system == "urn:oid:2.16.840.1.113883.2.4.15.1060"
    assert inst.type[0].coding[1].code == "prov"
    assert inst.type[0].coding[1].display == "Healthcare Provider"
    assert inst.type[0].coding[1].system == "http://terminology.hl7.org/CodeSystem/organization-type"


def test_organization_1(base_settings):
    """No. 1 tests collection for Organization.
    Test File: organization-example-f001-burgers.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-f001-burgers.json"
    )
    inst = organization.Organization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Organization" == inst.resource_type

    impl_organization_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_1(inst2)


def impl_organization_2(inst):
    assert inst.id == "2.16.840.1.113883.19.5"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.19.5"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Good Health Clinic"
    assert inst.text.status == "generated"


def test_organization_2(base_settings):
    """No. 2 tests collection for Organization.
    Test File: organization-example-good-health-care.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-good-health-care.json"
    )
    inst = organization.Organization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Organization" == inst.resource_type

    impl_organization_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_2(inst2)


def impl_organization_3(inst):
    assert inst.alias[0] == "Michigan State Department of Health"
    assert inst.id == "3"
    assert inst.identifier[0].system == "http://michigan.gov/state-dept-ids"
    assert inst.identifier[0].value == "25"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Michigan Health"
    assert inst.text.status == "generated"


def test_organization_3(base_settings):
    """No. 3 tests collection for Organization.
    Test File: organization-example-mihealth.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-mihealth.json"
    )
    inst = organization.Organization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Organization" == inst.resource_type

    impl_organization_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_3(inst2)


def impl_organization_4(inst):
    assert inst.active is True
    assert inst.contact[0].address.city == "Den Helder"
    assert inst.contact[0].address.country == "NLD"
    assert inst.contact[0].address.line[0] == "Walvisbaai 3"
    assert inst.contact[0].address.postalCode == "2333ZA"
    assert inst.contact[0].address.use == "work"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "+31715269111"
    assert inst.contact[1].address.city == "Den helder"
    assert inst.contact[1].address.country == "NLD"
    assert inst.contact[1].address.line[0] == "Walvisbaai 3"
    assert inst.contact[1].address.line[1] == "Gebouw 2"
    assert inst.contact[1].address.postalCode == "2333ZA"
    assert inst.contact[1].name[0].family == "Brand"
    assert inst.contact[1].name[0].given[0] == "Ronald"
    assert inst.contact[1].name[0].prefix[0] == "Prof.Dr."
    assert inst.contact[1].name[0].text == "Professor Brand"
    assert inst.contact[1].name[0].use == "official"
    assert inst.contact[1].telecom[0].system == "phone"
    assert inst.contact[1].telecom[0].use == "work"
    assert inst.contact[1].telecom[0].value == "+31715269702"
    assert inst.id == "f201"
    assert inst.identifier[0].system == "http://www.zorgkaartnederland.nl/"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "Artis University Medical Center"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Artis University Medical Center (AUMC)"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "405608006"
    assert inst.type[0].coding[0].display == "Academic Medical Center"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"
    assert inst.type[0].coding[1].code == "V6"
    assert inst.type[0].coding[1].display == "University Medical Hospital"
    assert inst.type[0].coding[1].system == "urn:oid:2.16.840.1.113883.2.4.15.1060"
    assert inst.type[0].coding[2].code == "prov"
    assert inst.type[0].coding[2].display == "Healthcare Provider"
    assert inst.type[0].coding[2].system == "http://terminology.hl7.org/CodeSystem/organization-type"


def test_organization_4(base_settings):
    """No. 4 tests collection for Organization.
    Test File: organization-example-f201-aumc.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-f201-aumc.json"
    )
    inst = organization.Organization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Organization" == inst.resource_type

    impl_organization_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_4(inst2)


def impl_organization_5(inst):
    assert inst.alias[0] == "HL7 International"
    assert inst.contact[0].address.city == "Ann Arbor"
    assert inst.contact[0].address.country == "USA"
    assert inst.contact[0].address.line[0] == "3300 Washtenaw Avenue, Suite 227"
    assert inst.contact[0].address.postalCode == "48104"
    assert inst.contact[0].address.state == "MI"
    assert inst.contact[0].extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/extended-contact-"
    "availability"
    )
    assert inst.contact[0].extension[0].valueAvailability.availableTime[0].availableEndTime == fhirtypes.Time.validate("07:00:00")
    assert inst.contact[0].extension[0].valueAvailability.availableTime[0].availableStartTime == fhirtypes.Time.validate("09:00:00")
    assert inst.contact[0].extension[0].valueAvailability.availableTime[0].daysOfWeek[0] == "mon"
    assert inst.contact[0].extension[0].valueAvailability.availableTime[0].daysOfWeek[1] == "tue"
    assert inst.contact[0].extension[0].valueAvailability.availableTime[0].daysOfWeek[2] == "wed"
    assert inst.contact[0].extension[0].valueAvailability.availableTime[0].daysOfWeek[3] == "thu"
    assert inst.contact[0].extension[0].valueAvailability.availableTime[0].daysOfWeek[4] == "fri"
    assert inst.contact[0].extension[0].valueAvailability.notAvailableTime[0].description == "Public holidays"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].value == "(+1) 734-677-7777"
    assert inst.contact[0].telecom[1].system == "fax"
    assert inst.contact[0].telecom[1].value == "(+1) 734-677-6622"
    assert inst.contact[0].telecom[2].system == "email"
    assert inst.contact[0].telecom[2].value == "hq@HL7.org"
    assert inst.endpoint[0].reference == "Endpoint/example"
    assert inst.id == "hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Health Level Seven International"
    assert inst.text.status == "generated"


def test_organization_5(base_settings):
    """No. 5 tests collection for Organization.
    Test File: organization-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example.json"
    )
    inst = organization.Organization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Organization" == inst.resource_type

    impl_organization_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_5(inst2)


def impl_organization_6(inst):
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "mobile"
    assert inst.contact[0].telecom[0].value == "+1 555 234 3523"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "gastro@acme.org"
    assert inst.id == "1"
    assert inst.identifier[0].system == "http://www.acme.org.au/units"
    assert inst.identifier[0].value == "Gastro"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Gastroenterology"
    assert inst.text.status == "generated"


def test_organization_6(base_settings):
    """No. 6 tests collection for Organization.
    Test File: organization-example-gastro.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-gastro.json"
    )
    inst = organization.Organization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Organization" == inst.resource_type

    impl_organization_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_6(inst2)


def impl_organization_7(inst):
    assert inst.alias[0] == "ABC Insurance"
    assert inst.id == "2"
    assert inst.identifier[0].system == "urn:oid:2.16.840.1.113883.3.19.2.3"
    assert inst.identifier[0].value == "666666"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "XYZ Insurance"
    assert inst.text.status == "generated"


def test_organization_7(base_settings):
    """No. 7 tests collection for Organization.
    Test File: organization-example-insurer.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-insurer.json"
    )
    inst = organization.Organization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Organization" == inst.resource_type

    impl_organization_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_7(inst2)


def impl_organization_8(inst):
    assert inst.active is True
    assert inst.contact[0].address.country == "Swizterland"
    assert inst.id == "mmanu"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Acme Corporation"
    assert inst.text.status == "generated"


def test_organization_8(base_settings):
    """No. 8 tests collection for Organization.
    Test File: organization-example-mmanu.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-mmanu.json"
    )
    inst = organization.Organization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Organization" == inst.resource_type

    impl_organization_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_8(inst2)


def impl_organization_9(inst):
    assert inst.id == "hl7pay"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "HL7 Payer network"
    assert inst.text.status == "generated"


def test_organization_9(base_settings):
    """No. 9 tests collection for Organization.
    Test File: organization-example-hl7pay.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-hl7pay.json"
    )
    inst = organization.Organization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Organization" == inst.resource_type

    impl_organization_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_9(inst2)


def impl_organization_10(inst):
    assert inst.active is True
    assert inst.contact[0].address.city == "Blijdorp"
    assert inst.contact[0].address.country == "NLD"
    assert inst.contact[0].address.line[0] == "apenrots 230"
    assert inst.contact[0].address.postalCode == "3056BE"
    assert inst.contact[0].address.use == "work"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "+31107040704"
    assert inst.id == "f203"
    assert inst.identifier[0].system == "http://www.zorgkaartnederland.nl/"
    assert inst.identifier[0].type.text == "Zorginstelling naam"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "Blijdorp MC"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Blijdorp Medisch Centrum (BUMC)"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "405608006"
    assert inst.type[0].coding[0].display == "Academic Medical Center"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"
    assert inst.type[0].coding[1].code == "prov"
    assert inst.type[0].coding[1].system == "http://terminology.hl7.org/CodeSystem/organization-type"


def test_organization_10(base_settings):
    """No. 10 tests collection for Organization.
    Test File: organization-example-f203-bumc.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organization-example-f203-bumc.json"
    )
    inst = organization.Organization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Organization" == inst.resource_type

    impl_organization_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Organization" == data["resourceType"]

    inst2 = organization.Organization(**data)
    impl_organization_10(inst2)