# Enterprise Data Patterns

Patterns for mapping domain objects to relational/document storage, alongside
the implementation examples in this directory.

| Pattern | File | Purpose |
|:---|:---|:---|
| Unit of Work | `unit_of_work.py` | track changes, commit atomically |
| Data Mapper | `data_mapper.py` | move data between objects and tables |
| Active Record | `active_record.py` | object wraps its own row |
| Identity Map | `identity_map.py` | one instance per row identity |
| Lazy Load | `lazy_load.py` | defer expensive loads |
| Data Access Object | `dao.py` | isolate persistence from domain |

Related: Repository (`../ddd_patterns/repository.py`), CQRS.
