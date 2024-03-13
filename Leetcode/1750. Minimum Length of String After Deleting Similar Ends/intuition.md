Solution using two pointers: Iterate over a string 
while the left and right pointers point at the same 
characters, and break the loop when they no longer 
do or when the left pointer becomes equal to the right.
Then, if the right pointer equals the left and they 
both are more than 0 (the length of the string is more 
than 1), we return 0, as we can certainly remove all 
characters from the string. If not, we return the 
distance between the two pointers (the length of the 
r:esulting string).
