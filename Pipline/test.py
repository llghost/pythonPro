from pipline.service import Graph,Edge,Vertex
from pipline.service import create_graph,add_vertex,add_edge
import  json

def test_create_dag():
    try:
        g=create_graph('test1')
        input={
            "ip":{
                'type':'str',
                'required':True,
                'default':'192.168.0.100'
            }
        }

        script={
            'script':'echo "test1.A"\nping{ip}',
            'next':'B'
        }

        a = add_vertex(g, 'A', json.dumps(input),json.dumps(script))
        b=add_vertex(g,'B',None,'echo B')
        c=add_vertex(g,'C',None,'echo C')
        d=add_vertex(g,'D',None,'echo D')

        ab=add_edge(g,a,b)
        ac=add_edge(g,a,c)
        cb=add_edge(g,c,b)
        bd=add_edge(g,b,d)

        #
        g=create_graph('test2')
        a = add_vertex(g, 'A', None, 'echo A')
        b = add_vertex(g, 'B', None, 'echo B')
        c = add_vertex(g, 'C', None, 'echo C')
        d = add_vertex(g, 'D', None, 'echo D')

        ba=add_edge(g,b,a)
        ac=add_edge(g,a,c)
        cb=add_edge(g,c,b)
        bd=add_edge(g,b,d)

        # 创建DAG
        g = create_graph('test3')
        a = add_vertex(g, 'A', None, 'echo A')
        b = add_vertex(g, 'B', None, 'echo B')
        c = add_vertex(g, 'C', None, 'echo C')
        d = add_vertex(g, 'D', None, 'echo D')

        ba = add_edge(g, b, a)
        ac = add_edge(g, a, c)
        bc = add_edge(g, b, c)
        bd = add_edge(g, b, d)

        # 创建DAG
        g = create_graph('test4')
        a = add_vertex(g, 'A', None, 'echo A')
        b = add_vertex(g, 'B', None, 'echo B')
        c = add_vertex(g, 'C', None, 'echo C')
        d = add_vertex(g, 'D', None, 'echo D')

        ab = add_edge(g, a, b)
        ac = add_edge(g, a, c)
        cb = add_edge(g, c, b)
        db = add_edge(g, d, b)
    except Exception as e:
        print(e)

test_create_dag()