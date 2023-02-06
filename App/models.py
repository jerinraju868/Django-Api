from django.db import models

class TodoList(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

