from django.db import models
from django.urls import reverse
# from datetime import date

STATUS = (
    ('OS', 'On Shelf'),
    ('SR', 'Started Reading'),
    ('FR', 'Finished Reading')
)

class Bookmark(models.Model):
    colour = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bookmark_detail', kwargs={'pk': self.id})

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    bookmark = models.ManyToManyField(Bookmark)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Reading(models.Model):
    date = models.DateField('date started')
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=STATUS[0][0]
    )

book = models.ForeignKey(Book, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.get_status_display()} on {self.date}"

class Meta:
    ordering = ['-date']