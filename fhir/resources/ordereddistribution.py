# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OrderedDistribution
Release: R4
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
import typing
from pydantic import Field
from pydantic import root_validator

from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import fhirtypes


from . import backbonetype


class OrderedDistribution(backbonetype.BackboneType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An ordered list (distribution) of statistics.
    """

    resource_type = Field("OrderedDistribution", const=True)

    bottomOfFirstInterval: fhirtypes.QuantityType = Field(
        None,
        alias="bottomOfFirstInterval",
        title="Bottom of first interval",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="A description of the content and value of the statistic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    interval: typing.List[fhirtypes.OrderedDistributionIntervalType] = Field(
        ...,
        alias="interval",
        title="Interval",
        description=None,
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

    numberOfIntervals: fhirtypes.Integer = Field(
        None,
        alias="numberOfIntervals",
        title="Number of intervals in an array, eg 4 for quartiles",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    numberOfIntervals__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfIntervals",
        title="Extension field for ``numberOfIntervals``.",
    )

    topOfInterval: fhirtypes.QuantityType = Field(
        None,
        alias="topOfInterval",
        title="Singular value of the statistic at the upper bound of the interval",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``OrderedDistribution`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "note",
            "numberOfIntervals",
            "bottomOfFirstInterval",
            "interval",
            "topOfInterval",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2178(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("numberOfIntervals", "numberOfIntervals__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


from . import element


class OrderedDistributionInterval(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Interval.
    """

    resource_type = Field("OrderedDistributionInterval", const=True)

    intervalStatistic: typing.List[fhirtypes.StatisticType] = Field(
        None,
        alias="intervalStatistic",
        title="Values and parameters for a single statistic related to the interval",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    rankOrder: fhirtypes.Integer = Field(
        None,
        alias="rankOrder",
        title="Relative order of interval",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    rankOrder__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rankOrder", title="Extension field for ``rankOrder``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``OrderedDistributionInterval`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "rankOrder", "intervalStatistic"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3013(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("rankOrder", "rankOrder__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
