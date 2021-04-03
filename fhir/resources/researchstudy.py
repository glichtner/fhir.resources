# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy
Release: R4
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
import typing
from pydantic import Field
from pydantic import root_validator

from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import fhirtypes


from . import domainresource


class ResearchStudy(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Investigation to increase healthcare-related patient-independent knowledge.
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques. A ResearchStudy
    involves the gathering of information about human or animal subjects or
    stability data about drug products or drug substances.
    """

    resource_type = Field("ResearchStudy", const=True)

    arm: typing.List[fhirtypes.ResearchStudyArmType] = Field(
        None,
        alias="arm",
        title="Defined path through the study for a subject",
        description=(
            "Describes an expected sequence of events for one of the participants "
            "of a study.  E.g. Exposure to drug A, wash-out, exposure to drug B, "
            "wash-out, follow-up."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    associatedParty: typing.List[fhirtypes.ResearchStudyAssociatedPartyType] = Field(
        None,
        alias="associatedParty",
        title="Sponsors, collaborators, and other parties",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Classifications for the study",
        description=(
            "Codes categorizing the type of study such as investigational vs. "
            "observational, type of blinding, type of randomization, safety vs. "
            "efficacy, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    classification: typing.List[fhirtypes.ResearchStudyClassificationType] = Field(
        None,
        alias="classification",
        title="Classification for the study",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    condition: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="condition",
        title="Condition being studied",
        description=(
            "The condition that is the focus of the study.  For example, In a study"
            " to examine risk factors for Lupus, might have as an inclusion "
            'criterion "healthy volunteer", but the target condition code would be '
            "a Lupus SNOMED code."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the study",
        description=(
            "Contact details to assist a user in learning more about or engaging "
            "with the study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    currentState: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="currentState",
        title=(
            "active | administratively-completed | approved | closed-to-accrual | "
            "closed-to-accrual-and-intervention | completed | disapproved | in-"
            "review | temporarily-closed-to-accrual | temporarily-closed-to-"
            "accrual-and-intervention | withdrawn"
        ),
        description="Current status of the study.",
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date the resource last changed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="What this is study doing",
        description=(
            "A full description of how the study is being conducted.  For a "
            "description of what the study objectives are see "
            "ResearchStudy.objective.description."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    descriptionSummary: fhirtypes.Markdown = Field(
        None,
        alias="descriptionSummary",
        title="A brief summary of the study description",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    descriptionSummary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_descriptionSummary",
        title="Extension field for ``descriptionSummary``.",
    )

    focus: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="focus",
        title="Drugs, devices, etc. under study",
        description=(
            "The medication(s), food(s), therapy(ies), device(s) or other concerns "
            "or interventions that the study is seeking to gain more information "
            "about."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for study",
        description=(
            "Identifiers assigned to this research study by the sponsor or other "
            "systems."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    keyword: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="keyword",
        title="Used to search for the study",
        description="Key terms to aid in searching for or filtering the study.",
        # if property is element of this resource.
        element_property=True,
    )

    label: typing.List[fhirtypes.ResearchStudyLabelType] = Field(
        None,
        alias="label",
        title="Additional names for the study",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    location: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="location",
        title="Geographic region(s) for study",
        description=(
            "Indicates a country, state or other region where the study is taking "
            "place."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this study (computer friendly)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the study",
        description=(
            "Comments made about the study by the performer, subject or other "
            "participants."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    objective: typing.List[fhirtypes.ResearchStudyObjectiveType] = Field(
        None,
        alias="objective",
        title="A goal for the study",
        description=(
            "A goal that the study is aiming to achieve in terms of a scientific "
            "question to be answered by the analysis of data collected during the "
            "study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    outcomeMeasure: typing.List[fhirtypes.ResearchStudyOutcomeMeasureType] = Field(
        None,
        alias="outcomeMeasure",
        title="An outcome or planned variable to measure during the study",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of larger study",
        description=(
            "A larger research study of which this particular study is a component "
            "or step."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="When the study began and ended",
        description=(
            "Identifies the start date and the expected (or actual, depending on "
            "status) end date for the study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    phase: fhirtypes.CodeableConceptType = Field(
        None,
        alias="phase",
        title=(
            "n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | "
            "phase-2-phase-3 | phase-3 | phase-4"
        ),
        description=(
            "The stage in the progression of a therapy from initial experimental "
            "use in humans in clinical trials to post-market evaluation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    primaryPurposeType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="primaryPurposeType",
        title=(
            "treatment | prevention | diagnostic | supportive-care | screening | "
            "health-services-research | basic-science | device-feasibility"
        ),
        description=(
            "The type of study based upon the intent of the study activities. A "
            "classification of the intent of the study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    principalInvestigator: fhirtypes.ReferenceType = Field(
        None,
        alias="principalInvestigator",
        title="Researcher who oversees multiple aspects of the study",
        description=(
            "A researcher in a study who oversees multiple aspects of the study, "
            "such as concept development, protocol writing, protocol submission for"
            " IRB approval, participant recruitment, informed consent, data "
            "collection, analysis, interpretation and presentation."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
    )

    protocol: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="protocol",
        title="Steps followed in executing study",
        description=(
            "The set of steps expected to be performed as part of the execution of "
            "the study."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["PlanDefinition"],
    )

    recruitment: typing.List[fhirtypes.ResearchStudyRecruitmentType] = Field(
        None,
        alias="recruitment",
        title="Target or actual group of participants enrolled in study",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="References and dependencies",
        description="Citations, references and other related documents.",
        # if property is element of this resource.
        element_property=True,
    )

    relatesTo: typing.List[fhirtypes.ResearchStudyRelatesToType] = Field(
        None,
        alias="relatesTo",
        title="Related artifact and type of relation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    result: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="result",
        title="Link to results generated during the study",
        description=(
            "Link to one or more sets of results generated by the study.  Could "
            "also link to a research registry holding the results such as "
            "ClinicalTrials.gov."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceReport", "Citation"],
    )

    site: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="site",
        title="Facility where study activities are conducted",
        description="A facility in which study activities are conducted.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location", "ResearchStudy"],
    )

    sponsor: fhirtypes.ReferenceType = Field(
        None,
        alias="sponsor",
        title="Organization that initiates and is legally responsible for the study",
        description=(
            "An organization that initiates the investigation and is legally "
            "responsible for the study."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The publication state of the resource (not of the study).",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusDate: typing.List[fhirtypes.ResearchStudyStatusDateType] = Field(
        None,
        alias="statusDate",
        title="Status of study with time for that status",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this study (for computers)",
        description=(
            "A short, descriptive label for the study particularly for compouter "
            "use."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Canonical identifier for this study resource",
        description=(
            "Canonical identifier for this study resource, represented as a "
            "globally unique URI."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business identifier for the study record",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    whyStopped: fhirtypes.CodeableConceptType = Field(
        None,
        alias="whyStopped",
        title=(
            "accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-"
            "study-progress | temporarily-closed-per-study-design"
        ),
        description=(
            "A description and/or code explaining the premature termination of the "
            "study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ResearchStudy`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "url",
            "identifier",
            "version",
            "name",
            "title",
            "label",
            "protocol",
            "partOf",
            "relatesTo",
            "relatedArtifact",
            "date",
            "status",
            "primaryPurposeType",
            "phase",
            "category",
            "focus",
            "condition",
            "contact",
            "keyword",
            "location",
            "descriptionSummary",
            "description",
            "period",
            "sponsor",
            "principalInvestigator",
            "site",
            "note",
            "classification",
            "associatedParty",
            "currentState",
            "statusDate",
            "whyStopped",
            "recruitment",
            "arm",
            "objective",
            "outcomeMeasure",
            "result",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1553(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


from . import backboneelement


class ResearchStudyArm(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defined path through the study for a subject.
    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """

    resource_type = Field("ResearchStudyArm", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Short explanation of study path",
        description=(
            "A succinct description of the path through the study that would be "
            "followed by a subject adhering to this arm."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifierIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifierIdentifier",
        title=(
            "Allows the arm for the study and the arm for the subject to be linked "
            "easily"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e identifier[x]
        one_of_many="identifier",
        one_of_many_required=False,
    )

    identifierUri: fhirtypes.Uri = Field(
        None,
        alias="identifierUri",
        title=(
            "Allows the arm for the study and the arm for the subject to be linked "
            "easily"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e identifier[x]
        one_of_many="identifier",
        one_of_many_required=False,
    )
    identifierUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identifierUri", title="Extension field for ``identifierUri``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Label for study arm",
        description="Unique, human-readable label for this arm of the study.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Categorization of study arm",
        description=(
            "Categorization of study arm, e.g. experimental, active comparator, "
            "placebo comparater."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ResearchStudyArm`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifierUri",
            "identifierIdentifier",
            "name",
            "type",
            "description",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1829(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1829(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"identifier": ["identifierIdentifier", "identifierUri"]}
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class ResearchStudyAssociatedParty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Sponsors, collaborators, and other parties.
    """

    resource_type = Field("ResearchStudyAssociatedParty", const=True)

    classifier: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="classifier",
        title="nih | fda",
        description="Organisational type of association.",
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of associated party",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    orgaanization: fhirtypes.ReferenceType = Field(
        None,
        alias="orgaanization",
        title=(
            "Organisation associated with study in role of sponsoring, providing "
            "funds etc"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    person: fhirtypes.ReferenceType = Field(
        None,
        alias="person",
        title=(
            "Individual associated with study (use practitionerRole to specify "
            "their organisation)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title=(
            "sponsor | sponsor-investigator | primary-investigator | collaborator |"
            " funding-source | recruitment-contact | sub-investigator | study-"
            "director | study-chair"
        ),
        description="Type of association.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ResearchStudyAssociatedParty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "role",
            "classifier",
            "person",
            "orgaanization",
        ]


class ResearchStudyClassification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Classification for the study.
    """

    resource_type = Field("ResearchStudyClassification", const=True)

    classifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classifier",
        title=(
            "n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | "
            "phase-2-phase-3 | phase-3 | phase-4"
        ),
        description="Value of classifier.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="phase | category | keyword ",
        description="Type of classifier.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ResearchStudyClassification`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "classifier"]


class ResearchStudyLabel(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional names for the study.
    """

    resource_type = Field("ResearchStudyLabel", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="short | public | scientific",
        description="Kind of name.",
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ResearchStudyLabel`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "value"]


class ResearchStudyObjective(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A goal for the study.
    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """

    resource_type = Field("ResearchStudyObjective", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Description of the objective",
        description=(
            "Free text description of the objective of the study.  This is what the"
            " study is trying to achieve rather than how it is going to achieve it "
            "(see ResearchStudy.description)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Label for the objective",
        description="Unique, human-readable label for this objective of the study.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="primary | secondary | exploratory",
        description="The kind of study objective.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ResearchStudyObjective`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "type", "description"]


class ResearchStudyOutcomeMeasure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An outcome or planned variable to measure during the study.
    """

    resource_type = Field("ResearchStudyOutcomeMeasure", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Description of the outcome",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Label for the outcome",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    reference: fhirtypes.ReferenceType = Field(
        None,
        alias="reference",
        title="Structured outcome definition",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="primary | secondary | exploratory",
        description=(
            "The parameter or characteristic being assessed as one of the values by"
            " which the study is assessed."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ResearchStudyOutcomeMeasure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "type",
            "description",
            "reference",
        ]


class ResearchStudyRecruitment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Target or actual group of participants enrolled in study.
    """

    resource_type = Field("ResearchStudyRecruitment", const=True)

    actualGroup: fhirtypes.ReferenceType = Field(
        None,
        alias="actualGroup",
        title="Group of participants who were enrolled in study",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    actualNumber: fhirtypes.UnsignedInt = Field(
        None,
        alias="actualNumber",
        title="Actual total number of participants enrolled in study",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    actualNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actualNumber", title="Extension field for ``actualNumber``."
    )

    eligibility: fhirtypes.ReferenceType = Field(
        None,
        alias="eligibility",
        title="Inclusion and exclusion criteria",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    targetNumber: fhirtypes.UnsignedInt = Field(
        None,
        alias="targetNumber",
        title="Estimated total number of participants to be enrolled",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    targetNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetNumber", title="Extension field for ``targetNumber``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ResearchStudyRecruitment`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "targetNumber",
            "actualNumber",
            "eligibility",
            "actualGroup",
        ]


class ResearchStudyRelatesTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related artifact and type of relation.
    """

    resource_type = Field("ResearchStudyRelatesTo", const=True)

    relationshipType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="relationshipType",
        title=(
            "replaces | amends | appends | transforms | replaced-with | amended-"
            "with | appended-with | transformed-with | derived-from | transformed-"
            "into | composed-of | part-of | supports | supported-with | depends-on "
            "| cites | cited-by"
        ),
        description="Describes the relationship of the artefact to the Research Study.",
        # if property is element of this resource.
        element_property=True,
    )

    targetAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="targetAttachment",
        title="Identification of the target artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=False,
    )

    targetClassifier: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="targetClassifier",
        title=(
            "Expanded-Access | Available | No-longer-available | Termporarily-not-"
            "available | Approved-for-marketing"
        ),
        description="Describes the access to the artefact.",
        # if property is element of this resource.
        element_property=True,
    )

    targetIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="targetIdentifier",
        title="Identification of the target artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=False,
    )

    targetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="targetReference",
        title="Identification of the target artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
    )

    targetUri: fhirtypes.Uri = Field(
        None,
        alias="targetUri",
        title="Identification of the target artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=False,
    )
    targetUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetUri", title="Extension field for ``targetUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ResearchStudyRelatesTo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "relationshipType",
            "targetClassifier",
            "targetUri",
            "targetIdentifier",
            "targetAttachment",
            "targetReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2458(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "target": [
                "targetAttachment",
                "targetIdentifier",
                "targetReference",
                "targetUri",
            ]
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class ResearchStudyStatusDate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Status of study with time for that status.
    """

    resource_type = Field("ResearchStudyStatusDate", const=True)

    activity: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="activity",
        title=(
            "Record-Verification | Overall-Study | Primary-Outcome-Data-Collection "
            "| Registration-Submission | Registration-Submission-QC | Registration-"
            "Posting | Results-Submission | Results-Submission-QC | Results-Posting"
            " | Disposition-Submission | Disposition-Submission-QC | Disposition-"
            "Posting | Update-Submission | Update-Posting"
        ),
        description="Label for status or state.",
        # if property is element of this resource.
        element_property=True,
    )

    actual: bool = Field(
        None,
        alias="actual",
        title="Actual if true else anticipated",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actual", title="Extension field for ``actual``."
    )

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Date range",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ResearchStudyStatusDate`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "activity", "actual", "period"]
