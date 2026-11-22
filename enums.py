from enum import Enum


class TaskStatus(Enum):
    TODO = "TODO"
    DONE = "DONE"
    MIGRATED = "MIGRATED"
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"


class Signifier(Enum):
    NONE = ""
    PRIORITY = "*"
    INSPIRATION = "!"