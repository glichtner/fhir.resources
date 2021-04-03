# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceDefinition
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


class DeviceDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An instance of a medical-related component of a medical device.
    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """

    resource_type = Field("DeviceDefinition", const=True)

    capability: typing.List[fhirtypes.DeviceDefinitionCapabilityType] = Field(
        None,
        alias="capability",
        title="Additional capabilities of the device",
        description=(
            "Additional capabilities that the device is defined or required to have"
            ' e.g. "water resistant", "long life".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="Details for human/organization for support",
        description=(
            "Contact details for an organization or a particular human that is "
            "responsible for the device."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    deviceName: typing.List[fhirtypes.DeviceDefinitionDeviceNameType] = Field(
        None,
        alias="deviceName",
        title="The name or names of the device as given by the manufacturer",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Instance identifier",
        description=(
            "Unique instance identifiers assigned to a device by the software, "
            "manufacturers, other organizations or owners. For example: handle ID."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    languageCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="languageCode",
        title=(
            "Language code for the human-readable text strings produced by the "
            "device (all supported)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    manufacturerReference: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturerReference",
        title="Name of device manufacturer",
        description=(
            "A name of the manufacturer  or legal representative e.g. labeler. "
            "Whether this is the actual manufacturer or the labeler or responsible "
            "depends on implementation and jurisdiction."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e manufacturer[x]
        one_of_many="manufacturer",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    manufacturerString: fhirtypes.String = Field(
        None,
        alias="manufacturerString",
        title="Name of device manufacturer",
        description=(
            "A name of the manufacturer  or legal representative e.g. labeler. "
            "Whether this is the actual manufacturer or the labeler or responsible "
            "depends on implementation and jurisdiction."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e manufacturer[x]
        one_of_many="manufacturer",
        one_of_many_required=False,
    )
    manufacturerString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_manufacturerString",
        title="Extension field for ``manufacturerString``.",
    )

    material: typing.List[fhirtypes.DeviceDefinitionMaterialType] = Field(
        None,
        alias="material",
        title="A substance used to create the material(s) of which the device is made",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    modelNumber: fhirtypes.String = Field(
        None,
        alias="modelNumber",
        title=(
            "The catalog or model number for the device for example as defined by "
            "the manufacturer"
        ),
        description=(
            "The model number for the device for example as defined by the "
            "manufacturer or labeler, or other agency."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    modelNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_modelNumber", title="Extension field for ``modelNumber``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Device notes and comments",
        description=(
            "Descriptive information, usage information or implantation information"
            " that is not captured in an existing element."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    onlineInformation: fhirtypes.Uri = Field(
        None,
        alias="onlineInformation",
        title="Access to on-line information",
        description="Access to on-line information about the device.",
        # if property is element of this resource.
        element_property=True,
    )
    onlineInformation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_onlineInformation",
        title="Extension field for ``onlineInformation``.",
    )

    owner: fhirtypes.ReferenceType = Field(
        None,
        alias="owner",
        title="Organization responsible for device",
        description=(
            "An organization that is responsible for the provision and ongoing "
            "maintenance of the device."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    parentDevice: fhirtypes.ReferenceType = Field(
        None,
        alias="parentDevice",
        title="The parent device it can be part of",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceDefinition"],
    )

    physicalCharacteristics: fhirtypes.ProdCharacteristicType = Field(
        None,
        alias="physicalCharacteristics",
        title=(
            "Physical characteristics to define or specify the product - for "
            "example dimensions, color etc."
        ),
        description=(
            "Physical characteristics to define or specify the product - for "
            "example dimensions, color etc. These can be defined by the "
            "manufacturer or labeler, or can be used to specify characteristics "
            "when ordering."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    property: typing.List[fhirtypes.DeviceDefinitionPropertyType] = Field(
        None,
        alias="property",
        title=(
            "The actual configuration settings of a device as it actually operates,"
            " e.g., regulation status, time properties"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "The quantity of the device present in the packaging (e.g. the number "
            "of devices present in a pack, or the number of devices in the same "
            "package of the medicinal product)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    safety: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="safety",
        title="Safety characteristics of the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    shelfLifeStorage: typing.List[fhirtypes.ProductShelfLifeType] = Field(
        None,
        alias="shelfLifeStorage",
        title="Shelf Life and storage information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    specialization: typing.List[fhirtypes.DeviceDefinitionSpecializationType] = Field(
        None,
        alias="specialization",
        title=(
            "The capabilities supported on a  device, the standards to which the "
            "device conforms for a particular purpose, and used for the "
            "communication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="What kind of device or device system this is",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    udiDeviceIdentifier: typing.List[
        fhirtypes.DeviceDefinitionUdiDeviceIdentifierType
    ] = Field(
        None,
        alias="udiDeviceIdentifier",
        title="Unique Device Identifier (UDI) Barcode string",
        description=(
            "Unique device identifier (UDI) assigned to device label or package.  "
            "Note that the Device may include multiple udiCarriers as it either may"
            " include just the udiCarrier for the jurisdiction it is sold, or for "
            "multiple jurisdictions it could have been sold."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: typing.List[fhirtypes.DeviceDefinitionVersionType] = Field(
        None,
        alias="version",
        title="The version of the device or software",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceDefinition`` according specification,
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
            "udiDeviceIdentifier",
            "manufacturerString",
            "manufacturerReference",
            "deviceName",
            "modelNumber",
            "type",
            "specialization",
            "version",
            "safety",
            "shelfLifeStorage",
            "physicalCharacteristics",
            "languageCode",
            "capability",
            "property",
            "owner",
            "contact",
            "onlineInformation",
            "note",
            "quantity",
            "parentDevice",
            "material",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1803(
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
            "manufacturer": ["manufacturerReference", "manufacturerString"]
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


from . import backboneelement


class DeviceDefinitionCapability(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional capabilities of the device.
    Additional capabilities that the device is defined or required to have e.g.
    "water resistant", "long life".
    """

    resource_type = Field("DeviceDefinitionCapability", const=True)

    description: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="description",
        title="The actual capability of the device",
        description="The actual capability of the device e.g. IP67.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title=(
            "The type of capability - whether it is a physical attribute, a "
            "customization needed"
        ),
        description=(
            "The type of capability - whether it is a physical attribute, a "
            'customization needed. For exampl e "water ingress protection".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceDefinitionCapability`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "description"]


class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The name or names of the device as given by the manufacturer.
    """

    resource_type = Field("DeviceDefinitionDeviceName", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="A name that is used to refer to the device",
        description=(
            "A human-friendly name that is used to refer to the device - depending "
            "on the type, it can be the brand name, the common name or alias, or "
            "other."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title=(
            "udi-label-name | user-friendly-name | patient-reported-name | "
            "manufacturer-name | model-name | other"
        ),
        description=(
            "The type of deviceName. UDILabelName | UserFriendlyName | "
            "PatientReportedName | ManufactureDeviceName | ModelName."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "udi-label-name",
            "user-friendly-name",
            "patient-reported-name",
            "manufacturer-name",
            "model-name",
            "other",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceDefinitionDeviceName`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "type"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2771(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext"), ("type", "type__ext")]
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


class DeviceDefinitionMaterial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A substance used to create the material(s) of which the device is made.
    """

    resource_type = Field("DeviceDefinitionMaterial", const=True)

    allergenicIndicator: bool = Field(
        None,
        alias="allergenicIndicator",
        title="Whether the substance is a known or suspected allergen",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_allergenicIndicator",
        title="Extension field for ``allergenicIndicator``.",
    )

    alternate: bool = Field(
        None,
        alias="alternate",
        title="Indicates an alternative material of the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    alternate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_alternate", title="Extension field for ``alternate``."
    )

    substance: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="substance",
        title=(
            "A relevant substance that the device contains, may contain, or is made"
            " of"
        ),
        description=(
            "A substance that the device contains, may contain, or is made of - for"
            " example latex - to be used to determine patient compatibility. This "
            "is not intended to represent the composition of the device, only the "
            "clinically relevant materials."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceDefinitionMaterial`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "substance",
            "alternate",
            "allergenicIndicator",
        ]


class DeviceDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """

    resource_type = Field("DeviceDefinitionProperty", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title=(
            "Code that specifies the property DeviceDefinitionPropetyCode "
            "(Extensible)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="valueCode",
        title="Property value as a code, e.g., NTP4 (synced to NTP)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueQuantity: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="valueQuantity",
        title="Property value as a quantity",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceDefinitionProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueQuantity",
            "valueCode",
        ]


class DeviceDefinitionSpecialization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """

    resource_type = Field("DeviceDefinitionSpecialization", const=True)

    systemType: fhirtypes.String = Field(
        None,
        alias="systemType",
        title="The standard that is used to operate and communicate",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    systemType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_systemType", title="Extension field for ``systemType``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="The version of the standard that is used to operate and communicate",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceDefinitionSpecialization`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "systemType", "version"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3274(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("systemType", "systemType__ext")]
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


class DeviceDefinitionUdiDeviceIdentifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Unique Device Identifier (UDI) Barcode string.
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """

    resource_type = Field("DeviceDefinitionUdiDeviceIdentifier", const=True)

    deviceIdentifier: fhirtypes.String = Field(
        None,
        alias="deviceIdentifier",
        title=(
            "The identifier that is to be associated with every Device that "
            "references this DeviceDefintiion for the issuer and jurisdication "
            "porvided in the DeviceDefinition.udiDeviceIdentifier"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_deviceIdentifier",
        title="Extension field for ``deviceIdentifier``.",
    )

    issuer: fhirtypes.Uri = Field(
        None,
        alias="issuer",
        title="The organization that assigns the identifier algorithm",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issuer", title="Extension field for ``issuer``."
    )

    jurisdiction: fhirtypes.Uri = Field(
        None,
        alias="jurisdiction",
        title="The jurisdiction to which the deviceIdentifier applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_jurisdiction", title="Extension field for ``jurisdiction``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceDefinitionUdiDeviceIdentifier`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "deviceIdentifier",
            "issuer",
            "jurisdiction",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3716(
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
            ("deviceIdentifier", "deviceIdentifier__ext"),
            ("issuer", "issuer__ext"),
            ("jurisdiction", "jurisdiction__ext"),
        ]
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


class DeviceDefinitionVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The version of the device or software.
    """

    resource_type = Field("DeviceDefinitionVersion", const=True)

    component: fhirtypes.IdentifierType = Field(
        None,
        alias="component",
        title=(
            "The hardware or software module of the device to which the version "
            "applies"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The type of the device version, e.g. manufacturer, approved, internal",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The version text",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceDefinitionVersion`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "component", "value"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2545(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
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
