from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag

class BaseMediaModel(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to="original/")
    thumbnail = models.ImageField(upload_to="thumbnails/")
    scaled = models.ImageField(upload_to="scaled/")
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)

class Photo(models.Model):
    pass

class Video(models.Model):
    pass

class BaseModel(models.Model):
    name = models.CharField(verbose_name="name", max_length=200, blank=False, null=False)
    description = models.TextField(verbose_name="description", blank=False, null=False)
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)

    class Meta:
        abstract = True

class BaseContentModel(BaseModel):
    videos = models.ManyToManyField('Video', related_name="%(app_label)s_%(class)s_related")
    photos = models.ManyToManyField('Photo', related_name="%(app_label)s_%(class)s_related")

    class Meta:
        abstract = True

class BodyPart(BaseModel):
    pass

class Treatment(BaseModel):
    pass

class Exercise(BaseModel):
    pass

class Injury(BaseModel):
    x_axis = models.IntegerField(verbose_name="x-axis position", default=0,blank=False, null=False)
    y_axis = models.IntegerField(verbose_name="y-axis position", default=0,blank=False, null=False)
    exercises = models.ManyToManyField('Exercise', verbose_name="exercises", blank=True, null=True)
    treatments = models.ManyToManyField(Treatment, verbose_name="treatments", blank=True, null=True)
    body_part = models.ManyToManyField(BodyPart, verbose_name="body part affected", null=False, blank=False)
    recovery_time = models.CharField(verbose_name="total recovery time", max_length=50, null=True, blank=True)
