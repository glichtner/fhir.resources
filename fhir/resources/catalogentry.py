# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CatalogEntry
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


class CatalogEntry(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An entry in a catalog.
    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """

    resource_type = Field("CatalogEntry", const=True)

    billingCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="billingCode",
        title="Billing code in the context of this catalog entry",
        description=(
            "Billing code associated to the  item in the context of this  entry of "
            "the catalog."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    billingSummary: fhirtypes.String = Field(
        None,
        alias="billingSummary",
        title="Billing summary in the context of this catalog entry",
        description=(
            "Billing summary attached to the  item in the context of this  entry of"
            " the catalog."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    billingSummary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_billingSummary", title="Extension field for ``billingSummary``."
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When this catalog entry is expected to be active",
        description="Period of usability of the catalog entry.",
        # if property is element of this resource.
        element_property=True,
    )

    estimatedDuration: fhirtypes.DurationType = Field(
        None,
        alias="estimatedDuration",
        title="Estimated duration of the orderable item",
        description=(
            "Estimated duration of the orderable item of this  entry of the " "catalog."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier of the catalog entry",
        description="Business identifier uniquely assigned to the catalog entry.",
        # if property is element of this resource.
        element_property=True,
    )

    limitationSummary: fhirtypes.String = Field(
        None,
        alias="limitationSummary",
        title="Summary of limitations for the catalog entry",
        description=(
            "Summary of limitations for the  item in the context of this  entry of "
            "the catalog."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    limitationSummary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_limitationSummary",
        title="Extension field for ``limitationSummary``.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Displayable name assigned to the catalog entry",
        description=(
            "The name of this catalog entry announces the item that is represented "
            "by the entry."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Notes and comments about this catalog entry",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    orderable: bool = Field(
        None,
        alias="orderable",
        title="Is orderable",
        description=(
            "Indicates whether or not the entry represents an item that is "
            "orderable."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    orderable__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_orderable", title="Extension field for ``orderable``."
    )

    referencedItem: fhirtypes.ReferenceType = Field(
        ...,
        alias="referencedItem",
        title="Item attached to this entry of the catalog",
        description="The item (resource) that this entry of the catalog represents.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "DeviceDefinition",
            "Organization",
            "Practitioner",
            "PractitionerRole",
            "HealthcareService",
            "ActivityDefinition",
            "PlanDefinition",
            "SpecimenDefinition",
            "ObservationDefinition",
            "MedicationKnowledge",
            "Substance",
            "Location",
        ],
    )

    regulatorySummary: fhirtypes.String = Field(
        None,
        alias="regulatorySummary",
        title="Regulatory  summary for the catalog entry",
        description=(
            "Regulatory summary for the  item in the context of this  entry of the "
            "catalog."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    regulatorySummary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_regulatorySummary",
        title="Extension field for ``regulatorySummary``.",
    )

    relatedEntry: typing.List[fhirtypes.CatalogEntryRelatedEntryType] = Field(
        None,
        alias="relatedEntry",
        title="Another entry of the catalog related to this one",
        description=(
            "Used for example, to point to a substance, or to a device used to "
            "administer a medication."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    scheduleSummary: fhirtypes.String = Field(
        None,
        alias="scheduleSummary",
        title="Schedule summary for the catalog entry",
        description=(
            "Schedule summary for the  item in the context of this  entry of the "
            "catalog."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    scheduleSummary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_scheduleSummary", title="Extension field for ``scheduleSummary``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired",
        description=(
            "Indicates whether this catalog entry is open to public usage (active) "
            "or not (draft or retired)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title=(
            "ActivityDefinition | PlanDefinition | SpecimenDefinition | "
            "ObservationDefinition | DeviceDefinition | Organization | Practitioner"
            " | PractitionerRole | HealthcareService | MedicationKnowledge | "
            "Medication | Substance | Location"
        ),
        description="The type of resource that is represented by this catalog entry.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "ActivityDefinition",
            "PlanDefinition",
            "SpecimenDefinition",
            "ObservationDefinition",
            "DeviceDefinition",
            "Organization",
            "Practitioner",
            "PractitionerRole",
            "HealthcareService",
            "MedicationKnowledge",
            "Medication",
            "Substance",
            "Location",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    updatedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="updatedBy",
        title="Last updater of this catalog entry",
        description="Last actor who recorded (created or updated) this catalog entry.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Person", "Device"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CatalogEntry`` according specification,
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
            "identifier",
            "name",
            "type",
            "status",
            "effectivePeriod",
            "orderable",
            "referencedItem",
            "relatedEntry",
            "updatedBy",
            "note",
            "estimatedDuration",
            "billingCode",
            "billingSummary",
            "scheduleSummary",
            "limitationSummary",
            "regulatorySummary",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1417(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("orderable", "orderable__ext")]
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


class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Another entry of the catalog related to this one.
    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """

    resource_type = Field("CatalogEntryRelatedEntry", const=True)

    relationship: fhirtypes.Code = Field(
        None,
        alias="relationship",
        title="triggers | is-replaced-by | excludes | includes",
        description="The type of relationship to the related entry.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["triggers", "is-replaced-by", "excludes", "includes"],
    )
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relationship", title="Extension field for ``relationship``."
    )

    target: fhirtypes.ReferenceType = Field(
        ...,
        alias="target",
        title="The reference to the related entry",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CatalogEntry"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``CatalogEntryRelatedEntry`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "relationship", "target"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2652(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("relationship", "relationship__ext")]
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
