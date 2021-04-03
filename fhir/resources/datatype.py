# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DataType
Release: R4
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic import Field

from . import element


class DataType(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Reuseable Types.
    The base class for all re-useable types defined as part of the FHIR
    Specification.
    """

    resource_type = Field("DataType", const=True)

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DataType`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension"]
