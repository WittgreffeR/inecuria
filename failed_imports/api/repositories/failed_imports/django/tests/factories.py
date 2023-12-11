import factory

from failed_imports.api.models import FailedImport
from failed_imports.core.tests.models.factories import BaseModelFactory


class FailedImportFactory(BaseModelFactory):
    class Meta:
        model = FailedImport

    data_id = factory.Faker("word")
    name = factory.Faker("word")
    data_type = factory.Faker("word")
    reason = factory.Faker("word")
    airtable_id = factory.Faker("word")
