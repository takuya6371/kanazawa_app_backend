from django.db import models

# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()

    class Meta:
        ordering = ('created',)

class Schema_test(models.Model):
    schema_name = models.CharField(max_length=20)
    describe = models.TextField()
    term_of_use = models.TextField()

class Table_test(models.Model):
    schemaID = models.IntegerField()
    table_name = models.CharField(max_length=20)
    describe = models.TextField()