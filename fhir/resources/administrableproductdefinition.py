# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdministrableProductDefinition
Release: R4
Version: 4.5.0
Build ID: 0d95498
Last updated: 2021-04-03T00:34:11.075+00:00
"""
import typing
from pydantic import Field
from pydantic import root_validator

from . import fhirtypes


from . import domainresource


class AdministrableProductDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A medicinal product in the final form which is suitable for administering
    to a patient (after any mixing of multiple components, dissolution etc. has
    been performed).
    """

    resource_type = Field("AdministrableProductDefinition", const=True)

    administrableDoseForm: fhirtypes.CodeableConceptType = Field(
        None,
        alias="administrableDoseForm",
        title=(
            "The administrable dose form, i.e. the dose form of the final product "
            "after necessary reconstitution or processing"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    device: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="device",
        title=(
            "A device that is integral to the medicinal product, in effect being "
            'considered as an "ingredient" of the medicinal product. This is not '
            "intended for devices that are just co-packaged"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceDefinition"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="An identifier for the administrable product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    ingredient: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="ingredient",
        title=(
            "The ingredients of this administrable medicinal product. Sometimes it "
            "may be appropriate to specify these via the associated manufactured "
            "item(s)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Ingredient"],
    )

    producedFrom: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="producedFrom",
        title=(
            "The manufactured item(s) that this administrable product is produced "
            "from. Either a single item, or several that are mixed before "
            "administration (e.g. a power item and a solution item). Note that "
            "these are not raw ingredients"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ManufacturedItemDefinition"],
    )

    property: typing.List[fhirtypes.AdministrableProductDefinitionPropertyType] = Field(
        None,
        alias="property",
        title="Characteristics e.g. a products onset of action",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    routeOfAdministration: typing.List[
        fhirtypes.AdministrableProductDefinitionRouteOfAdministrationType
    ] = Field(
        ...,
        alias="routeOfAdministration",
        title=(
            "The path by which the product is taken into or makes contact with the "
            "body. In some regions this is referred to as the licenced or approved "
            "route"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title=(
            "The medicinal product that this is an administrable form of. This is "
            "not a reference to the item(s) that make up this administrable form - "
            "it is the whole product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductDefinition"],
    )

    unitOfPresentation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unitOfPresentation",
        title=(
            "The units of presentation for the administrable product, for example "
            "'tablet'"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``AdministrableProductDefinition`` according specification,
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
            "subject",
            "administrableDoseForm",
            "unitOfPresentation",
            "producedFrom",
            "ingredient",
            "device",
            "property",
            "routeOfAdministration",
        ]


from . import backboneelement


class AdministrableProductDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Characteristics e.g. a products onset of action.
    """

    resource_type = Field("AdministrableProductDefinitionProperty", const=True)

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status of characteristic e.g. assigned or pending",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="A code expressing the type of characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``AdministrableProductDefinitionProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueQuantity",
            "valueDate",
            "valueBoolean",
            "valueAttachment",
            "status",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4168(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCodeableConcept",
                "valueDate",
                "valueQuantity",
            ]
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class AdministrableProductDefinitionRouteOfAdministration(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The path by which the product is taken into or makes contact with the body.
    In some regions this is referred to as the licenced or approved route.
    """

    resource_type = Field(
        "AdministrableProductDefinitionRouteOfAdministration", const=True
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Coded expression for the route",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    firstDose: fhirtypes.QuantityType = Field(
        None,
        alias="firstDose",
        title=(
            "The first dose (dose quantity) administered can be specified for the "
            "product, using a numerical value and its unit of measurement"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxDosePerDay: fhirtypes.QuantityType = Field(
        None,
        alias="maxDosePerDay",
        title=(
            "The maximum dose per day (maximum dose quantity to be administered in "
            "any one 24-h period) that can be administered"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxDosePerTreatmentPeriod: fhirtypes.RatioType = Field(
        None,
        alias="maxDosePerTreatmentPeriod",
        title="The maximum dose per treatment period that can be administered",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxSingleDose: fhirtypes.QuantityType = Field(
        None,
        alias="maxSingleDose",
        title=(
            "The maximum single dose that can be administered, can be specified "
            "using a numerical value and its unit of measurement"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxTreatmentPeriod: fhirtypes.DurationType = Field(
        None,
        alias="maxTreatmentPeriod",
        title=(
            "The maximum treatment period during which an Investigational Medicinal"
            " Product can be administered"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    targetSpecies: typing.List[
        fhirtypes.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType
    ] = Field(
        None,
        alias="targetSpecies",
        title="A species for which this route applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``AdministrableProductDefinitionRouteOfAdministration`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "firstDose",
            "maxSingleDose",
            "maxDosePerDay",
            "maxDosePerTreatmentPeriod",
            "maxTreatmentPeriod",
            "targetSpecies",
        ]


class AdministrableProductDefinitionRouteOfAdministrationTargetSpecies(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A species for which this route applies.
    """

    resource_type = Field(
        "AdministrableProductDefinitionRouteOfAdministrationTargetSpecies", const=True
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Coded expression for the species",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    withdrawalPeriod: typing.List[
        fhirtypes.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType
    ] = Field(
        None,
        alias="withdrawalPeriod",
        title=(
            "A species specific time during which consumption of animal product is "
            "not appropriate"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``AdministrableProductDefinitionRouteOfAdministrationTargetSpecies`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "withdrawalPeriod"]


class AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A species specific time during which consumption of animal product is not
    appropriate.
    """

    resource_type = Field(
        "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod",
        const=True,
    )

    supportingInformation: fhirtypes.String = Field(
        None,
        alias="supportingInformation",
        title="Extra information about the withdrawal period",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    supportingInformation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_supportingInformation",
        title="Extension field for ``supportingInformation``.",
    )

    tissue: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="tissue",
        title=(
            "Coded expression for the type of tissue for which the withdrawal "
            "period applues, e.g. meat, milk"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.QuantityType = Field(
        ...,
        alias="value",
        title="A value for the time",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "tissue",
            "value",
            "supportingInformation",
        ]
