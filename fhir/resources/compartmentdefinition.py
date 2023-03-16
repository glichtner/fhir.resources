# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CompartmentDefinition
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
import typing
from pydantic import Field
from pydantic import root_validator

from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import fhirtypes


from . import domainresource

class CompartmentDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Compartment Definition for a resource.
    A compartment definition that defines how resources are accessed on a
    server.
    """
    resource_type = Field("CompartmentDefinition", const=True)
	
    code: fhirtypes.Code = Field(
		None,
		alias="code",
		title=(
    "Patient | Encounter | RelatedPerson | Practitioner | Device | "
    "EpisodeOfCare"
    ),
		description="Which compartment this definition describes.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
		enum_values=["Patient", "Encounter", "RelatedPerson", "Practitioner", "Device", "EpisodeOfCare"],
	)
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_code",
        title="Extension field for ``code``."
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
    "The date  (and optionally time) when the compartment definition was "
    "last significantly changed. The date must change when the business "
    "version changes and it must change if the status code changes. In "
    "addition, it should change when the substantive content of the "
    "compartment definition changes."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_date",
        title="Extension field for ``date``."
    )
	
    description: fhirtypes.Markdown = Field(
		None,
		alias="description",
		title="Natural language description of the compartment definition",
		description=(
    "A free text natural language description of the compartment definition"
    " from a consumer's perspective."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_description",
        title="Extension field for ``description``."
    )
	
    experimental: bool = Field(
		None,
		alias="experimental",
		title="For testing purposes, not real usage",
		description=(
    "A Boolean value to indicate that this compartment definition is "
    "authored for testing purposes (or education/evaluation/marketing) and "
    "is not intended to be used for genuine usage."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_experimental",
        title="Extension field for ``experimental``."
    )
	
    name: fhirtypes.String = Field(
		None,
		alias="name",
		title="Name for this compartment definition (computer friendly)",
		description=(
    "A natural language name identifying the compartment definition. This "
    "name should be usable as an identifier for the module by machine "
    "processing applications such as code generation."
    ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
	)
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_name",
        title="Extension field for ``name``."
    )
	
    publisher: fhirtypes.String = Field(
		None,
		alias="publisher",
		title="Name of the publisher/steward (organization or individual)",
		description=(
    "The name of the organization or individual responsible for the release"
    " and ongoing maintenance of the compartment definition."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_publisher",
        title="Extension field for ``publisher``."
    )
	
    purpose: fhirtypes.Markdown = Field(
		None,
		alias="purpose",
		title="Why this compartment definition is defined",
		description=(
    "Explanation of why this compartment definition is needed and why it "
    "has been designed as it has."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_purpose",
        title="Extension field for ``purpose``."
    )
	
    resource: typing.List[fhirtypes.CompartmentDefinitionResourceType] = Field(
		None,
		alias="resource",
		title="How a resource is related to the compartment",
		description="Information about how a resource is related to the compartment.",
        # if property is element of this resource.
        element_property=True,
	)
	
    search: bool = Field(
		None,
		alias="search",
		title="Whether the search syntax is supported",
		description="Whether the search syntax is supported,.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
	)
    search__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_search",
        title="Extension field for ``search``."
    )
	
    status: fhirtypes.Code = Field(
		None,
		alias="status",
		title="draft | active | retired | unknown",
		description=(
    "The status of this compartment definition. Enables tracking the life-"
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
        None,
        alias="_status",
        title="Extension field for ``status``."
    )
	
    title: fhirtypes.String = Field(
		None,
		alias="title",
		title="Name for this compartment definition (human friendly)",
		description=(
    "A short, descriptive, user-friendly title for the capability "
    "statement."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_title",
        title="Extension field for ``title``."
    )
	
    url: fhirtypes.Uri = Field(
		None,
		alias="url",
		title=(
    "Canonical identifier for this compartment definition, represented as a"
    " URI (globally unique)"
    ),
		description=(
    "An absolute URI that is used to identify this compartment definition "
    "when it is referenced in a specification, model, design or an "
    "instance; also called its canonical identifier. This SHOULD be "
    "globally unique and SHOULD be a literal address at which an "
    "authoritative instance of this compartment definition is (or will be) "
    "published. This URL can be the target of a canonical reference. It "
    "SHALL remain the same when the compartment definition is stored on "
    "different servers."
    ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
	)
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_url",
        title="Extension field for ``url``."
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
    "indexing and searching for appropriate compartment definition "
    "instances."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    version: fhirtypes.String = Field(
		None,
		alias="version",
		title="Business version of the compartment definition",
		description=(
    "The identifier that is used to identify this version of the "
    "compartment definition when it is referenced in a specification, "
    "model, design or instance. This is an arbitrary value managed by the "
    "compartment definition author and is not expected to be globally "
    "unique. For example, it might be a timestamp (e.g. yyyymmdd) if a "
    "managed version is not available. There is also no expectation that "
    "versions can be placed in a lexicographical sequence."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_version",
        title="Extension field for ``version``."
    )
	
    versionAlgorithmCoding: fhirtypes.CodingType = Field(
		None,
		alias="versionAlgorithmCoding",
		title="How to compare versions",
		description=(
    "Indicates the mechanism used to compare versions to determine which is"
    " more current."
    ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
		one_of_many="versionAlgorithm",
		one_of_many_required=False,
	)
	
    versionAlgorithmString: fhirtypes.String = Field(
		None,
		alias="versionAlgorithmString",
		title="How to compare versions",
		description=(
    "Indicates the mechanism used to compare versions to determine which is"
    " more current."
    ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
		one_of_many="versionAlgorithm",
		one_of_many_required=False,
	)
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``."
    )
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompartmentDefinition`` according specification,
        with preserving original sequence order.
        """
        return ["id", "meta", "implicitRules", "language", "text", "contained", "extension", "modifierExtension", "url", "version", "versionAlgorithmString", "versionAlgorithmCoding", "name", "title", "status", "experimental", "date", "publisher", "contact", "description", "useContext", "purpose", "code", "search", "resource"]


    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2372(
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
			("code", "code__ext"),
			("name", "name__ext"),
			("search", "search__ext"),
			("status", "status__ext"),
			("url", "url__ext")]
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
    def validate_one_of_many_2372(
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
			"versionAlgorithm": [
			    "versionAlgorithmCoding",
			    "versionAlgorithmString"]}
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

class CompartmentDefinitionResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How a resource is related to the compartment.
    Information about how a resource is related to the compartment.
    """
    resource_type = Field("CompartmentDefinitionResource", const=True)
	
    code: fhirtypes.Code = Field(
		None,
		alias="code",
		title="Name of resource type",
		description="The name of a resource supported by the server.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
	)
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_code",
        title="Extension field for ``code``."
    )
	
    documentation: fhirtypes.String = Field(
		None,
		alias="documentation",
		title="Additional documentation about the resource and compartment",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_documentation",
        title="Extension field for ``documentation``."
    )
	
    endParam: fhirtypes.Uri = Field(
		None,
		alias="endParam",
		title="Search Param for interpreting $everything.end",
		description=(
    "Search Parameter for mapping requests made with $everything.end (e.g. "
    "on [Patient.$everything](patient-operation-everything.html))."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    endParam__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_endParam",
        title="Extension field for ``endParam``."
    )
	
    param: typing.List[typing.Optional[fhirtypes.String]] = Field(
		None,
		alias="param",
		title="Search Parameter Name, or chained parameters",
		description=(
    "The name of a search parameter that represents the link to the "
    "compartment. More than one may be listed because a resource may be "
    "linked to a compartment in more than one way,."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    param__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None,
        alias="_param",
        title="Extension field for ``param``."
    )
	
    startParam: fhirtypes.Uri = Field(
		None,
		alias="startParam",
		title="Search Param for interpreting $everything.start",
		description=(
    "Search Parameter for mapping requests made with $everything.start "
    "(e.g. on [Patient.$everything](patient-operation-everything.html))."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    startParam__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_startParam",
        title="Extension field for ``startParam``."
    )
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompartmentDefinitionResource`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "param", "documentation", "startParam", "endParam"]


    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3203(
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
			("code", "code__ext")]
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
