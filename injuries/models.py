from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tag


class BaseMediaModel(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)

    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        abstract = True


class Photo(BaseMediaModel):
    image = models.ImageField(upload_to="original/")
    thumbnail = models.ImageField(upload_to="thumbnails/")
    scaled = models.ImageField(upload_to="scaled/")

    def __unicode__(self):
        return "photo: {}, {} - {}".format(self.title, self.user, self.created_at)


class Video(BaseMediaModel):
    video_file = models.FileField(upload_to="videos/", null=True, blank=True)
    video_url = models.URLField(verbose_name="video URL", null=True, blank=True)

    def __unicode__(self):
        return "video: {}, {} - {}".format(self.title, self.user, self.created_at)


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
    is_accepted = models.BooleanField(default=True)
    x_axis = models.FloatField(verbose_name="x-axis position", default=0.0, blank=False, null=False)
    y_axis = models.FloatField(verbose_name="y-axis position", default=0.0, blank=False, null=False)
    exercises = models.TextField(verbose_name="exercises", blank=True, null=True)
    treatments = models.TextField(verbose_name="treatment", blank=True, null=True)
    recovery_time = models.TextField(verbose_name="total recovery time", null=True, blank=True)
    medication = models.TextField(verbose_name="suggested medication", null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = "Injury"
        verbose_name_plural = "Injuries"

    def __unicode__(self):
        return "{}, dodane {}.{}.{}".format(self.name, self.created_at.day, self.created_at.month, self.created_at.year)