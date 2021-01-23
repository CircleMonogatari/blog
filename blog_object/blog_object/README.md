blog_object


# Django
## 通用
### 创建项目
    python django startproject

### 添加app
    python manage.py startapp [appname]
    
### 启动
    python manage.py runserver 0.0.0.0:8000

## [视图](https://docs.djangoproject.com/zh-hans/2.2/ref/class-based-views/) 
### 通用视图


## Rest Fromwork
- GET（SELECT）：从服务器取出资源（一项或多项）。
- POST（CREATE）：在服务器新建一个资源。
- PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
- PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
- DELETE（DELETE）：从服务器删除资源。


## DB
### MYSQL 数据迁移

    命令行指定生成对应的数据文件
    python manage.py inspectdb > models.py
    python manage.py inspectdb --database=nld_pdc_admin > db_admin/models.py
    python manage.py inspectdb --database=nld_pdc_view > db_view/models.py


### 同步数据
    
    python manage.py makemigrations
    python manage.py migrate       
    
    如果更换数据库, 需要重新创建管理员账号


# Python 常用
## 项目依赖导入导出
    1.命令行键入： (将其放入工程文件中）
        pip freeze > requirements.txt

    2.通过以下命令安装相应包：
        pip install -r requirements.txt

## pycharm 进入django shell

    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_object.settings")
    
    import django
    django.setup()
    
    
## 权限问题

    权限表 （指所有的 url 路径， 一般包含get和 post请求）
    分组 （django自带， 可以自行创建）
    分组关联 （django自带， 需要提供修改分组功能）
    权限关联 （把权限和组关联起来， 需要自己创建）
    
    
### 
    接口:
    animal_info
    basic_data
    dict
    dict_item
    message_info
    plant_data_info
    plant_info
    replay_info
    scan_record
    system_config
    user_plus_info



