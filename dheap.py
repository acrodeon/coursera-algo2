##########################################################################
#                          Min D-ary Heap                                #
# Based  on http://www.cs.cmu.edu/~ckingsf/class/02713-s13/src/mst.py    #
##########################################################################

import math

class HeapItem(object):
    """Represents an item in the heap"""
    def __init__(self, key, item, arity=3):
        """key in Prim algorithm is the minimum weight of an edge to a given vertex item"""
        
        self.key = key
        self.item = item
        # the position in the heap as a list of pairs (key,item)
        
        self.pos = None
        

class DHeapHandler:
    """D-ary Min Heap"""
    def __init__(self, arity=3):
        """the branching factor of the d-Heaps"""
        self.arity = arity
    
    def parent(self, pos):
        """Return the position of the parent of HeapItem at position pos in heap"""
        if pos == 0:
            return None
        return int(math.ceil(pos / self.arity) - 1)

    def childrenPosRange(self, pos, heapLength):
        """Return a range object of children of HeapItem at position pos in heap"""
        return range(self.arity * pos + 1, min(self.arity * (pos + 1) + 1, heapLength))

    def minchild(self, pos, heap):
        """Return the child of HeapItem at position pos with the smallest key"""
        minpos = minkey = None
        for c in self.childrenPosRange(pos, len(heap)):
            if minkey == None or heap[c].key < minkey:
                minkey, minpos = heap[c].key, c
        return minpos

    def siftdown(self, hi, pos, heap):
        """Move HeapItem hi down from position pos in heap until its smallest child is bigger than hi's key"""
        c = self.minchild(pos, heap)
        while c != None and heap[c].key < hi.key:
            # min child c is moving up 
            heap[pos] = heap[c]
            heap[pos].pos = pos
            # continue with previous min child c position
            pos = c
            c = self.minchild(c, heap)
        # pos is the position of hi
        heap[pos] = hi
        hi.pos = pos

    def siftup(self, hi, pos, heap):
        """Move HeapItem hi up from position pos in heap until it's parent is smaller than hi.key"""
        p = self.parent(pos)
        while p is not None and heap[p].key > hi.key:
            # parent is moving down
            heap[pos] = heap[p]
            heap[pos].pos = pos
            # continue with previous parent p position
            pos = p
            p = self.parent(p)
        # pos is the position of hi
        heap[pos] = hi
        hi.pos = pos

    def makeheap(self, S):
        """Create a heap from set S, which should be a list of pairs (key, item)."""
        heap = list(HeapItem(k,i) for k,i in S)
        for pos in range(len(heap)-1, -1, -1):
            self.siftdown(heap[pos], pos, heap)
        return heap

    def findmin(self, heap):
        """Return HeapItem with smallest key, or None if heap is empty"""
        return heap[0] if len(heap) > 0 else None

    def deletemin(self, heap):
        """Delete the smallest item"""
        if len(heap) == 0: return None
        smallestHI = heap[0]
        lastHI = heap[-1]
        # delete the last item and insert it again in heap from position of smallest item which disappears
        del heap[-1]
        if len(heap) > 0:
            self.siftdown(lastHI, 0, heap)
        return smallestHI

    def heapinsert(self, key, item, heap):
        """Insert and return an HeapItem into the heap"""
        # start with adding a new position to list heap such that len(heap) is incremented to host an additional item 
        heap.append(None)
        hi = HeapItem(key,item)
        # moves up the additional item from end of heap
        self.siftup(hi, len(heap)-1, heap)
        return hi

    def heap_decreasekey(self, hi, newkey, heap):
        """Decrease the key of hi to newkey"""
        assert(newkey < hi.key)
        hi.key = newkey
        # moves up the item if parent items have greater keys
        self.siftup(hi, hi.pos, heap)
