from django.db import models

manageFlag = True


# Create your models here.
class DeviceInfo(models.Model):
    RESULT_CHOICES = {

        ('未测试', '未测试'),
        ('在线', '在线'),
        ('离线', '离线'),
    }

    name = models.CharField('设备名称', max_length=100, default='无')
    result = models.CharField('测试结果', max_length=100, choices=RESULT_CHOICES, default='未测试')

    sys_create_time = models.DateTimeField('创建时间', auto_now_add=True)
    sys_update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = manageFlag
        verbose_name = '设备表'
        verbose_name_plural = verbose_name
        db_table = 'device_info'
