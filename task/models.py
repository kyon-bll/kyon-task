from django.db import models

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey('auth.user')
    title = models.CharField(max_length=100)
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    done_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
