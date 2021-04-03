# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceDefinition
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


class SubstanceDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """

    resource_type = Field("SubstanceDefinition", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title=(
            "High level categorization, e.g. polymer or nucleic acid, or food, "
            "chemical, biological"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    classification: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classification",
        title=(
            "A lower level classification than category, such as the general types "
            "of polymer (linear or branch chain) or type of impurity (process "
            "related or contaminant)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    code: typing.List[fhirtypes.SubstanceDefinitionCodeType] = Field(
        None,
        alias="code",
        title="Codes associated with the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Textual description of the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    domain: fhirtypes.CodeableConceptType = Field(
        None,
        alias="domain",
        title="If the substance applies to only human or veterinary use",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    grade: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="grade",
        title=(
            "The quality standard, established benchmark, to which substance "
            "complies (e.g. USP/NF, Ph. Eur, JP, BP, Company Standard)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier by which this substance is known",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="A company that makes this substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    moiety: typing.List[fhirtypes.SubstanceDefinitionMoietyType] = Field(
        None,
        alias="moiety",
        title="Moiety, for structural modifications",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    molecularWeight: typing.List[
        fhirtypes.SubstanceDefinitionStructureIsotopeMolecularWeightType
    ] = Field(
        None,
        alias="molecularWeight",
        title=(
            "The molecular weight or weight range (for proteins, polymers or "
            "nucleic acids)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: typing.List[fhirtypes.SubstanceDefinitionNameType] = Field(
        None,
        alias="name",
        title="Names applicable to this substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Textual comment about the substance's catalogue or registry record",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    nucleicAcid: fhirtypes.ReferenceType = Field(
        None,
        alias="nucleicAcid",
        title="Data items specific to nucleic acids",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceNucleicAcid"],
    )

    polymer: fhirtypes.ReferenceType = Field(
        None,
        alias="polymer",
        title="Data items specific to polymers",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstancePolymer"],
    )

    property: typing.List[fhirtypes.SubstanceDefinitionPropertyType] = Field(
        None,
        alias="property",
        title=(
            "General specifications for this substance, including how it is related"
            " to other substances"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    protein: fhirtypes.ReferenceType = Field(
        None,
        alias="protein",
        title="Data items specific to proteins",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceProtein"],
    )

    referenceInformation: fhirtypes.ReferenceType = Field(
        None,
        alias="referenceInformation",
        title="General information detailing this substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceReferenceInformation"],
    )

    relationship: typing.List[fhirtypes.SubstanceDefinitionRelationshipType] = Field(
        None,
        alias="relationship",
        title=(
            "A link between this substance and another, with details of the "
            "relationship"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    sourceMaterial: fhirtypes.SubstanceDefinitionSourceMaterialType = Field(
        None,
        alias="sourceMaterial",
        title="Material or taxonomic/anatomical source for the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Status of substance within the catalogue e.g. approved",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    structure: fhirtypes.SubstanceDefinitionStructureType = Field(
        None,
        alias="structure",
        title="Structural information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    supplier: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supplier",
        title="A company that supplies this substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="A business level identifier of the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinition`` according specification,
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
            "version",
            "status",
            "category",
            "classification",
            "domain",
            "grade",
            "description",
            "source",
            "note",
            "manufacturer",
            "supplier",
            "moiety",
            "property",
            "referenceInformation",
            "structure",
            "code",
            "name",
            "molecularWeight",
            "relationship",
            "nucleicAcid",
            "polymer",
            "protein",
            "sourceMaterial",
        ]


from . import backboneelement


class SubstanceDefinitionCode(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Codes associated with the substance.
    """

    resource_type = Field("SubstanceDefinitionCode", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="The specific code",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Any comment can be provided in this field, if necessary",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Status of the code assignment, for example 'provisional', 'approved'",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title=(
            "The date at which the code status is changed as part of the "
            "terminology maintenance"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionCode`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "status",
            "statusDate",
            "note",
            "source",
        ]


class SubstanceDefinitionMoiety(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Moiety, for structural modifications.
    """

    resource_type = Field("SubstanceDefinitionMoiety", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title="Quantitative value for this moiety",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title="Quantitative value for this moiety",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountString", title="Extension field for ``amountString``."
    )

    amountType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="amountType",
        title="The measurement type of the quantitative value",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier by which this moiety substance is known",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    molecularFormula: fhirtypes.String = Field(
        None,
        alias="molecularFormula",
        title=(
            "Molecular formula for this moiety of this substance, typically using "
            "the Hill system"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    molecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_molecularFormula",
        title="Extension field for ``molecularFormula``.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Textual name for this moiety substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    opticalActivity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="opticalActivity",
        title="Optical activity type",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Role that the moiety is playing",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    stereochemistry: fhirtypes.CodeableConceptType = Field(
        None,
        alias="stereochemistry",
        title="Stereochemistry type",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionMoiety`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "role",
            "identifier",
            "name",
            "stereochemistry",
            "opticalActivity",
            "molecularFormula",
            "amountQuantity",
            "amountString",
            "amountType",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2804(
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
        one_of_many_fields = {"amount": ["amountQuantity", "amountString"]}
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


class SubstanceDefinitionName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Names applicable to this substance.
    """

    resource_type = Field("SubstanceDefinitionName", const=True)

    domain: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="domain",
        title=(
            "The use context of this name for example if there is a different name "
            "a drug active ingredient as opposed to a food colour additive"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="The jurisdiction where this name applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    language: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="language",
        title="Human language that the name is written in",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="The actual name",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    official: typing.List[fhirtypes.SubstanceDefinitionNameOfficialType] = Field(
        None,
        alias="official",
        title="Details of the official nature of this name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    preferred: bool = Field(
        None,
        alias="preferred",
        title="If this is the preferred name for this substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preferred", title="Extension field for ``preferred``."
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status of the name, for example 'current', 'proposed'",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    synonym: typing.List[fhirtypes.SubstanceDefinitionNameType] = Field(
        None,
        alias="synonym",
        title=(
            "A synonym of this particular name, by which the substance is also " "known"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    translation: typing.List[fhirtypes.SubstanceDefinitionNameType] = Field(
        None,
        alias="translation",
        title="A translation for this name into another human language",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Name type, for example 'systematic',  'scientific, 'brand'",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionName`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "type",
            "status",
            "preferred",
            "language",
            "domain",
            "jurisdiction",
            "synonym",
            "translation",
            "official",
            "source",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2538(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
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


class SubstanceDefinitionNameOfficial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of the official nature of this name.
    """

    resource_type = Field("SubstanceDefinitionNameOfficial", const=True)

    authority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="authority",
        title="Which authority uses this official name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date of official name change",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status of the official name, for example 'provisional', 'approved'",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionNameOfficial`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "authority", "status", "date"]


class SubstanceDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    General specifications for this substance, including how it is related to
    other substances.
    """

    resource_type = Field("SubstanceDefinitionProperty", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title="Quantitative value for this property",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title="Quantitative value for this property",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountString", title="Extension field for ``amountString``."
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="A category for this property, e.g. Physical, Chemical, Enzymatic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Property type e.g. viscosity, pH, isoelectric point",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    definingSubstance: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="definingSubstance",
        title=(
            "A substance upon which a defining property depends (e.g. for "
            "solubility: in water, in alcohol)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition", "Substance"],
    )

    parameters: fhirtypes.String = Field(
        None,
        alias="parameters",
        title=(
            "Parameters that were used in the measurement of a property (e.g. for "
            "viscosity: measured at 20C with a pH of 7.1)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    parameters__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_parameters", title="Extension field for ``parameters``."
    )

    referenceRange: fhirtypes.RangeType = Field(
        None,
        alias="referenceRange",
        title="Range of typical values",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "code",
            "parameters",
            "definingSubstance",
            "amountQuantity",
            "amountString",
            "referenceRange",
            "source",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3042(
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
        one_of_many_fields = {"amount": ["amountQuantity", "amountString"]}
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


class SubstanceDefinitionRelationship(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A link between this substance and another, with details of the relationship.
    """

    resource_type = Field("SubstanceDefinitionRelationship", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountRange: fhirtypes.RangeType = Field(
        None,
        alias="amountRange",
        title=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountRatio: fhirtypes.RatioType = Field(
        None,
        alias="amountRatio",
        title=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountRatioHighLimit: fhirtypes.RatioType = Field(
        None,
        alias="amountRatioHighLimit",
        title="For use when the numeric has an uncertain range",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountString", title="Extension field for ``amountString``."
    )

    amountType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="amountType",
        title=(
            'An operator for the amount, for example "average", "approximately", '
            '"less than"'
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    isDefining: bool = Field(
        None,
        alias="isDefining",
        title=(
            "For example where an enzyme strongly bonds with a particular "
            "substance, this is a defining relationship for that enzyme, out of "
            "several possible substance relationships"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isDefining", title="Extension field for ``isDefining``."
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    substanceDefinitionCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substanceDefinitionCodeableConcept",
        title=(
            "A pointer to another substance, as a resource or just a "
            "representational code"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e substanceDefinition[x]
        one_of_many="substanceDefinition",
        one_of_many_required=False,
    )

    substanceDefinitionReference: fhirtypes.ReferenceType = Field(
        None,
        alias="substanceDefinitionReference",
        title=(
            "A pointer to another substance, as a resource or just a "
            "representational code"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e substanceDefinition[x]
        one_of_many="substanceDefinition",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            'For example "salt to parent", "active moiety", "starting material", '
            '"polymorph", "impurity of"'
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionRelationship`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "substanceDefinitionReference",
            "substanceDefinitionCodeableConcept",
            "type",
            "isDefining",
            "amountQuantity",
            "amountRange",
            "amountRatio",
            "amountString",
            "amountRatioHighLimit",
            "amountType",
            "source",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3430(
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
            "amount": ["amountQuantity", "amountRange", "amountRatio", "amountString"],
            "substanceDefinition": [
                "substanceDefinitionCodeableConcept",
                "substanceDefinitionReference",
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


class SubstanceDefinitionSourceMaterial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Material or taxonomic/anatomical source for the substance.
    """

    resource_type = Field("SubstanceDefinitionSourceMaterial", const=True)

    countryOfOrigin: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="countryOfOrigin",
        title="The country or countries where the material is harvested",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    genus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="genus",
        title=(
            "The genus of an organism, typically referring to the Latin epithet of "
            "the genus element of the plant/animal scientific name"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    part: fhirtypes.CodeableConceptType = Field(
        None,
        alias="part",
        title="An anatomical origin of the source material within an organism",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    species: fhirtypes.CodeableConceptType = Field(
        None,
        alias="species",
        title=(
            "The species of an organism, typically referring to the Latin epithet "
            "of the species of the plant/animal"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "A classification that provides the origin of the raw material. "
            "Example: cat hair would be an Animal source type"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionSourceMaterial`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "genus",
            "species",
            "part",
            "countryOfOrigin",
        ]


class SubstanceDefinitionStructure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structural information.
    """

    resource_type = Field("SubstanceDefinitionStructure", const=True)

    isotope: typing.List[fhirtypes.SubstanceDefinitionStructureIsotopeType] = Field(
        None,
        alias="isotope",
        title=(
            "Applicable for single substances that contain a radionuclide or a non-"
            "natural isotopic ratio"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    molecularFormula: fhirtypes.String = Field(
        None,
        alias="molecularFormula",
        title="Molecular formula of this substance, typically using the Hill system",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    molecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_molecularFormula",
        title="Extension field for ``molecularFormula``.",
    )

    molecularFormulaByMoiety: fhirtypes.String = Field(
        None,
        alias="molecularFormulaByMoiety",
        title=(
            "Specified per moiety according to the Hill system, i.e. first C, then "
            "H, then alphabetical, each moiety separated by a dot"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    molecularFormulaByMoiety__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_molecularFormulaByMoiety",
        title="Extension field for ``molecularFormulaByMoiety``.",
    )

    molecularWeight: fhirtypes.SubstanceDefinitionStructureIsotopeMolecularWeightType = Field(
        None,
        alias="molecularWeight",
        title=(
            "The molecular weight or weight range (for proteins, polymers or "
            "nucleic acids)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    opticalActivity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="opticalActivity",
        title="Optical activity type",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    representation: typing.List[
        fhirtypes.SubstanceDefinitionStructureRepresentationType
    ] = Field(
        None,
        alias="representation",
        title="A depiction of the structure or characterization of the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    sourceDocument: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="sourceDocument",
        title="Supporting literature about the source of information",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    stereochemistry: fhirtypes.CodeableConceptType = Field(
        None,
        alias="stereochemistry",
        title="Stereochemistry type",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    technique: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="technique",
        title=(
            "The method used to elucidate the structure or characterization of the "
            "drug substance. Examples: X-ray, HPLC, NMR, Peptide mapping, Ligand "
            "binding assay"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionStructure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "stereochemistry",
            "opticalActivity",
            "molecularFormula",
            "molecularFormulaByMoiety",
            "isotope",
            "molecularWeight",
            "technique",
            "sourceDocument",
            "representation",
        ]


class SubstanceDefinitionStructureIsotope(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """

    resource_type = Field("SubstanceDefinitionStructureIsotope", const=True)

    halfLife: fhirtypes.QuantityType = Field(
        None,
        alias="halfLife",
        title="Half life - for a non-natural nuclide",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Substance identifier for each non-natural or radioisotope",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    molecularWeight: fhirtypes.SubstanceDefinitionStructureIsotopeMolecularWeightType = Field(
        None,
        alias="molecularWeight",
        title=(
            "The molecular weight or weight range (for proteins, polymers or "
            "nucleic acids)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.CodeableConceptType = Field(
        None,
        alias="name",
        title="Substance name for each non-natural or radioisotope",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    substitution: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substitution",
        title="The type of isotopic substitution present in a single substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionStructureIsotope`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "name",
            "substitution",
            "halfLife",
            "molecularWeight",
        ]


class SubstanceDefinitionStructureIsotopeMolecularWeight(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """

    resource_type = Field(
        "SubstanceDefinitionStructureIsotopeMolecularWeight", const=True
    )

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title=(
            "Used to capture quantitative values for a variety of elements. If only"
            " limits are given, the arithmetic mean would be the average. If only a"
            " single definite value for a given element is given, it would be "
            "captured in this field"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="The method by which the molecular weight was determined",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "Type of molecular weight such as exact, average (also known as. number"
            " average), weight average"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionStructureIsotopeMolecularWeight`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "method", "type", "amount"]


class SubstanceDefinitionStructureRepresentation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A depiction of the structure or characterization of the substance.
    """

    resource_type = Field("SubstanceDefinitionStructureRepresentation", const=True)

    document: fhirtypes.ReferenceType = Field(
        None,
        alias="document",
        title=(
            "An attached file with the structural representation or "
            "characterization e.g. a molecular structure graphic of the substance, "
            "a JCAMP or AnIML file"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    format: fhirtypes.CodeableConceptType = Field(
        None,
        alias="format",
        title=(
            "The format of the representation e.g. InChI, SMILES, MOLFILE, CDX, "
            "SDF, PDB, mmCIF. The logical content type rather than the physical "
            "file format of a document"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    representation: fhirtypes.String = Field(
        None,
        alias="representation",
        title=(
            "The structural representation or characterization as a text string in "
            "a standard format"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    representation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_representation", title="Extension field for ``representation``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "The kind of structural representation (e.g. full, partial) or the "
            "technique used to derive the analytical characterization of the "
            "substance (e.g. x-ray, HPLC, NMR, peptide mapping, ligand binding "
            "assay, etc.)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``SubstanceDefinitionStructureRepresentation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "representation",
            "format",
            "document",
        ]
