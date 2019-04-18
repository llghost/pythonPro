from .model import db
from .model import Graph,Vertex,Edge
from .model import Pipeline,Track

def transctional(fn):
    def wraper(*args,**kwargs):
        ret=fn(*args,**kwargs)
        try:
            db.session.commit()
            return ret
        except:
            db.session.rollback()
    return wraper

@transctional
def create_graph(name,desc=None):
    g=Graph()
    g.name=name
    g.desc=desc
    db.session.add(g)
    return g

#添加顶点
@transctional
def add_vertex(g:Graph,name:str,input:None,script:None):
    v=Vertex()
    v.graph_id=g.id
    v.name=name
    v.input=input
    v.script=script
    db.session.add(v)
    return v

#添加边
@transctional
def add_edge(g:Graph,tail:Vertex,head:Vertex):
    e=Edge()
    e.graph_id=g.id
    e.tail=tail.id
    e.head=head.id
    print("222222222222222222",e)
    db.session.add(e)
    return e

#添加边
@transctional
def del_Vertex(id):
    query=db.session.query(Vertex).filter(Vertex.id==id)
    v=query.first()
    if v:
            db.session.query(Edge).filter((Edge.tail==v.id) |(Edge.head==v.id)).delete()
            query.delete()
    return v

