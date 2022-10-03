# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import searchparameter


def impl_searchparameter_1(inst):
    assert inst.base[0] == "CodeSystem"
    assert inst.code == "workflow"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.expression == (
    "CodeSystem.extension('http://hl7.org/fhir/StructureDefinitio"
    "n/codesystem-workflowStatus').value"
    )
    assert inst.id == "codesystem-extensions-CodeSystem-workflow"
    assert inst.name == "workflow"
    assert inst.processingMode == "normal"
    assert inst.status == "draft"
    assert inst.type == "token"
    assert inst.url == (
    "http://hl7.org/fhir/SearchParameter/codesystem-extensions-"
    "CodeSystem-workflow"
    )
    assert inst.version == "5.0.0"


def test_searchparameter_1(base_settings):
    """No. 1 tests collection for SearchParameter.
    Test File: codesystem-extensions-CodeSystem-workflow.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-extensions-CodeSystem-workflow.json"
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
    assert inst.base[0] == "Bundle"
    assert inst.code == "example-constraint"
    assert inst.constraint == (
    "Bundle.type = 'document' and Bundle.entry[0].resource is "
    "Composition"
    )
    assert inst.description == "Search Composition Bundle"
    assert inst.experimental is True
    assert inst.expression == "Bundle.entry[0].resource"
    assert inst.id == "example-constraint"
    assert inst.name == "example-constraint"
    assert inst.processingMode == "normal"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "draft"
    assert inst.target[0] == "Composition"
    assert inst.text.status == "generated"
    assert inst.type == "reference"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/example-constraint"


def test_searchparameter_2(base_settings):
    """No. 2 tests collection for SearchParameter.
    Test File: searchparameter-example-constraint.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "searchparameter-example-constraint.json"
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
    assert inst.base[0] == "Resource"
    assert inst.code == "_id"
    assert inst.contact[0].name == "[string]"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2013-10-23")
    assert inst.derivedFrom == "http://hl7.org/fhir/SearchParameter/Resource-id"
    assert inst.description == (
    "Search by resource identifier - e.g. same as the read "
    "interaction, but can return included resources"
    )
    assert inst.experimental is True
    assert inst.expression == "id"
    assert inst.id == "example"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.name == "ID-SEARCH-PARAMETER"
    assert inst.processingMode == "normal"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.purpose == (
    "Need to search by identifier for various infrastructural "
    "cases - mainly retrieving packages, and matching as part of "
    "a chain"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.type == "token"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/example"
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.system == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "positive"
    assert inst.useContext[0].valueCodeableConcept.coding[0].system == "http://terminology.hl7.org/CodeSystem/variant-state"
    assert inst.version == "1"


def test_searchparameter_3(base_settings):
    """No. 3 tests collection for SearchParameter.
    Test File: searchparameter-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "searchparameter-example.json"
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
    assert inst.base[0] == "CodeSystem"
    assert inst.code == "end"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.expression == (
    "CodeSystem.extension('http://hl7.org/fhir/StructureDefinitio"
    "n/codesystem-expirationDate').value"
    )
    assert inst.id == "codesystem-extensions-CodeSystem-end"
    assert inst.name == "end"
    assert inst.processingMode == "normal"
    assert inst.status == "draft"
    assert inst.type == "date"
    assert inst.url == (
    "http://hl7.org/fhir/SearchParameter/codesystem-extensions-"
    "CodeSystem-end"
    )
    assert inst.version == "5.0.0"


def test_searchparameter_4(base_settings):
    """No. 4 tests collection for SearchParameter.
    Test File: codesystem-extensions-CodeSystem-end.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-extensions-CodeSystem-end.json"
    )
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
    assert inst.base[0] == "Patient"
    assert inst.code == "part-agree"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == (
    "Search by url for a participation agreement, which is stored"
    " as an extension referencing a DocumentReference"
    )
    assert inst.experimental is True
    assert inst.expression == (
    "Patient.extension('http://example.org/fhir/StructureDefiniti"
    "on/participation-agreement').value"
    )
    assert inst.id == "example-extension"
    assert inst.name == "Example Search Parameter on an extension"
    assert inst.processingMode == "normal"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "draft"
    assert inst.target[0] == "DocumentReference"
    assert inst.text.status == "generated"
    assert inst.type == "reference"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/example-extension"


def test_searchparameter_5(base_settings):
    """No. 5 tests collection for SearchParameter.
    Test File: searchparameter-example-extension.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "searchparameter-example-extension.json"
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
    assert inst.base[0] == "ValueSet"
    assert inst.code == "workflow"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.expression == (
    "CodeSystem.extension('http://hl7.org/fhir/StructureDefinitio"
    "n/valueset-workflowStatus').value"
    )
    assert inst.id == "valueset-extensions-ValueSet-workflow"
    assert inst.name == "workflow"
    assert inst.processingMode == "normal"
    assert inst.status == "draft"
    assert inst.type == "token"
    assert inst.url == (
    "http://hl7.org/fhir/SearchParameter/valueset-extensions-"
    "ValueSet-workflow"
    )
    assert inst.version == "5.0.0"


def test_searchparameter_6(base_settings):
    """No. 6 tests collection for SearchParameter.
    Test File: valueset-extensions-ValueSet-workflow.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-extensions-ValueSet-workflow.json"
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
    assert inst.base[0] == "Patient"
    assert inst.code == "age"
    assert inst.description == (
    "Searches for patients based on age as calculated based on "
    "current date and date of birth.  Deceased patients are "
    "excluded from the search."
    )
    assert inst.experimental is True
    assert inst.expression == "Patient.birthDate"
    assert inst.id == "patient-extensions-Patient-age"
    assert inst.name == "age"
    assert inst.processingMode == "normal"
    assert inst.status == "draft"
    assert inst.type == "number"
    assert inst.url == (
    "http://hl7.org/fhir/SearchParameter/patient-extensions-"
    "Patient-age"
    )
    assert inst.version == "5.0.0"


def test_searchparameter_7(base_settings):
    """No. 7 tests collection for SearchParameter.
    Test File: patient-extensions-Patient-age.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "patient-extensions-Patient-age.json"
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
    assert inst.base[0] == "CodeSystem"
    assert inst.code == "effective"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.expression == (
    "CodeSystem.extension('http://hl7.org/fhir/StructureDefinitio"
    "n/codesystem-effectiveDate'.value)"
    )
    assert inst.id == "codesystem-extensions-CodeSystem-effective"
    assert inst.name == "effective"
    assert inst.processingMode == "normal"
    assert inst.status == "draft"
    assert inst.type == "date"
    assert inst.url == (
    "http://hl7.org/fhir/SearchParameter/codesystem-extensions-"
    "CodeSystem-effective"
    )
    assert inst.version == "5.0.0"


def test_searchparameter_8(base_settings):
    """No. 8 tests collection for SearchParameter.
    Test File: codesystem-extensions-CodeSystem-effective.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-extensions-CodeSystem-effective.json"
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


def test_searchparameter_9(base_settings):
    """No. 9 tests collection for SearchParameter.
    Test File: searchparameter-filter.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "searchparameter-filter.json"
    )
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
    assert inst.processingMode == "normal"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.purpose == "Need to search Condition by subject"
    assert inst.status == "draft"
    assert inst.target[0] == "Organization"
    assert inst.text.status == "generated"
    assert inst.type == "reference"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/example-reference"


def test_searchparameter_10(base_settings):
    """No. 10 tests collection for SearchParameter.
    Test File: searchparameter-example-reference.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "searchparameter-example-reference.json"
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