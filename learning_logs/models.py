from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,blank=True)
    image=models.ImageField(upload_to='images/%Y/%m/%d/')
    description=models.TextField()
    created = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

class Entry(models.Model):
        topic = models.ForeignKey(Post, on_delete=models.CASCADE)
        text = models.CharField(max_length=250)
        date_added = models.DateTimeField(auto_now_add=True)

        class Meta:
            verbose_name_plural = 'Коментарии'

        def __str__(self):
            return f"{self.text[:20]}..."