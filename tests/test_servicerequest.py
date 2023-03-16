# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ServiceRequest
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import servicerequest


def impl_servicerequest_1(inst):
    assert inst.basedOn[0].display == "Original Request"
    assert inst.bodySite[0].coding[0].display == "Right arm"
    assert inst.bodySite[0].text == "Right arm"
    assert inst.code.concept.coding[0].code == "35542-0"
    assert inst.code.concept.coding[0].system == "http://loinc.org"
    assert inst.code.concept.text == "Peanut IgG"
    assert inst.id == "subrequest"
    assert inst.intent == "instance-order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2013-05-08T09:33:27+07:00")
    assert inst.performerType.coding[0].display == "Qualified nurse"
    assert inst.performerType.text == "Nurse"
    assert inst.priority == "routine"
    assert inst.reason[0].concept.text == "Check for Peanut Allergy"
    assert inst.replaces[0].display == "Previous allergy test"
    assert inst.requester.display == "Dr. Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.requisition.value == "A13848392"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/dicom"
    assert inst.text.status == "generated"


def test_servicerequest_1(base_settings):
    """No. 1 tests collection for ServiceRequest.
    Test File: servicerequest-example-subrequest.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example-subrequest.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_1(inst2)


def impl_servicerequest_2(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-03-05")
    assert inst.code.concept.coding[0].code == "76164006"
    assert inst.code.concept.coding[0].display == "Biopsy of colon (procedure)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.code.concept.text == "Biopsy of colon"
    assert inst.id == "colon-biopsy"
    assert inst.identifier[0].value == "12345"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].display == "Dr Adam Careful"
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.requester.display == "Dr. Beverly Crusher"
    assert inst.requester.reference == "Practitioner/3ad0687e-f477-468c-afd5-fcc2bf897809"
    assert inst.requisition.system == "http://bumc.org/requisitions"
    assert inst.requisition.value == "req12345"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_2(base_settings):
    """No. 2 tests collection for ServiceRequest.
    Test File: servicerequest-example-colonoscopy-bx.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example-colonoscopy-bx.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_2(inst2)


def impl_servicerequest_3(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2018-02-20")
    assert inst.code.concept.coding[0].code == "40617009"
    assert inst.code.concept.coding[0].display == "Artificial respiration (procedure)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.code.concept.text == "Mechanical Ventilation"
    assert inst.id == "vent"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.performer[0].display == "Dr Cecil Surgeon"
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.reason[0].concept.text == "chronic obstructive lung disease (COLD)"
    assert inst.requester.display == "Dr. Beverly Crusher"
    assert inst.requester.reference == "Practitioner/3ad0687e-f477-468c-afd5-fcc2bf897809"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_3(base_settings):
    """No. 3 tests collection for ServiceRequest.
    Test File: servicerequest-example-ventilation.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example-ventilation.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_3(inst2)


def impl_servicerequest_4(inst):
    assert inst.code.concept.coding[0].code == "3024-7"
    assert inst.code.concept.coding[0].system == "http://loinc.org"
    assert inst.code.concept.text == "Free T4"
    assert inst.id == "ft4"
    assert inst.intent == "reflex-order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2015-08-27T09:33:27+07:00")
    assert inst.requester.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"


def test_servicerequest_4(base_settings):
    """No. 4 tests collection for ServiceRequest.
    Test File: servicerequest-example-ft4.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example-ft4.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_4(inst2)


def impl_servicerequest_5(inst):
    assert inst.code.concept.coding[0].code == "3981005"
    assert inst.code.concept.coding[0].display == "Carrier detection, molecular genetics (procedure)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/genomicEncounter"
    assert inst.id == "genomicServiceRequest2"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/serviceRequests"
    assert inst.identifier[0].type.coding[0].code == "LACSN"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].type.text == "Laboratory Accession ID"
    assert inst.identifier[0].value == "111111112"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/genomicPatient"
    assert inst.text.status == "generated"


