from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=200)
    quota = models.PositiveIntegerField(
        default=0, help_text='The limit on the number of students. If is zero is unlimited')

    # Stats
    enrolled_students = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name