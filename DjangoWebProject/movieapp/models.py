from django.db import models

# Create your models here.

class Movie(models.Model):
    """Movie model for movieapp"""
    title = models.CharField(u'电影名',max_length=50)
    img = models.CharField(u'电影海报',max_length=100)
    filename = models.CharField(u'电影文件名',max_length=50)
    typefile = models.CharField(u'所属类别',max_length=50)
    timelong = models.IntegerField(u'电影时长')
    filelong = models.IntegerField(u'电影大小')
    filehd = models.CharField(u'高清类别',max_length=10)
    description =models.TextField(u'电影简介')
    director = models.CharField(u'导演',max_length=10)
    actors = models.TextField(u'主要演员')
    language = models.CharField(u'电影语言',max_length=10)
    issrt = models.CharField(u'是否字幕',max_length=10)
    startyear = models.CharField(u'上映年份',max_length=10)
    star = models.IntegerField(u'豆瓣评分')
    pub_date = models.DateTimeField(u'记录时间',auto_now_add=True)

    def __unicode__(self):
        return self.title
