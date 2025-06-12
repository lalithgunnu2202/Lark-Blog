from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name
    
class Author(models.Model):
    author = models.CharField(max_length=50)
    def __str__(self):
        return self.author

class blog_data(models.Model):
    title = models.CharField(max_length=150)
    disc = models.TextField()
    img_url = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ForeignKey(Tag,default=1, on_delete=models.CASCADE)
    author = models.ForeignKey("Author",default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
