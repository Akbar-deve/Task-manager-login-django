from django.db import models


class NUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username


class Todo(models.Model):

    STATUS_CHOICES = [
        ('todo', 'Todo'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
    ]


    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    due_date = models.DateTimeField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title