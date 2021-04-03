# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubscriptionStatus
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


class SubscriptionStatus(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Status information about a Subscription provided during event notification.
    The SubscriptionStatus resource describes the state of a Subscription
    during notifications.
    """

    resource_type = Field("SubscriptionStatus", const=True)

    error: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="error",
        title="List of errors on the subscription",
        description=(
            "A record of errors that occurred when the server processed a "
            "notification."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    eventsInNotification: fhirtypes.Integer = Field(
        None,
        alias="eventsInNotification",
        title="The number of actual notifications represented by this bundle",
        description=(
            "The total number of actual events represented within this "
            "notification.  For handshake and heartbeat notifications, this will be"
            " zero or not present.  For event-notifications, this number may be one"
            " or more, depending on server batching."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    eventsInNotification__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_eventsInNotification",
        title="Extension field for ``eventsInNotification``.",
    )

    eventsSinceSubscriptionStart: fhirtypes.Integer64 = Field(
        None,
        alias="eventsSinceSubscriptionStart",
        title="Events since the Subscription was created",
        description=(
            "The total number of actual events which have been generated since the "
            "Subscription was created (inclusive of this notification) - regardless"
            " of how many have been successfully communicated.  This number is NOT "
            "incremented for handshake and heartbeat notifications."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    eventsSinceSubscriptionStart__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_eventsSinceSubscriptionStart",
        title="Extension field for ``eventsSinceSubscriptionStart``.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="requested | active | error | off | entered-in-error",
        description=(
            "The status of the subscription, which marks the server state for "
            "managing the subscription."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["requested", "active", "error", "off", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subscription: fhirtypes.ReferenceType = Field(
        ...,
        alias="subscription",
        title="Reference to the Subscription responsible for this notification",
        description="The reference to the Subscription which generated this notification.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Subscription"],
    )

    topic: fhirtypes.Canonical = Field(
        None,
        alias="topic",
        title="Reference to the SubscriptionTopic this notification relates to",
        description=(
            "The reference to the SubscriptionTopic for the Subscription which "
            "generated this notification."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubscriptionTopic"],
    )
    topic__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_topic", title="Extension field for ``topic``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="handshake | heartbeat | event-notification | query-status",
        description="The type of event being conveyed with this notificaiton.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["handshake", "heartbeat", "event-notification", "query-status"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubscriptionStatus`` according specification,
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
            "type",
            "eventsSinceSubscriptionStart",
            "eventsInNotification",
            "subscription",
            "topic",
            "error",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2127(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("topic", "topic__ext"), ("type", "type__ext")]
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
