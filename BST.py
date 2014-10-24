
class Node:
    def __init__(self, key_val=0):
        self.right=None
        self.left=None
        self.parent=None
        self.key=key_val



def insert(tree, k):
##    def __init__(self):
##        self.root=None
    checker=Node()
    if k<tree.key:
        if tree.left!=None:
            insert(tree.left, k)
            print "here 1"
        else:
            tree.left=Node(k)
            tree.left.parent=tree
            checker=tree.left
            
            print "here 2"
            print checker.key
            print checker.left
            print checker.right
    else:
        if tree.right!=None:
            insert(tree.right, k)
            print "here 3"
        else:
            tree.right=Node(k)
            tree.right.parent=tree
            checker=tree.right
            print "here 4"
            print checker.key
            print checker.left
            print checker.right
        

def max_val(tree):
    node=tree
##    val=tree.key
    while node.right!=None:
        node=node.right
        val=node.key
    return val
def find_val(tree, k):
    node=tree
    while node!=None and k!=node.key:
        if k<node.key:
            node=node.left
        else:
            node=node.right
    return node.parent.key
            
    

root=Node(2)

values=[3,1,2,4,3,8,3,6,7]

for i in range(len(values)):
    insert(root, values[i])

print find_val(root, 3)


            
            
  
                    
            
        
