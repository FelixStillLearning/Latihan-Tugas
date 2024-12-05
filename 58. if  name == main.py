#if __name__ == '__main__':


'''
kenapa bisa muncul kode seperti diatas ketika sedang code menggunakan python ?
1. module ini bisa stand alone 
2. module ini juga bisa digunakan sebagai library dalam module lain 

pyhon akan menginterpretasi kode ini sebagai variabel spesial yang bernama __name__
pyhon will assign the value __main__ to the variable __name__
the initial model being run will be __main__
'''

import module_two 
print(__name__)
print(module_two,__name__)