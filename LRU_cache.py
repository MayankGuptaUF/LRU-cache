import time
import os

class Node:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value
class simple_cache:
	def __init__(self, size):			
		self.size = size
		self.dictionary = {}
		self.head = None                #the head and tail are now just pointers and not nodes
		self.tail = None    
	def _add(self, node):  # Now _add and _evict under normal circumstances cannot be accessed outside the simple_cache.
		if node ==None:
			return -1
		if self.head == None and self.tail == None:
			self.head = node
			self.tail = node
			node.prev = None
			node.next = None
		else:
			node.next = None
			node.prev = self.tail
			self.tail.next = node
			self.tail = node
			
	def _evict(self, node):    #add and evict both are checked for corner cases
		if node == None:
			return -1
		if node == self.head and node == self.tail:
		    self.head = None
		    self.tail = None					
		elif node == self.head:
		    self.head = node.next
		    node.next.prev = None
		elif node == self.tail:
		    self.tail = node.prev
		    node.prev.next = None
		else:  
		    node.prev.next = node.next
		    node.next.prev = node.prev
		node.next = None
		node.prev = None					# nodes not used are freed so that they dont point to invalid addresses
	def _check(self,key):
		if key in self.dictionary:
			node=self.dictionary[key]              # seperated dictionary out for modularity
			return node
		else:
			return -1
	def retrieve(self, key): 
		nnode=self._check(key) 
		if nnode!=-1:                            # retrieve and new_entry are the only ones main can access directly
			self._evict(nnode)
			self._add(nnode)
			return nnode.value
		else:
			value=self._lookup(key)
			self.new_entry(key,value)
			if value!=-1:
				return value
			return -1		
	def new_entry(self, key, value):
		if len(self.dictionary)>=self.size:	    # For practical application first we need to remove an element from a full cache before entering new data 
			nnode = self.head					# dictionary delete and add are singular operations they are performed after linked list is updated
			self._evict(nnode)
			del self.dictionary[nnode.key]
		nnode = Node(key, value)          
		self._add(nnode)
		self.dictionary[key] = nnode
	def _lookup(self,key):
		lookup = '	' + key	+'	'
		with open('Untitled Document') as myFile:
			for num, line in enumerate(myFile, 1):
				if lookup in line:
					k=line
					k=k.rstrip()
					m=k.split("	")
					return m[2]
				  
def main():
	cache = simple_cache(4)
	print(cache.retrieve('3')) 
	print(cache.retrieve('1'))
	print(cache.retrieve('5'))
	print(cache.retrieve('8'))
	print(cache.retrieve('15'))
	print(cache.dictionary)
if __name__ == "__main__":
	start = time.time()
	main()
	total_time=(time.time()-start)
	print("Execution Time",total_time)
	
