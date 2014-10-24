class list_node:
    def __init__(self, k):
        self.key=k
        self.front=None
        self.back=None
        self.color='W'
        self.distance=None
        self.pred=None
        self.A=[]

        

class Graph:
    def __init__(self, node_key):
        self.node1=list_node(node_key)
        self.adjlist={}
        self.adjlist[node_key]=self.node1
        
##def add_node(adj_list, node, loc):
##
##    while True:
##        if adj_list[loc].back==None:
##            adj_list[loc].back=list_node(node)
##        else:
##            add_node(adj_list, node,loc)
##            break

        
def to_back(node, k):
    
    if node.back!=None:
        to_back(node.back, k)
        
    else:
        node.back=list_node(k)
        node.A.append(k)
            
         

def add_end(Graph, node, pairs):
    
    node1=list_node(node)
    Graph.adjlist[node]=node1
    for i in range(len(pairs)):
        to_back(Graph.adjlist[node], pairs[i])
    for i in range(len(pairs)):
        to_back(Graph.adjlist[pairs[i]], node)
        

        
def BFS(Graph, node):
    Graph.adjlist[node].color='G'
    Graph.adjlist[node].distance=0
    dist=0
    Que=[]
    Que.append(Graph.adjlist[node])

    while len(Que)!=0:
        u=Que.pop(0)
        
        for i in range(len(u.A)):
            if Graph.adjlist[u.A[i]].color=='W':
                Graph.adjlist[u.A[i]].color='G'
                Graph.adjlist[u.A[i]].distance=u.distance+1
                Graph.adjlist[u.A[i]].pred=u
                Que.append(Graph.adjlist[u.A[i]])
        Graph.adjlist[u.key].color='B'
            
            
            
    

    
    
    




test=Graph(2)
pairs=[2]
pairs1=[5]
add_end(test, 5, pairs)
add_end(test, 3, pairs1)

print test.adjlist[2].key
print test.adjlist[2].back.key
print test.adjlist
print test.adjlist[2].A
print test.adjlist[5].A
print test.adjlist[3].A

BFS(test, 2)

print test.adjlist[5].color



