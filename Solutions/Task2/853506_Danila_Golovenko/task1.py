import sys 
import tempfile
  
class MinHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1


    def insert(self, element): 
        if self.size >= self.maxsize : 
            return False
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
        return True

    def pop(self): 
        popped = self.Heap[self.FRONT] 
        if self.size != 1:
            self.Heap[self.FRONT] = self.Heap[self.size] 
            self.size-= 1
            self.minHeapify(self.FRONT) 
        else:
            self.size -= 1
        return popped 

    def isEmpty(self):
        return self.size == 0
    
    def parent(self, pos): 
        return pos//2

    def leftChild(self, pos): 
        return 2 * pos 
  
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    def isLeaf(self, pos): 
        if pos > (self.size//2) and pos <= self.size: 
            return True
        return False
  
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    def minHeapify(self, pos): 
  
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  

   
            
    
def sorting(path):
    full = tempfile.NamedTemporaryFile('w+')
    empty = tempfile.NamedTemporaryFile('w+')
    minHeap = MinHeap(1000) 

    def merge():
        nonlocal full, empty, minHeap 
        full.seek(0)
        fileNum = full.readline()
        heapNum = minHeap.pop()
        while len(fileNum) > 0:
            if not minHeap.isEmpty() or heapNum != None:
                if int(fileNum) < heapNum:
                    empty.write(fileNum)
                    fileNum = full.readline()
                else:
                    empty.write('{}\n'.format(str(heapNum)))
                    if not minHeap.isEmpty():
                        heapNum = minHeap.pop()
                    else:
                        heapNum = None
            else:
                empty.write(fileNum)
                fileNum = full.readline()
        if heapNum != None:
            empty.write('{}\n'.format(str(heapNum)))
        while not minHeap.isEmpty():
            heapNum = minHeap.pop()
            empty.write('{}\n'.format(str(heapNum)))
        full.close()
        full = tempfile.NamedTemporaryFile('w+')
        full, empty = empty, full 

    with open(path) as bigFile:
        for num in bigFile:
            if not minHeap.insert(int(num)): 
                merge()
                minHeap.insert(int(num)) 
        merge()

    with open("sorted.txt", 'w') as sortedBigFile:
        full.seek(0)
        sortedBigFile.writelines('{}'.format(i) for i in full)
    full.close()
    empty.close()

if __name__ == "__main__":
    sorting('numbers.txt')