from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField()

    def __str__(self):
        return self.name

class Comic(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='comic/')
    file = models.FileField(upload_to='comicfiles/')    

    def __str__(self):
        return f"{self.title}: by {self.author.name}"
