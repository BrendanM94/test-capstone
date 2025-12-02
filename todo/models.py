from django.db import models
from django.contrib.auth.models import User   # ⬅ add this


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ⬅ add this line
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
