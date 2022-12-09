from django.db import models
from django.urls import reverse

STATUS = (
    ('OS', 'On Shelf'),
    ('SR', 'Started Reading'),
    ('FR', 'Finished Reading')
)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

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

# class Meta:
#     ordering = ['-date']