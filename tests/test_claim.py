# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import claim


def impl_claim_1(inst):
    assert (
        inst.careTeam[0].provider.identifier.system
        == "http://www.jurisdiction.com/providerId"
    )
    assert inst.careTeam[0].provider.identifier.value == "MD98765"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "123456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "100154"
    assert inst.identifier[0].system == "http://happyvalley.com/claim"
    assert inst.identifier[0].value == "12347"
    assert (
        inst.insurance[0].coverage.identifier.system
        == "http://www.jurisdiction.com/nationalplan"
    )
    assert inst.insurance[0].coverage.identifier.value == "123AB345"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.identifier.system == "http://www.jurisdiction.com/insurers"
    assert inst.insurer.identifier.value == "123456"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(135.57)
    assert inst.item[0].productOrService.coding[0].code == "1200"
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.currency == "USD"
    assert float(inst.item[0].unitPrice.value) == float(135.57)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.identifier.system == "http://www.jurisdiction.com/nationalId"
    assert inst.patient.identifier.value == "123AB345"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert (
        inst.provider.identifier.system
        == "http://www.jurisdiction.com/careorganizations"
    )
    assert inst.provider.identifier.value == "HOSP12345"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">This example '
        "assumes a national health care scheme where patients, "
        "providers and organizations have known business "
        "identifiers.</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "oral"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_claim_1(base_settings):
    """No. 1 tests collection for Claim.
    Test File: claim-example-oral-identifier.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-oral-identifier.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_1(inst2)


def impl_claim_2(inst):
    assert (
        inst.careTeam[0].provider.identifier.system
        == "http://www.jurisdiction.com/providerId"
    )
    assert inst.careTeam[0].provider.identifier.value == "MD98765"
    assert inst.careTeam[0].sequence == 1
    assert inst.contained[0].id == "patient-1"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "123456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "100155"
    assert inst.identifier[0].system == "http://happyvalley.com/claim"
    assert inst.identifier[0].value == "12347"
    assert (
        inst.insurance[0].coverage.reference
        == "http://www.jurisdiction.com/nationalplan/123AB345"
    )
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.identifier.system == "http://www.jurisdiction.com/insurers"
    assert inst.insurer.identifier.value == "123456"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(135.57)
    assert inst.item[0].productOrService.coding[0].code == "1200"
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.currency == "USD"
    assert float(inst.item[0].unitPrice.value) == float(135.57)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "#patient-1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert (
        inst.provider.identifier.system
        == "http://www.jurisdiction.com/careorganizations"
    )
    assert inst.provider.identifier.value == "HOSP12345"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">This example '
        "assumes a national health care scheme where patients, "
        "providers and organizations have known business "
        "identifiers.</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "oral"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_claim_2(base_settings):
    """No. 2 tests collection for Claim.
    Test File: claim-example-oral-contained-identifier.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "claim-example-oral-contained-identifier.json"
    )
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_2(inst2)


