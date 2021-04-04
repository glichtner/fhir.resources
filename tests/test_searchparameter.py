# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import searchparameter


def impl_searchparameter_1(inst):
    assert inst.code == "keyword"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.id == "codesystem-extensions-CodeSystem-keyword"
    assert inst.name == "keyword"
    assert inst.status == "draft"
    assert inst.type == "string"
    assert inst.url == (
        "http://hl7.org/fhir/SearchParameter/codesystem-extensions-"
        "CodeSystem-keyword"
    )
    assert inst.version == "4.5.0"
    assert inst.xpath == (
        "f:CodeSystem/f:extension[@url='http://hl7.org/fhir/Structure"
        "Definition/codesystem-keyWord'] | /f:#keyWord"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_1(base_settings):
    """No. 1 tests collection for SearchParameter.
    Test File: codesystem-extensions-CodeSystem-keyword.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-extensions-CodeSystem-keyword.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_1(inst2)


def impl_searchparameter_2(inst):
    assert inst.code == "keyword"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.id == "valueset-extensions-ValueSet-keyword"
    assert inst.name == "keyword"
    assert inst.status == "draft"
    assert inst.type == "string"
    assert inst.url == (
        "http://hl7.org/fhir/SearchParameter/valueset-extensions-" "ValueSet-keyword"
    )
    assert inst.version == "4.5.0"
    assert inst.xpath == (
        "f:ValueSet/f:extension[@url='http://hl7.org/fhir/StructureDe"
        "finition/valueset-keyWord'] | /f:#keyWord"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_2(base_settings):
    """No. 2 tests collection for SearchParameter.
    Test File: valueset-extensions-ValueSet-keyword.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-extensions-ValueSet-keyword.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_2(inst2)


def impl_searchparameter_3(inst):
    assert inst.code == "workflow"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.id == "codesystem-extensions-CodeSystem-workflow"
    assert inst.name == "workflow"
    assert inst.status == "draft"
    assert inst.type == "token"
    assert inst.url == (
        "http://hl7.org/fhir/SearchParameter/codesystem-extensions-"
        "CodeSystem-workflow"
    )
    assert inst.version == "4.5.0"
    assert inst.xpath == (
        "f:CodeSystem/f:extension[@url='http://hl7.org/fhir/Structure"
        "Definition/codesystem-workflowStatus'] | /f:#workflowStatus"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_3(base_settings):
    """No. 3 tests collection for SearchParameter.
    Test File: codesystem-extensions-CodeSystem-workflow.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-extensions-CodeSystem-workflow.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_3(inst2)


def impl_searchparameter_4(inst):
    assert inst.base[0] == "Resource"
    assert inst.code == "_filter"
    assert inst.contact[0].name == "FHIR Project"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2018-07-26")
    assert inst.description == (
        "This is the formal declaration for the _filter parameter, "
        "documented at [http://hl7.org/fhir/search_filter.html](http:"
        "//hl7.org/fhir/search_filter.html)"
    )
    assert inst.experimental is False
    assert inst.id == "filter"
    assert inst.name == "FilterSearchParameter"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.purpose == (
        "Support combination searches when the simple name=value "
        "basis of search cannot express what is required"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.type == "special"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/filter"
    assert inst.version == "1"


def test_searchparameter_4(base_settings):
    """No. 4 tests collection for SearchParameter.
    Test File: searchparameter-filter.json
    """
    filename = base_settings["unittest_data_dir"] / "searchparameter-filter.json"
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_4(inst2)


def impl_searchparameter_5(inst):
    assert inst.base[0] == "Condition"
    assert inst.chain[0] == "name"
    assert inst.chain[1] == "identifier"
    assert inst.code == "subject"
    assert inst.contact[0].name == "[string]"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2013-10-23")
    assert inst.description == "Search by condition subject"
    assert inst.experimental is True
    assert inst.expression == "Condition.subject"
    assert inst.id == "example-reference"
    assert inst.modifier[0] == "missing"
    assert inst.name == "Example Search Parameter"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.purpose == "Need to search Condition by subject"
    assert inst.status == "draft"
    assert inst.target[0] == "Organization"
    assert inst.text.status == "generated"
    assert inst.type == "reference"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/example-reference"
    assert inst.xpathUsage == "normal"


def test_searchparameter_5(base_settings):
    """No. 5 tests collection for SearchParameter.
    Test File: searchparameter-example-reference.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "searchparameter-example-reference.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_5(inst2)


def impl_searchparameter_6(inst):
    assert inst.base[0] == "Patient"
    assert inst.code == "mothersMaidenName"
    assert inst.description == "Search based on patient's mother's maiden name"
    assert inst.experimental is True
    assert inst.expression == (
        "Patient.extension('http://hl7.org/fhir/StructureDefinition/p"
        "atient-mothersMaidenName')"
    )
    assert inst.id == "patient-extensions-Patient-mothersMaidenName"
    assert inst.name == "mothersMaidenName"
    assert inst.status == "draft"
    assert inst.type == "string"
    assert inst.url == (
        "http://hl7.org/fhir/SearchParameter/patient-extensions-"
        "Patient-mothersMaidenName"
    )
    assert inst.version == "4.5.0"
    assert inst.xpathUsage == "normal"


def test_searchparameter_6(base_settings):
    """No. 6 tests collection for SearchParameter.
    Test File: patient-extensions-Patient-mothersMaidenName.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "patient-extensions-Patient-mothersMaidenName.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_6(inst2)


def impl_searchparameter_7(inst):
    assert inst.code == "workflow"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.id == "valueset-extensions-ValueSet-workflow"
    assert inst.name == "workflow"
    assert inst.status == "draft"
    assert inst.type == "token"
    assert inst.url == (
        "http://hl7.org/fhir/SearchParameter/valueset-extensions-" "ValueSet-workflow"
    )
    assert inst.version == "4.5.0"
    assert inst.xpath == (
        "f:ValueSet/f:extension[@url='http://hl7.org/fhir/StructureDe"
        "finition/valueset-workflowStatus'] | /f:#workflowStatus"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_7(base_settings):
    """No. 7 tests collection for SearchParameter.
    Test File: valueset-extensions-ValueSet-workflow.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-extensions-ValueSet-workflow.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_7(inst2)


def impl_searchparameter_8(inst):
    assert inst.base[0] == "Patient"
    assert inst.code == "birthOrderBoolean"
    assert inst.description == (
        "Search based on whether a patient was part of a multiple " "birth or not."
    )
    assert inst.experimental is True
    assert inst.id == "patient-extensions-Patient-birthOrderBoolean"
    assert inst.name == "birthOrderBoolean"
    assert inst.status == "draft"
    assert inst.type == "token"
    assert inst.url == (
        "http://hl7.org/fhir/SearchParameter/patient-extensions-"
        "Patient-birthOrderBoolean"
    )
    assert inst.version == "4.5.0"
    assert inst.xpath == (
        "f:Patient/f:multipleBirthBoolean | " "f:Patient/f:multipleBirthInteger"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_8(base_settings):
    """No. 8 tests collection for SearchParameter.
    Test File: patient-extensions-Patient-birthOrderBoolean.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "patient-extensions-Patient-birthOrderBoolean.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_8(inst2)


def impl_searchparameter_9(inst):
    assert inst.base[0] == "Device"
    assert inst.code == "din"
    assert inst.description == "The donation identification number (DIN)"
    assert inst.experimental is True
    assert inst.expression == (
        "Device.extension('http://hl7.org/fhir/SearchParameter/device"
        "-extensions-Device-din')"
    )
    assert inst.id == "device-extensions-Device-din"
    assert inst.name == "din"
    assert inst.status == "draft"
    assert inst.type == "token"
    assert inst.url == (
        "http://hl7.org/fhir/SearchParameter/device-extensions-" "Device-din"
    )
    assert inst.version == "4.5.0"
    assert inst.xpathUsage == "normal"


def test_searchparameter_9(base_settings):
    """No. 9 tests collection for SearchParameter.
    Test File: device-extensions-Device-din.json
    """
    filename = base_settings["unittest_data_dir"] / "device-extensions-Device-din.json"
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_9(inst2)


def impl_searchparameter_10(inst):
    assert inst.code == "effective"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.id == "codesystem-extensions-CodeSystem-effective"
    assert inst.name == "effective"
    assert inst.status == "draft"
    assert inst.type == "date"
    assert inst.url == (
        "http://hl7.org/fhir/SearchParameter/codesystem-extensions-"
        "CodeSystem-effective"
    )
    assert inst.version == "4.5.0"
    assert inst.xpath == (
        "f:CodeSystem/f:extension[@url='http://hl7.org/fhir/Structure"
        "Definition/codesystem-effectiveDate'] | /f:#effectiveDate"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_10(base_settings):
    """No. 10 tests collection for SearchParameter.
    Test File: codesystem-extensions-CodeSystem-effective.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-extensions-CodeSystem-effective.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_10(inst2)
