# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing
from pydantic import Field
from . import fhirtypes


from . import domainresource

class OrganizationAffiliation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines an affiliation/association/relationship between 2 distinct
    organizations, that is not a part-of relationship/sub-division relationship.
    """
    resource_type = Field("OrganizationAffiliation", const=True)
	
    active: bool = Field(
		None,
		alias="active",
		title="Whether this organization affiliation record is in active use",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_active",
        title="Extension field for ``active``."
    )
	
    code: typing.List[fhirtypes.CodeableConceptType] = Field(
		None,
		alias="code",
		title="Definition of the role the participatingOrganization plays",
		description=(
    "Definition of the role the participatingOrganization plays in the "
    "association."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    contact: typing.List[fhirtypes.ExtendedContactDetailType] = Field(
		None,
		alias="contact",
		title=(
    "Official contact details at the participatingOrganization relevant to "
    "this Affiliation"
    ),
		description=(
    "The contact details of communication devices available at the "
    "participatingOrganization relevant to this Affiliation."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="endpoint",
		title=(
    "Technical endpoints providing access to services operated for this "
    "role"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Endpoint"],
	)
	
    healthcareService: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="healthcareService",
		title="Healthcare services provided through the role",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["HealthcareService"],
	)
	
    identifier: typing.List[fhirtypes.IdentifierType] = Field(
		None,
		alias="identifier",
		title="Business identifiers that are specific to this role",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    location: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="location",
		title="The location(s) at which the role occurs",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Location"],
	)
	
    network: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="network",
		title=(
    "The network in which the participatingOrganization provides the role's"
    " services (if defined) at the indicated locations (if defined)"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Organization"],
	)
	
    organization: fhirtypes.ReferenceType = Field(
		None,
		alias="organization",
		title="Organization where the role is available",
		description=(
    "Organization where the role is available (primary organization/has "
    "members)."
    ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Organization"],
	)
	
    participatingOrganization: fhirtypes.ReferenceType = Field(
		None,
		alias="participatingOrganization",
		title=(
    "Organization that provides/performs the role (e.g. providing services "
    "or is a member of)"
    ),
		description=(
    "The Participating Organization provides/performs the role(s) defined "
    "by the code to the Primary Organization (e.g. providing services or is"
    " a member of)."
    ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Organization"],
	)
	
    period: fhirtypes.PeriodType = Field(
		None,
		alias="period",
		title=(
    "The period during which the participatingOrganization is affiliated "
    "with the primary organization"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    specialty: typing.List[fhirtypes.CodeableConceptType] = Field(
		None,
		alias="specialty",
		title=(
    "Specific specialty of the participatingOrganization in the context of "
    "the role"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``OrganizationAffiliation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "meta", "implicitRules", "language", "text", "contained", "extension", "modifierExtension", "identifier", "active", "period", "organization", "participatingOrganization", "network", "code", "specialty", "location", "healthcareService", "contact", "endpoint"]