def impl_claim_3(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.contained[0].id == "patient-1"
    assert inst.contained[1].id == "coverage-1"
    assert inst.created == fhirtypes.DateTime.validate("2015-10-16T00:00:00-07:00")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "M96.1"
    assert (
        inst.diagnosis[0].diagnosisCodeableConcept.coding[0].display
        == "Postlaminectomy syndrome, not elsewhere classified"
    )
    assert (
        inst.diagnosis[0].diagnosisCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/sid/icd-10-cm"
    )
    assert inst.diagnosis[0].sequence == 1
    assert inst.diagnosis[1].diagnosisCodeableConcept.coding[0].code == "G89.4"
    assert (
        inst.diagnosis[1].diagnosisCodeableConcept.coding[0].display
        == "Chronic pain syndrome"
    )
    assert (
        inst.diagnosis[1].diagnosisCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/sid/icd-10-cm"
    )
    assert inst.diagnosis[1].sequence == 2
    assert inst.diagnosis[2].diagnosisCodeableConcept.coding[0].code == "M53.88"
    assert inst.diagnosis[2].diagnosisCodeableConcept.coding[0].display == (
        "Other specified dorsopathies, sacral and sacrococcygeal " "region"
    )
    assert (
        inst.diagnosis[2].diagnosisCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/sid/icd-10-cm"
    )
    assert inst.diagnosis[2].sequence == 3
    assert inst.diagnosis[3].diagnosisCodeableConcept.coding[0].code == "M47.816"
    assert inst.diagnosis[3].diagnosisCodeableConcept.coding[0].display == (
        "Spondylosis without myelopathy or radiculopathy, lumbar " "region"
    )
    assert (
        inst.diagnosis[3].diagnosisCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/sid/icd-10-cm"
    )
    assert inst.diagnosis[3].sequence == 4
    assert inst.id == "MED-00050"
    assert inst.identifier[0].system == "http://CedarArmsMedicalCenter.com/claim"
    assert inst.identifier[0].value == "MED-00050"
    assert inst.insurance[0].coverage.reference == "#coverage-1"
    assert inst.insurance[0].focal is True
    assert (
        inst.insurance[0].identifier.system == "http://CedarArmsMedicalCenter.com/claim"
    )
    assert inst.insurance[0].identifier.value == "MED-00050"
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.display == "Humana Inc."
    assert inst.insurer.identifier.system == "http://www.bindb.com/bin"
    assert inst.insurer.identifier.value == "123456"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].diagnosisSequence[0] == 2
    assert inst.item[0].diagnosisSequence[1] == 4
    assert inst.item[0].informationSequence[0] == 1
    assert inst.item[0].locationCodeableConcept.coding[0].code == "24"
    assert (
        inst.item[0].locationCodeableConcept.coding[0].display
        == "Ambulatory Surgical Center"
    )
    assert inst.item[0].locationCodeableConcept.coding[0].system == (
        "https://www.cms.gov/medicare/coding/place-of-service-"
        "codes/place_of_service_code_set.html"
    )
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(12500.0)
    assert inst.item[0].productOrService.coding[0].code == "62264"
    assert (
        inst.item[0].productOrService.coding[0].display
        == "Surgical Procedures on the Spine and Spinal Cord"
    )
    assert (
        inst.item[0].productOrService.coding[0].system
        == "http://www.ama-assn.org/go/cpt"
    )
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2015-10-13")
    assert inst.item[0].unitPrice.currency == "USD"
    assert float(inst.item[0].unitPrice.value) == float(12500.0)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "#patient-1"
    assert inst.payee.party.reference == "Organization/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert (
        inst.payee.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/payeetype"
    )
    assert inst.priority.coding[0].code == "normal"
    assert inst.provider.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.subType.coding[0].code == "831"
    assert inst.subType.coding[0].system == "https://www.cms.gov/codes/billtype"
    assert inst.supportingInfo[0].category.coding[0].code == "hospitalized"
    assert inst.supportingInfo[0].category.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/claiminformationcatego" "ry"
    )
    assert inst.supportingInfo[0].sequence == 1
    assert inst.supportingInfo[0].timingPeriod.end == fhirtypes.DateTime.validate(
        "2015-10-05T00:00:00-07:00"
    )
    assert inst.supportingInfo[0].timingPeriod.start == fhirtypes.DateTime.validate(
        "2015-10-01T00:00:00-07:00"
    )
    assert inst.supportingInfo[1].category.coding[0].code == "discharge"
    assert inst.supportingInfo[1].category.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/claiminformationcatego" "ry"
    )
    assert inst.supportingInfo[1].code.coding[0].code == "01"
    assert (
        inst.supportingInfo[1].code.coding[0].display
        == "Discharge to Home or Self Care"
    )
    assert inst.supportingInfo[1].code.coding[0].system == (
        "https://www.cms.gov/Outreach-and-Education/Medicare-"
        "Learning-Network-MLN/MLNMattersArticles/downloads/SE0801.pdf"
    )
    assert inst.supportingInfo[1].sequence == 2
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of a CMS 1500 Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total.currency == "USD"
    assert float(inst.total.value) == float(12500.0)
    assert inst.type.coding[0].code == "institutional"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_claim_3(base_settings):
    """No. 3 tests collection for Claim.
    Test File: claim-example-cms1500-medical.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-cms1500-medical.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_3(inst2)


def impl_claim_4(inst):
    assert inst.careTeam[0].provider.reference == "#provider-1"
    assert inst.careTeam[0].sequence == 1
    assert inst.contained[0].id == "org-insurer"
    assert inst.contained[1].id == "org-org"
    assert inst.contained[2].id == "provider-1"
    assert inst.contained[3].id == "patient-1"
    assert inst.contained[4].id == "coverage-1"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "123456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "100152"
    assert inst.identifier[0].system == "http://happyvalley.com/claim"
    assert inst.identifier[0].value == "12347"
    assert inst.insurance[0].coverage.reference == "#coverage-1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "#org-insurer"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(135.57)
    assert inst.item[0].productOrService.coding[0].code == "1200"
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.currency == "USD"
    assert float(inst.item[0].unitPrice.value) == float(135.57)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "#patient-1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.provider.reference == "#org-org"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Oral Health Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "oral"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_claim_4(base_settings):
    """No. 4 tests collection for Claim.
    Test File: claim-example-oral-contained.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-oral-contained.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_4(inst2)


