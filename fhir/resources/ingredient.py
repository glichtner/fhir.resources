# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Ingredient
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


class Ingredient(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An ingredient of a manufactured item or pharmaceutical product.
    """

    resource_type = Field("Ingredient", const=True)

    allergenicIndicator: bool = Field(
        None,
        alias="allergenicIndicator",
        title="If the ingredient is a known or suspected allergen",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_allergenicIndicator",
        title="Extension field for ``allergenicIndicator``.",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title=(
            "A general description of the ingredient, or any supporting text. May "
            "be used for an unstructured list of excipients"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    function: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="function",
        title=(
            "A classification of the ingredient identifying its precise purpose(s) "
            "in the drug product. This extends the Ingredient.role to add more "
            "detail. Example: Antioxidant, Alkalizing Agent"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    group: fhirtypes.CodeableConceptType = Field(
        None,
        alias="group",
        title=(
            "A classification of the ingredient according to where in the physical "
            "item it tends to be used, such the outer shell of a tablet, inner body"
            " or ink"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="An identifier or code by which the ingredient can be referenced",
        description=(
            "The identifier(s) of this Ingredient that are assigned by business "
            "processes and/or used to refer to it when a direct URL reference to "
            "the resource itself is not appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="The organization that manufactures this ingredient",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title=(
            "A classification of the ingredient identifying its purpose within the "
            "product, e.g. active, inactive"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    specifiedSubstance: typing.List[fhirtypes.IngredientSpecifiedSubstanceType] = Field(
        None,
        alias="specifiedSubstance",
        title="A specified substance that comprises this ingredient",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    substance: fhirtypes.IngredientSubstanceType = Field(
        None,
        alias="substance",
        title="The substance that comprises this ingredient",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``Ingredient`` according specification,
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
            "role",
            "function",
            "group",
            "description",
            "allergenicIndicator",
            "manufacturer",
            "substance",
            "specifiedSubstance",
        ]


from . import backboneelement


class IngredientSpecifiedSubstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A specified substance that comprises this ingredient.
    """

    resource_type = Field("IngredientSpecifiedSubstance", const=True)

    code: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="code",
        title=(
            "Substance as a 'specified substance', implying extra substance related"
            " characteristics"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition", "Substance"],
    )

    confidentiality: fhirtypes.CodeableConceptType = Field(
        None,
        alias="confidentiality",
        title="Confidentiality level of the specified substance as the ingredient",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    group: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="group",
        title=(
            "The group of specified substance, e.g. group 1 to 4, where the group "
            "categorises the level of  description of the substance according to "
            "standardised sets of properties"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    strength: typing.List[fhirtypes.IngredientSubstanceStrengthType] = Field(
        None,
        alias="strength",
        title=(
            "Quantity of the substance or specified substance present in the "
            "manufactured item or pharmaceutical product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``IngredientSpecifiedSubstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "group",
            "confidentiality",
            "strength",
        ]


class IngredientSubstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The substance that comprises this ingredient.
    """

    resource_type = Field("IngredientSubstance", const=True)

    code: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="code",
        title="A code or full resource that represents the ingredient substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition", "Substance"],
    )

    strength: typing.List[fhirtypes.IngredientSubstanceStrengthType] = Field(
        None,
        alias="strength",
        title=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item. When there is a range of strengths, this represents the lower "
            "limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``IngredientSubstance`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "strength"]


class IngredientSubstanceStrength(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The quantity of substance in the unit of presentation, or in the volume (or
    mass) of the single pharmaceutical product or manufactured item. When there
    is a range of strengths, this represents the lower limit.
    """

    resource_type = Field("IngredientSubstanceStrength", const=True)

    basis: fhirtypes.CodeableConceptType = Field(
        None,
        alias="basis",
        title=(
            "A code that indicates if the strength is, for example, based on the "
            "ingredient substance as stated or on the substance base (when the "
            "ingredient is a salt)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    concentrationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="concentrationCodeableConcept",
        title="The strength per unitary volume (or mass)",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e concentration[x]
        one_of_many="concentration",
        one_of_many_required=False,
    )

    concentrationHighLimitQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="concentrationHighLimitQuantity",
        title=(
            "An upper limit for the strength per unitary volume (or mass), for when"
            " there is a range. The concentration attribute then becomes the lower "
            "limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e concentrationHighLimit[x]
        one_of_many="concentrationHighLimit",
        one_of_many_required=False,
    )

    concentrationHighLimitRatio: fhirtypes.RatioType = Field(
        None,
        alias="concentrationHighLimitRatio",
        title=(
            "An upper limit for the strength per unitary volume (or mass), for when"
            " there is a range. The concentration attribute then becomes the lower "
            "limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e concentrationHighLimit[x]
        one_of_many="concentrationHighLimit",
        one_of_many_required=False,
    )

    concentrationQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="concentrationQuantity",
        title="The strength per unitary volume (or mass)",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e concentration[x]
        one_of_many="concentration",
        one_of_many_required=False,
    )

    concentrationRatio: fhirtypes.RatioType = Field(
        None,
        alias="concentrationRatio",
        title="The strength per unitary volume (or mass)",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e concentration[x]
        one_of_many="concentration",
        one_of_many_required=False,
    )

    concentrationText: fhirtypes.String = Field(
        None,
        alias="concentrationText",
        title=(
            "A textual represention of either the whole of the concentration "
            "strength or a part of it - with the rest being in "
            "Strength.concentration as a ratio"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    concentrationText__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_concentrationText",
        title="Extension field for ``concentrationText``.",
    )

    country: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="country",
        title="The country or countries for which the strength range applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    measurementPoint: fhirtypes.String = Field(
        None,
        alias="measurementPoint",
        title="For when strength is measured at a particular point or distance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_measurementPoint",
        title="Extension field for ``measurementPoint``.",
    )

    presentationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="presentationCodeableConcept",
        title=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e presentation[x]
        one_of_many="presentation",
        one_of_many_required=False,
    )

    presentationHighLimitQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="presentationHighLimitQuantity",
        title=(
            "An upper limit for the quantity of substance in the unit of "
            "presentation. When there is a range of strengths, this represents the "
            "upper limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e presentationHighLimit[x]
        one_of_many="presentationHighLimit",
        one_of_many_required=False,
    )

    presentationHighLimitRatio: fhirtypes.RatioType = Field(
        None,
        alias="presentationHighLimitRatio",
        title=(
            "An upper limit for the quantity of substance in the unit of "
            "presentation. When there is a range of strengths, this represents the "
            "upper limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e presentationHighLimit[x]
        one_of_many="presentationHighLimit",
        one_of_many_required=False,
    )

    presentationQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="presentationQuantity",
        title=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e presentation[x]
        one_of_many="presentation",
        one_of_many_required=False,
    )

    presentationRatio: fhirtypes.RatioType = Field(
        None,
        alias="presentationRatio",
        title=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e presentation[x]
        one_of_many="presentation",
        one_of_many_required=False,
    )

    presentationText: fhirtypes.String = Field(
        None,
        alias="presentationText",
        title=(
            "A textual represention of either the whole of the presentation "
            "strength or a part of it - with the rest being in "
            "Strength.presentation as a ratio"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    presentationText__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_presentationText",
        title="Extension field for ``presentationText``.",
    )

    referenceStrength: typing.List[
        fhirtypes.IngredientSubstanceStrengthReferenceStrengthType
    ] = Field(
        None,
        alias="referenceStrength",
        title="Strength expressed in terms of a reference substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``IngredientSubstanceStrength`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "presentationRatio",
            "presentationCodeableConcept",
            "presentationQuantity",
            "presentationHighLimitRatio",
            "presentationHighLimitQuantity",
            "presentationText",
            "concentrationRatio",
            "concentrationCodeableConcept",
            "concentrationQuantity",
            "concentrationHighLimitRatio",
            "concentrationHighLimitQuantity",
            "concentrationText",
            "basis",
            "measurementPoint",
            "country",
            "referenceStrength",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2993(
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
            "concentration": [
                "concentrationCodeableConcept",
                "concentrationQuantity",
                "concentrationRatio",
            ],
            "concentrationHighLimit": [
                "concentrationHighLimitQuantity",
                "concentrationHighLimitRatio",
            ],
            "presentation": [
                "presentationCodeableConcept",
                "presentationQuantity",
                "presentationRatio",
            ],
            "presentationHighLimit": [
                "presentationHighLimitQuantity",
                "presentationHighLimitRatio",
            ],
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


class IngredientSubstanceStrengthReferenceStrength(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Strength expressed in terms of a reference substance.
    """

    resource_type = Field("IngredientSubstanceStrengthReferenceStrength", const=True)

    country: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="country",
        title="The country or countries for which the strength range applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    measurementPoint: fhirtypes.String = Field(
        None,
        alias="measurementPoint",
        title="For when strength is measured at a particular point or distance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_measurementPoint",
        title="Extension field for ``measurementPoint``.",
    )

    strengthHighLimitQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="strengthHighLimitQuantity",
        title=(
            "Strength expressed in terms of a reference substance. When there is a "
            "range of strengths, this represents the upper limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e strengthHighLimit[x]
        one_of_many="strengthHighLimit",
        one_of_many_required=False,
    )

    strengthHighLimitRatio: fhirtypes.RatioType = Field(
        None,
        alias="strengthHighLimitRatio",
        title=(
            "Strength expressed in terms of a reference substance. When there is a "
            "range of strengths, this represents the upper limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e strengthHighLimit[x]
        one_of_many="strengthHighLimit",
        one_of_many_required=False,
    )

    strengthQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="strengthQuantity",
        title=(
            "Strength expressed in terms of a reference substance. When there is a "
            "range of strengths, this represents the lower limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e strength[x]
        one_of_many="strength",
        one_of_many_required=True,
    )

    strengthRatio: fhirtypes.RatioType = Field(
        None,
        alias="strengthRatio",
        title=(
            "Strength expressed in terms of a reference substance. When there is a "
            "range of strengths, this represents the lower limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e strength[x]
        one_of_many="strength",
        one_of_many_required=True,
    )

    substance: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="substance",
        title="Relevant reference substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition", "Substance"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``IngredientSubstanceStrengthReferenceStrength`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "substance",
            "strengthRatio",
            "strengthQuantity",
            "strengthHighLimitRatio",
            "strengthHighLimitQuantity",
            "measurementPoint",
            "country",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4751(
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
            "strengthHighLimit": [
                "strengthHighLimitQuantity",
                "strengthHighLimitRatio",
            ],
            "strength": ["strengthQuantity", "strengthRatio"],
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
