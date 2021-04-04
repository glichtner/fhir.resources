# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Procedure
Release: R5
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import procedure


def impl_procedure_1(inst):
    assert inst.bodySite[0].coding[0].code == "83030008"
    assert inst.bodySite[0].coding[0].display == "Retropharyngeal area"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.code.coding[0].code == "48387007"
    assert inst.code.coding[0].display == "Tracheotomy"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/f003"
    assert inst.followUp[0].text == "described in care plan"
    assert inst.id == "f004"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrencePeriod.end == fhirtypes.DateTime.validate(
        "2013-03-22T10:30:10+01:00"
    )
    assert inst.occurrencePeriod.start == fhirtypes.DateTime.validate(
        "2013-03-22T09:30:10+01:00"
    )
    assert inst.outcome.text == "removal of the retropharyngeal abscess"
    assert inst.performer[0].actor.display == "A. Langeveld"
    assert inst.performer[0].actor.reference == "Practitioner/f005"
    assert inst.performer[0].function.coding[0].code == "01.000"
    assert inst.performer[0].function.coding[0].display == "Arts"
    assert (
        inst.performer[0].function.coding[0].system
        == "urn:oid:2.16.840.1.113883.2.4.15.111"
    )
    assert inst.performer[0].function.text == "Care role"
    assert inst.reason[0].concept.text == "ensure breathing during surgery"
    assert inst.report[0].display == "???????????"
    assert inst.report[0].reference == "DiagnosticReport/f001"
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_procedure_1(base_settings):
    """No. 1 tests collection for Procedure.
    Test File: procedure-example-f004-tracheotomy.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "procedure-example-f004-tracheotomy.json"
    )
    inst = procedure.Procedure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Procedure" == inst.resource_type

    impl_procedure_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Procedure" == data["resourceType"]

    inst2 = procedure.Procedure(**data)
    impl_procedure_1(inst2)


def impl_procedure_2(inst):
    assert inst.bodySite[0].coding[0].code == "83030008"
    assert inst.bodySite[0].coding[0].display == "Retropharyngeal area"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.code.coding[0].code == "172960003"
    assert inst.code.coding[0].display == "Incision of retropharyngeal abscess"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/f003"
    assert inst.followUp[0].text == "described in care plan"
    assert inst.id == "f003"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrencePeriod.end == fhirtypes.DateTime.validate(
        "2013-03-24T10:30:10+01:00"
    )
    assert inst.occurrencePeriod.start == fhirtypes.DateTime.validate(
        "2013-03-24T09:30:10+01:00"
    )
    assert inst.outcome.text == "removal of the retropharyngeal abscess"
    assert inst.performer[0].actor.display == "E.M.J.M. van den broek"
    assert inst.performer[0].actor.reference == "Practitioner/f001"
    assert inst.performer[0].function.coding[0].code == "01.000"
    assert inst.performer[0].function.coding[0].display == "Arts"
    assert (
        inst.performer[0].function.coding[0].system
        == "urn:oid:2.16.840.1.113883.2.4.15.111"
    )
    assert inst.performer[0].function.text == "Care role"
    assert inst.reason[0].concept.text == "abcess in retropharyngeal area"
    assert inst.report[0].display == "Lab results blood test"
    assert inst.report[0].reference == "DiagnosticReport/f001"
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_procedure_2(base_settings):
    """No. 2 tests collection for Procedure.
    Test File: procedure-example-f003-abscess.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "procedure-example-f003-abscess.json"
    )
    inst = procedure.Procedure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Procedure" == inst.resource_type

    impl_procedure_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Procedure" == data["resourceType"]

    inst2 = procedure.Procedure(**data)
    impl_procedure_2(inst2)


