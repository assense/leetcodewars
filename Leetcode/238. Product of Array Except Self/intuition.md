The solution is a memory/speed tradeoff(O(n) memory 
as implied in the problem description). We iterate 
over the list once to determine the number of zeros
and the total product. Based on one of three cases 
(0, 1, or 2 zeros in the list), we return the 
resulting list: consisting only of zeros if there are 
2 or more in the original list, all zeros except at the 
position of a single zero in the original list, or the 
product of elements except the element at the position.
