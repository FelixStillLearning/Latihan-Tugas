#how to import module random
#psudeo random

import random

x = (random.randint(1,10))

print(x)

#create a random float number between 0 - 1
y = (random.random())

print(y)

#create a random choice from a list
i = ['gunting','batu','kertas']
print(random.choice(i))

#create a shuffle random from a list
cards = ['ace',2,3,4,5,6,7,8,9,10,'jack','queen','king','joker']
random.shuffle(cards)
print(cards)