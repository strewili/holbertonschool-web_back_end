#!/usr/bin/env python3
"""Update the topics of a school document."""


def update_topics(mongo_collection, name, topics):
    """Replace the topics of every school matching the given name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
