from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class FailedImport:
    id: str
    name: str
    data_type: str
    reason: Optional[str]
    airtable_id: Optional[str] = None
    updated_at: Optional[datetime] = None
    url: Optional[str] = None
