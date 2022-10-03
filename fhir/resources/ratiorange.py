# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RatioRange
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic import Field
from . import fhirtypes


from . import datatype

class RatioRange(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Range of ratio values.
    A range of ratios expressed as a low and high numerator and a denominator.
    """
    resource_type = Field("RatioRange", const=True)
	
    denominator: fhirtypes.QuantityType = Field(
		None,
		alias="denominator",
		title="Denominator value",
		description="The value of the denominator.",
        # if property is element of this resource.
        element_property=True,
	)
	
    highNumerator: fhirtypes.QuantityType = Field(
		None,
		alias="highNumerator",
		title="High Numerator limit",
		description="The value of the high limit numerator.",
        # if property is element of this resource.
        element_property=True,
	)
	
    lowNumerator: fhirtypes.QuantityType = Field(
		None,
		alias="lowNumerator",
		title="Low Numerator limit",
		description="The value of the low limit numerator.",
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RatioRange`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "lowNumerator", "highNumerator", "denominator"]

