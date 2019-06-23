from django.db import models

# Create your models here.

class Article (models.Model):
    """A Article model for blog."""
    title= models.CharField(u"标题",max_length=50)
    body=models.CharField(u"内容",max_length=200)
    pub_date=models.DateTimeField('发布时间')

    def __str__(self):
        """return a string repersentation for Article."""
        return self.title
