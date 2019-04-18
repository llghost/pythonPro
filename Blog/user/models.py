from django.db import models

# Create your models here.
#python manage.py makemigrations  生成迁移文件
# python manage.py migrate 执行迁移 生成数据库表

class User(models.Model):
    class Meta:
        db_table='user' #数据库表
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=48,null=False)
    email=models.CharField(max_length=64,null=False,unique=True)
    password=models.CharField(max_length=128,null=False)

    def __repr__(self):
        return 'name:{} email:{}'.format(self.name,self.email)

    __str__=__repr__