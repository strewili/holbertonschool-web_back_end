#!/usr/bin/env python3
"""List all documents stored in a MongoDB collection."""


def list_all(mongo_collection):
    """Return every document of the collection, or an empty list."""
    return list(mongo_collection.find())
