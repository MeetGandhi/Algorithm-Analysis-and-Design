def printtree(lst):
    print (stringg(lst))
def stringg(lst):
    if lst==None:
        return ""
    t=list2tree(lst)
    return "\n"+"\n".join(buildstr(t)[0])
def list2tree(lst):
    nodes=[None for i in lst]
    root=Node(lst[0])
    nodes[0]=root
    i=1
    while i<len(lst):
        v=lst[i]
        if v!=None:
            pi=int((i+1)/2)-1
            pn=nodes[pi]
            cn=Node(v)
            if i%2:
                pn.left=cn
            else:
                pn.right=cn
            nodes[i]=cn
        i+=1
    return root
                
def buildstr(node):
    if node==None:
        return [],0,0,0
    set1=[]
    set2=[]
    nrw=gs=len(str(node.value))
    lb,lbw,lrstart,lrend=buildstr(node.left)
    rb,rbw,rrstart,rrend=buildstr(node.right)
    if lbw>0:
        lr=-int(-(lrstart+lrend)/2)+1
        set1.append(" "*(lr+1))
        set1.append("_"*(lbw-lr))
        set2.append(" "*lr+'/')
        set2.append(" "*(lbw-lr))
        nrs=lbw+1
        gs+=1
    else:
        nrs=0

    set1.append(str(node.value))
    set2.append(" "*nrw)

    if rbw>0:
        rr=int((rrstart+rrend)/2)
        set1.append("_"*rr)
        set1.append(" "*(rbw-rr+1))
        set2.append(" "*rr+"\\")
        set2.append(" "*(rbw-rr))
        gs+=1
    nre=nrs+nrw-1
    
    g=" "*gs
    nb=["".join(set1),"".join(set2)]
    for i in xrange(max(len(lb),len(rb))):
        lline=lb[i]if i<len(lb) else" "*lbw
        rline=rb[i]if i<len(rb) else" "*rbw
        nb.append(lline+g+rline)
    return nb, len(nb[0]),nrs,nre
        
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
        
class Node():
    def __init__(self,value,left=None,right=None,parent=None):
        self.value=value
        self.left=left
        self.right=right
        #self.root=self
        self.parent=parent
R=input("Enter the value of root in the Initial Tree:")
L=input("Enter the value of left child of the root in the Initial Tree:")
Ri=input("Enter the value of right child of the root in the Initial Tree:")
tree=Node(R, Node(L,None,None,R), Node(Ri,None,None,R),None)
#t.root=Node(1, Node(2,None,None,1), Node(3,None,None,1),None)
print ("Initial Tree:")
printtree([R,L,Ri])
while True:
    t=input("Enter the operation you want to perform:\nEnter 1 for Move\nEnter 2 for Add\nEnter 3 for Print\nEnter 4 for Exit\n")
    if t==1:
        f=raw_input("Enter the movement pattern,\nA movement pattern is a string with letters L, R, P, r where L=left, R=Right, P=Parent, r=root:")
        lst=list(f)
        for i in xrange(len(lst)):
            if lst[i]=="L":
                if tree.left==None:
                    print "Movement not possible"
                else:
                    t=tree
                    tree=tree.left
                    tree.parent=t
            elif lst[i]=="R":
                if tree.right==None:
                    print "Movement not possible"
                else:
                    t=tree
                    tree=tree.right
                    tree.parent=t
            elif lst[i]=="P":
                tree=tree.parent
            else:
                while tree.parent!=None:
                    tree=tree.parent
    if t==2:
        g=raw_input("Left(L) or Right(R):")
        if g=="L":
            if tree.left==None:
                t=tree
                y=input("Enter Value:")
                tree=tree.left
                tree=Node(y)
                #tree.value=y
                """tree.value=y
                tree.left=None
                tree.right=None"""
                tree.parent=t
                t.left=tree
            else:
                print("Cannot Add, Place not empty")
        if g=="R":
            if tree.right==None:
                t=tree
                y=input("Enter Value:")
                tree=tree.right
                tree=Node(y)
                """tree.value=y
                tree.left=None
                tree.right=None"""
                tree.parent=t
                t.right=tree
            else:
                print("Cannot Add, Place not empty")
    if t==3:
        q=Queue()
        while tree.parent!=None:
            tree=tree.parent
        lst=[]
        lst1=[]
        lst2=[]
        q.enqueue(tree)
        while q.size()!=0:
            m=q.dequeue()
            print m.value,
            if m.left!=None and m.right!=None:
                q.enqueue(m.left)
                q.enqueue(m.right)
                #lst1.append(m.left.value)
            if m.right==None and m.left!=None:
                q.enqueue(m.left)
                m.right=Node("")
                q.enqueue(m.right)
                #lst.append(0)
            #if m.right!=None:
                #q.enqueue(m.right)
                #lst2.append(m.right.value)
            if m.left==None and m.right!=None:
                m.left=Node("")
                q.enqueue(m.left)
                q.enqueue(m.right)
                #lst.append(0)
            lst.append(m.value)
        printtree(lst)
    if t==4:
        print("Thank You!")
        break

        
    
