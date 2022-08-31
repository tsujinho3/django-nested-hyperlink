import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True
        ordering = ["-created_date"]


class Publisher(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta(BaseModel.Meta):
        db_table = "publisher"


class Book(BaseModel):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(
        Publisher, related_name="book", on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=100, unique=True)

    class Meta(BaseModel.Meta):
        db_table = "book"
