# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Base
Release: R4
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
from pydantic import Field

from . import fhirabstractmodel


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
        """returning all elements names from ``Base`` according specification,
        with preserving original sequence order.
        """
        return []