def test_servicerequest_5(base_settings):
    """No. 5 tests collection for ServiceRequest.
    Test File: ServiceRequest-genomicServiceRequest2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "ServiceRequest-genomicServiceRequest2.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_5(inst2)


def impl_servicerequest_6(inst):
    assert inst.asNeededCodeableConcept.text == "as needed to clear mucus"
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-02-01T17:23:07Z")
    assert inst.basedOn[0].reference == "CarePlan/gpvisit"
    assert inst.code.concept.coding[0].code == "34431008"
    assert inst.code.concept.coding[0].display == "Physiotherapy of chest (regime/therapy)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "signature"
    assert inst.contained[1].id == "cystic-fibrosis"
    assert inst.id == "physiotherapy"
    assert inst.identifier[0].system == "http://goodhealth.org/placer-ids"
    assert inst.identifier[0].type.coding[0].code == "PLAC"
    assert inst.identifier[0].type.coding[0].display == "Placer Identifier"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].type.text == "Placer"
    assert inst.identifier[0].value == "20170201-0001"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert float(inst.occurrenceTiming.repeat.duration) == float(15)
    assert float(inst.occurrenceTiming.repeat.durationMax) == float(25)
    assert inst.occurrenceTiming.repeat.durationUnit == "min"
    assert inst.occurrenceTiming.repeat.frequency == 1
    assert inst.occurrenceTiming.repeat.frequencyMax == 4
    assert float(inst.occurrenceTiming.repeat.period) == float(1)
    assert inst.occurrenceTiming.repeat.periodUnit == "d"
    assert inst.reason[0].reference.reference == "#cystic-fibrosis"
    assert inst.relevantHistory[0].display == "Author's Signature"
    assert inst.relevantHistory[0].reference == "#signature"
    assert inst.requester.display == "Dr Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_6(base_settings):
    """No. 6 tests collection for ServiceRequest.
    Test File: servicerequest-example2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example2.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_6(inst2)


def impl_servicerequest_7(inst):
    assert inst.code.concept.coding[0].code == "3981005"
    assert inst.code.concept.coding[0].display == "Carrier detection, molecular genetics (procedure)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/denovoEncounter"
    assert inst.id == "genomicServiceRequest3"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/serviceRequests"
    assert inst.identifier[0].type.coding[0].code == "LACSN"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].type.text == "Laboratory Accession ID"
    assert inst.identifier[0].value == "111111113"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/denovoMother"
    assert inst.text.status == "generated"


def test_servicerequest_7(base_settings):
    """No. 7 tests collection for ServiceRequest.
    Test File: ServiceRequest-genomicServiceRequest3.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "ServiceRequest-genomicServiceRequest3.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_7(inst2)


def impl_servicerequest_8(inst):
    assert inst.category[0].coding[0].code == "103693007"
    assert inst.category[0].coding[0].display == "Diagnostic procedure (procedure)"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].text == "Diagnostics Procedure"
    assert inst.code.concept.coding[0].code == "303653007"
    assert inst.code.concept.coding[0].display == "Computed tomography of head"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "example"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
    "<div xmlns=\"http://www.w3.org/1999/xhtml\">To be "
    "added</div>"
    )
    assert inst.text.status == "generated"


def test_servicerequest_8(base_settings):
    """No. 8 tests collection for ServiceRequest.
    Test File: servicerequest-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_8(inst2)


def impl_servicerequest_9(inst):
    assert inst.category[0].coding[0].code == "386637004"
    assert inst.category[0].coding[0].display == "Obstetric procedure (procedure)"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].text == "OB"
    assert inst.code.concept.coding[0].code == "22633006"
    assert inst.code.concept.coding[0].display == "Vaginal delivery, medical personnel present (procedure)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.code.concept.text == "Vaginal delivery"
    assert inst.id == "ob"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2012-06-02")
    assert inst.performer[0].display == "Martha Midwife, RNP"
    assert inst.reason[0].concept.text == "term pregnancy, active labor"
    assert inst.requester.display == "Women’s Hospital"
    assert inst.status == "completed"
    assert inst.subject.display == "Jane Doe"
    assert inst.text.status == "generated"


def test_servicerequest_9(base_settings):
    """No. 9 tests collection for ServiceRequest.
    Test File: servicerequest-example-ob.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example-ob.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_9(inst2)


def impl_servicerequest_10(inst):
    assert inst.code.concept.coding[0].code == "3981005"
    assert inst.code.concept.coding[0].display == "Carrier detection, molecular genetics (procedure)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/denovoEncounter"
    assert inst.id == "genomicServiceRequest"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/serviceRequests"
    assert inst.identifier[0].type.coding[0].code == "LACSN"
    assert inst.identifier[0].type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.identifier[0].type.text == "Laboratory Accession ID"
    assert inst.identifier[0].value == "111111111"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/denovoChild"
    assert inst.text.status == "generated"


def test_servicerequest_10(base_settings):
    """No. 10 tests collection for ServiceRequest.
    Test File: ServiceRequest-genomicServiceRequest.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "ServiceRequest-genomicServiceRequest.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_10(inst2)