# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
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


class Device(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item used in healthcare.
    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """

    resource_type = Field("Device", const=True)

    associationStatus: fhirtypes.DeviceAssociationStatusType = Field(
        None,
        alias="associationStatus",
        title="The state of the usage or application of the device",
        description=(
            "The state of the usage or application of the device - whether the "
            "device is implanted, or explanted, or attached to the patient."
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

    definition: fhirtypes.ReferenceType = Field(
        None,
        alias="definition",
        title="The reference to the definition for the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceDefinition"],
    )

    deviceName: typing.List[fhirtypes.DeviceDeviceNameType] = Field(
        None,
        alias="deviceName",
        title=(
            "The name or names of the device as known to the manufacturer and/or "
            "patient"
        ),
        description=(
            "This represents the manufacturer's name of the device as provided by "
            "the device, from a UDI label, or by a person describing the Device.  "
            "This typically would be used when a person provides the name(s) or "
            "when the device represents one of the names available from "
            "DeviceDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    displayName: fhirtypes.String = Field(
        None,
        alias="displayName",
        title="The name used to display by default when the device is referenced",
        description=(
            "The name used to display by default when the device is referenced. "
            "Based on intent of use by the resource creator, this may reflect one "
            "of the names in Device.deviceName, or may be another simple name."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    displayName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_displayName", title="Extension field for ``displayName``."
    )

    distinctIdentifier: fhirtypes.String = Field(
        None,
        alias="distinctIdentifier",
        title="The distinct identification string",
        description=(
            "The distinct identification string as required by regulation for a "
            "human cell, tissue, or cellular and tissue-based product."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    distinctIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_distinctIdentifier",
        title="Extension field for ``distinctIdentifier``.",
    )

    expirationDate: fhirtypes.DateTime = Field(
        None,
        alias="expirationDate",
        title="Date and time of expiry of this device (if applicable)",
        description=(
            "The date and time beyond which this device is no longer valid or "
            "should not be used (if applicable)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expirationDate", title="Extension field for ``expirationDate``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Instance identifier",
        description=(
            "Unique instance identifiers assigned to a device by manufacturers "
            "other organizations or owners."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where the device is found",
        description="The place where the device can be found.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="Lot number of manufacture",
        description="Lot number assigned by the manufacturer.",
        # if property is element of this resource.
        element_property=True,
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    manufactureDate: fhirtypes.DateTime = Field(
        None,
        alias="manufactureDate",
        title="Date when the device was made",
        description="The date and time when the device was manufactured.",
        # if property is element of this resource.
        element_property=True,
    )
    manufactureDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_manufactureDate", title="Extension field for ``manufactureDate``."
    )

    manufacturer: fhirtypes.String = Field(
        None,
        alias="manufacturer",
        title="Name of device manufacturer",
        description=(
            "A name of the manufacturer or entity legally responsible for the "
            "device."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    manufacturer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_manufacturer", title="Extension field for ``manufacturer``."
    )

    modelNumber: fhirtypes.String = Field(
        None,
        alias="modelNumber",
        title="The manufacturer's model number for the device",
        description=None,
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

    operationalStatus: fhirtypes.DeviceOperationalStatusType = Field(
        None,
        alias="operationalStatus",
        title=(
            "The status of the device itself - whether it is switched on, or "
            "activated, etc"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title="The device that this device is attached to or is part of",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    partNumber: fhirtypes.String = Field(
        None,
        alias="partNumber",
        title="The part number or catalog number of the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    partNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_partNumber", title="Extension field for ``partNumber``."
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Patient to whom Device is affixed",
        description=(
            "Patient information, if the device is affixed to, or associated to a "
            "patient for their specific use, irrespective of the procedure, use, "
            "observation, or other activity that the device is involved in."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    property: typing.List[fhirtypes.DevicePropertyType] = Field(
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

    safety: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="safety",
        title="Safety Characteristics of Device",
        description=(
            "Provides additional safety characteristics about a medical device.  "
            "For example devices containing latex."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    serialNumber: fhirtypes.String = Field(
        None,
        alias="serialNumber",
        title="Serial number assigned by the manufacturer",
        description=(
            "The serial number assigned by the organization when the device was "
            "manufactured."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    serialNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_serialNumber", title="Extension field for ``serialNumber``."
    )

    specialization: typing.List[fhirtypes.DeviceSpecializationType] = Field(
        None,
        alias="specialization",
        title=(
            "The capabilities supported on a  device, the standards to which the "
            "device conforms for a particular purpose, and used for the "
            "communication"
        ),
        description=(
            "The device function, including in some cases whether or not the "
            "functionality conforms to some standard. For example, a PHD blood "
            "pressure specialization indicates that the device conforms to the IEEE"
            " 11073-10407 Blood Pressure Specialization. This is NOT an alternate "
            "name or an additional descriptive name given by the manufacturer. That"
            " would be found in the deviceName element. In the PHD case, there are "
            "11073 10101 nomenclature codes that define the specialization "
            "standards and that will be used, for example, in the PHD case for the "
            "specialization.systemType element. The specialization.version would be"
            " the version of the standard if the systemType referred to a standard."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | inactive | entered-in-error | unknown",
        description=(
            "Status of the Device record. This is not the status of the device like"
            " availability."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "entered-in-error", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="statusReason",
        title="discarded | obsolete | removed",
        description=(
            "Reason for the status of the Device record. For example, why is the "
            "record not active."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="The kind or type of device",
        description=(
            "The kind or type of device. A device instance may have more than one "
            "type - in which case those are the types that apply to the specific "
            "instance of the device."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    udiCarrier: typing.List[fhirtypes.DeviceUdiCarrierType] = Field(
        None,
        alias="udiCarrier",
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

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Network address to contact device",
        description="A network address on which the device may be contacted directly.",
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    version: typing.List[fhirtypes.DeviceVersionType] = Field(
        None,
        alias="version",
        title=(
            "The actual design of the device or software version running on the "
            "device"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``Device`` according specification,
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
            "displayName",
            "definition",
            "udiCarrier",
            "status",
            "statusReason",
            "distinctIdentifier",
            "manufacturer",
            "manufactureDate",
            "expirationDate",
            "lotNumber",
            "serialNumber",
            "deviceName",
            "modelNumber",
            "partNumber",
            "type",
            "specialization",
            "version",
            "property",
            "patient",
            "operationalStatus",
            "associationStatus",
            "owner",
            "contact",
            "location",
            "url",
            "note",
            "safety",
            "parent",
        ]


from . import backboneelement


class DeviceAssociationStatus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The state of the usage or application of the device.
    The state of the usage or application of the device - whether the device is
    implanted, or explanted, or attached to the patient.
    """

    resource_type = Field("DeviceAssociationStatus", const=True)

    reason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="The reasons given for the current association status",
        description=(
            "The reasons given for the current association status - i.e. why is the"
            " device explanted, or attached to the patient, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.CodeableConceptType = Field(
        None,
        alias="value",
        title="implanted|explanted|attached",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceAssociationStatus`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "value", "reason"]


class DeviceDeviceName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The name or names of the device as known to the manufacturer and/or patient.
    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """

    resource_type = Field("DeviceDeviceName", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="The name that identifies the device",
        description=None,
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
            "The type of deviceName. Note that ManufactureDeviceName means that the"
            " name is the name as given by the manufacturer, not the name of the "
            "manufacturer. UDILabelName | UserFriendlyName | PatientReportedName | "
            "ManufactureDeviceName | ModelName."
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
        """returning all elements names from ``DeviceDeviceName`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "type"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1738(
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


class DeviceOperationalStatus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The status of the device itself - whether it is switched on, or activated,
    etc.
    """

    resource_type = Field("DeviceOperationalStatus", const=True)

    reason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="The reasons given for the current operational status",
        description=(
            "The reasons given for the current operational status - i.e. why is the"
            " device switched on etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.CodeableConceptType = Field(
        None,
        alias="value",
        title="on |off | standby",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceOperationalStatus`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "value", "reason"]


class DeviceProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """

    resource_type = Field("DeviceProperty", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Code that specifies the property being represented",
        description=(
            "Code that specifies the property being represented. No codes are "
            "specified but the MDC codes are an example: "
            "https://build.fhir.org/mdc.html."
        ),
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
        """returning all elements names from ``DeviceProperty`` according specification,
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


class DeviceSpecialization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    The device function, including in some cases whether or not the
    functionality conforms to some standard. For example, a PHD blood pressure
    specialization indicates that the device conforms to the IEEE 11073-10407
    Blood Pressure Specialization. This is NOT an alternate name or an
    additional descriptive name given by the manufacturer. That would be found
    in the deviceName element.
    In the PHD case, there are 11073 10101 nomenclature codes that define the
    specialization standards and that will be used, for example, in the PHD
    case for the specialization.systemType element. The specialization.version
    would be the version of the standard if the systemType referred to a
    standard.
    """

    resource_type = Field("DeviceSpecialization", const=True)

    systemType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="systemType",
        title="The standard that is used to operate and communicate",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        """returning all elements names from ``DeviceSpecialization`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "systemType", "version"]


class DeviceUdiCarrier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Unique Device Identifier (UDI) Barcode string.
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """

    resource_type = Field("DeviceUdiCarrier", const=True)

    carrierAIDC: fhirtypes.Base64Binary = Field(
        None,
        alias="carrierAIDC",
        title="UDI Machine Readable Barcode String",
        description=(
            "The full UDI carrier of the Automatic Identification and Data Capture "
            "(AIDC) technology representation of the barcode string as printed on "
            "the packaging of the device - e.g., a barcode or RFID.   Because of "
            "limitations on character sets in XML and the need to round-trip JSON "
            "data through XML, AIDC Formats *SHALL* be base64 encoded."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    carrierAIDC__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_carrierAIDC", title="Extension field for ``carrierAIDC``."
    )

    carrierHRF: fhirtypes.String = Field(
        None,
        alias="carrierHRF",
        title="UDI Human Readable Barcode String",
        description=(
            "The full UDI carrier as the human readable form (HRF) representation "
            "of the barcode string as printed on the packaging of the device."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    carrierHRF__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_carrierHRF", title="Extension field for ``carrierHRF``."
    )

    deviceIdentifier: fhirtypes.String = Field(
        None,
        alias="deviceIdentifier",
        title="Mandatory fixed portion of UDI",
        description=(
            "The device identifier (DI) is a mandatory, fixed portion of a UDI that"
            " identifies the labeler and the specific version or model of a device."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_deviceIdentifier",
        title="Extension field for ``deviceIdentifier``.",
    )

    entryType: fhirtypes.Code = Field(
        None,
        alias="entryType",
        title=(
            "barcode | rfid | manual | card | self-reported | electronic-"
            "transmission | unknown"
        ),
        description="A coded entry to indicate how the data was entered.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "barcode",
            "rfid",
            "manual",
            "card",
            "self-reported",
            "electronic-transmission",
            "unknown",
        ],
    )
    entryType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_entryType", title="Extension field for ``entryType``."
    )

    issuer: fhirtypes.Uri = Field(
        None,
        alias="issuer",
        title="UDI Issuing Organization",
        description=(
            "Organization that is charged with issuing UDIs for devices.  For "
            "example, the US FDA issuers include : 1) GS1:  "
            "http://hl7.org/fhir/NamingSystem/gs1-di,  2) HIBCC: "
            "http://hl7.org/fhir/NamingSystem/hibcc-dI,  3) ICCBBA for blood "
            "containers: http://hl7.org/fhir/NamingSystem/iccbba-blood-di,  4) "
            "ICCBA for other devices: http://hl7.org/fhir/NamingSystem/iccbba-"
            "other-di."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issuer", title="Extension field for ``issuer``."
    )

    jurisdiction: fhirtypes.Uri = Field(
        None,
        alias="jurisdiction",
        title="Regional UDI authority",
        description=(
            "The identity of the authoritative source for UDI generation within a  "
            "jurisdiction.  All UDIs are globally unique within a single namespace "
            "with the appropriate repository uri as the system.  For example,  UDIs"
            " of devices managed in the U.S. by the FDA, the value is  "
            "http://hl7.org/fhir/NamingSystem/fda-udi."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_jurisdiction", title="Extension field for ``jurisdiction``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``DeviceUdiCarrier`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "deviceIdentifier",
            "issuer",
            "jurisdiction",
            "carrierAIDC",
            "carrierHRF",
            "entryType",
        ]


class DeviceVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual design of the device or software version running on the device.
    """

    resource_type = Field("DeviceVersion", const=True)

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
        """returning all elements names from ``DeviceVersion`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "component", "value"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1512(
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
