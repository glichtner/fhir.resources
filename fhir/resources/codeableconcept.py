# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeableConcept
Release: R4
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
import typing
from pydantic import Field
from . import fhirtypes


from . import datatype


class CodeableConcept(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Concept - reference to a terminology or just  text.
    A concept that may be defined by a formal reference to a terminology or
    ontology or may be provided by text.
    """

    resource_type = Field("CodeableConcept", const=True)

    coding: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="coding",
        title="Code defined by a terminology system",
        description="A reference to a code defined by a terminology system.",
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Plain text representation of the concept",
        description=(
            "A human language representation of the concept as "
            "seen/selected/uttered by the user who entered the data and/or which "
            "represents the intended meaning of the user."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CodeableConcept`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "coding", "text"]
