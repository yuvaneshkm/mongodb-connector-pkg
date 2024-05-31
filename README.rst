MongoDB Connector Package
=========================

Overview
--------

**mdb_connect_pkg** is a Python package designed to simplify the process of connecting to and interacting with MongoDB databases. This package provides a streamlined API for performing CRUD (Create, Read, Update, Delete) operations, handling connections, and managing MongoDB collections with ease.

Features
--------

* Easy connection management to MongoDB instances
* Simple CRUD operations
* Handling of MongoDB collections

Directory Structure
-------------------

.. code-block:: text

    mongodb-connector-pkg/
    ├── .github/
    │   └── workflows/
    │       └── ci.yaml
    │       └── python-publish.yaml
    ├── src/
    │   └── mdb_connect_pkg/
    │       └── mongo_crud.py
    ├── tests/
    │   ├── unit/
    │   │   └── test_unit.py
    │   └── integration/
    │       └── test_integration.py
    ├── .gitignore
    ├── init_setup.sh
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── README.rst
    ├── requirements_dev.txt
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    ├── template.py
    └── tox.ini

How to Use This Package
-----------------------

Installation
~~~~~~~~~~~~

To install the package, use pip:

.. code-block:: bash

    pip install mdb-connect-pkg==1.1.1

Usage
~~~~~

Connecting to MongoDB
~~~~~~~~~~~~~~~~~~~~~

First, import the package and create a connection instance:

.. code-block:: python

    # Importing the package
    from mdb_connect_pkg import mongo_crud

    # Initialize the connector
    db_connection_url = 'mongodb://localhost:27017'
    database_name = 'mydatabase'
    collection_name = 'mycollection'
    mongo = mongo_crud.MongoDBConnection(db_connection_url, database_name, collection_name)

    # Creating the client and connect to the database
    mongo.create_mongo_client()
    mongo.database_()
    mongo.collection_()

CRUD Operations
~~~~~~~~~~~~~~~

Create
^^^^^^

To insert a single record into the collection:

.. code-block:: python

    mongo.single_insert({"name": "John Doe", "age": 30, "email": "johndoe@example.com"})

To insert a JSON file into the collection:

.. code-block:: python

    json_file_path = 'example.json'
    mongo.bulk_insert(json_file_path)

To insert a CSV file into the collection:

.. code-block:: python

    csv_file_path = 'example.csv'
    mongo.bulk_insert(csv_file_path)

Read
^^^^

To load the data from the MongoDB database to a pandas DataFrame:

.. code-block:: python

    df = mongo.load_data()
    df.head()

Update
^^^^^^

To update the records in the collection:

.. code-block:: python

    mongo.update_data({"name": "John Doe"},{"$set": {"age": 31}})

Delete
^^^^^^

To delete records in the collection:

.. code-block:: python

    mongo.delete_record({"name": "John Doe"})

To delete the entire collection:

.. code-block:: python

    mongo.drop_collection()

To delete the entire database:

.. code-block:: python

    mongo.drop_database()

Contributing
------------

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

License
-------

This project is licensed under the MIT License.

Contact
-------

For any questions or suggestions, please contact `yuvaneshkm05@gmail.com <mailto:yuvaneshkm05@gmail.com>`_

Connect
-------

Connect with me on `LinkedIn <https://www.linkedin.com/in/yuvaneshkm>`_