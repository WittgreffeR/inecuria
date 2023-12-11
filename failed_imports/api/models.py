from django.db import models

from failed_imports.core.models import BaseModel


class FailedImport(BaseModel):
    data_id = models.TextField()
    name = models.TextField()
    data_type = models.TextField()
    reason = models.TextField(null=True, blank=True)
    airtable_id = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ("data_id", "reason")
