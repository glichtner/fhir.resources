# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GenomicStudy
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
import typing
from pydantic import Field
from pydantic import root_validator

from . import fhirtypes


from . import domainresource

class GenomicStudy(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Genomic Study.
    A Genomic Study is a set of analysis performed to analyze and generate
    genomic data.
    """
    resource_type = Field("GenomicStudy", const=True)
	
    analysis: typing.List[fhirtypes.GenomicStudyAnalysisType] = Field(
		None,
		alias="analysis",
		title="Genomic Analysis Event",
		description=(
    "The details about a specific analysis that was performed in this "
    "GenomicStudy."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="basedOn",
		title="Event resources that the genomic study is based on",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["ServiceRequest", "Task"],
	)
	
    description: fhirtypes.String = Field(
		None,
		alias="description",
		title="Description of the genomic study",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_description",
        title="Extension field for ``description``."
    )
	
    encounter: fhirtypes.ReferenceType = Field(
		None,
		alias="encounter",
		title="The healthcare event with which this genomics study is associated",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Encounter"],
	)
	
    identifier: typing.List[fhirtypes.IdentifierType] = Field(
		None,
		alias="identifier",
		title="Identifiers for this genomic study",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    instantiatesCanonical: fhirtypes.Canonical = Field(
		None,
		alias="instantiatesCanonical",
		title="The defined protocol that describes the study",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["PlanDefinition"],
	)
    instantiatesCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``."
    )
	
    instantiatesUri: fhirtypes.Uri = Field(
		None,
		alias="instantiatesUri",
		title=(
    "The URL pointing to an externally maintained protocol that describes "
    "the study"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_instantiatesUri",
        title="Extension field for ``instantiatesUri``."
    )
	
    interpreter: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="interpreter",
		title="Healthcare professionals who interpreted the genomic study",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Practitioner", "PractitionerRole"],
	)
	
    note: typing.List[fhirtypes.AnnotationType] = Field(
		None,
		alias="note",
		title="Comments related to the genomic study",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    reason: typing.List[fhirtypes.CodeableReferenceType] = Field(
		None,
		alias="reason",
		title="Why the genomic study was performed",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Condition", "Observation"],
	)
	
    referrer: fhirtypes.ReferenceType = Field(
		None,
		alias="referrer",
		title="Healthcare professional who requested or referred the genomic study",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Practitioner", "PractitionerRole"],
	)
	
    startDate: fhirtypes.DateTime = Field(
		None,
		alias="startDate",
		title="When the genomic study was started",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    startDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_startDate",
        title="Extension field for ``startDate``."
    )
	
    status: fhirtypes.CodeableConceptType = Field(
		...,
		alias="status",
		title="The status of the genomic study",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    subject: fhirtypes.ReferenceType = Field(
		...,
		alias="subject",
		title="The primary subject of the genomic study",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Patient", "Group", "Device", "Location", "Organization", "Procedure", "Practitioner", "Medication", "Substance", "BiologicallyDerivedProduct", "NutritionProduct"],
	)
	
    type: typing.List[fhirtypes.CodeableConceptType] = Field(
		None,
		alias="type",
		title=(
    "The type of the study (e.g., Familial variant segregation, Functional "
    "variation detection, or Gene expression profiling)"
    ),
		description=(
    "The type of the study, e.g., Familial variant segregation, Functional "
    "variation detection, or Gene expression profiling."
    ),
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``GenomicStudy`` according specification,
        with preserving original sequence order.
        """
        return ["id", "meta", "implicitRules", "language", "text", "contained", "extension", "modifierExtension", "identifier", "status", "type", "subject", "encounter", "startDate", "basedOn", "referrer", "interpreter", "reason", "instantiatesCanonical", "instantiatesUri", "note", "description", "analysis"]



from . import backboneelement

class GenomicStudyAnalysis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Genomic Analysis Event.
    The details about a specific analysis that was performed in this
    GenomicStudy.
    """
    resource_type = Field("GenomicStudyAnalysis", const=True)
	
    changeType: typing.List[fhirtypes.CodeableConceptType] = Field(
		None,
		alias="changeType",
		title=(
    "Type of the genomic changes studied in the analysis (e.g., DNA, RNA, "
    "or AA change)"
    ),
		description=(
    "Type of the genomic changes studied in the analysis, e.g., DNA, RNA, "
    "or amino acid change."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    date: fhirtypes.DateTime = Field(
		None,
		alias="date",
		title="The date of the analysis event",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_date",
        title="Extension field for ``date``."
    )
	
    device: typing.List[fhirtypes.GenomicStudyAnalysisDeviceType] = Field(
		None,
		alias="device",
		title=(
    "Devices used for the analysis (e.g., instruments, software), with "
    "settings and parameters"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    genomeBuild: fhirtypes.CodeableConceptType = Field(
		None,
		alias="genomeBuild",
		title="Genome build that is used in this analysis",
		description="The reference genome build that is used in this analysis.",
        # if property is element of this resource.
        element_property=True,
	)
	
    identifier: typing.List[fhirtypes.IdentifierType] = Field(
		None,
		alias="identifier",
		title="Identifiers for the analysis event",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    input: typing.List[fhirtypes.GenomicStudyAnalysisInputType] = Field(
		None,
		alias="input",
		title="Inputs for the analysis event",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    instantiatesCanonical: fhirtypes.Canonical = Field(
		None,
		alias="instantiatesCanonical",
		title="The defined protocol that describes the analysis",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["PlanDefinition", "ActivityDefinition"],
	)
    instantiatesCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``."
    )
	
    instantiatesUri: fhirtypes.Uri = Field(
		None,
		alias="instantiatesUri",
		title=(
    "The URL pointing to an externally maintained protocol that describes "
    "the analysis"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_instantiatesUri",
        title="Extension field for ``instantiatesUri``."
    )
	
    methodType: typing.List[fhirtypes.CodeableConceptType] = Field(
		None,
		alias="methodType",
		title=(
    "Type of the methods used in the analysis (e.g., FISH, Karyotyping, "
    "MSI)"
    ),
		description=(
    "Type of the methods used in the analysis, e.g., Fluorescence in situ "
    "hybridization (FISH), Karyotyping, or Microsatellite instability "
    "testing (MSI)."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    note: typing.List[fhirtypes.AnnotationType] = Field(
		None,
		alias="note",
		title="Any notes capture with the analysis event",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    output: typing.List[fhirtypes.GenomicStudyAnalysisOutputType] = Field(
		None,
		alias="output",
		title="Outputs for the analysis event",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    performer: typing.List[fhirtypes.GenomicStudyAnalysisPerformerType] = Field(
		None,
		alias="performer",
		title="Performer for the analysis event",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    protocolPerformed: fhirtypes.ReferenceType = Field(
		None,
		alias="protocolPerformed",
		title="The protocol that was performed for the analysis event",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Procedure", "Task"],
	)
	
    regionsCalled: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="regionsCalled",
		title="Genomic regions actually called in the analysis event (BED file)",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["DocumentReference", "Observation"],
	)
	
    regionsStudied: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="regionsStudied",
		title="The genomic regions to be studied in the analysis (BED file)",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["DocumentReference", "Observation"],
	)
	
    specimen: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="specimen",
		title="The specimen used in the analysis event",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Specimen"],
	)
	
    subject: fhirtypes.ReferenceType = Field(
		None,
		alias="subject",
		title="The subject of the analysis event",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Patient", "Group", "Device", "Location", "Organization", "Procedure", "Practitioner", "Medication", "Substance", "BiologicallyDerivedProduct", "NutritionProduct"],
	)
	
    title: fhirtypes.String = Field(
		None,
		alias="title",
		title="Name of the analysis event (human friendly)",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_title",
        title="Extension field for ``title``."
    )
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``GenomicStudyAnalysis`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "identifier", "methodType", "changeType", "genomeBuild", "instantiatesCanonical", "instantiatesUri", "title", "subject", "specimen", "date", "note", "protocolPerformed", "regionsStudied", "regionsCalled", "input", "output", "performer", "device"]



class GenomicStudyAnalysisDevice(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Devices used for the analysis (e.g., instruments, software), with settings
    and parameters.
    """
    resource_type = Field("GenomicStudyAnalysisDevice", const=True)
	
    device: fhirtypes.ReferenceType = Field(
		None,
		alias="device",
		title="Device used for the analysis",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Device"],
	)
	
    function: fhirtypes.CodeableConceptType = Field(
		None,
		alias="function",
		title="Specific function for the device used for the analysis",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``GenomicStudyAnalysisDevice`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "device", "function"]



class GenomicStudyAnalysisInput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Inputs for the analysis event.
    """
    resource_type = Field("GenomicStudyAnalysisInput", const=True)
	
    file: fhirtypes.ReferenceType = Field(
		None,
		alias="file",
		title="File containing input data",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["DocumentReference"],
	)
	
    generatedByIdentifier: fhirtypes.IdentifierType = Field(
		None,
		alias="generatedByIdentifier",
		title=(
    "The analysis event or other GenomicStudy that generated this input "
    "file"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e generatedBy[x]
		one_of_many="generatedBy",
		one_of_many_required=False,
	)
	
    generatedByReference: fhirtypes.ReferenceType = Field(
		None,
		alias="generatedByReference",
		title=(
    "The analysis event or other GenomicStudy that generated this input "
    "file"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e generatedBy[x]
		one_of_many="generatedBy",
		one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["GenomicStudy"],
	)
	
    type: fhirtypes.CodeableConceptType = Field(
		None,
		alias="type",
		title="Type of input data (e.g., BAM, CRAM, or FASTA)",
		description="Type of input data, e.g., BAM, CRAM, or FASTA.",
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``GenomicStudyAnalysisInput`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "file", "type", "generatedByIdentifier", "generatedByReference"]


    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2794(
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
			"generatedBy": [
			    "generatedByIdentifier",
			    "generatedByReference"]}
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


class GenomicStudyAnalysisOutput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Outputs for the analysis event.
    """
    resource_type = Field("GenomicStudyAnalysisOutput", const=True)
	
    file: fhirtypes.ReferenceType = Field(
		None,
		alias="file",
		title="File containing output data",
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["DocumentReference"],
	)
	
    type: fhirtypes.CodeableConceptType = Field(
		None,
		alias="type",
		title="Type of output data (e.g., VCF, MAF, or BAM)",
		description="Type of output data, e.g., VCF, MAF, or BAM.",
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``GenomicStudyAnalysisOutput`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "file", "type"]



class GenomicStudyAnalysisPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Performer for the analysis event.
    """
    resource_type = Field("GenomicStudyAnalysisPerformer", const=True)
	
    actor: fhirtypes.ReferenceType = Field(
		None,
		alias="actor",
		title=(
    "The organization, healthcare professional, or others who participated "
    "in performing this analysis"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
		enum_reference_types=["Practitioner", "PractitionerRole", "Organization", "Device"],
	)
	
    role: fhirtypes.CodeableConceptType = Field(
		None,
		alias="role",
		title="Role of the actor for this analysis",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``GenomicStudyAnalysisPerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "actor", "role"]

