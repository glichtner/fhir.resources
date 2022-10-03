# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BodyStructure
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
import typing
from pydantic import Field
from . import fhirtypes


from . import domainresource

class BodyStructure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specific and identified anatomical structure.
    Record details about an anatomical structure.  This resource may be used
    when a coded concept does not provide the necessary detail needed for the
    use case.
    """
    resource_type = Field("BodyStructure", const=True)
	
    active: bool = Field(
		None,
		alias="active",
		title="Whether this record is in active use",
		description="Whether this body site is in active use.",
        # if property is element of this resource.
        element_property=True,
	)
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_active",
        title="Extension field for ``active``."
    )
	
    description: fhirtypes.String = Field(
		None,
		alias="description",
		title="Text description",
		description="A summary, characterization or explanation of the body structure.",
        # if property is element of this resource.
        element_property=True,
	)
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_description",
        title="Extension field for ``description``."
    )
	
    excludedStructure: typing.List[fhirtypes.BodyStructureExcludedStructureType] = Field(
		None,
		alias="excludedStructure",
		title="Excluded anatomic locations(s)",
		description=(
    "The anatomical location(s) or region(s) not occupied or represented by"
    " the specimen, lesion, or body structure."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    identifier: typing.List[fhirtypes.IdentifierType] = Field(
		None,
		alias="identifier",
		title="Bodystructure identifier",
		description="Identifier for this instance of the anatomical structure.",
        # if property is element of this resource.
        element_property=True,
	)
	
    image: typing.List[fhirtypes.AttachmentType] = Field(
		None,
		alias="image",
		title="Attached images",
		description="Image or images used to identify a location.",
        # if property is element of this resource.
        element_property=True,
	)
	
    includedStructure: typing.List[fhirtypes.BodyStructureIncludedStructureType] = Field(
		...,
		alias="includedStructure",
		title="Included anatomic location(s)",
		description=(
    "The anatomical location(s) or region(s) of the specimen, lesion, or "
    "body structure."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    morphology: fhirtypes.CodeableConceptType = Field(
		None,
		alias="morphology",
		title="Kind of Structure",
		description=(
    "The kind of structure being represented by the body structure at "
    "`BodyStructure.location`.  This can define both normal and abnormal "
    "morphologies."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    patient: fhirtypes.ReferenceType = Field(
		...,
		alias="patient",
		title="Who this is about",
		description="The person to which the body site belongs.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Patient"],
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BodyStructure`` according specification,
        with preserving original sequence order.
        """
        return ["id", "meta", "implicitRules", "language", "text", "contained", "extension", "modifierExtension", "identifier", "active", "morphology", "includedStructure", "excludedStructure", "description", "image", "patient"]



from . import backboneelement

class BodyStructureExcludedStructure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Excluded anatomic locations(s).
    The anatomical location(s) or region(s) not occupied or represented by the
    specimen, lesion, or body structure.
    """
    resource_type = Field("BodyStructureExcludedStructure", const=True)
	
    laterality: fhirtypes.CodeableConceptType = Field(
		None,
		alias="laterality",
		title="Code that represents the excluded structure laterality",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    qualifier: typing.List[fhirtypes.CodeableConceptType] = Field(
		None,
		alias="qualifier",
		title="Code that represents the excluded structure qualifier",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    structure: fhirtypes.CodeableConceptType = Field(
		...,
		alias="structure",
		title="Code that represents the excluded structure",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BodyStructureExcludedStructure`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "structure", "laterality", "qualifier"]



class BodyStructureIncludedStructure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Included anatomic location(s).
    The anatomical location(s) or region(s) of the specimen, lesion, or body
    structure.
    """
    resource_type = Field("BodyStructureIncludedStructure", const=True)
	
    laterality: fhirtypes.CodeableConceptType = Field(
		None,
		alias="laterality",
		title="Code that represents the included structure laterality",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    qualifier: typing.List[fhirtypes.CodeableConceptType] = Field(
		None,
		alias="qualifier",
		title="Code that represents the included structure qualifier",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    structure: fhirtypes.CodeableConceptType = Field(
		...,
		alias="structure",
		title="Code that represents the included structure",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BodyStructureIncludedStructure`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "structure", "laterality", "qualifier"]

