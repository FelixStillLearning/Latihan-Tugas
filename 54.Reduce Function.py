'''
Reduce = apply function to an iretable and reduce it to a single cumulative value.
        Perform function on first two elements and repeats process unitl 1 value remains

Reduce(function,iretable)


'''

import functools 
huruf = ["F","u","N","N","Y"]
Kata = functools.reduce(lambda x,y,:x+y,huruf)

print(Kata)

factorial = [5,4,3,2,1]
hasil = functools.reduce(lambda x,y:x+y,factorial)

print(hasil)