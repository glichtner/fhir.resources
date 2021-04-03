# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductDefinition
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


class MedicinalProductDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use, drug catalogs).
    """

    resource_type = Field("MedicinalProductDefinition", const=True)

    additionalMonitoringIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additionalMonitoringIndicator",
        title=(
            "Whether the Medicinal Product is subject to additional monitoring for "
            "regulatory reasons"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    administrableProduct: typing.List[
        fhirtypes.MedicinalProductDefinitionAdministrableProductType
    ] = Field(
        None,
        alias="administrableProduct",
        title=(
            "The product in its final form, mixed from its components if necessary,"
            " and ready to be administered to the patient. Also known as the "
            "'Pharmaceutical Product'. Can repeat, for cases where the product has "
            "components that result in more than one administrable item"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    attachedDocument: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="attachedDocument",
        title=(
            "Additional information or supporting documentation about the medicinal"
            " product"
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
            'Allows the key product features to be recorded, such as "sugar free", '
            '"modified release", "parallel import"'
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    classification: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classification",
        title="Allows the product to be classified by various systems",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    clinicalTrial: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="clinicalTrial",
        title="Clinical trials or studies that this product is involved in",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
    )

    combinedPharmaceuticalDoseForm: fhirtypes.CodeableConceptType = Field(
        None,
        alias="combinedPharmaceuticalDoseForm",
        title=(
            "The dose form for a single part product, or combined form of a "
            "multiple part product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.MedicinalProductDefinitionContactType] = Field(
        None,
        alias="contact",
        title="A product specific contact, person (in a role), or an organization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    crossReference: typing.List[
        fhirtypes.MedicinalProductDefinitionCrossReferenceType
    ] = Field(
        None,
        alias="crossReference",
        title=(
            "Reference to another product, e.g. for linking authorised to "
            "investigational product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="General description of this product",
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
        title="If this medicine applies to human or veterinary uses",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for this product. Could be an MPID",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    impurity: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="impurity",
        title=(
            "Any component of the drug product which is not the chemical entity "
            "defined as the drug substance or an excipient in the drug product. "
            "This includes process-related impurities and contaminants, product-"
            "related impurities including degradation products"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition"],
    )

    indication: fhirtypes.Markdown = Field(
        None,
        alias="indication",
        title=(
            "Description of indication(s) for this product, used when structured "
            "indications are not required. In cases where structured indications "
            "are required, they are captured using the ClinicalUseIssue resource. "
            "An indication is a medical situation for which using the product is "
            "appropriate"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    indication__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_indication", title="Extension field for ``indication``."
    )

    ingredient: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="ingredient",
        title=(
            "The ingredients of this medicinal product - when not detailed in other"
            " resources. This is only needed if the ingredients are not specified "
            "by the AdministrableProductDefinition or via the "
            "PackagedProductDefinition references above. In cases where those "
            "levels of detail are not used, the ingredients may be specified "
            "directly here"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Ingredient"],
    )

    legalStatusOfSupply: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalStatusOfSupply",
        title=(
            "The legal status of supply of the medicinal product as classified by "
            "the regulator"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    marketingStatus: typing.List[fhirtypes.MarketingStatusType] = Field(
        None,
        alias="marketingStatus",
        title=(
            "Marketing status of the medicinal product, in contrast to marketing "
            "authorization"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    masterFile: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="masterFile",
        title=(
            "A master file for to the medicinal product (e.g. Pharmacovigilance "
            "System Master File)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    name: typing.List[fhirtypes.MedicinalProductDefinitionNameType] = Field(
        ...,
        alias="name",
        title="The product's name, including full name and possibly coded parts",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    operation: typing.List[fhirtypes.MedicinalProductDefinitionOperationType] = Field(
        None,
        alias="operation",
        title=(
            "A manufacturing or administrative process or step associated with (or "
            "performed on) the medicinal product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    package: typing.List[fhirtypes.MedicinalProductDefinitionPackageType] = Field(
        None,
        alias="package",
        title="Package representation for the product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    paediatricUseIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="paediatricUseIndicator",
        title="If authorised for use in children",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    specialMeasures: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialMeasures",
        title=(
            "Whether the Medicinal Product is subject to special measures for "
            "regulatory reasons"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title=(
            "The status within the lifecycle of this product record. A high-level "
            "status, this is not intended to duplicate details carried elsewhere "
            "such as legal status, or authorization status"
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

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Regulatory type, e.g. Investigational or Authorized",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title=(
            "A business identifier relating to a specific version of the product, "
            "this is commonly used to support revisions to an existing product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``MedicinalProductDefinition`` according specification,
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
            "type",
            "domain",
            "version",
            "status",
            "statusDate",
            "description",
            "combinedPharmaceuticalDoseForm",
            "indication",
            "legalStatusOfSupply",
            "additionalMonitoringIndicator",
            "specialMeasures",
            "paediatricUseIndicator",
            "classification",
            "characteristic",
            "marketingStatus",
            "ingredient",
            "impurity",
            "attachedDocument",
            "masterFile",
            "contact",
            "clinicalTrial",
            "name",
            "crossReference",
            "operation",
            "package",
            "administrableProduct",
        ]


from . import backboneelement


class MedicinalProductDefinitionAdministrableProduct(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The product in its final form, mixed from its components if necessary, and
    ready to be administered to the patient. Also known as the 'Pharmaceutical
    Product'. Can repeat, for cases where the product has components that
    result in more than one administrable item.
    """

    resource_type = Field("MedicinalProductDefinitionAdministrableProduct", const=True)

    product: fhirtypes.ReferenceType = Field(
        None,
        alias="product",
        title="Full description of the administrable product",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["AdministrableProductDefinition"],
    )

    route: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="route",
        title=(
            "The path by which the product is taken into or makes contact with the "
            "body. In some regions this is referred to as the licenced or approved "
            "route"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``MedicinalProductDefinitionAdministrableProduct`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "route", "product"]


class MedicinalProductDefinitionContact(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A product specific contact, person (in a role), or an organization.
    """

    resource_type = Field("MedicinalProductDefinitionContact", const=True)

    contact: fhirtypes.ReferenceType = Field(
        ...,
        alias="contact",
        title="A product specific contact, person (in a role), or an organization",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "PractitionerRole"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "Allows the contact to be classified, for example QPPV, "
            "Pharmacovigilance Enquiry Information"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``MedicinalProductDefinitionContact`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "contact"]


