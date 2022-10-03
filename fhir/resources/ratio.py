# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Ratio
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic import Field
from . import fhirtypes


from . import datatype

class Ratio(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A ratio of two Quantity values - a numerator and a denominator.
    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """
    resource_type = Field("Ratio", const=True)
	
    denominator: fhirtypes.QuantityType = Field(
		None,
		alias="denominator",
		title="Denominator value",
		description="The value of the denominator.",
        # if property is element of this resource.
        element_property=True,
	)
	
    numerator: fhirtypes.QuantityType = Field(
		None,
		alias="numerator",
		title="Numerator value",
		description="The value of the numerator.",
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Ratio`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "numerator", "denominator"]

