from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=255, default='some_default_value')
    user = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='related_users')

    def __str__(self): 
        return self.email
    
class Post(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ('-created','-updated')
    
    def __str__(self):
        return self.name
 