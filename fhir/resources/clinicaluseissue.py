# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalUseIssue
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


class ClinicalUseIssue(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single issue - either an indication, contraindication, interaction or an
    undesirable effect for a medicinal product, medication, device or procedure.
    """

    resource_type = Field("ClinicalUseIssue", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title=(
            "A categorisation of the issue, primarily for dividing warnings into "
            'subject heading areas such as "Pregnancy and Lactation", "Overdose", '
            '"Effects on Ability to Drive and Use Machines"'
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    contraindication: fhirtypes.ClinicalUseIssueContraindicationType = Field(
        None,
        alias="contraindication",
        title="Specifics for when this is a contraindication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title=(
            "General description of an effect (particularly for a general warning, "
            "rather than any of the more specific types such as indication) for "
            "when a distinct coded or textual description is not appropriate using"
            "  Indication.diseaseSymptomProcedure.text, "
            'Contraindication.diseaseSymptomProcedure.text etc. For example "May '
            'affect ability to drive"'
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
        title="Business identifier for this issue",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    indication: fhirtypes.ClinicalUseIssueIndicationType = Field(
        None,
        alias="indication",
        title="Specifics for when this is an indication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    interaction: fhirtypes.ClinicalUseIssueInteractionType = Field(
        None,
        alias="interaction",
        title="Specifics for when this is an interaction",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    population: typing.List[fhirtypes.PopulationType] = Field(
        None,
        alias="population",
        title="The population group to which this applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Whether this is a current issue or one that has been retired etc",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title="The medication or procedure for which this is an indication",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicinalProductDefinition",
            "Medication",
            "ActivityDefinition",
            "PlanDefinition",
            "Device",
            "DeviceDefinition",
            "Substance",
        ],
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title=(
            "indication | contraindication | interaction | undesirable-effect | "
            "warning"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "indication",
            "contraindication",
            "interaction",
            "undesirable-effect",
            "warning",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    undesirableEffect: fhirtypes.ClinicalUseIssueUndesirableEffectType = Field(
        None,
        alias="undesirableEffect",
        title="A possible negative outcome from the use of this treatment",
        description="Describe the undesirable effects of the medicinal product.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ClinicalUseIssue`` according specification,
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
            "category",
            "subject",
            "status",
            "description",
            "contraindication",
            "indication",
            "interaction",
            "population",
            "undesirableEffect",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1789(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
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


class ClinicalUseIssueContraindication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifics for when this is a contraindication.
    """

    resource_type = Field("ClinicalUseIssueContraindication", const=True)

    comorbidity: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="comorbidity",
        title="A comorbidity (concurrent condition) or coinfection",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    diseaseStatus: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="diseaseStatus",
        title="The status of the disease or symptom for the contraindication",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    diseaseSymptomProcedure: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="diseaseSymptomProcedure",
        title=(
            "The situation that is being documented as contraindicating against "
            "this item"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    indication: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="indication",
        title="The indication which this is a contraidication for",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClinicalUseIssue"],
    )

    otherTherapy: typing.List[
        fhirtypes.ClinicalUseIssueContraindicationOtherTherapyType
    ] = Field(
        None,
        alias="otherTherapy",
        title=(
            "Information about the use of the medicinal product in relation to "
            "other therapies described as part of the contraindication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ClinicalUseIssueContraindication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "diseaseSymptomProcedure",
            "diseaseStatus",
            "comorbidity",
            "indication",
            "otherTherapy",
        ]


class ClinicalUseIssueContraindicationOtherTherapy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the use of the medicinal product in relation to other
    therapies described as part of the contraindication.
    """

    resource_type = Field("ClinicalUseIssueContraindicationOtherTherapy", const=True)

    relationshipType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="relationshipType",
        title=(
            "The type of relationship between the medicinal product indication or "
            "contraindication and another therapy"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    therapy: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="therapy",
        title=(
            "Reference to a specific medication (active substance, medicinal "
            "product or class of products) as part of an indication or "
            "contraindication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicinalProductDefinition",
            "Medication",
            "Substance",
            "SubstanceDefinition",
            "ActivityDefinition",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ClinicalUseIssueContraindicationOtherTherapy`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "relationshipType", "therapy"]


class ClinicalUseIssueIndication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifics for when this is an indication.
    """

    resource_type = Field("ClinicalUseIssueIndication", const=True)

    comorbidity: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="comorbidity",
        title=(
            "A comorbidity (concurrent condition) or coinfection as part of the "
            "indication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    diseaseStatus: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="diseaseStatus",
        title="The status of the disease or symptom for the indication",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    diseaseSymptomProcedure: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="diseaseSymptomProcedure",
        title="The situation that is being documented as an indicaton for this item",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    duration: fhirtypes.QuantityType = Field(
        None,
        alias="duration",
        title="Timing or duration information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    intendedEffect: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="intendedEffect",
        title="The intended effect, aim or strategy to be achieved",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    otherTherapy: typing.List[
        fhirtypes.ClinicalUseIssueContraindicationOtherTherapyType
    ] = Field(
        None,
        alias="otherTherapy",
        title=(
            "Information about the use of the medicinal product in relation to "
            "other therapies described as part of the indication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    undesirableEffect: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="undesirableEffect",
        title="The specific undesirable effects of the medicinal product",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClinicalUseIssue"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ClinicalUseIssueIndication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "diseaseSymptomProcedure",
            "diseaseStatus",
            "comorbidity",
            "intendedEffect",
            "duration",
            "undesirableEffect",
            "otherTherapy",
        ]


class ClinicalUseIssueInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifics for when this is an interaction.
    """

    resource_type = Field("ClinicalUseIssueInteraction", const=True)

    effect: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="effect",
        title=(
            'The effect of the interaction, for example "reduced gastric absorption'
            ' of primary medication"'
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    incidence: fhirtypes.CodeableConceptType = Field(
        None,
        alias="incidence",
        title="The incidence of the interaction, e.g. theoretical, observed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    interactant: typing.List[
        fhirtypes.ClinicalUseIssueInteractionInteractantType
    ] = Field(
        None,
        alias="interactant",
        title=(
            "The specific medication, food, substance or laboratory test that "
            "interacts"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    management: fhirtypes.CodeableConceptType = Field(
        None,
        alias="management",
        title="Actions for managing the interaction",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "The type of the interaction e.g. drug-drug interaction, drug-food "
            "interaction, drug-lab test interaction"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ClinicalUseIssueInteraction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "interactant",
            "type",
            "effect",
            "incidence",
            "management",
        ]


class ClinicalUseIssueInteractionInteractant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The specific medication, food, substance or laboratory test that interacts.
    """

    resource_type = Field("ClinicalUseIssueInteractionInteractant", const=True)

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="The specific medication, food or laboratory test that interacts",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="The specific medication, food or laboratory test that interacts",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicinalProductDefinition",
            "Medication",
            "Substance",
            "ObservationDefinition",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ClinicalUseIssueInteractionInteractant`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemReference",
            "itemCodeableConcept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4105(
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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


class ClinicalUseIssueUndesirableEffect(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A possible negative outcome from the use of this treatment.
    Describe the undesirable effects of the medicinal product.
    """

    resource_type = Field("ClinicalUseIssueUndesirableEffect", const=True)

    classification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="classification",
        title="High level classification of the effect",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    frequencyOfOccurrence: fhirtypes.CodeableConceptType = Field(
        None,
        alias="frequencyOfOccurrence",
        title="How often the effect is seen",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    symptomConditionEffect: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="symptomConditionEffect",
        title="The situation in which the undesirable effect may manifest",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``ClinicalUseIssueUndesirableEffect`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "symptomConditionEffect",
            "classification",
            "frequencyOfOccurrence",
        ]
