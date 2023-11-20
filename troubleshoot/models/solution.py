from django.db import models
from .issue import Issue


class Solution(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    description = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sulotion for {self.issue.title}"
