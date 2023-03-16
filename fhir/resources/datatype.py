# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DataType
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
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
        """returning all elements names from
        ``DataType`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension"]

