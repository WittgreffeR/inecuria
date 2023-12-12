from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class PermissionLevel(Enum):
    PUBLIC = 1
    PRIVILEGED = 2
    ADMIN = 3


@dataclass
class Article:
    name: str
    body: str
    level: PermissionLevel
    updated_at: datetime
