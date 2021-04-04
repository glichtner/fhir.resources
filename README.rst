=======================================
FHIR® Resources (Release R5 Preview #3)
=======================================

.. image:: https://www.hl7.org/fhir/assets/images/fhir-logo-www.png
        :target: https://www.hl7.org/implement/standards/product_brief.cfm?product_id=449
        :alt: HL7® FHIR®

Powered by pydantic_, all `FHIR Resources <https://build.fhir.org/resourcelist.html>`_ are available as python class with built-in
data validation, faster in performance and optionally ``orjson`` support has been included as a performance booster! Written in modern python.

* Easy to construct, easy to extended validation, easy to export.
* By inheriting behaviour from pydantic_, compatible with `ORM <https://en.wikipedia.org/wiki/Object-relational_mapping>`_.
* Full support of FHIR® Extensibility for Primitive Data Types are available.
* Preview release of the next FHIR version.
* Free software: BSD license

Package Origin
--------------
Forked from https://github.com/nazrulworld/fhir.resources, recreated to only include FHIR Release R5 Preview #3 resources.


FHIR® Version Info
------------------

FHIR® (Release R5, version 4.5.0) - https://build.fhir.org



Installation
------------

Install from github:

.. code-block:: shell

    $ pip install git+https://github.com/glichtner/fhir.resources.git


FHIR class creation
-------------------
The classes in this package were created using the fhir-parser_ package, cloned from https://github.com/nazrulworld/fhir-parser. To create the classes yourself, clone fhir-parser_ and run generate.py:

.. code-block:: shell

    $ git clone https://github.com/glichtner/fhir-parser.git
    $ cd fhir-parser
    $ ./generate.py


Usages
------

**Example: 1**: Construct Resource Model object


.. code-block:: python


    from fhir.resources.organization import Organization
    from fhir.resources.address import Address

    data = {
        "id": "f001",
        "active": True,
        "name": "Acme Corporation",
        "address": [{"country": "Switzerland"}]
    }
    org = Organization(**data)
    org.resource_type == "Organization"
    # True

    isinstance(org.address[0], Address)
    # True

    org.address[0].country == "Switzerland"
    # True

    org.dict()['active'] is True
    # True

**Example: 2**: Resource object created from json string

.. code-block:: python

    from fhir.resources.organization import Organization
    from fhir.resources.address import Address

    json_str = '''{"resourceType": "Organization",
        "id": "f001",
        "active": True,
        "name": "Acme Corporation",
        "address": [{"country": "Switzerland"}]
    }'''

    org = Organization.parse_raw(json_str)
    isinstance(org.address[0], Address)
    # True

    org.address[0].country == "Switzerland"
    # True

    org.dict()['active'] is True
    # True


**Example: 3**: Resource object created from json object(py dict)

.. code-block:: python

    from fhir.resources.patient import Patient
    from fhir.resources.humanname import HumanName
    from datetime import date

    json_obj = {"resourceType": "Patient",
        "id": "p001",
        "active": True,
        "name": [
            {"text": "Adam Smith"}
         ],
        "birthDate": "1985-06-12"
    }

    pat = Patient.parse_obj(json_obj)
    isinstance(pat.name[0], HumanName)
    # True

    org.birthDate == date(year=1985, month=6, day=12)
    # True

    org.active is True
    # True



**Example: 4**: Construct Resource object from json file

.. code-block:: python

    from fhir.resources.patient import Patient
    import os
    import pathlib

    filename = pathlib.Path("foo/bar.json")
    pat = Patient.parse_file(filename)
    pat.resource_type == "Patient"
    # True


**Example: 5**: Construct resource object in python way

.. code-block:: python

    from fhir.resources.organization import Organization
    from fhir.resources.address import Address

    json_obj = {"resourceType": "Organization",
        "id": "f001",
        "active": True,
        "name": "Acme Corporation",
        "address": [{"country": "Switzerland"}]
    }

    org = Organization.construct()
    org.id = "f001"
    org.active = True
    org.name = "Acme Corporation"
    org.address = list()
    address = Address.construct()
    address.country = "Switzerland"
    org.address.append(address)
    org.dict() == json_obj
    # True


.. note::
    Please note that due to the way the validation works, you will run into issues if you are using ``construct()`` to create
    resources that have more than one mandatory field. See `this comment in issue#56 <https://github.com/nazrulworld/fhir.resources/issues/56#issuecomment-784520234>`_ for details.

**Example: 6**: Using Resource Factory Function

.. code-block:: python

    from fhir.resources import construct_fhir_element

    json_dict = {"resourceType": "Organization",
        "id": "mmanu",
        "active": True,
        "name": "Acme Corporation",
        "address": [{"country": "Switzerland"}]
    }
    org = construct_fhir_element('Organization', json_dict)
    org.address[0].country == "Switzerland"
    # True

    org.dict()['active'] is True
    # True


**Example: 7**: Auto validation while providing wrong datatype

.. code-block:: python

    try:
        org = Organization({"id": "fmk", "address": ["i am wrong type"]})
        raise AssertionError("Code should not come here")
    except ValueError:
        pass


More Information
----------------
For more information and usages, please visit the original repository of the package: https://github.com/nazrulworld/fhir.resources


Credits
-------
This repository just applied the code from nazrulworld_ to create python classes from the FHIR Release R5 Preview#3 build.

All FHIR® Resources (python classes) are generated using fhir-parser_ which is forked from https://github.com/smart-on-fhir/fhir-parser.git.

.. _`nazrulworld`: https://github.com/nazrulworld/
.. _`fhir-parser`: https://github.com/glichtner/fhir-parser
.. _`pydantic`: https://pydantic-docs.helpmanual.io/
.. _`orjson`: <https://pypi.org/project/orjson/>

© Copyright HL7® logo, FHIR® logo and the flaming fire are registered trademarks
owned by `Health Level Seven International <https://www.hl7.org/legal/trademarks.cfm?ref=https://pypi.org/project/fhir-resources/>`_

.. role:: strike
    :class: strike
.. role:: raw-html(raw)
    :format: html