def impl_procedure_3(inst):
    assert (
        inst.basedOn[0].display == "Order for the assessment of passive range of motion"
    )
    assert inst.basedOn[0].reference == "ServiceRequest/physical-therapy"
    assert inst.bodySite[0].coding[0].code == "36701003"
    assert inst.bodySite[0].coding[0].display == "Both knees (body structure)"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.bodySite[0].text == "Both knees"
    assert inst.category[0].coding[0].code == "386053000"
    assert inst.category[0].coding[0].display == "Evaluation procedure (procedure)"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].text == "Evaluation"
    assert inst.code.coding[0].code == "710830005"
    assert (
        inst.code.coding[0].display
        == "Assessment of passive range of motion (procedure)"
    )
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Assessment of passive range of motion"
    assert inst.id == "physical-therapy"
    assert inst.location.display == "Sawbones Orthopedic Clinic"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2016-09-27")
    assert inst.performer[0].actor.display == "Paul Therapist, PT"
    assert (
        inst.reason[0].concept.text
        == "assessment of mobility limitations due to osteoarthritis"
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Assessment of '
        "passive range of motion for both knees on Sept 27, 2016 due "
        "to osteoarthritis</div>"
    )
    assert inst.text.status == "generated"


def test_procedure_3(base_settings):
    """No. 3 tests collection for Procedure.
    Test File: procedure-example-physical-therapy.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "procedure-example-physical-therapy.json"
    )
    inst = procedure.Procedure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Procedure" == inst.resource_type

    impl_procedure_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Procedure" == data["resourceType"]

    inst2 = procedure.Procedure(**data)
    impl_procedure_3(inst2)


def impl_procedure_4(inst):
    assert inst.basedOn[0].display == "Maternity care plan"
    assert inst.basedOn[0].reference == "CarePlan/preg"
    assert inst.code.coding[0].code == "62013009"
    assert inst.code.coding[0].display == "Ambulating patient (procedure)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Ambulation"
    assert inst.id == "ambulation"
    assert inst.identifier[0].value == "12345"
    assert inst.instantiatesUri[0] == (
        "http://example.org/protocol-for-hypertension-during-" "pregnancy"
    )
    assert (
        inst.location.display
        == "Burgers University Medical Center, South Wing, second floor"
    )
    assert inst.location.reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.display == "Carla Espinosa"
    assert inst.performer[0].actor.reference == "Practitioner/f204"
    assert inst.performer[0].onBehalfOf.display == "University Medical Hospital"
    assert inst.performer[0].onBehalfOf.reference == "Organization/f001"
    assert inst.reason[0].reference.display == "Blood Pressure"
    assert inst.reason[0].reference.reference == "Observation/blood-pressure"
    assert inst.status == "not-done"
    assert inst.statusReason.coding[0].code == "398254007"
    assert inst.statusReason.coding[0].display == "  Pre-eclampsia (disorder)"
    assert inst.statusReason.coding[0].system == "http://snomed.info/sct"
    assert inst.statusReason.text == "Pre-eclampsia"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Ambulation '
        "procedure was not done</div>"
    )
    assert inst.text.status == "generated"


def test_procedure_4(base_settings):
    """No. 4 tests collection for Procedure.
    Test File: procedure-example-ambulation.json
    """
    filename = base_settings["unittest_data_dir"] / "procedure-example-ambulation.json"
    inst = procedure.Procedure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Procedure" == inst.resource_type

    impl_procedure_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Procedure" == data["resourceType"]

    inst2 = procedure.Procedure(**data)
    impl_procedure_4(inst2)


def impl_procedure_5(inst):
    assert inst.bodySite[0].coding[0].code == "17401000"
    assert inst.bodySite[0].coding[0].display == "Heart valve structure"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.code.coding[0].code == "34068001"
    assert inst.code.coding[0].display == "Heart valve replacement"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.followUp[0].text == "described in care plan"
    assert inst.id == "f001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrencePeriod.end == fhirtypes.DateTime.validate("2011-06-27")
    assert inst.occurrencePeriod.start == fhirtypes.DateTime.validate("2011-06-26")
    assert inst.outcome.text == "improved blood circulation"
    assert inst.performer[0].actor.display == "P. Voigt"
    assert inst.performer[0].actor.reference == "Practitioner/f002"
    assert inst.performer[0].function.coding[0].code == "01.000"
    assert inst.performer[0].function.coding[0].display == "Arts"
    assert (
        inst.performer[0].function.coding[0].system
        == "urn:oid:2.16.840.1.113883.2.4.15.111"
    )
    assert inst.performer[0].function.text == "Care role"
    assert inst.reason[0].concept.text == "Heart valve disorder"
    assert inst.report[0].display == "Lab results blood test"
    assert inst.report[0].reference == "DiagnosticReport/f001"
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_procedure_5(base_settings):
    """No. 5 tests collection for Procedure.
    Test File: procedure-example-f001-heart.json
    """
    filename = base_settings["unittest_data_dir"] / "procedure-example-f001-heart.json"
    inst = procedure.Procedure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Procedure" == inst.resource_type

    impl_procedure_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Procedure" == data["resourceType"]

    inst2 = procedure.Procedure(**data)
    impl_procedure_5(inst2)


def impl_procedure_6(inst):
    assert inst.bodySite[0].coding[0].code == "39607008"
    assert inst.bodySite[0].coding[0].display == "Lung structure"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.code.coding[0].code == "359615001"
    assert inst.code.coding[0].display == "Partial lobectomy of lung"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/f002"
    assert inst.followUp[0].text == "described in care plan"
    assert inst.id == "f002"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrencePeriod.end == fhirtypes.DateTime.validate(
        "2013-03-08T09:30:10+01:00"
    )
    assert inst.occurrencePeriod.start == fhirtypes.DateTime.validate(
        "2013-03-08T09:00:10+01:00"
    )
    assert inst.outcome.text == "improved blood circulation"
    assert inst.performer[0].actor.display == "M.I.M. Versteegh"
    assert inst.performer[0].actor.reference == "Practitioner/f003"
    assert inst.performer[0].function.coding[0].code == "01.000"
    assert inst.performer[0].function.coding[0].display == "Arts"
    assert (
        inst.performer[0].function.coding[0].system
        == "urn:oid:2.16.840.1.113883.2.4.15.111"
    )
    assert inst.performer[0].function.text == "Care role"
    assert inst.reason[0].concept.text == "Malignant tumor of lung"
    assert inst.report[0].display == "Lab results blood test"
    assert inst.report[0].reference == "DiagnosticReport/f001"
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_procedure_6(base_settings):
    """No. 6 tests collection for Procedure.
    Test File: procedure-example-f002-lung.json
    """
    filename = base_settings["unittest_data_dir"] / "procedure-example-f002-lung.json"
    inst = procedure.Procedure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Procedure" == inst.resource_type

    impl_procedure_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Procedure" == data["resourceType"]

    inst2 = procedure.Procedure(**data)
    impl_procedure_6(inst2)


def impl_procedure_7(inst):
    assert inst.id == "appendectomy-narrative"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Routine '
        "Appendectomy in April 2013 performed by Dr Cecil "
        "Surgeon</div>"
    )
    assert inst.text.status == "additional"


def test_procedure_7(base_settings):
    """No. 7 tests collection for Procedure.
    Test File: procedure-example-appendectomy-narrative.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "procedure-example-appendectomy-narrative.json"
    )
    inst = procedure.Procedure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Procedure" == inst.resource_type

    impl_procedure_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Procedure" == data["resourceType"]

    inst2 = procedure.Procedure(**data)
    impl_procedure_7(inst2)


