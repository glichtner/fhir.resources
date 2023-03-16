# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Location
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import location


def impl_location_1(inst):
    assert inst.alias[0] == "South Wing OR 5"
    assert inst.alias[1] == "Main Wing OR 2"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].value == "2329"
    assert inst.description == (
    "Old South Wing, Neuro Radiology Operation Room 1 on second "
    "floor"
    )
    assert inst.form.coding[0].code == "ro"
    assert inst.form.coding[0].display == "Room"
    assert inst.form.coding[0].system == "http://terminology.hl7.org/CodeSystem/location-physical-type"
    assert inst.id == "2"
    assert inst.identifier[0].value == "B1-S.F2.1.00"
    assert inst.managingOrganization.reference == "Organization/f001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.mode == "instance"
    assert inst.name == "South Wing Neuro OR 1"
    assert inst.operationalStatus.code == "H"
    assert inst.operationalStatus.display == "Housekeeping"
    assert inst.operationalStatus.system == "http://terminology.hl7.org/CodeSystem/v2-0116"
    assert inst.partOf.reference == "Location/1"
    assert inst.status == "suspended"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Burgers UMC, "
    "South Wing, second floor, Neuro Radiology Operation Room "
    "1</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "RNEU"
    assert inst.type[0].coding[0].display == "Neuroradiology unit"
    assert inst.type[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"


def test_location_1(base_settings):
    """No. 1 tests collection for Location.
    Test File: location-example-room.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "location-example-room.json"
    )
    inst = location.Location.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Location" == inst.resource_type

    impl_location_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Location" == data["resourceType"]

    inst2 = location.Location(**data)
    impl_location_1(inst2)


def impl_location_2(inst):
    assert inst.alias[0] == "BU MC, SW, F2"
    assert inst.alias[1] == "Burgers University Medical Center, South Wing, second floor"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "2328"
    assert inst.contact[0].telecom[1].system == "fax"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "2329"
    assert inst.contact[0].telecom[2].system == "email"
    assert inst.contact[0].telecom[2].value == "second wing admissions"
    assert inst.contact[1].telecom[0].system == "url"
    assert inst.contact[1].telecom[0].use == "work"
    assert inst.contact[1].telecom[0].value == "http://sampleorg.com/southwing"
    assert inst.contact[2].address.city == "Den Burg"
    assert inst.contact[2].address.country == "NLD"
    assert inst.contact[2].address.line[0] == "Galapagosweg 91, Building A"
    assert inst.contact[2].address.postalCode == "9105 PZ"
    assert inst.contact[2].address.use == "work"
    assert inst.description == (
    "Second floor of the Old South Wing, formerly in use by "
    "Psychiatry"
    )
    assert inst.endpoint[0].reference == "Endpoint/example"
    assert inst.form.coding[0].code == "wi"
    assert inst.form.coding[0].display == "Wing"
    assert inst.form.coding[0].system == "http://terminology.hl7.org/CodeSystem/location-physical-type"
    assert inst.id == "1"
    assert inst.identifier[0].value == "B1-S.F2"
    assert inst.managingOrganization.reference == "Organization/f001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.mode == "instance"
    assert inst.name == "South Wing, second floor"
    assert float(inst.position.altitude) == float(0)
    assert float(inst.position.latitude) == float(42.25475478)
    assert float(inst.position.longitude) == float(-83.6945691)
    assert inst.status == "active"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Burgers UMC, "
    "South Wing, second floor</div>"
    )
    assert inst.text.status == "generated"


def test_location_2(base_settings):
    """No. 2 tests collection for Location.
    Test File: location-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "location-example.json"
    )
    inst = location.Location.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Location" == inst.resource_type

    impl_location_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Location" == data["resourceType"]

    inst2 = location.Location(**data)
    impl_location_2(inst2)


