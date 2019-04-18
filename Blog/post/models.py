from django.db import models
from user.models import User

# Create your models here.
#博文管理
class Post(models.Model):
    class Meta:
        db_table='post'
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=256,null=False)
    postdate=models.DateTimeField(null=False)
    #作者对应User表
    author=models.ForeignKey(User)#指定外键 migrate 会生成author_id

    def __repr__(self):
        return "title:{} postdate:{} author:{}".format(self.title,self.postdate,self.author,self.content)
    __str__=__repr__

class Content(models.Model):
    class Meta:
        db_table='content'
    #没有主键 会自动生成一个主键
    post=models.OneToOneField(Post)#一对一 会有一个外键引用 post.id
    content=models.TextField(null=False)

    def __repr__(self):
        return "post:{} content:{}".format(self.post.id,self.content[:20])

    __str__ = __repr__