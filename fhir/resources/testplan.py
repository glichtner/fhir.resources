# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TestPlan
Release: 5.0.0-draft-final
Version: 5.0.0-draft-final
Build ID: 043d3d5
Last updated: 2023-03-01T23:03:57.298+11:00
"""
import typing
from pydantic import Field
from pydantic import root_validator

from . import fhirtypes


from . import domainresource

class TestPlan(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A plan for executing testing on an artifact or specifications.
    """
    resource_type = Field("TestPlan", const=True)
	
    category: typing.List[fhirtypes.CodeableConceptType] = Field(
		None,
		alias="category",
		title="The category of the Test Plan - can be acceptance, unit, performance",
		description=(
    "The category of the Test Plan - can be acceptance, unit, performance, "
    "etc."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    contact: typing.List[fhirtypes.ContactDetailType] = Field(
		None,
		alias="contact",
		title="Contact",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    copyright: fhirtypes.Markdown = Field(
		None,
		alias="copyright",
		title="Copyright",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_copyright",
        title="Extension field for ``copyright``."
    )
	
    date: typing.List[fhirtypes.DateTime] = Field(
		None,
		alias="date",
		title="Date",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    date__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None,
        alias="_date",
        title="Extension field for ``date``."
    )
	
    dependencies: typing.List[fhirtypes.TestPlanDependenciesType] = Field(
		None,
		alias="dependencies",
		title=(
    "The required criteria to execute the test plan - e.g. preconditions, "
    "previous tests"
    ),
		description=(
    "The required criteria to execute the test plan - e.g. preconditions, "
    "previous tests..."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    description: fhirtypes.Markdown = Field(
		None,
		alias="description",
		title="Description",
		description="Description of the test plan.",
        # if property is element of this resource.
        element_property=True,
	)
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_description",
        title="Extension field for ``description``."
    )
	
    exitCriteria: fhirtypes.Markdown = Field(
		None,
		alias="exitCriteria",
		title=(
    "The threshold or criteria for the test plan to be considered "
    "successfully executed - narrative"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    exitCriteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_exitCriteria",
        title="Extension field for ``exitCriteria``."
    )
	
    identifier: typing.List[fhirtypes.IdentifierType] = Field(
		None,
		alias="identifier",
		title="Business identifier",
		description="Business identifier for the Test Plan.",
        # if property is element of this resource.
        element_property=True,
	)
	
    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
		None,
		alias="jurisdiction",
		title="Jurisdiction",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    name: typing.List[typing.Optional[fhirtypes.String]] = Field(
		None,
		alias="name",
		title="Name",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    name__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None,
        alias="_name",
        title="Extension field for ``name``."
    )
	
    publisher: typing.List[typing.Optional[fhirtypes.String]] = Field(
		None,
		alias="publisher",
		title="Publisher",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    publisher__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None,
        alias="_publisher",
        title="Extension field for ``publisher``."
    )
	
    purpose: fhirtypes.Markdown = Field(
		None,
		alias="purpose",
		title="Purpose",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_purpose",
        title="Extension field for ``purpose``."
    )
	
    scope: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="scope",
		title=(
    "What is being tested with this Test Plan - a conformance resource, or "
    "narrative criteria, or an external reference"
    ),
		description=(
    "What is being tested with this Test Plan - a conformance resource, or "
    "narrative criteria, or an external reference..."
    ),
        # if property is element of this resource.
        element_property=True,
	)
	
    status: typing.List[fhirtypes.Code] = Field(
		None,
		alias="status",
		title="draft | active | retired | unknown",
		description="Status.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
		enum_values=["draft", "active", "retired", "unknown"],
	)
    status__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None,
        alias="_status",
        title="Extension field for ``status``."
    )
	
    testCase: typing.List[fhirtypes.TestPlanTestCaseType] = Field(
		None,
		alias="testCase",
		title="The test cases that are part of this plan",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    testTools: fhirtypes.Markdown = Field(
		None,
		alias="testTools",
		title=(
    "A description of test tools to be used in the test plan - narrative "
    "for now"
    ),
		description="A description of test tools to be used in the test plan.",
        # if property is element of this resource.
        element_property=True,
	)
    testTools__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_testTools",
        title="Extension field for ``testTools``."
    )
	
    title: typing.List[typing.Optional[fhirtypes.String]] = Field(
		None,
		alias="title",
		title="Human-readable title",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    title__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None,
        alias="_title",
        title="Extension field for ``title``."
    )
	
    url: fhirtypes.Uri = Field(
		None,
		alias="url",
		title="Canonical identifier URL",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_url",
        title="Extension field for ``url``."
    )
	
    version: typing.List[typing.Optional[fhirtypes.String]] = Field(
		None,
		alias="version",
		title="Version",
		description="Version of the test plan.",
        # if property is element of this resource.
        element_property=True,
	)
    version__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None,
        alias="_version",
        title="Extension field for ``version``."
    )
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlan`` according specification,
        with preserving original sequence order.
        """
        return ["id", "meta", "implicitRules", "language", "text", "contained", "extension", "modifierExtension", "url", "identifier", "version", "name", "title", "status", "date", "publisher", "contact", "description", "jurisdiction", "purpose", "copyright", "category", "scope", "testTools", "dependencies", "exitCriteria", "testCase"]



from . import backboneelement

class TestPlanDependencies(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The required criteria to execute the test plan - e.g. preconditions,
    previous tests.
    The required criteria to execute the test plan - e.g. preconditions,
    previous tests...
    """
    resource_type = Field("TestPlanDependencies", const=True)
	
    description: fhirtypes.Markdown = Field(
		None,
		alias="description",
		title="Description of the criteria",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_description",
        title="Extension field for ``description``."
    )
	
    predecessor: fhirtypes.ReferenceType = Field(
		None,
		alias="predecessor",
		title="Link to predecessor test plans",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanDependencies`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "description", "predecessor"]



class TestPlanTestCase(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The test cases that are part of this plan.
    """
    resource_type = Field("TestPlanTestCase", const=True)
	
    assertions: typing.List[fhirtypes.TestPlanTestCaseAssertionsType] = Field(
		None,
		alias="assertions",
		title="The test assertions",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    dependencies: typing.List[fhirtypes.TestPlanTestCaseDependenciesType] = Field(
		None,
		alias="dependencies",
		title=(
    "The required criteria to execute the test case - e.g. preconditions, "
    "previous tests"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    scope: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="scope",
		title="Specific test scope for one test case",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    sequence: fhirtypes.Integer = Field(
		None,
		alias="sequence",
		title="Sequence of testing",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_sequence",
        title="Extension field for ``sequence``."
    )
	
    testData: typing.List[fhirtypes.TestPlanTestCaseTestDataType] = Field(
		None,
		alias="testData",
		title="The test data used in the test case",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    testRun: typing.List[fhirtypes.ReferenceType] = Field(
		None,
		alias="testRun",
		title="The actual test to be executed",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCase`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "sequence", "scope", "dependencies", "testRun", "testData", "assertions"]



class TestPlanTestCaseAssertions(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The test assertions.
    """
    resource_type = Field("TestPlanTestCaseAssertions", const=True)
	
    object: typing.List[fhirtypes.CodeableReferenceType] = Field(
		None,
		alias="object",
		title="The focus or object of the assertion",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    result: typing.List[fhirtypes.CodeableReferenceType] = Field(
		None,
		alias="result",
		title="The test assertions",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    type: typing.List[fhirtypes.CodeableConceptType] = Field(
		None,
		alias="type",
		title="The test assertion type",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCaseAssertions`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "object", "result"]



class TestPlanTestCaseDependencies(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The required criteria to execute the test case - e.g. preconditions,
    previous tests.
    """
    resource_type = Field("TestPlanTestCaseDependencies", const=True)
	
    description: fhirtypes.Markdown = Field(
		None,
		alias="description",
		title="Description of the criteria",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_description",
        title="Extension field for ``description``."
    )
	
    predecessor: fhirtypes.ReferenceType = Field(
		None,
		alias="predecessor",
		title="Link to predecessor test plans",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCaseDependencies`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "description", "predecessor"]



class TestPlanTestCaseTestData(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The test data used in the test case.
    """
    resource_type = Field("TestPlanTestCaseTestData", const=True)
	
    content: fhirtypes.ReferenceType = Field(
		None,
		alias="content",
		title="The actual test resources when they exist",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    sourceReference: fhirtypes.ReferenceType = Field(
		None,
		alias="sourceReference",
		title=(
    "Pointer to a definition of test resources - narrative or structured "
    "e.g. synthetic data generation, etc"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
		one_of_many="source",
		one_of_many_required=False,
	)
	
    sourceString: fhirtypes.String = Field(
		None,
		alias="sourceString",
		title=(
    "Pointer to a definition of test resources - narrative or structured "
    "e.g. synthetic data generation, etc"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
		one_of_many="source",
		one_of_many_required=False,
	)
    sourceString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_sourceString",
        title="Extension field for ``sourceString``."
    )
	
    type: fhirtypes.CodingType = Field(
		...,
		alias="type",
		title="The type of test data description, e.g. 'synthea'",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCaseTestData`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "content", "sourceString", "sourceReference"]


    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2582(
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
			"source": [
			    "sourceReference",
			    "sourceString"]}
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


from . import reference

class TestPlanTestCaseTestRun(reference.Reference):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual test to be executed.
    """
    resource_type = Field("TestPlanTestCaseTestRun", const=True)
	
    narrative: fhirtypes.Markdown = Field(
		None,
		alias="narrative",
		title="The narrative description of the tests",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    narrative__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_narrative",
        title="Extension field for ``narrative``."
    )
	
    script: fhirtypes.TestPlanTestCaseTestRunScriptType = Field(
		None,
		alias="script",
		title=(
    "The test cases in a structured language e.g. gherkin, Postman, or FHIR"
    " TestScript"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCaseTestRun`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "reference", "type", "identifier", "display", "narrative", "script"]



class TestPlanTestCaseTestRunScript(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The test cases in a structured language e.g. gherkin, Postman, or FHIR
    TestScript.
    """
    resource_type = Field("TestPlanTestCaseTestRunScript", const=True)
	
    language: fhirtypes.CodeableConceptType = Field(
		None,
		alias="language",
		title="The language for the test cases e.g. 'gherkin', 'testscript'",
		description=None,
        # if property is element of this resource.
        element_property=True,
	)
	
    sourceReference: fhirtypes.ReferenceType = Field(
		None,
		alias="sourceReference",
		title=(
    "The actual content of the cases - references to TestScripts or "
    "externally defined content"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
		one_of_many="source",
		one_of_many_required=False,
	)
	
    sourceString: fhirtypes.String = Field(
		None,
		alias="sourceString",
		title=(
    "The actual content of the cases - references to TestScripts or "
    "externally defined content"
    ),
		description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
		one_of_many="source",
		one_of_many_required=False,
	)
    sourceString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_sourceString",
        title="Extension field for ``sourceString``."
    )
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCaseTestRunScript`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "sourceString", "sourceReference"]


    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3161(
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
			"source": [
			    "sourceReference",
			    "sourceString"]}
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
