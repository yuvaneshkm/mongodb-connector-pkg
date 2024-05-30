# MongoDB connector package

## Overview
**mongodb_connector_pkg** is a Python package designed to simplify the process of connecting to and interacting with MongoDB databases. This package provides a streamlined API for performing CRUD (Create, Read, Update, Delete) operations, handling connections, and managing MongoDB collections with ease.

## Features
* Easy connection management to MongoDB instances
* Simple CRUD operations
* Handling of MongoDB collections

## Installation
To install the package, use pip:
```
pip install mdb_connect_pkg
```

## Usage
### Connecting to MongoDB
First, import the package and create a connection instance:
```
# Importing the package:
from mdb_connect_pkg import mongo_crud

# Initialize the connector:
db_connection_url = 'mongodb://localhost:27017'
database_name = 'mydatabase'
collection_name = 'mycollection'
mongo = mongo_crud.MongoDBConnection(db_connection_url, database_name, collection_name)

# Creating the client and connect to the database:
mongo.create_mongo_client()
mongo.database_()
mongo.collection_()
```