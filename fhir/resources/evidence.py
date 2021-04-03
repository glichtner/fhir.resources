# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Evidence
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


from . import metadataresource


class Evidence(metadataresource.MetadataResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Single evidence bit.
    The Evidence Resource provides a machine-interpretable expression of an
    evidence concept including the evidence variables (eg population,
    exposures/interventions, comparators, outcomes, measured variables,
    confounding variables), the statistics, and the certainty of this evidence.
    """

    resource_type = Field("Evidence", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the summary was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    assertion: fhirtypes.Markdown = Field(
        None,
        alias="assertion",
        title="Declarative description of the Evidence",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    assertion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assertion", title="Extension field for ``assertion``."
    )

    author: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="Who authored the content",
        description=(
            "An individiual, organization, or device primarily involved in the "
            "creation and maintenance of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    certainty: typing.List[fhirtypes.EvidenceCertaintyType] = Field(
        None,
        alias="certainty",
        title="Certainty or quality of the evidence",
        description=(
            "Assessment of certainty, confidence in the estimates, or quality of "
            "the evidence."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    citeAsMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="citeAsMarkdown",
        title="Citation for this evidence",
        description="Citation Resource or display of suggested citation for this evidence.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e citeAs[x]
        one_of_many="citeAs",
        one_of_many_required=False,
    )
    citeAsMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_citeAsMarkdown", title="Extension field for ``citeAsMarkdown``."
    )

    citeAsReference: fhirtypes.ReferenceType = Field(
        None,
        alias="citeAsReference",
        title="Citation for this evidence",
        description="Citation Resource or display of suggested citation for this evidence.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e citeAs[x]
        one_of_many="citeAs",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Citation"],
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the summary was published. The "
            "date must change when the business version changes and it must change "
            "if the status code changes. In addition, it should change when the "
            "substantive content of the summary changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Description of the particular summary",
        description=(
            "A free text natural language description of the evidence from a "
            "consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    distribution: typing.List[fhirtypes.OrderedDistributionType] = Field(
        None,
        alias="distribution",
        title="An ordered group of statistics",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    editor: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="editor",
        title="Who edited the content",
        description=(
            "An individiual, organization, or device primarily responsible for "
            "internal coherence of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    endorser: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individiual, organization, or device responsible for officially "
            "endorsing the content for use in some setting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the summary",
        description=(
            "A formal identifier that is used to identify this summary when it is "
            "represented in other formats, or referenced in a specification, model,"
            " design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the summary was last reviewed",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnotes and/or explanatory notes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the " "evidence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="Link or citation to artifact associated with the summary",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="Who reviewed the content",
        description=(
            "An individiual, organization, or device primarily responsible for "
            "review of some aspect of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    statistic: typing.List[fhirtypes.StatisticType] = Field(
        None,
        alias="statistic",
        title="Values and parameters for a single statistic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this summary. Enables tracking the life-cycle of the "
            "content."
        ),
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

    studyType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="studyType",
        title="The type of study that produced this evidence",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    synthesisType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="synthesisType",
        title="The method to combine studies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this summary (human friendly)",
        description="A short, descriptive, user-friendly title for the summary.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this evidence, represented as a globally "
            "unique URI"
        ),
        description=(
            "An absolute URI that is used to identify this evidence when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which at which an authoritative "
            "instance of this summary is (or will be) published. This URL can be "
            "the target of a canonical reference. It SHALL remain the same when the"
            " summary is stored on different servers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate evidence instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    variableDefinition: typing.List[fhirtypes.EvidenceVariableDefinitionType] = Field(
        ...,
        alias="variableDefinition",
        title="Evidence variable such as population, exposure, or outcome",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of this summary",
        description=(
            "The identifier that is used to identify this version of the summary "
            "when it is referenced in a specification, model, design or instance. "
            "This is an arbitrary value managed by the summary author and is not "
            "expected to be globally unique. For example, it might be a timestamp "
            "(e.g. yyyymmdd) if a managed version is not available. There is also "
            "no expectation that versions can be placed in a lexicographical "
            "sequence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``Evidence`` according specification,
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
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "copyright",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "topic",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatedArtifact",
            "url",
            "identifier",
            "version",
            "title",
            "citeAsReference",
            "citeAsMarkdown",
            "status",
            "date",
            "useContext",
            "approvalDate",
            "lastReviewDate",
            "publisher",
            "contact",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatedArtifact",
            "description",
            "assertion",
            "note",
            "variableDefinition",
            "synthesisType",
            "studyType",
            "statistic",
            "distribution",
            "certainty",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_973(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_973(
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
        one_of_many_fields = {"citeAs": ["citeAsMarkdown", "citeAsReference"]}
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


from . import backboneelement


class EvidenceCertainty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Certainty or quality of the evidence.
    Assessment of certainty, confidence in the estimates, or quality of the
    evidence.
    """

    resource_type = Field("EvidenceCertainty", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description of certainty",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnotes and/or explanatory notes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    rater: fhirtypes.String = Field(
        None,
        alias="rater",
        title="Individual or group who did the rating",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    rater__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rater", title="Extension field for ``rater``."
    )

    rating: fhirtypes.CodeableConceptType = Field(
        None,
        alias="rating",
        title="Assessment or judgement of the aspect",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subcomponent: typing.List[fhirtypes.EvidenceCertaintyType] = Field(
        None,
        alias="subcomponent",
        title="A domain or subdomain of certainty",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Aspect of certainty being rated",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``EvidenceCertainty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "note",
            "type",
            "rating",
            "rater",
            "subcomponent",
        ]


class EvidenceVariableDefinition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Evidence variable such as population, exposure, or outcome.
    """

    resource_type = Field("EvidenceVariableDefinition", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="A text description or summary of the variable",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    directnessMatch: fhirtypes.CodeableConceptType = Field(
        None,
        alias="directnessMatch",
        title="low | moderate | high | exact",
        description=(
            "Indication of quality of match between intended variable to actual "
            "variable."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    intended: fhirtypes.ReferenceType = Field(
        None,
        alias="intended",
        title="Definition of the intended variable related to the Evidence",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group", "EvidenceVariable"],
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnotes and/or explanatory notes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    observed: fhirtypes.ReferenceType = Field(
        None,
        alias="observed",
        title="Definition of the actual variable related to the statistic(s)",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group", "EvidenceVariable"],
    )

    variableRole: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="variableRole",
        title=(
            "population | subpopulation | exposure | referenceExposure | "
            "measuredVariable | confounder"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``EvidenceVariableDefinition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "note",
            "variableRole",
            "observed",
            "intended",
            "directnessMatch",
        ]
