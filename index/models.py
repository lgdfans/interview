from django.db import models


# Create your models here.
class RankingList(models.Model):
    cid = models.AutoField(primary_key=True, verbose_name='序号')
    cname = models.CharField(max_length=30, verbose_name='姓名', null=False)
    cscore = models.IntegerField(default=0)

    def __str__(self):
        return self.cname