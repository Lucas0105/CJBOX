from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

def user_image_path(instance, filename):
    return f'images/{instance.username}/{filename}'

# Create your models here.
class User(AbstractUser):
    friends = models.ManyToManyField('self', symmetrical=False, related_name='followed')
    nickname = models.CharField(max_length=50, unique=True)
    intro = models.TextField(null=True, default='')
    my_image = models.ImageField(blank=True, upload_to=user_image_path)
    my_image_thumbnail = ImageSpecField(
        source = 'my_image',
        processors = [Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 80},
    )

