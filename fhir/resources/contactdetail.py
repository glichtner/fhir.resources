# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ContactDetail
Release: R4
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
import typing
from pydantic import Field
from . import fhirtypes


from . import datatype


class ContactDetail(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contact information.
    Specifies contact information for a person or organization.
    """

    resource_type = Field("ContactDetail", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of an individual to contact",
        description="The name of an individual to contact.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    telecom: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contact details for individual or organization",
        description=(
            "The contact details for the individual (if a name was provided) or the"
            " organization."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ContactDetail`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "name", "telecom"]
