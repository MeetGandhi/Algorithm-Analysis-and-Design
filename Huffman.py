from itertools import groupby
from heapq import *
import Queue

f= [
    (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
    (12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'), 
    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'), 
    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
    (1.974, 'y'), (0.074, 'z') ]#Example taken from Internet
class Node(object):
    def __init__(o,l=None, r=None,root=None):
        o.left=l
        o.right=r
        o.root=root
    def children(o):
        return(o.left, o.right)
    def preorder(o, p=None):
        if p is None:
            p=[]
        if o.left is not None:
            if isinstance(o.left[1], Node):
                o.left[1].preorder(p+[0])
            else:
                print(o.left,p+[0])
        if o.right is not None:
            if isinstance(o.right[1], Node):
                o.right[1].preorder(p+[1])
            else:
                print(o.right,p+[1])

def huffman(d):
    q=Queue.PriorityQueue()
    for i in d:
        q.put(i)


    while q.qsize()>1:
        m,n=q.get(),q.get()
        node=Node(m,n)
        q.put((m[0]+n[0],node))
    return q.get()
dis=huffman(f)
print(dis[1].preorder())
