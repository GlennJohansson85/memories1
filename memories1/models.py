from django.db import models
from profiles.models import Profile


#________________________________________________________________________________POSTCATEGORY
#________________________________________________________________________________POST
class Post(models.Model):
    title           = models.CharField(max_length=255)
    content         = models.TextField()
    image           = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_on      = models.DateTimeField(auto_now_add=True)
    last_modified   = models.DateTimeField(auto_now=True)
    user            = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
