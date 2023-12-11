from django.db import models

from inecuria.core.models import BaseModel


class Article(BaseModel):
    name = models.TextField()
    body = models.TextField()
