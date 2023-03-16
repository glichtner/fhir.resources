# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MonetaryComponent
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
import typing
from pydantic import Field
from pydantic import root_validator

from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import fhirtypes


from . import datatype

class MonetaryComponent(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Availability data for an {item}.
    """
    resource_type = Field("MonetaryComponent", const=True)
	
    amount: fhirtypes.MoneyType = Field(
		None,
		alias="amount",
		title="Explicit value amount to be used",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    code: fhirtypes.CodeableConceptType = Field(
		None,
		alias="code",
		title=(
    "Codes may be used to differentiate between kinds of taxes, surcharges,"
    " discounts etc."
    ),
		description=(
    "Codes may be used to differentiate between kinds of taxes, surcharges,"
    " discounts etc."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    factor: fhirtypes.Decimal = Field(
		None,
		alias="factor",
		title="Factor used for calculating this component",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_factor",
        title="Extension field for ``factor``."
    )
	
    type: fhirtypes.Code = Field(
		None,
		alias="type",
		title="base | surcharge | deduction | discount | tax | informational",
		description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
		enum_values=["base", "surcharge", "deduction", "discount", "tax", "informational"],
	)
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_type",
        title="Extension field for ``type``."
    )
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MonetaryComponent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "type", "code", "factor", "amount"]


    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1987(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
			("type", "type__ext")]
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
