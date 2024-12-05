'''
Multithreading
5.52

Thread = a flow of execution within a program, like a separated of program in python
        however in python there is only one thread
        GIL = Global Interpreter Lock
        Multithreading = running multiple threads at the same time

cpu bound = program/task where the task is limited by cpu use mutithreading

io bound = program/task where the task is limited by io (input/ output)

'''

import threading
import time 

print (threading,active_count())
print (threading,enumerate())