class MedicinalProductDefinitionCrossReference(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Reference to another product, e.g. for linking authorised to
    investigational product.
    """

    resource_type = Field("MedicinalProductDefinitionCrossReference", const=True)

    product: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="product",
        title=(
            "Reference to another product, e.g. for linking authorised to "
            "investigational product"
        ),
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
            "The type of relationship, for instance branded to generic, product to "
            "development product (investigational), parallel import version"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``MedicinalProductDefinitionCrossReference`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "product", "type"]


class MedicinalProductDefinitionName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The product's name, including full name and possibly coded parts.
    """

    resource_type = Field("MedicinalProductDefinitionName", const=True)

    countryLanguage: typing.List[
        fhirtypes.MedicinalProductDefinitionNameCountryLanguageType
    ] = Field(
        None,
        alias="countryLanguage",
        title="Country where the name applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    namePart: typing.List[fhirtypes.MedicinalProductDefinitionNameNamePartType] = Field(
        None,
        alias="namePart",
        title="Coding words or phrases of the name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    productName: fhirtypes.String = Field(
        None,
        alias="productName",
        title="The full product name",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    productName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_productName", title="Extension field for ``productName``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of product name, such as rINN, BAN, Proprietary, Non-Proprietary",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``MedicinalProductDefinitionName`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "productName",
            "type",
            "namePart",
            "countryLanguage",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3235(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("productName", "productName__ext")]
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


class MedicinalProductDefinitionNameCountryLanguage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Country where the name applies.
    """

    resource_type = Field("MedicinalProductDefinitionNameCountryLanguage", const=True)

    country: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="country",
        title="Country code for where this name applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="jurisdiction",
        title="Jurisdiction code for where this name applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    language: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="language",
        title="Language code for this name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``MedicinalProductDefinitionNameCountryLanguage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "country",
            "jurisdiction",
            "language",
        ]


class MedicinalProductDefinitionNameNamePart(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Coding words or phrases of the name.
    """

    resource_type = Field("MedicinalProductDefinitionNameNamePart", const=True)

    part: fhirtypes.String = Field(
        None,
        alias="part",
        title="A fragment of a product name",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    part__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_part", title="Extension field for ``part``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Identifying type for this part of the name (e.g. strength part)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``MedicinalProductDefinitionNameNamePart`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "part", "type"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4042(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("part", "part__ext")]
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


class MedicinalProductDefinitionOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A manufacturing or administrative process or step associated with (or
    performed on) the medicinal product.
    """

    resource_type = Field("MedicinalProductDefinitionOperation", const=True)

    authorization: fhirtypes.ReferenceType = Field(
        None,
        alias="authorization",
        title=(
            "An authorization for this process, either as a logical reference, "
            "holding just an identifier, or a full reference to a resource that "
            "captures the details. The authorization may possibly apply to several "
            "products or a wider scope of process of which this is a part"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["RegulatedAuthorization"],
    )

    confidentialityIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="confidentialityIndicator",
        title=(
            "Specifies whether this particular business or manufacturing process is"
            " considered proprietary or confidential"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    effectiveDate: fhirtypes.PeriodType = Field(
        None,
        alias="effectiveDate",
        title="Date range of applicability",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    organization: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="organization",
        title=(
            "The organization or establishment responsible for (or associated with)"
            " the particular process or step, examples include the manufacturer, "
            "importer, agent"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    type: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="type",
        title=(
            "The type of manufacturing operation e.g. manufacturing itself, re-"
            "packaging. This may be a subtype of some other wider scope of "
            "authorized operation, referenced by the authorization attribute"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ActivityDefinition"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``MedicinalProductDefinitionOperation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "effectiveDate",
            "organization",
            "authorization",
            "confidentialityIndicator",
        ]


class MedicinalProductDefinitionPackage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Package representation for the product.
    """

    resource_type = Field("MedicinalProductDefinitionPackage", const=True)

    package: fhirtypes.ReferenceType = Field(
        None,
        alias="package",
        title="Full package representation for the product",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["PackagedProductDefinition"],
    )

    sizeInteger: fhirtypes.Integer = Field(
        None,
        alias="sizeInteger",
        title="The amount of items, or of substance, in the package",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e size[x]
        one_of_many="size",
        one_of_many_required=False,
    )
    sizeInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sizeInteger", title="Extension field for ``sizeInteger``."
    )

    sizeQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="sizeQuantity",
        title="The amount of items, or of substance, in the package",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e size[x]
        one_of_many="size",
        one_of_many_required=False,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="A descriptive type for this package, such as box, carton or bottle",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``MedicinalProductDefinitionPackage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "sizeQuantity",
            "sizeInteger",
            "package",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3534(
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
        one_of_many_fields = {"size": ["sizeInteger", "sizeQuantity"]}
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
