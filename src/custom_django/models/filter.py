class SFilterOps:
    PRIMARY_KEY = ["exact", "in"]

    IDENTIFIER = ["exact", "in", "isnull"]
    RELATION = ["exact", "in", "isnull"]

    CHAR = ["exact", "in", "isnull"]
    STRING = ["exact", "iexact", "contains", "icontains", "isnull"]
    EXACT_STRING = ["exact"]

    BOOLEAN = ["exact", "isnull"]

    NUMBER = ["exact", "gt", "lt", "gte", "lte"]

    TIMESTAMP = ["exact", "gt", "lt", "gte", "lte"]
