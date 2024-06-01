from django.db import models
import uuid

class Mymodel(models.Model):
    char_field = models.CharField(max_length=100, default='Anne')
    time_field = models.TimeField()
    email_field = models.EmailField()
    text_field = models.TextField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    float_field = models.FloatField()
    integer_field = models.IntegerField()
    positive_big_integer_field = models.PositiveBigIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    duration_field = models.DurationField()
    url_field = models.URLField()
    boolean_field = models.BooleanField(default=True)
    positive_small_integer_field = models.PositiveSmallIntegerField()
    small_integer_field = models.SmallIntegerField()
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug_field = models.SlugField()
