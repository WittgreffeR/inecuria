from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    name: str
    body: str
    updated_at: datetime
