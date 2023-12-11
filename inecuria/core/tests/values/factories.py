import factory


class BaseObjectFactory(factory.Factory):
    class Meta:
        abstract = True

    id = factory.Faker("uuid4")
    created_at = factory.Faker("date_time")
    updated_at = factory.Faker("date_time")
