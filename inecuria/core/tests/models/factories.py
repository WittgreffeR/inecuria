import factory

from inecuria.core.models import BaseModel


class BaseModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseModel

    id = factory.Faker("uuid4")
    created_at = factory.Faker("date_time")
    updated_at = factory.Faker("date_time")
