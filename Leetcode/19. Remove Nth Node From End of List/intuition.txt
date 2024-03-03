The optimal solution can be constructed using two pointers.
The naive solution would be to iterate through the linked list, 
store all the nodes in an array, and then find the Nth last 
indexed node in that array to modify the list. However, an 
observation can be made that we only need to know the node 
that is before the one we need to remove (so we can change 
its next node to the next next, skipping the one that we need 
to remove). This node is always n + 1 nodes from the end of 
the list, regardless of its length. Using two pointers, we 
can move the first one n nodes forward while keeping the 
second still. Then, we can iterate through the linked list 
with both nodes. At the end, the second pointer will point 
to the desired node.
