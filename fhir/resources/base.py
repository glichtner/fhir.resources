# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Base
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
from pydantic import Field

from fhir.resources.core import fhirabstractmodel

class Base(fhirabstractmodel.FHIRAbstractModel):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base for all types and resources.
    Base definition for all types defined in FHIR type system.
    """
    resource_type = Field("Base", const=True)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Base`` according specification,
        with preserving original sequence order.
        """
        return []

