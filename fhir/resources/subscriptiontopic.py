# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubscriptionTopic
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


class SubscriptionTopic(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition Pattern.
    Describes a stream of resource state changes identified by trigger criteria
    and annotated with labels useful to filter projections from this topic.
    """

    resource_type = Field("SubscriptionTopic", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When SubscriptionTopic is/was approved by publisher",
        description=(
            "The date on which the asset content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
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

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the SubscriptionTopic and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the SubscriptionTopic."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date status first applied",
        description=(
            "For draft definitions, indicates the date of initial creation.  For "
            "active definitions, represents the date of activation.  For withdrawn "
            "definitions, indicates the date of withdrawal."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFrom: typing.List[fhirtypes.Canonical] = Field(
        None,
        alias="derivedFrom",
        title="Based on FHIR protocol or definition",
        description=(
            "The canonical URL pointing to another FHIR-defined SubscriptionTopic "
            "that is adhered to in whole or in part by this SubscriptionTopic."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubscriptionTopic"],
    )
    derivedFrom__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_derivedFrom", title="Extension field for ``derivedFrom``.")

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the ToSubscriptionTopicpic",
        description=(
            "A free text natural language description of the Topic from the "
            "consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="The effective date range for the SubscriptionTopic",
        description=(
            "The period during which the SubscriptionTopic content was or is "
            "planned to be effective."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="If for testing purposes, not real usage",
        description=(
            "A flag to indicate that this TopSubscriptionTopicic is authored for "
            "testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for SubscriptionTopic",
        description=(
            "Business identifiers assigned to this SubscriptionTopic by the "
            "performer and/or other systems.  These identifiers remain constant as "
            "the resource is updated and propagates from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for Topic (if applicable)",
        description="A jurisdiction in which the Topic is intended to be used.",
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Date the Subscription Topic was last reviewed by the publisher",
        description=(
            "The date on which the asset content was last reviewed. Review happens "
            "periodically after that, but doesn't change the original approval "
            "date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    publisher: fhirtypes.ReferenceType = Field(
        None,
        alias="publisher",
        title=(
            "The name of the individual or organization that published the "
            "SubscriptionTopic"
        ),
        description=(
            'Helps establish the "authority/credibility" of the SubscriptionTopic.'
            "  May also allow for contact."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this SubscriptionTopic is defined",
        description=(
            "Explains why this Topic is needed and why it has been designed as it "
            "has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    resourceTrigger: typing.List[
        fhirtypes.SubscriptionTopicResourceTriggerType
    ] = Field(
        None,
        alias="resourceTrigger",
        title="Criteria for including a resource update in the subscription topic",
        description=(
            "The criteria for including updates to a nominated resource in the "
            "subscription topic.  Thie criteria may be just a human readable "
            "description and/or a full FHIR search string or FHIRPath expression."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The current state of the SubscriptionTopic.",
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

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this SubscriptionTopic (Human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the SubscriptionTopic, "
            'for example, "admission".'
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
        title=(
            "Logical canonical URL to reference this SubscriptionTopic (globally "
            "unique)"
        ),
        description=(
            "An absolute URL that is used to identify this SubscriptionTopic when "
            "it is referenced in a specification, model, design or an instance. "
            "This SHALL be a URL, SHOULD be globally unique, and SHOULD be an "
            "address at which this Topic is (or will be) published. The URL SHOULD "
            "include the major version of the Topic. For more information see "
            "[Technical and Business Versions](resource.html#versions)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="Content intends to support these contexts",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching of code system definitions."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the SubscriptionTopic",
        description=(
            "The identifier that is used to identify this version of the "
            "SubscriptionTopic when it is referenced in a specification, model, "
            "design or instance. This is an arbitrary value managed by the Topic "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions are orderable."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubscriptionTopic`` according specification,
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
            "title",
            "derivedFrom",
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
            "resourceTrigger",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1978(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext"), ("url", "url__ext")]
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


class SubscriptionTopicResourceTrigger(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Criteria for including a resource update in the subscription topic.
    The criteria for including updates to a nominated resource in the
    subscription topic.  Thie criteria may be just a human readable description
    and/or a full FHIR search string or FHIRPath expression.
    """

    resource_type = Field("SubscriptionTopicResourceTrigger", const=True)

    canFilterBy: typing.List[
        fhirtypes.SubscriptionTopicResourceTriggerCanFilterByType
    ] = Field(
        None,
        alias="canFilterBy",
        title=(
            "Properties by which a Subscription can further filter a "
            "SubscriptionTopic"
        ),
        description=(
            "List of properties by which Subscriptions on the subscription topic "
            "can be filtered."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Text representation of the trigger",
        description=(
            "The human readable description of what triggers inclusion into this "
            'subscription topic -  for example, "Beginning of a clinical '
            'encounter".'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    fhirPathCriteria: typing.List[fhirtypes.String] = Field(
        None,
        alias="fhirPathCriteria",
        title="FHIRPath based trigger rule",
        description=(
            "The FHIRPath based rules that the server should use to determine when "
            "to trigger a notification for this topic.  If there are multiple, "
            "FHIRPath filters are joined with AND."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    fhirPathCriteria__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_fhirPathCriteria",
        title="Extension field for ``fhirPathCriteria``.",
    )

    methodCriteria: typing.List[fhirtypes.Code] = Field(
        None,
        alias="methodCriteria",
        title="create | update | delete",
        description=(
            "The REST interaction based rules that the server should use to "
            "determine when to trigger a notification for this topic."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["create", "update", "delete"],
    )
    methodCriteria__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_methodCriteria", title="Extension field for ``methodCriteria``."
    )

    queryCriteria: fhirtypes.SubscriptionTopicResourceTriggerQueryCriteriaType = Field(
        None,
        alias="queryCriteria",
        title="Query based trigger rule",
        description=(
            "The FHIR query based rules that the server should use to determine "
            "when to trigger a notification for this subscription topic."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    resourceType: fhirtypes.Uri = Field(
        None,
        alias="resourceType",
        title=(
            "Allowed Data type or Resource (reference to definition) for this "
            "definition"
        ),
        description=(
            "URL of the Resource that is the type used in this trigger.  Relative "
            "URLs are relative to the StructureDefinition root of the implemented "
            "FHIR version (e.g., http://hl7.org/fhir/StructureDefinition). For "
            'example, "Patient" maps to '
            "http://hl7.org/fhir/StructureDefinition/Patient.  For more "
            'information, see <a href="elementdefinition-definitions.html#ElementDe'
            'finition.type.code">ElementDefinition.type.code</a>.'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    resourceType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resourceType", title="Extension field for ``resourceType``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubscriptionTopicResourceTrigger`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "resourceType",
            "methodCriteria",
            "queryCriteria",
            "fhirPathCriteria",
            "canFilterBy",
        ]


class SubscriptionTopicResourceTriggerCanFilterBy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Properties by which a Subscription can further filter a SubscriptionTopic.
    List of properties by which Subscriptions on the subscription topic can be
    filtered.
    """

    resource_type = Field("SubscriptionTopicResourceTriggerCanFilterBy", const=True)

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="Description of this filter parameter",
        description="Description of how this filter parameter is intended to be used.",
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    searchModifier: typing.List[fhirtypes.Code] = Field(
        None,
        alias="searchModifier",
        title=(
            "= | eq | ne | gt | lt | ge | le | sa | eb | ap | above | below | in | "
            "not-in | of-type"
        ),
        description=(
            "Allowable operators to apply when determining matches (Search "
            "Modifiers)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "=",
            "eq",
            "ne",
            "gt",
            "lt",
            "ge",
            "le",
            "sa",
            "eb",
            "ap",
            "above",
            "below",
            "in",
            "not-in",
            "of-type",
        ],
    )
    searchModifier__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_searchModifier", title="Extension field for ``searchModifier``."
    )

    searchParamName: fhirtypes.String = Field(
        None,
        alias="searchParamName",
        title="Search parameter that serves as filter key",
        description='A search parameter (like "patient") which is a label for the filter.',
        # if property is element of this resource.
        element_property=True,
    )
    searchParamName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_searchParamName", title="Extension field for ``searchParamName``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubscriptionTopicResourceTriggerCanFilterBy`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "searchParamName",
            "searchModifier",
            "documentation",
        ]


class SubscriptionTopicResourceTriggerQueryCriteria(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Query based trigger rule.
    The FHIR query based rules that the server should use to determine when to
    trigger a notification for this subscription topic.
    """

    resource_type = Field("SubscriptionTopicResourceTriggerQueryCriteria", const=True)

    current: fhirtypes.String = Field(
        None,
        alias="current",
        title="Rule applied to current resource state",
        description="The FHIR query based rules are applied to the current resource state.",
        # if property is element of this resource.
        element_property=True,
    )
    current__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_current", title="Extension field for ``current``."
    )

    previous: fhirtypes.String = Field(
        None,
        alias="previous",
        title="Rule applied to previous resource state",
        description="The FHIR query based rules are applied to the previous resource state.",
        # if property is element of this resource.
        element_property=True,
    )
    previous__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_previous", title="Extension field for ``previous``."
    )

    requireBoth: bool = Field(
        None,
        alias="requireBoth",
        title="Both must be true flag",
        description=(
            "If set to true, both current and previous criteria must evaluate true "
            "to  trigger a notification for this topic.  Otherwise a notification "
            "for this topic will be triggered if either one evaluates to true."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    requireBoth__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requireBoth", title="Extension field for ``requireBoth``."
    )

    resultForCreate: fhirtypes.Code = Field(
        None,
        alias="resultForCreate",
        title="test-passes | test-fails",
        description=(
            "What behavior a server will exhibit if the previous state of a "
            "resource does NOT exist (e.g., during a CREATE)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["test-passes", "test-fails"],
    )
    resultForCreate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resultForCreate", title="Extension field for ``resultForCreate``."
    )

    resultForDelete: fhirtypes.Code = Field(
        None,
        alias="resultForDelete",
        title="test-passes | test-fails",
        description=(
            "What behavior a server will exhibit if the current state of a resource"
            " does NOT exist (e.g., during a DELETE)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["test-passes", "test-fails"],
    )
    resultForDelete__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resultForDelete", title="Extension field for ``resultForDelete``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubscriptionTopicResourceTriggerQueryCriteria`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "previous",
            "resultForCreate",
            "current",
            "resultForDelete",
            "requireBoth",
        ]
