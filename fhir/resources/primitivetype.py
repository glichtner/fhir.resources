# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PrimitiveType
Release: R4
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic import Field

from . import datatype


class PrimitiveType(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Parent type for DataTypes with a simple value.
    The base type for all re-useable types defined that have a simple property.
    """

    resource_type = Field("PrimitiveType", const=True)

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``PrimitiveType`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension"]
