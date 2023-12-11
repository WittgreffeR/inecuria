import factory

from failed_imports.api.values import FailedImport


class FailedImportFactory(factory.Factory):
    class Meta:
        model = FailedImport

    id = factory.Faker("word")
    name = factory.Faker("word")
    data_type = factory.Faker("word")
    reason = factory.Faker("word")
    updated_at = factory.Faker("date_time")
