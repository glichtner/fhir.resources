# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement2
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


from . import canonicalresource


class CapabilityStatement2(canonicalresource.CanonicalResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A statement of system capabilities.
    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server for a particular version of FHIR that may be used as a
    statement of actual server functionality or a statement of required or
    desired server implementation.
    """

    resource_type = Field("CapabilityStatement2", const=True)

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
            "A copyright statement relating to the capability statement2 and/or its"
            " contents. Copyright statements are generally legal restrictions on "
            "the use and publishing of the capability statement2."
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
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the capability statement2 was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the capability statement2 "
            "changes."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the capability statement2",
        description=(
            "A free text natural language description of the capability statement2 "
            "from a consumer's perspective. Typically, this is used when the "
            "capability statement describes a desired rather than an actual "
            "solution, for example as a formal expression of requirements as part "
            "of an RFP."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this capability statement2 is "
            "authored for testing purposes (or education/evaluation/marketing) and "
            "is not intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fhirVersion: fhirtypes.Code = Field(
        None,
        alias="fhirVersion",
        title="FHIR Version the system supports",
        description=(
            "The version of the FHIR specification that this CapabilityStatement2 "
            "describes (which SHALL be the same as the FHIR version of the "
            "CapabilityStatement2 itself). There is no default value."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fhirVersion", title="Extension field for ``fhirVersion``."
    )

    format: typing.List[fhirtypes.Code] = Field(
        None,
        alias="format",
        title="formats supported (xml | json | ttl | mime type)",
        description=(
            "A list of the formats supported by this implementation using their "
            "content types."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["formats", "json", "ttl", "mime"],
    )
    format__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_format", title="Extension field for ``format``.")

    implementation: fhirtypes.CapabilityStatement2ImplementationType = Field(
        None,
        alias="implementation",
        title="If this describes a specific instance",
        description=(
            "Identifies a specific implementation instance that is described by the"
            " capability statement - i.e. a particular installation, rather than "
            "the capabilities of a software program."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    implementationGuide: typing.List[fhirtypes.Canonical] = Field(
        None,
        alias="implementationGuide",
        title="Implementation guides supported",
        description=(
            "A list of implementation guides that the server does (or should) "
            "support in their entirety."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ImplementationGuide"],
    )
    implementationGuide__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_implementationGuide",
        title="Extension field for ``implementationGuide``.",
    )

    imports: typing.List[fhirtypes.Canonical] = Field(
        None,
        alias="imports",
        title="Canonical URL of another capability statement this adds to",
        description=(
            "Reference to a canonical URL of another CapabilityStatement2 that this"
            " software adds to. The capability statement automatically includes "
            "everything in the other statement, and it is not duplicated, though "
            "the server may repeat the same resources, interactions and operations "
            "to add additional details to them."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CapabilityStatement2"],
    )
    imports__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_imports", title="Extension field for ``imports``.")

    instantiates: typing.List[fhirtypes.Canonical] = Field(
        None,
        alias="instantiates",
        title="Canonical URL of another capability statement this implements",
        description=(
            "Reference to a canonical URL of another CapabilityStatement2 that this"
            " software implements. This capability statement is a published API "
            "description that corresponds to a business service. The server may "
            "actually implement a subset of the capability statement it claims to "
            "implement, so the capability statement must specify the full "
            "capability details."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CapabilityStatement2"],
    )
    instantiates__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiates", title="Extension field for ``instantiates``."
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for capability statement2 (if applicable)",
        description=(
            "A legal or geographic region in which the capability statement2 is "
            "intended to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    kind: fhirtypes.Code = Field(
        None,
        alias="kind",
        title="instance | capability | requirements",
        description=(
            "The way that this statement is intended to be used, to describe an "
            "actual running instance of software, a particular product (kind, not "
            "instance of software) or a class of implementation (e.g. a desired "
            "purchase)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["instance", "capability", "requirements"],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this capability statement2 (computer friendly)",
        description=(
            "A natural language name identifying the capability statement2. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    patchFormat: typing.List[fhirtypes.Code] = Field(
        None,
        alias="patchFormat",
        title="Patch formats supported",
        description=(
            "A list of the patch formats supported by this implementation using "
            "their content types."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    patchFormat__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_patchFormat", title="Extension field for ``patchFormat``.")

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the "
            "capability statement2."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this capability statement2 is defined",
        description=(
            "Explanation of why this capability statement2 is needed and why it has"
            " been designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    rest: typing.List[fhirtypes.CapabilityStatement2RestType] = Field(
        None,
        alias="rest",
        title="If the endpoint is a RESTful one",
        description="A definition of the restful capabilities of the solution, if any.",
        # if property is element of this resource.
        element_property=True,
    )

    software: fhirtypes.CapabilityStatement2SoftwareType = Field(
        None,
        alias="software",
        title="Software that is covered by this capability statement",
        description=(
            "Software that is covered by this capability statement.  It is used "
            "when the capability statement describes the capabilities of a "
            "particular software version, independent of an installation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this capability statement2. Enables tracking the life-"
            "cycle of the content."
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

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this capability statement2 (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the capability "
            "statement2."
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
            "Canonical identifier for this capability statement2, represented as a "
            "URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this capability statement2 "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this capability statement2 is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the capability statement2 is stored on "
            "different servers."
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
            "indexing and searching for appropriate capability statement2 "
            "instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the capability statement2",
        description=(
            "The identifier that is used to identify this version of the capability"
            " statement2 when it is referenced in a specification, model, design or"
            " instance. This is an arbitrary value managed by the capability "
            "statement2 author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CapabilityStatement2`` according specification,
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
            "url",
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
            "kind",
            "instantiates",
            "imports",
            "software",
            "implementation",
            "fhirVersion",
            "format",
            "patchFormat",
            "implementationGuide",
            "rest",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2174(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("date", "date__ext"),
            ("fhirVersion", "fhirVersion__ext"),
            ("format", "format__ext"),
            ("kind", "kind__ext"),
            ("status", "status__ext"),
        ]
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


class CapabilityStatement2Implementation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this describes a specific instance.
    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """

    resource_type = Field("CapabilityStatement2Implementation", const=True)

    custodian: fhirtypes.ReferenceType = Field(
        None,
        alias="custodian",
        title="Organization that manages the data",
        description=(
            "The organization responsible for the management of the instance and "
            "oversight of the data on the server at the specified URL."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Describes this specific instance",
        description=(
            "Information about the specific installation that this capability "
            "statement relates to."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    url: fhirtypes.Url = Field(
        None,
        alias="url",
        title="Base URL for the installation",
        description=(
            "An absolute base URL for the implementation.  This forms the base for "
            "REST interfaces as well as the mailbox and document interfaces."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CapabilityStatement2Implementation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "url",
            "custodian",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3680(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("description", "description__ext")]
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


class CapabilityStatement2Rest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If the endpoint is a RESTful one.
    A definition of the restful capabilities of the solution, if any.
    """

    resource_type = Field("CapabilityStatement2Rest", const=True)

    compartment: typing.List[fhirtypes.Canonical] = Field(
        None,
        alias="compartment",
        title="Compartments served/used by system",
        description=(
            "An absolute URI which is a reference to the definition of a "
            "compartment that the system supports. The reference is to a "
            "CompartmentDefinition resource by its canonical URL ."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CompartmentDefinition"],
    )
    compartment__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_compartment", title="Extension field for ``compartment``.")

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="General description of implementation",
        description=(
            "Information about the system's restful capabilities that apply across "
            "all applications, such as security."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    feature: typing.List[fhirtypes.CapabilityStatement2RestFeatureType] = Field(
        None,
        alias="feature",
        title="Statement of support for a feature",
        description="A statement that affirms support for a feature.",
        # if property is element of this resource.
        element_property=True,
    )

    interaction: typing.List[fhirtypes.CapabilityStatement2RestInteractionType] = Field(
        None,
        alias="interaction",
        title="What operations are supported?",
        description="A specification of restful operations supported by the system.",
        # if property is element of this resource.
        element_property=True,
    )

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="client | server",
        description=(
            "Identifies whether this portion of the statement is describing the "
            "ability to initiate or receive restful operations."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["client", "server"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    operation: typing.List[
        fhirtypes.CapabilityStatement2RestResourceOperationType
    ] = Field(
        None,
        alias="operation",
        title="Definition of a system level operation",
        description=(
            "Definition of an operation or a named query together with its "
            "parameters and their meaning and type."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    resource: typing.List[fhirtypes.CapabilityStatement2RestResourceType] = Field(
        None,
        alias="resource",
        title="Resource served on the REST interface",
        description=(
            "A specification of the restful capabilities of the solution for a "
            "specific resource type."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    searchParam: typing.List[
        fhirtypes.CapabilityStatement2RestResourceSearchParamType
    ] = Field(
        None,
        alias="searchParam",
        title="Search parameters for searching all resources",
        description=(
            "Search parameters that are supported for searching all resources for "
            "implementations to support and/or make use of - either references to "
            "ones defined in the specification, or additional ones defined for/by "
            "the implementation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CapabilityStatement2Rest`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "mode",
            "documentation",
            "feature",
            "resource",
            "interaction",
            "searchParam",
            "operation",
            "compartment",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2622(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext")]
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


class CapabilityStatement2RestFeature(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Statement of support for a feature.
    A statement that affirms support for a feature.
    """

    resource_type = Field("CapabilityStatement2RestFeature", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Feature that is being reported",
        description="A code that describes the feature being reported on.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    value: fhirtypes.Code = Field(
        None,
        alias="value",
        title="Value of the feature (true, false, or a code)",
        description=(
            "A value for the feature - maybe true, false, or one of the set of "
            "codes allowed in the definition of the feature code."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CapabilityStatement2RestFeature`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "value"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3323(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("value", "value__ext")]
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


class CapabilityStatement2RestInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What operations are supported?.
    A specification of restful operations supported by the system.
    """

    resource_type = Field("CapabilityStatement2RestInteraction", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="transaction | batch | search-system | history-system",
        description="A coded identifier of the operation, supported by the system.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["transaction", "batch", "search-system", "history-system"],
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="Anything special about operation behavior",
        description=(
            "Guidance specific to the implementation of this operation, such as "
            "limitations on the kind of transactions allowed, or information about "
            "system wide search is implemented."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    feature: typing.List[fhirtypes.CapabilityStatement2RestFeatureType] = Field(
        None,
        alias="feature",
        title="Statement of support for a feature in this context",
        description="A statement that affirms support for a feature, in this context.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CapabilityStatement2RestInteraction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "documentation",
            "feature",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3768(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
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


class CapabilityStatement2RestResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource served on the REST interface.
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """

    resource_type = Field("CapabilityStatement2RestResource", const=True)

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="Additional information about the use of the resource type",
        description="Additional information about the resource type used by the system.",
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    feature: typing.List[fhirtypes.CapabilityStatement2RestFeatureType] = Field(
        None,
        alias="feature",
        title="Statement of support for a feature in this context",
        description="A statement that affirms support for a feature, in this context.",
        # if property is element of this resource.
        element_property=True,
    )

    interaction: typing.List[
        fhirtypes.CapabilityStatement2RestResourceInteractionType
    ] = Field(
        None,
        alias="interaction",
        title="What operations are supported?",
        description="Identifies a restful operation supported by the solution.",
        # if property is element of this resource.
        element_property=True,
    )

    operation: typing.List[
        fhirtypes.CapabilityStatement2RestResourceOperationType
    ] = Field(
        None,
        alias="operation",
        title="Definition of a resource operation",
        description=(
            "Definition of an operation or a named query together with its "
            "parameters and their meaning and type. Consult the definition of the "
            "operation for details about how to invoke the operation, and the "
            "parameters."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    profile: fhirtypes.Canonical = Field(
        None,
        alias="profile",
        title="Base System profile for all uses of resource",
        description=(
            "A specification of the profile that describes the solution's overall "
            "support for the resource, including any constraints on cardinality, "
            "bindings, lengths or other limitations. See further discussion in "
            "[Using Profiles](profiling.html#profile-uses)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    searchParam: typing.List[
        fhirtypes.CapabilityStatement2RestResourceSearchParamType
    ] = Field(
        None,
        alias="searchParam",
        title="Search parameters supported by implementation",
        description=(
            "Search parameters for implementations to support and/or make use of - "
            "either references to ones defined in the specification, or additional "
            "ones defined for/by the implementation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    supportedProfile: typing.List[fhirtypes.Canonical] = Field(
        None,
        alias="supportedProfile",
        title="Profiles for use cases supported",
        description=(
            "A list of profiles that represent different use cases supported by the"
            ' system. For a server, "supported by the system" means the system '
            "hosts/produces a set of resources that are conformant to a particular "
            "profile, and allows clients that use its services to search using this"
            " profile and to find appropriate data. For a client, it means the "
            "system will search by this profile and process data according to the "
            "guidance implicit in the profile. See further discussion in [Using "
            "Profiles](profiling.html#profile-uses)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    supportedProfile__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_supportedProfile",
        title="Extension field for ``supportedProfile``.",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="A resource type that is supported",
        description="A type of resource exposed via the restful interface.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CapabilityStatement2RestResource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "profile",
            "supportedProfile",
            "documentation",
            "feature",
            "interaction",
            "searchParam",
            "operation",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3447(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
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


class CapabilityStatement2RestResourceInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What operations are supported?.
    Identifies a restful operation supported by the solution.
    """

    resource_type = Field("CapabilityStatement2RestResourceInteraction", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title=(
            "read | vread | update | patch | delete | history-instance | history-"
            "type | create | search-type"
        ),
        description="Coded identifier of the operation, supported by the system resource.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "read",
            "vread",
            "update",
            "patch",
            "delete",
            "history-instance",
            "history-type",
            "create",
            "search-type",
        ],
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="Anything special about operation behavior",
        description=(
            "Guidance specific to the implementation of this operation, such as "
            "'delete is a logical delete' or 'updates are only allowed with version"
            " id' or 'creates permitted from pre-authorized certificates only'."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    feature: typing.List[fhirtypes.CapabilityStatement2RestFeatureType] = Field(
        None,
        alias="feature",
        title="Statement of support for a feature in this context",
        description="A statement that affirms support for a feature, in this context.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CapabilityStatement2RestResourceInteraction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "documentation",
            "feature",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4608(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
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


class CapabilityStatement2RestResourceOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of a resource operation.
    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """

    resource_type = Field("CapabilityStatement2RestResourceOperation", const=True)

    definition: fhirtypes.Canonical = Field(
        None,
        alias="definition",
        title="The defined operation/query",
        description=(
            "Where the formal definition can be found. If a server references the "
            "base definition of an Operation (i.e. from the specification itself "
            "such as ```http://hl7.org/fhir/OperationDefinition/ValueSet-"
            "expand```), that means it supports the full capabilities of the "
            "operation - e.g. both GET and POST invocation.  If it only supports a "
            "subset, it must define its own custom "
            "[OperationDefinition](operationdefinition.html#) with a 'base' of the "
            "original OperationDefinition.  The custom definition would describe "
            "the specific subset of functionality supported."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["OperationDefinition"],
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="Specific details about operation behavior",
        description=(
            "Documentation that describes anything special about the operation "
            "behavior, possibly detailing different behavior for system, type and "
            "instance-level invocation of the operation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    feature: typing.List[fhirtypes.CapabilityStatement2RestFeatureType] = Field(
        None,
        alias="feature",
        title="Statement of support for a feature in this context",
        description="A statement that affirms support for a feature, in this context.",
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name by which the operation/query is invoked",
        description=(
            "The name of the operation or query. For an operation, this is the name"
            "  prefixed with $ and used in the URL. For a query, this is the name "
            "used in the _query parameter when the query is called."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CapabilityStatement2RestResourceOperation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "definition",
            "documentation",
            "feature",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4401(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("definition", "definition__ext"), ("name", "name__ext")]
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


class CapabilityStatement2RestResourceSearchParam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Search parameters supported by implementation.
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """

    resource_type = Field("CapabilityStatement2RestResourceSearchParam", const=True)

    definition: fhirtypes.Canonical = Field(
        None,
        alias="definition",
        title="Source of definition for parameter",
        description=(
            "An absolute URI that is a formal reference to where this parameter was"
            " first defined, so that a client can be confident of the meaning of "
            "the search parameter (a reference to "
            "[SearchParameter.url](searchparameter-"
            "definitions.html#SearchParameter.url)). This element SHALL be "
            "populated if the search parameter refers to a SearchParameter defined "
            "by the FHIR core specification or externally defined IGs."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SearchParameter"],
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="Server-specific usage",
        description=(
            "This allows documentation of any distinct behaviors about how the "
            "search parameter is used.  For example, text matching algorithms."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    feature: typing.List[fhirtypes.CapabilityStatement2RestFeatureType] = Field(
        None,
        alias="feature",
        title="Statement of support for a feature in this context",
        description="A statement that affirms support for a feature, in this context.",
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of search parameter",
        description="The name of the search parameter used in the interface.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title=(
            "number | date | string | token | reference | composite | quantity | "
            "uri | special"
        ),
        description=(
            "The type of value a search parameter refers to, and how the content is"
            " interpreted."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "number",
            "date",
            "string",
            "token",
            "reference",
            "composite",
            "quantity",
            "uri",
            "special",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CapabilityStatement2RestResourceSearchParam`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "definition",
            "type",
            "documentation",
            "feature",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4550(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext"), ("type", "type__ext")]
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


class CapabilityStatement2Software(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Software that is covered by this capability statement.
    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """

    resource_type = Field("CapabilityStatement2Software", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="A name the software is known by",
        description="Name the software is known by.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    releaseDate: fhirtypes.DateTime = Field(
        None,
        alias="releaseDate",
        title="Date this version was released",
        description="Date this version of the software was released.",
        # if property is element of this resource.
        element_property=True,
    )
    releaseDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_releaseDate", title="Extension field for ``releaseDate``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Version covered by this statement",
        description="The version identifier for the software covered by this statement.",
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CapabilityStatement2Software`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "version",
            "releaseDate",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3036(
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
