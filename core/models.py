from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class InsecureUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # PLAIN TEXT (VULNERABLE)

    def __str__(self):
        return self.username
