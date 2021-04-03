# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Permission
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


from . import domainresource


class Permission(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Permission.
    """

    resource_type = Field("Permission", const=True)

    asserter: fhirtypes.ReferenceType = Field(
        None,
        alias="asserter",
        title="The person or entity that asserts the permission",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Person"],
    )

    assertionDate: typing.List[fhirtypes.DateTime] = Field(
        None,
        alias="assertionDate",
        title="The date that permission was asserted",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    assertionDate__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_assertionDate", title="Extension field for ``assertionDate``."
    )

    dataScope: typing.List[fhirtypes.ExpressionType] = Field(
        None,
        alias="dataScope",
        title=(
            "This can be 1) the definition of data elements, or 2) a category or "
            "label) e.g. \u201csensitive\u201d. It could also be a c) graph-like definition "
            "of a set of data elements"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    intent: fhirtypes.CodeableConceptType = Field(
        None,
        alias="intent",
        title="grant|refuse",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    justification: fhirtypes.PermissionJustificationType = Field(
        None,
        alias="justification",
        title="The asserted justification for using the data",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    processingActivity: typing.List[fhirtypes.PermissionProcessingActivityType] = Field(
        None,
        alias="processingActivity",
        title=(
            "A description or definition of which activities are allowed to be done"
            " on the data"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    purpose: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="purpose",
        title="The purpose for which the permission is given",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | entered-in-error | draft | rejected",
        description="Status.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "entered-in-error", "draft", "rejected"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    usageLimitations: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="usageLimitations",
        title="What limits apply to the use of the data",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    validity: fhirtypes.PeriodType = Field(
        None,
        alias="validity",
        title="The period in which the permission is active",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``Permission`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "status",
            "intent",
            "asserter",
            "assertionDate",
            "validity",
            "purpose",
            "dataScope",
            "processingActivity",
            "justification",
            "usageLimitations",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1255(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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


from . import backboneelement


class PermissionJustification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The asserted justification for using the data.
    """

    resource_type = Field("PermissionJustification", const=True)

    evidence: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="evidence",
        title=(
            "Evidence \u2013 reference to consent, or a contract, or a policy, or a "
            "regulation, or an attachment that contains a screenshot"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Consent"],
    )

    grounds: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="grounds",
        title=(
            "This would be a codeableconcept, or a coding, which can be constrained"
            " to , for example, the 6 grounds for processing in GDPR"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``PermissionJustification`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "evidence", "grounds"]


class PermissionProcessingActivity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A description or definition of which activities are allowed to be done on
    the data.
    """

    resource_type = Field("PermissionProcessingActivity", const=True)

    partyCodeableConcept: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="partyCodeableConcept",
        title=(
            "If the processing is a transfer, or involves another party, we must "
            "capture where it the data allowed or expected to be shared - with a "
            "party or person. This can be a party instance or party type \u00a7 Purpose "
            "\u2013 a specific purpose of the data"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    partyReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partyReference",
        title=(
            "If the processing is a transfer, we must capture where it the data "
            "allowed or expected to be shared - with a party or person"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    purpose: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="purpose",
        title="The purpose for which the permission is given",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``PermissionProcessingActivity`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "partyReference",
            "partyCodeableConcept",
            "purpose",
        ]
