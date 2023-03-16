# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import diagnosticreport


def impl_diagnosticreport_1(inst):
    assert inst.code.coding[0].code == "38269-7"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "DXA BONE DENSITOMETRY"
    assert inst.conclusionCode[0].coding[0].code == "391040000"
    assert inst.conclusionCode[0].coding[0].display == "At risk of osteoporotic fracture"
    assert inst.conclusionCode[0].coding[0].system == "http://snomed.info/sct"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2008-06-17")
    assert inst.id == "102"
    assert inst.issued == fhirtypes.Instant.validate("2008-06-18T09:23:00+10:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].display == "Dr Henry Seven"
    assert inst.performer[0].reference == "Practitioner/3ad0687e-f477-468c-afd5-fcc2bf897809"
    assert inst.result[0].reference == "Observation/bmd"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"


def test_diagnosticreport_1(base_settings):
    """No. 1 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-dxa.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example-dxa.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_1(inst2)


def impl_diagnosticreport_2(inst):
    assert inst.category[0].coding[0].code == "394914008"
    assert inst.category[0].coding[0].display == "Radiology"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].coding[1].code == "RAD"
    assert inst.category[0].coding[1].system == "http://terminology.hl7.org/CodeSystem/v2-0074"
    assert inst.code.coding[0].code == "429858000"
    assert inst.code.coding[0].display == "Computed tomography (CT) of head and neck"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "CT of head-neck"
    assert inst.conclusion == "CT brains: large tumor sphenoid/clivus."
    assert inst.conclusionCode[0].coding[0].code == "188340000"
    assert inst.conclusionCode[0].coding[0].display == "Malignant tumor of craniopharyngeal duct"
    assert inst.conclusionCode[0].coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "is1"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2012-12-01T12:00:00+01:00")
    assert inst.id == "f201"
    assert inst.issued == fhirtypes.Instant.validate("2012-12-01T12:00:00+01:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].display == "Blijdorp MC"
    assert inst.performer[0].reference == "Organization/f203"
    assert inst.status == "final"
    assert inst.study[0].reference == "#is1"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"


def test_diagnosticreport_2(base_settings):
    """No. 2 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-f201-brainct.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example-f201-brainct.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_2(inst2)


def impl_diagnosticreport_3(inst):
    assert inst.category[0].coding[0].code == "PAT"
    assert inst.category[0].coding[0].display == "Pathology (gross & histopath, not surgical)"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0074"
    assert inst.category[0].text == "Pathology"
    assert inst.code.coding[0].code == "4503"
    assert inst.code.coding[0].display == (
    "Biopsy without Microscopic Description (1 "
    "Site/Lesion)-Standard"
    )
    assert inst.code.coding[0].system == "https://www.acmeonline.com"
    assert inst.code.text == (
    "Biopsy without Microscopic Description (1 "
    "Site/Lesion)-Standard"
    )
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2018-03-02")
    assert inst.id == "gingival-biopsy"
    assert inst.identifier[0].system == "https://www.acmeonline.com"
    assert inst.identifier[0].value == "P73456090"
    assert inst.issued == fhirtypes.Instant.validate("2018-03-15T08:13:08Z")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].display == "Acme Animal Labs"
    assert inst.presentedForm[0].contentType == "application/pdf"
    assert inst.presentedForm[0].language == "en"
    assert inst.presentedForm[0].title == (
    "LAB ID: P73456090 MAX JONES Biopsy without Microscopic "
    "Description (1 Site/Lesion)-Standard"
    )
    assert inst.status == "final"
    assert inst.subject.display == "Max Jones"
    assert inst.supportingInfo[0].reference.reference == "DiagnosticReport/gingival-mass"
    assert inst.supportingInfo[0].type.coding[0].code == "historical"
    assert inst.text.status == "generated"


def test_diagnosticreport_3(base_settings):
    """No. 3 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-gingival-biopsy.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example-gingival-biopsy.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_3(inst2)


def impl_diagnosticreport_4(inst):
    assert inst.category[0].coding[0].code == "PAT"
    assert inst.category[0].coding[0].display == "Pathology (gross & histopath, not surgical)"
    assert inst.category[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0074"
    assert inst.category[0].text == "Pathology"
    assert inst.code.coding[0].code == "4503"
    assert inst.code.coding[0].display == (
    "Biopsy without Microscopic Description (1 "
    "Site/Lesion)-Standard"
    )
    assert inst.code.coding[0].system == "https://www.acmeonline.com"
    assert inst.code.text == (
    "Biopsy without Microscopic Description (1 "
    "Site/Lesion)-Standard"
    )
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2017-03-02")
    assert inst.id == "gingival-mass"
    assert inst.identifier[0].system == "https://www.acmeonline.com"
    assert inst.identifier[0].value == "P73456090"
    assert inst.issued == fhirtypes.Instant.validate("2017-03-15T08:13:08Z")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].display == "Acme Animal Labs"
    assert inst.presentedForm[0].contentType == "application/pdf"
    assert inst.presentedForm[0].language == "en"
    assert inst.presentedForm[0].title == (
    "LAB ID: P73456090 MAX JONES Biopsy without Microscopic "
    "Description (1 Site/Lesion)-Standard"
    )
    assert inst.status == "final"
    assert inst.subject.display == "Max Jones"
    assert inst.text.status == "generated"


def test_diagnosticreport_4(base_settings):
    """No. 4 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-gingival-mass.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example-gingival-mass.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_4(inst2)


def impl_diagnosticreport_5(inst):
    assert inst.category[0].coding[0].code == "394914008"
    assert inst.category[0].coding[0].display == "Radiology"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].coding[1].code == "RAD"
    assert inst.category[0].coding[1].system == "http://terminology.hl7.org/CodeSystem/v2-0074"
    assert inst.code.coding[0].code == "45036003"
    assert inst.code.coding[0].display == "Ultrasonography of abdomen"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Abdominal Ultrasound"
    assert inst.conclusion == "Unremarkable study"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2012-12-01T12:00:00+01:00")
    assert inst.id == "ultrasound"
    assert inst.issued == fhirtypes.Instant.validate("2012-12-01T12:00:00+01:00")
    assert inst.media[0].comment == "A comment about the image"
    assert inst.media[0].link.display == "WADO example image"
    assert inst.media[0].link.reference == (
    "DocumentReference/1.2.840.11361907579238403408700.3.1.04.199"
    "70327150033"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_diagnosticreport_5(base_settings):
    """No. 5 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-ultrasound.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example-ultrasound.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_5(inst2)


def impl_diagnosticreport_6(inst):
    assert inst.code.coding[0].code == "47527-7"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2013-02-11T10:33:33+11:00")
    assert inst.id == "pap"
    assert inst.issued == fhirtypes.Instant.validate("2013-02-13T11:45:33+11:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/b248b1b2-1686-4b94-9936-37d7a5f94b51"
    assert inst.text.status == "additional"


def test_diagnosticreport_6(base_settings):
    """No. 6 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-papsmear.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example-papsmear.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_6(inst2)