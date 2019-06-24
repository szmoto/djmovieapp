from django.db import models

# Create your models here.

class Movie(models.Model):
    """Movie model for movieapp"""
    issrt_choice = (
        (0, '否'),
        (1, '是'),
    )
    language_choice = (
        (0, '国语'),
        (1, '外语'),
    )
    hd_choice = (
        (0, '1080P'),
        (1, '720P'),
        (2,'720P/1080P'),
    )

    title = models.CharField(u'电影名',max_length=50)
    img = models.CharField(u'电影海报',max_length=100)
    videopath = models.CharField(u'电影路径',max_length=200)
    filehd = models.IntegerField(u'高清类别',choices=hd_choice, default=0)
    description =models.TextField(u'电影简介')
    director = models.CharField(u'导演',max_length=10)
    actors = models.TextField(u'主要演员')
    language = models.IntegerField(u'电影语言',choices=language_choice, default=0)
    issrt = models.IntegerField(u'是否字幕',choices=issrt_choice, default=0)
    startyear = models.CharField(u'上映年份',max_length=10)
    star = models.IntegerField(u'豆瓣评分',default=0)
    xl720_id=models.IntegerField(u'迅雷ID',default=0)
    db_id=models.IntegerField(u'豆瓣ID',default=0)
    pub_date = models.DateTimeField(u'记录时间',auto_now_add=True)

    def __unicode__(self):
        return self.title
