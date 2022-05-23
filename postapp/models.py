from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    shorttext = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    date = models.DateField(null=True)
    img = models.ImageField(null=True)

    @property
    def get_image(self):
        try:
            return self.img.url
        except:
            return ""

    def __str__(self):
        return self.title
