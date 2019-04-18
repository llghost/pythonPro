from sqlalchemy import Column,Integer,String,Text,ForeignKey,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from .util import signleton
from .config import URL,DATABASE_DEBUG
Base=declarative_base()

STATE_WAITING=0
STATE_RUNNING=1
STATE_SUCCEED=2
STATE_FAILED=3
STATE_FINISH=4

@signleton
class Database:
    def __init__(self,url,**kwargs):
        self._engine=create_engine(url,**kwargs)
        self._session=sessionmaker(bind=self._engine)()#调用返回session实例

    @property
    def session(self):
         return self._session

    @property
    def engine(self):
        return  self._engine
    #创建表
    def create_all(self):
         Base.metadata.create_all(self._engine)
    #删除表
    def drop_all(self):
         Base.metadata.drop_all(self._engine)

#模块加载一次 db也是单例的
db=Database(URL,echo=DATABASE_DEBUG)

#schema 定义
#图
class Graph(Base):
    __tablename__='graph'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(48),nullable=False,unique=True)
    desc=Column(Text,nullable=True)

    #经常从图查看所有顶点、边的信息
    vertexes=relationship('Vertex')
    edges=relationship('Edge')

#顶点表
class Vertex(Base):
    __tablename__="vertex"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(48),nullable=False)
    script=Column(Text,nullable=True)
    input=Column(Text,nullable=True)
    graph_id=Column(Integer,ForeignKey('graph.id'),nullable=False)

    graph=relationship('Graph')

    #从顶点查边
    tails=relationship('Edge',foreign_keys='Edge.tail')
    heads=relationship('Edge',foreign_keys='Edge.head')
    graph_id=Column(Integer,ForeignKey('graph.id'),nullable=False)



class Edge(Base):
    __tablename__="edge"
    id=Column(Integer,primary_key=True,autoincrement=True)
    tail=Column(Integer,ForeignKey('vertex.id'),nullable=False)
    head = Column(Integer, ForeignKey('vertex.id'),nullable=False)
    graph_id=Column(Integer,ForeignKey('graph.id'),nullable=False)

class Pipeline(Base):
    __tablename__="pipeline"
    id=Column(Integer,primary_key=True,autoincrement=True)
    graph_id=Column(Integer,ForeignKey('graph.id'),nullable=False)
    vertex_id = Column(Integer, ForeignKey('vertex.id'),nullable=False)
    state=Column(Integer,nullable=False,default=STATE_WAITING)

    vertex=relationship('Vertex')

class Track(Base):
    __tablename__="track"
    id=Column(Integer,primary_key=True,autoincrement=True)
    pipeline_id=Column(Integer,ForeignKey('pipeline.id'),nullable=False)
    vertex_id = Column(Integer, ForeignKey('vertex.id'),nullable=False)
    input = Column(Text, nullable=True)
    output = Column(Text, nullable=True) #任务输出
    state=Column(Integer,nullable=False,default=STATE_WAITING)

    vertex = relationship('Vertex')
    pipeline=relationship('Pipeline')
