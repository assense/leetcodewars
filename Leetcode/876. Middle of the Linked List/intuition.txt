Problem could be solved using rabbit/turtle pointers 
method. Initiate 2 pointers, one mmoving one node at
a time and other 2 nodes. When the second(rabbit) pointer
will point at the last node - it will indicate that 
the list has odd number of nodes (2 * n nodes where n
is the amount of moves + 1 head node) and turtle pointer
is exactly at middle position. If it will point at second
to last node (fast.next.next = None) it will indicate 
that list has even amount of nodes and turtle pointer 
points at left middle node.