def impl_procedure_8(inst):
    assert inst.bodySite[0].coding[0].code == "272676008"
    assert inst.bodySite[0].coding[0].display == "Sphenoid bone"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.code.coding[0].code == "367336001"
    assert inst.code.coding[0].display == "Chemotherapy"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.display == "Roel's encounter on January 28th, 2013"
    assert inst.encounter.reference == "Encounter/f202"
    assert inst.id == "f201"
    assert (
        inst.instantiatesCanonical[0] == "http://example.org/fhir/PlanDefinition/KDN5"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == (
        "Eerste neo-adjuvante TPF-kuur bij groot proces in sphenoid "
        "met intracraniale uitbreiding."
    )
    assert inst.occurrencePeriod.end == fhirtypes.DateTime.validate(
        "2013-01-28T14:27:00+01:00"
    )
    assert inst.occurrencePeriod.start == fhirtypes.DateTime.validate(
        "2013-01-28T13:31:00+01:00"
    )
    assert inst.performer[0].actor.display == "Dokter Bronsig"
    assert inst.performer[0].actor.reference == "Practitioner/f201"
    assert inst.performer[0].function.coding[0].code == "310512001"
    assert inst.performer[0].function.coding[0].display == "Medical oncologist"
    assert inst.performer[0].function.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].concept.text == "DiagnosticReport/f201"
    assert inst.status == "completed"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"