def impl_location_3(inst):
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "mobile"
    assert inst.contact[0].telecom[0].value == "2329"
    assert inst.description == "Ambulance provided by Burgers University Medical Center"
    assert inst.form.coding[0].code == "ve"
    assert inst.form.coding[0].display == "Vehicle"
    assert inst.form.coding[0].system == "http://terminology.hl7.org/CodeSystem/location-physical-type"
    assert inst.id == "amb"
    assert inst.managingOrganization.reference == "Organization/f001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.mode == "kind"
    assert inst.name == "BUMC Ambulance"
    assert inst.status == "active"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Mobile "
    "Clinic</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "AMB"
    assert inst.type[0].coding[0].display == "Ambulance"
    assert inst.type[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"


def test_location_3(base_settings):
    """No. 3 tests collection for Location.
    Test File: location-example-ambulance.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "location-example-ambulance.json"
    )
    inst = location.Location.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Location" == inst.resource_type

    impl_location_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Location" == data["resourceType"]

    inst2 = location.Location(**data)
    impl_location_3(inst2)


def impl_location_4(inst):
    assert inst.extension[0].url == (
    "http://hl7.org/fhir/StructureDefinition/location-boundary-"
    "geojson"
    )
    assert inst.extension[0].valueAttachment.contentType == "application/geo+json"
    # Don't know how to create unit test
    # for "extension[0].valueAttachment.size",
    # which is a Integer64
    assert inst.extension[0].valueAttachment.url == (
    "https://github.com/OpenDataDE/State-zip-code-GeoJSON/raw/mas"
    "ter/dc_district_of_columbia_zip_codes_geo.min.json"
    )
    assert inst.form.coding[0].code == "area"
    assert inst.form.coding[0].display == "Area"
    assert inst.form.coding[0].system == "http://terminology.hl7.org/CodeSystem/location-physical-type"
    assert inst.id == "wash-dc-metro"
    assert inst.meta.profile[0] == (
    "http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-"
    "location"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.name == "Washington, DC metro area"
    assert inst.status == "active"
    assert inst.text.status == "extensions"


def test_location_4(base_settings):
    """No. 4 tests collection for Location.
    Test File: location-wash-dc-metro.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "location-wash-dc-metro.json"
    )
    inst = location.Location.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Location" == inst.resource_type

    impl_location_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Location" == data["resourceType"]

    inst2 = location.Location(**data)
    impl_location_4(inst2)


def impl_location_5(inst):
    assert inst.description == "Patient's Home"
    assert inst.form.coding[0].code == "ho"
    assert inst.form.coding[0].display == "House"
    assert inst.form.coding[0].system == "http://terminology.hl7.org/CodeSystem/location-physical-type"
    assert inst.id == "ph"
    assert inst.managingOrganization.reference == "Organization/f001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.mode == "kind"
    assert inst.name == "Patient's Home"
    assert inst.status == "active"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">Patient's "
    "Home</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "PTRES"
    assert inst.type[0].coding[0].display == "Patient's Residence"
    assert inst.type[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"


def test_location_5(base_settings):
    """No. 5 tests collection for Location.
    Test File: location-example-patients-home.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "location-example-patients-home.json"
    )
    inst = location.Location.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Location" == inst.resource_type

    impl_location_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Location" == data["resourceType"]

    inst2 = location.Location(**data)
    impl_location_5(inst2)


def impl_location_6(inst):
    assert inst.description == (
    "All Pharmacies in the United Kingdom covered by the National"
    " Pharmacy Association"
    )
    assert inst.form.coding[0].code == "jdn"
    assert inst.form.coding[0].display == "Jurisdiction"
    assert inst.form.coding[0].system == "http://terminology.hl7.org/CodeSystem/location-physical-type"
    assert inst.id == "ukp"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.mode == "kind"
    assert inst.name == "UK Pharmacies"
    assert inst.status == "active"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">UK "
    "Pharmacies</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "PHARM"
    assert inst.type[0].coding[0].display == "Pharmacy"
    assert inst.type[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"


def test_location_6(base_settings):
    """No. 6 tests collection for Location.
    Test File: location-example-ukpharmacy.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "location-example-ukpharmacy.json"
    )
    inst = location.Location.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Location" == inst.resource_type

    impl_location_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Location" == data["resourceType"]

    inst2 = location.Location(**data)
    impl_location_6(inst2)


def impl_location_7(inst):
    assert inst.contact[0].address.city == "Ann Arbor"
    assert inst.contact[0].address.country == "USA"
    assert inst.contact[0].address.line[0] == "3300 Washtenaw Avenue, Suite 227"
    assert inst.contact[0].address.postalCode == "48104"
    assert inst.contact[0].address.state == "MI"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].value == "(+1) 734-677-7777"
    assert inst.contact[0].telecom[1].system == "fax"
    assert inst.contact[0].telecom[1].value == "(+1) 734-677-6622"
    assert inst.contact[0].telecom[2].system == "email"
    assert inst.contact[0].telecom[2].value == "hq@HL7.org"
    assert inst.description == "HL7 Headquarters"
    assert inst.form.coding[0].code == "bu"
    assert inst.form.coding[0].display == "Building"
    assert inst.form.coding[0].system == "http://terminology.hl7.org/CodeSystem/location-physical-type"
    assert inst.id == "hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.mode == "instance"
    assert inst.name == "Health Level Seven International"
    assert float(inst.position.latitude) == float(-83.69471)
    assert float(inst.position.longitude) == float(42.2565)
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "SLEEP"
    assert inst.type[0].coding[0].display == "Sleep disorders unit"
    assert inst.type[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"


def test_location_7(base_settings):
    """No. 7 tests collection for Location.
    Test File: location-example-hl7hq.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "location-example-hl7hq.json"
    )
    inst = location.Location.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Location" == inst.resource_type

    impl_location_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Location" == data["resourceType"]

    inst2 = location.Location(**data)
    impl_location_7(inst2)