# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Money
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic import Field
from . import fhirtypes


from . import datatype

class Money(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An amount of economic utility in some recognized currency.
    """
    resource_type = Field("Money", const=True)
	
    currency: fhirtypes.Code = Field(
		None,
		alias="currency",
		title="ISO 4217 Currency Code",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    currency__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_currency",
        title="Extension field for ``currency``."
    )
	
    value: fhirtypes.Decimal = Field(
		None,
		alias="value",
		title="Numerical value (with implicit precision)",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_value",
        title="Extension field for ``value``."
    )
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Money`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "currency"]

