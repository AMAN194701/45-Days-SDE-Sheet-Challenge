# Implement Max Heap
# You need to implement the Max Heap with the following given methods.
# insert (x) -> insert value x to the max heap
# getMax -> Output the maximum value from the max heap
# exctractMax -> Remove the maximum element from the heap
# heapSize -> return the current size of the heap
# isEmpty -> returns if heap is empty or not
# changeKey (ind, val) -> update the value at given index to val (index will be given 0-based indexing)
# initializeHeap -> Initialize the heap

# Note: When extracting max, if both left and right children are equal, you must swap with the LEFT child.

class Solution:
    # initialize the heap
    def initialize_heap(self):
        self.heap=[]
     
    def insert(self,key):
        # insert the new key at the end of the heap
        self.heap.append(key)

        # index of newly inserted element
        i=len(self.heap)-1

        # check the max heap property and swap with parent if violated
        while i > 0 :
            parent = (i-1)//2
            
            # check if the curr element is larger than its parent, if so then swap them and chek again for new parent 
            if self.heap[parent] < self.heap[i]:          
                self.heap[parent],self.heap[i]= self.heap[i], self.heap[parent]
                i=parent
            else :
                break 

    def extract_amx(self):
        # check if heap is empty 
        if self.heap==0:
            return -1
        
        # save the max element 
        max_ele= self.heap[0]

        # replace the root with last elemnt and then remove the last element 
        self.heap[0]= self.heap[-1]
        self.heap.pop()

        # heapify Down 
        i =0 
        while True:
            left = 2*i +1
            right =2*i +2 

            largest = i 

            if left < len(self.heap) and self.heap[left]> self.heap[largest]:
                largest = left 
            
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest= right 

            # heap property already satisfied 
            if largest ==i :
                break 

            self.heap[i], self.heap[largest]= self.heap[largest], self.heap[i]

            i = largest 

        return max_ele
    
    
    def change_key(self, index, new_val):
        old_value= self.heap[index]
        self.heap[index] =new_val

        # if value is greater then perform heapify up
        if new_val > old_value:
            while index >0:
                parent= self.heap[index-1]//2
                if self.head[parent]<self.heap[index]:
                    self.heap[parent], self.heap[index]= self.heap[index], self.heap[parent]
                    index = parent 
                else :
                    break 

        
        else :
            i = index 
            while True :
                largest= i 
                left = 2*i+1
                right = 2*i +1
                # check with left node 
                if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                    largest = self.heap[left]
                
                if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                    largest = self.heap[right]

                if largest==i :
                    break 
                
                self.heap[i], self.heap[largest]= self.heap[largest], self.heap[i]

                i = largest 


    def get_max(self):
        if (self.heap)==0:
            return -1
        return self.heap[0]
    
    def heap_size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap)==0