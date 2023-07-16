from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.caption

class Author(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Post(models.Model):
    slug = models.SlugField(unique = True , db_index = True)
    image_name = models.CharField(max_length = 50)
    date = models.DateField(auto_now = True)
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, related_name = "post", null = True)
    title = models.CharField(null = True, blank = True, max_length = 256)
    excerpt = models.CharField(null = True, blank = True, max_length = 100)
    content = models.TextField(validators = [MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title