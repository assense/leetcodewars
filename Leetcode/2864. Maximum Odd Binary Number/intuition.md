In binary representation, an odd number always has a 1 as its
least significant bit (the last bit). Therefore, constructing 
the maximum number from a given binary string involves shifting 
all bits (except one) to the beginning. This ensures that all 
possible most significant bits are utilized, followed by appending 
zeros and finishing with the last bit, which is always 1 for odd numbers.
