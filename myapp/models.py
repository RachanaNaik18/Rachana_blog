from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    Image = models.ImageField(upload_to='Images', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def get_Image_url(self):
        if self.Image and hasattr(self.Image, 'url'):
            return self.Image.url
        else:
            return "/static/logo_blog.png"
        
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=100, default="Anonumous")
    body = models.TextField()
    active = models.BooleanField(default=True)
    

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)

    
    