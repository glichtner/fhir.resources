# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Range
Release: R4
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic import Field
from . import fhirtypes


from . import datatype


class Range(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Set of values bounded by low and high.
    A set of ordered Quantities defined by a low and high limit.
    """

    resource_type = Field("Range", const=True)

    high: fhirtypes.QuantityType = Field(
        None,
        alias="high",
        title="High limit",
        description="The high limit. The boundary is inclusive.",
        # if property is element of this resource.
        element_property=True,
    )

    low: fhirtypes.QuantityType = Field(
        None,
        alias="low",
        title="Low limit",
        description="The low limit. The boundary is inclusive.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``Range`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "low", "high"]
