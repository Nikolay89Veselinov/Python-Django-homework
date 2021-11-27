from django.urls import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from .validators import validate_max_instance


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def clean(self):
        validate_max_instance(self)

    def get_absolute_url(self):
        return reverse('categories:category_list')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


