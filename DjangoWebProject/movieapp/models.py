# -*- coding: UTF-8 *-*

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
    type_choice =(
        (0,"动作片"),
        (1,"科幻片"),
        (2,"喜剧片"),
        (3,"恐怖片"),
        (4,"悬疑片"),
        (5,"剧情片"),
        (6,"动画片"),
        (7,"纪录片"),
        )
    area_choice =(
        (0,"中国/内地"),
        (1,"中国/香港"),
        (2,"美国"),
        (3,"欧洲"),
        (4,"日韩"),
        (5,"印度"),
        (6,"其他"),
        )

    title = models.CharField(u'电影名',max_length=50)
    img = models.CharField(u'电影海报',max_length=100)
    videopath = models.CharField(u'电影路径',max_length=200)
    filehd = models.IntegerField(u'高清类别',choices=hd_choice, default=0)
    description =models.TextField(u'电影简介')
    director = models.CharField(u'导演',max_length=10)
    actors = models.TextField(u'主要演员')
    mvtype = models.IntegerField(u'电影类型',choices=type_choice,default=0)
    mvarea = models.IntegerField(u'发行地区',choices=area_choice,default=0)
    language = models.IntegerField(u'电影语言',choices=language_choice, default=0)
    issrt = models.IntegerField(u'是否字幕',choices=issrt_choice, default=0)
    startyear = models.CharField(u'上映年份',max_length=10)
    star = models.IntegerField(u'豆瓣评分',default=0)
    xl720_id=models.IntegerField(u'迅雷ID',default=0)
    db_id=models.IntegerField(u'豆瓣ID',default=0)
    pub_date = models.DateTimeField(u'记录时间',auto_now_add=True)

    def __unicode__(self):
        return self.title
