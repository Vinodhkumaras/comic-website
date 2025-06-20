from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField()

    def __str__(self):
        return self.name

class Comic(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='comic/')
    file = models.FileField(upload_to='comicfiles/')    
    price = models.PositiveIntegerField(default=0)
    # desc = models.TextField(max_length=500, null = True)

    def __str__(self):
        return f"{self.title}: by {self.author.name}"


class ComicPage(models.Model):
    comic = models.ForeignKey(Comic, related_name='pages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comics/pages/')
    page_number = models.PositiveIntegerField()

    class Meta:
        ordering = ['page_number']

    def __str__(self):
        return f"{self.comic.title} - Page {self.page_number}"