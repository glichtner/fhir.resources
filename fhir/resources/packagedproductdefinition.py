# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PackagedProductDefinition
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


class PackagedProductDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A medically related item or items, in a container or package.
    """

    resource_type = Field("PackagedProductDefinition", const=True)

    attachedDocument: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="attachedDocument",
        title=(
            "Additional information or supporting documentation about the packaged "
            "product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    characteristic: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="characteristic",
        title=(
            'Allows the key features to be recorded, such as "hospital pack", '
            '"nurse prescribable", "calendar pack"'
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    containedItemQuantity: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="containedItemQuantity",
        title=(
            "A total of the amount of items in the package, per item type. This can"
            " be considered as the pack size. This attribite is repeatable so that "
            "the different item types in one pack type can be counted (e.g. a count"
            " of vials and count of syringes). Repeats are not to be used to "
            "represent differerent pack sizes (e.g. 20 pack vs 50 pack) - which "
            "would be different resource instances. This attribute differs from  "
            "containedItem.amount in that it can give a single count of all tablet "
            "types in a pack, even when these are different manufactured items"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    copackagedIndicator: bool = Field(
        None,
        alias="copackagedIndicator",
        title=(
            "States whether a drug product is supplied with another item such as a "
            "diluent or adjuvant"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    copackagedIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_copackagedIndicator",
        title="Extension field for ``copackagedIndicator``.",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title=(
            "Textual description. Note that this is not the name of the package or "
            "product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    legalStatusOfSupply: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalStatusOfSupply",
        title=(
            "The legal status of supply of the packaged item as classified by the "
            "regulator"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title=(
            "Manufacturer of this package type. When there are multiple it means "
            "these are all possible manufacturers"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    marketingAuthorization: fhirtypes.ReferenceType = Field(
        None,
        alias="marketingAuthorization",
        title="An authorization for this package type",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["RegulatedAuthorization"],
    )

    marketingStatus: typing.List[fhirtypes.MarketingStatusType] = Field(
        None,
        alias="marketingStatus",
        title="Marketing information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title=(
            "A name for this package. Typically what it would be listed as in a "
            "drug formulary or catalogue, inventory etc"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    package: fhirtypes.PackagedProductDefinitionPackageType = Field(
        None,
        alias="package",
        title=(
            "A packaging item, as a container for medically related items, possibly"
            " with other packaging items within, or a packaging component, such as "
            "bottle cap (which is not a device or a medication manufactured item)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title=(
            "The status within the lifecycle of this item. A high level status, "
            "this is not intended to duplicate details carried elsewhere such as "
            "legal status, or authorization or marketing status"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="The date at which the given status became applicable",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title="The product that this is a pack for",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductDefinition"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "A high level category e.g. medicinal product, raw material, "
            "shipping/transport container, etc"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``PackagedProductDefinition`` according specification,
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
            "subject",
            "status",
            "statusDate",
            "containedItemQuantity",
            "description",
            "legalStatusOfSupply",
            "marketingStatus",
            "characteristic",
            "copackagedIndicator",
            "marketingAuthorization",
            "manufacturer",
            "attachedDocument",
            "package",
        ]


from . import backboneelement


class PackagedProductDefinitionPackage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A packaging item, as a container for medically related items, possibly with
    other packaging items within, or a packaging component, such as bottle cap
    (which is not a device or a medication manufactured item).
    """

    resource_type = Field("PackagedProductDefinitionPackage", const=True)

    alternateMaterial: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="alternateMaterial",
        title="A possible alternate material for the packaging",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    containedItem: typing.List[
        fhirtypes.PackagedProductDefinitionPackageContainedItemType
    ] = Field(
        None,
        alias="containedItem",
        title="The item(s) within the packaging",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Including possibly Data Carrier Identifier",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title=(
            "Manufacturer of this package Item. When there are multiple it means "
            "these are all possible manufacturers"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    material: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="material",
        title="Material type of the package item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    package: typing.List[fhirtypes.PackagedProductDefinitionPackageType] = Field(
        None,
        alias="package",
        title="Allows containers within containers",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    property: typing.List[
        fhirtypes.PackagedProductDefinitionPackagePropertyType
    ] = Field(
        None,
        alias="property",
        title="General characteristics of this item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.Integer = Field(
        None,
        alias="quantity",
        title=(
            "The quantity of this level of packaging in the package that contains "
            "it. If specified, the outermost level is always 1"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_quantity", title="Extension field for ``quantity``."
    )

    shelfLifeStorage: typing.List[fhirtypes.ProductShelfLifeType] = Field(
        None,
        alias="shelfLifeStorage",
        title="Shelf Life and storage information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The physical type of the container of the items",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``PackagedProductDefinitionPackage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "type",
            "quantity",
            "material",
            "alternateMaterial",
            "shelfLifeStorage",
            "manufacturer",
            "property",
            "containedItem",
            "package",
        ]


class PackagedProductDefinitionPackageContainedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The item(s) within the packaging.
    """

    resource_type = Field("PackagedProductDefinitionPackageContainedItem", const=True)

    amountInteger: fhirtypes.Integer = Field(
        None,
        alias="amountInteger",
        title="The number of this type of item within this packaging",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )
    amountInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountInteger", title="Extension field for ``amountInteger``."
    )

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title="The number of this type of item within this packaging",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    item: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="item",
        title=(
            "The actual item(s) of medication, as manufactured, or a device "
            "(typically, but not necessarily, a co-packaged one), or other "
            "medically related item (such as food, biologicals, raw materials, "
            "medical fluids, gases etc.), as contained in the package. This also "
            "allows another packaged product to be included, which is solely for "
            "the case where a package of other entire packages is wanted - such as "
            "a wholesale or distribution pack"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "ManufacturedItemDefinition",
            "DeviceDefinition",
            "PackagedProductDefinition",
            "BiologicallyDerivedProduct",
            "NutritionProduct",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``PackagedProductDefinitionPackageContainedItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "item",
            "amountQuantity",
            "amountInteger",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4743(
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
        one_of_many_fields = {"amount": ["amountInteger", "amountQuantity"]}
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


class PackagedProductDefinitionPackageProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    General characteristics of this item.
    """

    resource_type = Field("PackagedProductDefinitionPackageProperty", const=True)

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
        """returning all elements names from ``PackagedProductDefinitionPackageProperty`` according specification,
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
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4308(
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
