def non_trivial_power_set(A):
    if len(A)==0:
        Set=[]
        Set.append(A)
        return Set
    elif len(A)==1:
        B=[[A[0]]]
        return B

    else:
        P=non_trivial_power_set([A[0]])
        Q=non_trivial_power_set(A[1:])
        R=P+Q
        S=[]
        for i in Q:
            i=i+P[0]
            S.append(i)
         
        return S+R
        
def power_set(A):
    B=non_trivial_power_set(A)
    B.append([])
    return B
    
    class list_node:
    def __init__(self, k):
        self.key=k
        self.front=None
        self.back=None
        self.color='W'
        self.distance=None
        self.pred=None
        self.A=[]
        self.stime=0
        self.ftime=0

        

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
    
##    if node.back!=None:
##        to_back(node.back, k)
##        
##    else:
##    node.back=list_node(k)
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
            
def DFS(Graph):
    time=0
    for l in Graph.adjlist:
        if Graph.adjlist[l].color=='W':
            DFS_Visit(Graph.adjlist[l], Graph.adjlist, time)

def DFS_Visit(Graphnode, adjlists, time):
    time=time+1
    Graphnode.color='G'
    Graphnode.stime=time
    for i in Graphnode.A:
        if adjlists[i].color=='W':
            adjlists[i].front=Graphnode
            DFS_Visit(adjlists[i], adjlists,time )
    Graphnode.color='B'
    Graphnode.ftime=time+1
    
        
    
    
test=Graph(2)
pairs=[2]
pairs1=[5]
pairs2=[3]
add_end(test, 5, [2])
add_end(test, 4, [5])
add_end(test,3, [2])

print test.adjlist[2].key
##print test.adjlist[2].back.key
print test.adjlist
print test.adjlist[2].A
print test.adjlist[5].A
print test.adjlist[3].A

#BFS(test, 2)
DFS(test)
print test.adjlist[3].color



print test.adjlist[2].ftime
print test.adjlist[5].stime
