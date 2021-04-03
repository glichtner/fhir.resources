# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Statistic
Release: R4
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
import typing
from pydantic import Field
from . import fhirtypes


from . import backbonetype


class Statistic(backbonetype.BackboneType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Single statistic.
    A fact or piece of data from a  study of a large quantity of numerical
    data.  A mathematical or quantified characteristic of a group of
    observations.
    """

    resource_type = Field("Statistic", const=True)

    attributeEstimate: typing.List[fhirtypes.StatisticAttributeEstimateType] = Field(
        None,
        alias="attributeEstimate",
        title="An attribute of the Statistic",
        description=(
            "A statistical attribute of the statistic such as a measure of "
            "heterogeneity."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title='Associated category for categorical variable"',
        description=(
            "When the measured variable is handled categorically, the category "
            "element is used to define which category the statistic is reporting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Description of content",
        description="A description of the content value of the statistic.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    modelCharacteristic: typing.List[
        fhirtypes.StatisticModelCharacteristicType
    ] = Field(
        None,
        alias="modelCharacteristic",
        title="Model characteristic",
        description="A component of the method to generate the statistic.",
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnotes and/or explanatory notes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    numberAffected: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberAffected",
        title="The number of participants affected",
        description=(
            "The number of participants affected where the unit of analysis is the "
            "same as sampleSize.knownDataCount and sampleSize.numberOfParticipants."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberAffected__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberAffected", title="Extension field for ``numberAffected``."
    )

    numberOfEvents: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfEvents",
        title="The number of events associated with the statistic",
        description=(
            "The number of events associated with the statistic, where the unit of "
            "analysis is different from numberAffected, sampleSize.knownDataCount "
            "and sampleSize.numberOfParticipants."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberOfEvents__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfEvents", title="Extension field for ``numberOfEvents``."
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Statistic value",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    sampleSize: fhirtypes.StatisticSampleSizeType = Field(
        None,
        alias="sampleSize",
        title="Number of samples in the statistic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    statisticType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statisticType",
        title="Type of statistic, eg relative risk",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``Statistic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "note",
            "statisticType",
            "category",
            "quantity",
            "numberOfEvents",
            "numberAffected",
            "sampleSize",
            "attributeEstimate",
            "modelCharacteristic",
        ]


from . import element


class StatisticAttributeEstimate(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An attribute of the Statistic.
    A statistical attribute of the statistic such as a measure of
    heterogeneity.
    """

    resource_type = Field("StatisticAttributeEstimate", const=True)

    attributeEstimate: typing.List[
        fhirtypes.StatisticAttributeEstimateAttributeEstimateType
    ] = Field(
        None,
        alias="attributeEstimate",
        title=(
            "A nested attribute estimate; which is the attribute estimate of an "
            "attribute estimate"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description of the attribute estimate",
        description="Human-readable summary of the estimate.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    level: fhirtypes.Decimal = Field(
        None,
        alias="level",
        title="Level of confidence interval, eg 0.95 for 95% confidence interval",
        description="Use 95 for a 95% confidence interval.",
        # if property is element of this resource.
        element_property=True,
    )
    level__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_level", title="Extension field for ``level``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnote or explanatory note about the estimate",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "The singular quantity of the attribute estimate, for attribute "
            "estimates represented as single values; also used to report unit of "
            "measure"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    range: fhirtypes.RangeType = Field(
        None,
        alias="range",
        title="Lower and upper bound values of the attribute estimate",
        description="Lower bound of confidence interval.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The type of attribute estimate, eg confidence interval or p value",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``StatisticAttributeEstimate`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "description",
            "note",
            "type",
            "quantity",
            "level",
            "range",
            "attributeEstimate",
        ]


class StatisticAttributeEstimateAttributeEstimate(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A nested attribute estimate; which is the attribute estimate of an
    attribute estimate.
    """

    resource_type = Field("StatisticAttributeEstimateAttributeEstimate", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description of the attribute estimate",
        description="Human-readable summary of the estimate.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    level: fhirtypes.Decimal = Field(
        None,
        alias="level",
        title="Level of confidence interval, eg 0.95 for 95% confidence interval",
        description="Use 95 for a 95% confidence interval.",
        # if property is element of this resource.
        element_property=True,
    )
    level__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_level", title="Extension field for ``level``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnote or explanatory note about the estimate",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "The singular quantity of the attribute estimate, for attribute "
            "estimates represented as single values; also used to report unit of "
            "measure"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    range: fhirtypes.RangeType = Field(
        None,
        alias="range",
        title="Lower and upper bound values of the attribute estimate",
        description="Lower bound of confidence interval.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The type of attribute estimate, eg confidence interval or p value",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``StatisticAttributeEstimateAttributeEstimate`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "description",
            "note",
            "type",
            "quantity",
            "level",
            "range",
        ]


class StatisticModelCharacteristic(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Model characteristic.
    A component of the method to generate the statistic.
    """

    resource_type = Field("StatisticModelCharacteristic", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Model specification",
        description="Description of a component of the method to generate the statistic.",
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.QuantityType = Field(
        None,
        alias="value",
        title="Numerical value to complete model specification",
        description=(
            "Further specification of the quantified value of the component of the "
            "method to generate the statistic."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    variable: typing.List[fhirtypes.StatisticModelCharacteristicVariableType] = Field(
        None,
        alias="variable",
        title="A variable adjusted for in the adjusted analysis",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``StatisticModelCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "code", "value", "variable"]


class StatisticModelCharacteristicVariable(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A variable adjusted for in the adjusted analysis.
    """

    resource_type = Field("StatisticModelCharacteristicVariable", const=True)

    handling: fhirtypes.Code = Field(
        None,
        alias="handling",
        title="continuous | dichotomous | ordinal | polychotomous",
        description="How the variable is classified for use in adjusted analysis.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["continuous", "dichotomous", "ordinal", "polychotomous"],
    )
    handling__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_handling", title="Extension field for ``handling``."
    )

    valueCategory: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="valueCategory",
        title="Description for grouping of ordinal or polychotomous variables",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueQuantity: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="valueQuantity",
        title="Discrete value for grouping of ordinal or polychotomous variables",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueRange: typing.List[fhirtypes.RangeType] = Field(
        None,
        alias="valueRange",
        title="Range of values for grouping of ordinal or polychotomous variables",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    variableDefinition: fhirtypes.ReferenceType = Field(
        ...,
        alias="variableDefinition",
        title="Description of the variable",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group", "EvidenceVariable"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``StatisticModelCharacteristicVariable`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "variableDefinition",
            "handling",
            "valueCategory",
            "valueQuantity",
            "valueRange",
        ]


class StatisticSampleSize(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Number of samples in the statistic.
    """

    resource_type = Field("StatisticSampleSize", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description of sample size for statistic",
        description="Human-readable summary of population sample size.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    knownDataCount: fhirtypes.UnsignedInt = Field(
        None,
        alias="knownDataCount",
        title="Number of participants with known results for measured variables",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    knownDataCount__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_knownDataCount", title="Extension field for ``knownDataCount``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnote or explanatory note about the sample size",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    numberOfParticipants: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfParticipants",
        title="Cumulative number of participants",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "sample size."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberOfParticipants__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfParticipants",
        title="Extension field for ``numberOfParticipants``.",
    )

    numberOfStudies: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfStudies",
        title="Number of contributing studies",
        description="Number of participants in the population.",
        # if property is element of this resource.
        element_property=True,
    )
    numberOfStudies__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfStudies", title="Extension field for ``numberOfStudies``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``StatisticSampleSize`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "description",
            "note",
            "numberOfStudies",
            "numberOfParticipants",
            "knownDataCount",
        ]
