# LRU-cache

Environment:	Ubuntu 16.04
Libraries:	No
Version:	Python 3.0+

The Program has 4 functions

1) update- This is used when we need to add a new entry to the cache. It can the functions add and evict.
2) retrieve- This is used when we need to look for an entry already in the cache or if we need to make a new entry.
3) add- Add is used to link the current node at the end by reaching the tail.
4) evict- Evict is used to delink a node. Unlike add, this doesnt always need to occur at one specific position but can occur even in a middle node.
For example,if that node becomes the most recently accessed node we need to put it in the front.
This is an LRU cache, so if the size of entries is greater than cache size the least recently used entry is evicted.

Structures Used-

1) Doublely Linked List- The reason for using doublely linked list is that when we need to add a node or evict a node. 
We don't need to traverse the entire linked list to get to the previous node.
Also, given that this is a cache we would be required to put a node at the end plenty of times and if we had used a singlely linked list,we would have to traverse the entire list.

2) Dictionary- Dictionary is an unordered data structure it is used to find if we have the particular entry in the DLL. Dictionary searches are O(1). 
We store the key and in the value pair we store the node.  

All functions take node as an arguement.
While creating a new cache the arguement given defines the size of the cache.

Complexity-
Since we eliminated the need to traverse a list, we make use of no loops and time complexity of the algorithm is O(1).

Disadvantages-

The primary disadvantage is that because it is a doublely linked list memory allocation needed is more.

Improvements-
By using the time function, we can maintain a timer of sort that will evict entries after a certain amount of time has passed.


