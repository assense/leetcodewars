The optimal (memory-wise) solution involves the rabbit/turtle 
pointers idea. We maintain two pointers moving at different 
speeds: one advances one node per iteration, while the other 
moves two nodes. Eventually, if there's a loop, these pointers 
will converge at the same node.

The naive approach involves storing all nodes in a list and 
checking if they were encountered before. While this approach 
is more time-effective, requiring only len(l) operations, 
the previous method relies on waiting until the pointers match. 
Thus, it's a trade-off between speed and memory usage.
