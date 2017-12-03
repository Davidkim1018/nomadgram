from django.db import models
from nomadgram.users import models as user_models

# Create your models here.

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampedModel):
    '''image model'''
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User,null=True)

class Comment(TimeStampedModel):
    '''comment model'''
    message = models.TextField()
    creator = models.ForeignKey(user_models.User,null=True)
    image = models.ForeignKey(Image,null=True)

class Like(TimeStampedModel):
    '''like model'''
    creator = models.ForeignKey(user_models.User,null=True)
    image = models.ForeignKey(Image, null=True)