def impl_claim_5(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.contained[0].id == "device-frame"
    assert inst.contained[1].id == "device-lens"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654321"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "660152"
    assert inst.identifier[0].system == "http://happysight.com/claim"
    assert inst.identifier[0].value == "6612347"
    assert inst.insurance[0].claimResponse.reference == "ClaimResponse/R3500"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is False
    assert inst.insurance[0].preAuthRef[0] == "PR7652387237"
    assert inst.insurance[0].sequence == 1
    assert inst.insurance[1].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[1].focal is True
    assert inst.insurance[1].preAuthRef[0] == "AB543GTD7567"
    assert inst.insurance[1].sequence == 2
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].category.coding[0].code == "F6"
    assert inst.item[0].category.coding[0].display == "Vision Coverage"
    assert (
        inst.item[0].category.coding[0].system
        == "http://example.org/fhir/CodeSystem/benefit-subcategory"
    )
    assert inst.item[0].detail[0].category.coding[0].code == "F6"
    assert inst.item[0].detail[0].category.coding[0].display == "Vision Coverage"
    assert (
        inst.item[0].detail[0].category.coding[0].system
        == "http://example.org/fhir/CodeSystem/benefit-subcategory"
    )
    assert float(inst.item[0].detail[0].factor) == float(1.1)
    assert inst.item[0].detail[0].modifier[0].coding[0].code == "rooh"
    assert (
        inst.item[0].detail[0].modifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/modifiers"
    )
    assert inst.item[0].detail[0].net.currency == "USD"
    assert float(inst.item[0].detail[0].net.value) == float(110.0)
    assert inst.item[0].detail[0].productOrService.coding[0].code == "frame"
    assert (
        inst.item[0].detail[0].productOrService.coding[0].system
        == "http://example.org/fhir/CodeSystem/ex-visionservice"
    )
    assert inst.item[0].detail[0].revenue.coding[0].code == "0010"
    assert inst.item[0].detail[0].revenue.coding[0].display == "Vision Clinic"
    assert (
        inst.item[0].detail[0].revenue.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-revenue-center"
    )
    assert inst.item[0].detail[0].sequence == 1
    assert inst.item[0].detail[0].udi[0].reference == "#device-frame"
    assert inst.item[0].detail[0].unitPrice.currency == "USD"
    assert float(inst.item[0].detail[0].unitPrice.value) == float(100.0)
    assert inst.item[0].detail[1].category.coding[0].code == "F6"
    assert inst.item[0].detail[1].category.coding[0].display == "Vision Coverage"
    assert (
        inst.item[0].detail[1].category.coding[0].system
        == "http://example.org/fhir/CodeSystem/benefit-subcategory"
    )
    assert inst.item[0].detail[1].net.currency == "USD"
    assert float(inst.item[0].detail[1].net.value) == float(110.0)
    assert inst.item[0].detail[1].productOrService.coding[0].code == "lens"
    assert (
        inst.item[0].detail[1].productOrService.coding[0].system
        == "http://example.org/fhir/CodeSystem/ex-visionservice"
    )
    assert inst.item[0].detail[1].programCode[0].coding[0].code == "none"
    assert (
        inst.item[0].detail[1].programCode[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-programcode"
    )
    assert float(inst.item[0].detail[1].quantity.value) == float(2)
    assert inst.item[0].detail[1].revenue.coding[0].code == "0010"
    assert inst.item[0].detail[1].revenue.coding[0].display == "Vision Clinic"
    assert (
        inst.item[0].detail[1].revenue.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-revenue-center"
    )
    assert inst.item[0].detail[1].sequence == 2
    assert inst.item[0].detail[1].subDetail[0].category.coding[0].code == "F6"
    assert (
        inst.item[0].detail[1].subDetail[0].category.coding[0].display
        == "Vision Coverage"
    )
    assert (
        inst.item[0].detail[1].subDetail[0].category.coding[0].system
        == "http://example.org/fhir/CodeSystem/benefit-subcategory"
    )
    assert float(inst.item[0].detail[1].subDetail[0].factor) == float(1.1)
    assert inst.item[0].detail[1].subDetail[0].modifier[0].coding[0].code == "rooh"
    assert (
        inst.item[0].detail[1].subDetail[0].modifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/modifiers"
    )
    assert inst.item[0].detail[1].subDetail[0].net.currency == "USD"
    assert float(inst.item[0].detail[1].subDetail[0].net.value) == float(66.0)
    assert inst.item[0].detail[1].subDetail[0].productOrService.coding[0].code == "lens"
    assert (
        inst.item[0].detail[1].subDetail[0].productOrService.coding[0].system
        == "http://example.org/fhir/CodeSystem/ex-visionservice"
    )
    assert inst.item[0].detail[1].subDetail[0].programCode[0].coding[0].code == "none"
    assert (
        inst.item[0].detail[1].subDetail[0].programCode[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-programcode"
    )
    assert float(inst.item[0].detail[1].subDetail[0].quantity.value) == float(2)
    assert inst.item[0].detail[1].subDetail[0].revenue.coding[0].code == "0010"
    assert (
        inst.item[0].detail[1].subDetail[0].revenue.coding[0].display == "Vision Clinic"
    )
    assert (
        inst.item[0].detail[1].subDetail[0].revenue.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-revenue-center"
    )
    assert inst.item[0].detail[1].subDetail[0].sequence == 1
    assert inst.item[0].detail[1].subDetail[0].udi[0].reference == "#device-lens"
    assert inst.item[0].detail[1].subDetail[0].unitPrice.currency == "USD"
    assert float(inst.item[0].detail[1].subDetail[0].unitPrice.value) == float(30.0)
    assert inst.item[0].detail[1].subDetail[1].category.coding[0].code == "F6"
    assert (
        inst.item[0].detail[1].subDetail[1].category.coding[0].display
        == "Vision Coverage"
    )
    assert (
        inst.item[0].detail[1].subDetail[1].category.coding[0].system
        == "http://example.org/fhir/CodeSystem/benefit-subcategory"
    )
    assert float(inst.item[0].detail[1].subDetail[1].factor) == float(1.1)
    assert inst.item[0].detail[1].subDetail[1].modifier[0].coding[0].code == "rooh"
    assert (
        inst.item[0].detail[1].subDetail[1].modifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/modifiers"
    )
    assert inst.item[0].detail[1].subDetail[1].net.currency == "USD"
    assert float(inst.item[0].detail[1].subDetail[1].net.value) == float(33.0)
    assert (
        inst.item[0].detail[1].subDetail[1].productOrService.coding[0].code
        == "hardening"
    )
    assert (
        inst.item[0].detail[1].subDetail[1].productOrService.coding[0].system
        == "http://example.org/fhir/CodeSystem/ex-visionservice"
    )
    assert float(inst.item[0].detail[1].subDetail[1].quantity.value) == float(2)
    assert inst.item[0].detail[1].subDetail[1].revenue.coding[0].code == "0010"
    assert (
        inst.item[0].detail[1].subDetail[1].revenue.coding[0].display == "Vision Clinic"
    )
    assert (
        inst.item[0].detail[1].subDetail[1].revenue.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-revenue-center"
    )
    assert inst.item[0].detail[1].subDetail[1].sequence == 2
    assert inst.item[0].detail[1].subDetail[1].unitPrice.currency == "USD"
    assert float(inst.item[0].detail[1].subDetail[1].unitPrice.value) == float(15.0)
    assert inst.item[0].detail[1].subDetail[2].category.coding[0].code == "F6"
    assert (
        inst.item[0].detail[1].subDetail[2].category.coding[0].display
        == "Vision Coverage"
    )
    assert (
        inst.item[0].detail[1].subDetail[2].category.coding[0].system
        == "http://example.org/fhir/CodeSystem/benefit-subcategory"
    )
    assert float(inst.item[0].detail[1].subDetail[2].factor) == float(1.1)
    assert inst.item[0].detail[1].subDetail[2].modifier[0].coding[0].code == "rooh"
    assert (
        inst.item[0].detail[1].subDetail[2].modifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/modifiers"
    )
    assert inst.item[0].detail[1].subDetail[2].net.currency == "USD"
    assert float(inst.item[0].detail[1].subDetail[2].net.value) == float(11.0)
    assert (
        inst.item[0].detail[1].subDetail[2].productOrService.coding[0].code
        == "UV coating"
    )
    assert (
        inst.item[0].detail[1].subDetail[2].productOrService.coding[0].system
        == "http://example.org/fhir/CodeSystem/ex-visionservice"
    )
    assert float(inst.item[0].detail[1].subDetail[2].quantity.value) == float(2)
    assert inst.item[0].detail[1].subDetail[2].revenue.coding[0].code == "0010"
    assert (
        inst.item[0].detail[1].subDetail[2].revenue.coding[0].display == "Vision Clinic"
    )
    assert (
        inst.item[0].detail[1].subDetail[2].revenue.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-revenue-center"
    )
    assert inst.item[0].detail[1].subDetail[2].sequence == 3
    assert inst.item[0].detail[1].subDetail[2].unitPrice.currency == "USD"
    assert float(inst.item[0].detail[1].subDetail[2].unitPrice.value) == float(5.0)
    assert inst.item[0].detail[1].unitPrice.currency == "USD"
    assert float(inst.item[0].detail[1].unitPrice.value) == float(55.0)
    assert inst.item[0].detail[2].category.coding[0].code == "F6"
    assert inst.item[0].detail[2].category.coding[0].display == "Vision Coverage"
    assert (
        inst.item[0].detail[2].category.coding[0].system
        == "http://example.org/fhir/CodeSystem/benefit-subcategory"
    )
    assert float(inst.item[0].detail[2].factor) == float(0.07)
    assert inst.item[0].detail[2].net.currency == "USD"
    assert float(inst.item[0].detail[2].net.value) == float(15.4)
    assert inst.item[0].detail[2].productOrService.coding[0].code == "fst"
    assert (
        inst.item[0].detail[2].productOrService.coding[0].system
        == "http://example.org/fhir/CodeSystem/ex-visionservice"
    )
    assert inst.item[0].detail[2].revenue.coding[0].code == "0010"
    assert inst.item[0].detail[2].revenue.coding[0].display == "Vision Clinic"
    assert (
        inst.item[0].detail[2].revenue.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-revenue-center"
    )
    assert inst.item[0].detail[2].sequence == 3
    assert inst.item[0].detail[2].unitPrice.currency == "USD"
    assert float(inst.item[0].detail[2].unitPrice.value) == float(220.0)
    assert inst.item[0].modifier[0].coding[0].code == "rooh"
    assert (
        inst.item[0].modifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/modifiers"
    )
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(235.4)
    assert inst.item[0].productOrService.coding[0].code == "glasses"
    assert (
        inst.item[0].productOrService.coding[0].system
        == "http://example.org/fhir/CodeSystem/ex-visionservice"
    )
    assert inst.item[0].programCode[0].coding[0].code == "none"
    assert (
        inst.item[0].programCode[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-programcode"
    )
    assert inst.item[0].revenue.coding[0].code == "0010"
    assert inst.item[0].revenue.coding[0].display == "Vision Clinic"
    assert (
        inst.item[0].revenue.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-revenue-center"
    )
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.currency == "USD"
    assert float(inst.item[0].unitPrice.value) == float(235.4)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.prescription.reference == "http://www.optdocs.com/prescription/12345"
    assert inst.priority.coding[0].code == "normal"
    assert inst.provider.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Vision Claim for Glasses</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "vision"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_claim_5(base_settings):
    """No. 5 tests collection for Claim.
    Test File: claim-example-vision-glasses-3tier.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "claim-example-vision-glasses-3tier.json"
    )
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_5(inst2)


def impl_claim_6(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "860150"
    assert inst.identifier[0].system == "http://happypdocs.com/claim"
    assert inst.identifier[0].value == "8612345"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(75.0)
    assert inst.item[0].productOrService.coding[0].code == "exam"
    assert (
        inst.item[0].productOrService.coding[0].system
        == "http://hl7.org/fhir/ex-serviceproduct"
    )
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.currency == "USD"
    assert float(inst.item[0].unitPrice.value) == float(75.0)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.provider.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "professional"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_claim_6(base_settings):
    """No. 6 tests collection for Claim.
    Test File: claim-example-professional.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-professional.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_6(inst2)


def impl_claim_7(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654321"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "660150"
    assert inst.identifier[0].system == "http://happysight.com/claim"
    assert inst.identifier[0].value == "6612345"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(80.0)
    assert inst.item[0].productOrService.coding[0].code == "exam"
    assert (
        inst.item[0].productOrService.coding[0].system
        == "http://example.org/fhir/CodeSystem/ex-visionservice"
    )
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.currency == "USD"
    assert float(inst.item[0].unitPrice.value) == float(80.0)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.provider.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Vision Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "vision"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_claim_7(base_settings):
    """No. 7 tests collection for Claim.
    Test File: claim-example-vision.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-vision.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_7(inst2)


def impl_claim_8(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654456"
    assert inst.diagnosis[0].sequence == 1
    assert (
        inst.enterer.identifier.system
        == "http://jurisdiction.org/facilities/HOSP1234/users"
    )
    assert inst.enterer.identifier.value == "UC1234"
    assert inst.facility.identifier.system == "http://jurisdiction.org/facilities"
    assert inst.facility.identifier.value == "HOSP1234"
    assert inst.id == "960150"
    assert inst.identifier[0].system == "http://happyhospital.com/claim"
    assert inst.identifier[0].value == "9612345"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].encounter[0].reference == "Encounter/example"
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(125.0)
    assert inst.item[0].productOrService.coding[0].code == "exam"
    assert (
        inst.item[0].productOrService.coding[0].system
        == "http://hl7.org/fhir/ex-serviceproduct"
    )
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.currency == "USD"
    assert float(inst.item[0].unitPrice.value) == float(125.0)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.procedure[0].date == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.procedure[0].procedureCodeableConcept.coding[0].code == "SDI9901"
    assert (
        inst.procedure[0].procedureCodeableConcept.text
        == "Subcutaneous diagnostic implant"
    )
    assert inst.procedure[0].sequence == 1
    assert inst.procedure[0].type[0].coding[0].code == "primary"
    assert inst.procedure[0].udi[0].reference == "Device/example"
    assert inst.provider.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.subType.coding[0].code == "emergency"
    assert (
        inst.subType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-claimsubtype"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total.currency == "USD"
    assert float(inst.total.value) == float(125.0)
    assert inst.type.coding[0].code == "institutional"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_claim_8(base_settings):
    """No. 8 tests collection for Claim.
    Test File: claim-example-institutional.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-institutional.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_8(inst2)


def impl_claim_9(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "760152"
    assert inst.identifier[0].system == "http://happypharma.com/claim"
    assert inst.identifier[0].value == "7612345"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].detail[0].net.currency == "USD"
    assert float(inst.item[0].detail[0].net.value) == float(20.0)
    assert inst.item[0].detail[0].productOrService.coding[0].code == "44001"
    assert (
        inst.item[0].detail[0].productOrService.coding[0].display
        == "Acetaminophen 250mg"
    )
    assert (
        inst.item[0].detail[0].productOrService.coding[0].system
        == "http://localdruglist.org"
    )
    assert inst.item[0].detail[0].quantity.unit == "mg"
    assert float(inst.item[0].detail[0].quantity.value) == float(250)
    assert inst.item[0].detail[0].sequence == 1
    assert inst.item[0].detail[0].subDetail[0].net.currency == "USD"
    assert float(inst.item[0].detail[0].subDetail[0].net.value) == float(20.0)
    assert (
        inst.item[0].detail[0].subDetail[0].productOrService.coding[0].code
        == "drugcost"
    )
    assert (
        inst.item[0].detail[0].subDetail[0].productOrService.coding[0].system
        == "http://hl7.org/fhir/ex-pharmaservice"
    )
    assert inst.item[0].detail[0].subDetail[0].sequence == 1
    assert inst.item[0].detail[1].net.currency == "USD"
    assert float(inst.item[0].detail[1].net.value) == float(25.0)
    assert inst.item[0].detail[1].productOrService.coding[0].code == "44035"
    assert (
        inst.item[0].detail[1].productOrService.coding[0].display == "Phenacetin 50mg"
    )
    assert (
        inst.item[0].detail[1].productOrService.coding[0].system
        == "http://localdruglist.org"
    )
    assert inst.item[0].detail[1].quantity.unit == "mg"
    assert float(inst.item[0].detail[1].quantity.value) == float(50)
    assert inst.item[0].detail[1].sequence == 2
    assert inst.item[0].detail[1].subDetail[0].net.currency == "USD"
    assert float(inst.item[0].detail[1].subDetail[0].net.value) == float(25.0)
    assert (
        inst.item[0].detail[1].subDetail[0].productOrService.coding[0].code
        == "drugcost"
    )
    assert (
        inst.item[0].detail[1].subDetail[0].productOrService.coding[0].system
        == "http://hl7.org/fhir/ex-pharmaservice"
    )
    assert inst.item[0].detail[1].subDetail[0].sequence == 1
    assert inst.item[0].detail[2].net.currency == "USD"
    assert float(inst.item[0].detail[2].net.value) == float(28.0)
    assert inst.item[0].detail[2].productOrService.coding[0].code == "44057"
    assert inst.item[0].detail[2].productOrService.coding[0].display == "Codeine 25mg"
    assert (
        inst.item[0].detail[2].productOrService.coding[0].system
        == "http://localdruglist.org"
    )
    assert inst.item[0].detail[2].quantity.unit == "mg"
    assert float(inst.item[0].detail[2].quantity.value) == float(25)
    assert inst.item[0].detail[2].sequence == 3
    assert inst.item[0].detail[2].subDetail[0].net.currency == "USD"
    assert float(inst.item[0].detail[2].subDetail[0].net.value) == float(28.0)
    assert (
        inst.item[0].detail[2].subDetail[0].productOrService.coding[0].code
        == "drugcost"
    )
    assert (
        inst.item[0].detail[2].subDetail[0].productOrService.coding[0].system
        == "http://hl7.org/fhir/ex-pharmaservice"
    )
    assert inst.item[0].detail[2].subDetail[0].sequence == 1
    assert inst.item[0].detail[3].net.currency == "USD"
    assert float(inst.item[0].detail[3].net.value) == float(22.0)
    assert inst.item[0].detail[3].productOrService.coding[0].code == "markup"
    assert (
        inst.item[0].detail[3].productOrService.coding[0].system
        == "http://hl7.org/fhir/ex-pharmaservice"
    )
    assert inst.item[0].detail[3].sequence == 2
    assert inst.item[0].detail[4].net.currency == "USD"
    assert float(inst.item[0].detail[4].net.value) == float(60.0)
    assert inst.item[0].detail[4].productOrService.coding[0].code == "compoundfee"
    assert (
        inst.item[0].detail[4].productOrService.coding[0].system
        == "http://hl7.org/fhir/ex-pharmaservice"
    )
    assert inst.item[0].detail[4].sequence == 3
    assert inst.item[0].informationSequence[0] == 1
    assert inst.item[0].informationSequence[1] == 2
    assert inst.item[0].informationSequence[2] == 3
    assert inst.item[0].informationSequence[3] == 4
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(155.0)
    assert inst.item[0].productOrService.coding[0].code == "compound"
    assert inst.item[0].productOrService.coding[0].display == "Custom compound"
    assert inst.item[0].productOrService.coding[0].system == "http://localdruglist.org"
    assert inst.item[0].quantity.code == "TAB"
    assert (
        inst.item[0].quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.item[0].quantity.unit == "TAB"
    assert float(inst.item[0].quantity.value) == float(30)
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "stat"
    assert inst.provider.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.supportingInfo[0].category.coding[0].code == "pharmacyrefill"
    assert inst.supportingInfo[0].code.coding[0].code == "new"
    assert (
        inst.supportingInfo[0].code.coding[0].system
        == "http://example.org/fhir/CodeSystem/pharmacy-refill"
    )
    assert inst.supportingInfo[0].sequence == 1
    assert inst.supportingInfo[1].category.coding[0].code == "pharmacyinformation"
    assert inst.supportingInfo[1].code.coding[0].code == "refillsremaining"
    assert (
        inst.supportingInfo[1].code.coding[0].system
        == "http://example.org/fhir/CodeSystem/pharmacy-information"
    )
    assert inst.supportingInfo[1].sequence == 2
    assert float(inst.supportingInfo[1].valueQuantity.value) == float(0)
    assert inst.supportingInfo[2].category.coding[0].code == "pharmacyinformation"
    assert inst.supportingInfo[2].code.coding[0].code == "dayssupply"
    assert (
        inst.supportingInfo[2].code.coding[0].system
        == "http://example.org/fhir/CodeSystem/pharmacy-information"
    )
    assert inst.supportingInfo[2].sequence == 3
    assert float(inst.supportingInfo[2].valueQuantity.value) == float(10)
    assert inst.supportingInfo[3].category.coding[0].code == "pharmacy"
    assert inst.supportingInfo[3].code.coding[0].code == "capsule"
    assert (
        inst.supportingInfo[3].code.coding[0].system
        == "http://example.org/fhir/CodeSystem/pharmacy-form"
    )
    assert inst.supportingInfo[3].sequence == 4
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Pharmacy Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total.currency == "USD"
    assert float(inst.total.value) == float(155.0)
    assert inst.type.coding[0].code == "pharmacy"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_claim_9(base_settings):
    """No. 9 tests collection for Claim.
    Test File: claim-example-pharmacy-compound.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "claim-example-pharmacy-compound.json"
    )
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_9(inst2)


def impl_claim_10(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "123456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "100150"
    assert inst.identifier[0].system == "http://happyvalley.com/claim"
    assert inst.identifier[0].value == "12345"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].identifier.system == "http://happyvalley.com/claim"
    assert inst.insurance[0].identifier.value == "12345"
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(135.57)
    assert inst.item[0].productOrService.coding[0].code == "1200"
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.currency == "USD"
    assert float(inst.item[0].unitPrice.value) == float(135.57)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.provider.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Oral Health Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "oral"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_claim_10(base_settings):
    """No. 10 tests collection for Claim.
    Test File: claim-example.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_10(inst2)
