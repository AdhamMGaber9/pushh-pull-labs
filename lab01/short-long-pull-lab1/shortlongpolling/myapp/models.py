from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    class Meta:
        app_label = 'myapp'