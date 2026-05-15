from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Категории'

class Extension(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    version = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    file = models.FileField(upload_to='extensions/', blank=True, null=True)
    icon = models.URLField(default='https://via.placeholder.com/128')
    
    download_count = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def increment_downloads(self):
        self.download_count += 1
        self.save()

class Review(models.Model):
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.extension.name}'
