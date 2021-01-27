from django.db import models

manageFlag = True


# Create your models here.
class Category(models.Model):
    """
    文章分类
    """

    name = models.CharField(verbose_name='文章类别', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        managed = manageFlag
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name
        db_table = 'category_info'


class Tag(models.Model):
    """
    文章标签
    """

    name = models.CharField(verbose_name='文章标签', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        managed = manageFlag
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name
        db_table = 'tag_info'


class Blog(models.Model):
    """
    博客设计
    """

    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='正文', default='')
    sys_create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    sys_update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    category = models.ForeignKey(Category, verbose_name='博客类别', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='博客标签')

    def __str__(self):
        return self.title

    class Meta:
        managed = manageFlag
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name
        db_table = 'blog_info'
