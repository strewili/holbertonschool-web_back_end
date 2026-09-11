# NoSQL

An introduction to MongoDB: querying from the Mongo shell and from Python
with PyMongo.

## Requirements

- Ubuntu 20.04 LTS, MongoDB 4.4, `python3` (3.9), PyMongo 4.8.0
- Mongo shell scripts start with a comment: `// my comment`
- Python scripts start with `#!/usr/bin/env python3`, follow `pycodestyle`
  2.5.*, and document every module and function
- All files end with a new line

## Mongo shell scripts

| File | Description |
| --- | --- |
| `0-list_databases` | Lists all databases |
| `1-use_or_create_database` | Creates or uses `my_db` |
| `2-insert` | Inserts a document in `school` |
| `3-all` | Lists all documents in `school` |
| `4-match` | Lists documents matching `name="Holberton school"` |
| `5-count` | Counts the documents in `school` |
| `6-update` | Adds the `address` attribute to matching documents |
| `7-delete` | Deletes documents matching `name="Holberton school"` |

## Python scripts

| File | Description |
| --- | --- |
| `8-all.py` | `list_all(mongo_collection)` — all documents, or `[]` |
| `9-insert_school.py` | `insert_school(mongo_collection, **kwargs)` — returns the new `_id` |
| `10-update_topics.py` | `update_topics(mongo_collection, name, topics)` |
| `11-schools_by_topic.py` | `schools_by_topic(mongo_collection, topic)` |
| `12-log_stats.py` | Stats about Nginx logs in the `logs.nginx` collection |

## Usage

```
cat 0-list_databases | mongo
echo 'db.school.find()' | mongo my_db
./12-log_stats.py
```
