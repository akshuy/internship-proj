from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    # content = models.TextField()
    content = RichTextUploadingField(default=" ")
    
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return 'Message from ' + self.title + ' by '+ self.author

class BlogComment(models.Model):
    sno =  models.AutoField(primary_key=True)
    comment = models.TextField()
    user    = models.ForeignKey(User, on_delete =models.CASCADE)
    post  = models.ForeignKey(Post, on_delete = models.CASCADE)
    parent  = models.ForeignKey('self', on_delete = models.CASCADE,null=True)
    timestange  = models.DateTimeField(default=now)  
    def __str__(self):
        return self.comment[0:13]+ '...'+'by '+ self.user.username  
    