def test_procedure_8(base_settings):
    """No. 8 tests collection for Procedure.
    Test File: procedure-example-f201-tpf.json
    """
    filename = base_settings["unittest_data_dir"] / "procedure-example-f201-tpf.json"
    inst = procedure.Procedure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Procedure" == inst.resource_type

    impl_procedure_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Procedure" == data["resourceType"]

    inst2 = procedure.Procedure(**data)
    impl_procedure_8(inst2)


def impl_procedure_9(inst):
    assert inst.basedOn[0].display == "Order for health education"
    assert inst.basedOn[0].reference == "ServiceRequest/education"
    assert inst.category[0].coding[0].code == "311401005"
    assert inst.category[0].coding[0].display == "Patient education (procedure)"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].text == "Education"
    assert inst.code.coding[0].code == "48023004"
    assert (
        inst.code.coding[0].display
        == "Breast self-examination technique education (procedure)"
    )
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Health education - breast examination"
    assert inst.id == "education"
    assert inst.location.display == "Southside Community Health Center"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.performer[0].actor.display == "Pamela Educator, RN"
    assert inst.reason[0].concept.text == "early detection of breast mass"
    assert inst.status == "completed"
    assert inst.subject.display == "Jane Doe"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Health education'
        " - breast examination for early detection of breast "
        "mass</div>"
    )
    assert inst.text.status == "generated"


def test_procedure_9(base_settings):
    """No. 9 tests collection for Procedure.
    Test File: procedure-example-education.json
    """
    filename = base_settings["unittest_data_dir"] / "procedure-example-education.json"
    inst = procedure.Procedure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Procedure" == inst.resource_type

    impl_procedure_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Procedure" == data["resourceType"]

    inst2 = procedure.Procedure(**data)
    impl_procedure_9(inst2)


def impl_procedure_10(inst):
    assert inst.bodySite[0].coding[0].code == "368225008"
    assert inst.bodySite[0].coding[0].display == "Entire Left Forearm"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.bodySite[0].text == "Left forearm"
    assert inst.category[0].coding[0].code == "103693007"
    assert inst.category[0].coding[0].display == "Diagnostic procedure (procedure)"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].text == "Diagnostic procedure"
    assert inst.code.coding[0].code == "90105005"
    assert inst.code.coding[0].display == "Biopsy of soft tissue of forearm (Procedure)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Biopsy of suspected melanoma L) arm"
    assert inst.complication[0].coding[0].code == "67750007"
    assert (
        inst.complication[0].coding[0].display
        == "Ineffective airway clearance (finding)"
    )
    assert inst.complication[0].coding[0].system == "http://snomed.info/sct"
    assert inst.complication[0].text == "Ineffective airway clearance"
    assert inst.followUp[0].text == "Review in clinic"
    assert inst.id == "biopsy"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Standard Biopsy"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2014-02-03")
    assert inst.performer[0].actor.display == "Dr Bert Biopser"
    assert inst.performer[0].actor.reference == "Practitioner/example"
    assert (
        inst.reason[0].concept.text
        == "Dark lesion l) forearm. getting darker last 3 months."
    )
    assert inst.recorded == fhirtypes.DateTime.validate("2014-02-03")
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Biopsy of '
        "suspected melanoma L) arm</div>"
    )
    assert inst.text.status == "generated"
    assert inst.used[0].concept.coding[0].code == "79068005"
    assert inst.used[0].concept.coding[0].display == "Needle, device (physical object)"
    assert inst.used[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.used[0].concept.text == "30-guage needle"


def test_procedure_10(base_settings):
    """No. 10 tests collection for Procedure.
    Test File: procedure-example-biopsy.json
    """
    filename = base_settings["unittest_data_dir"] / "procedure-example-biopsy.json"
    inst = procedure.Procedure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Procedure" == inst.resource_type

    impl_procedure_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Procedure" == data["resourceType"]

    inst2 = procedure.Procedure(**data)
    impl_procedure_10(inst2)
