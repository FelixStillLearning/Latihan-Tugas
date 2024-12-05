'''
zip(iretable) = mengembalikan sebuah objek zip, aggragate elements 
create a zip object from multiple iterables
 

'''

username = ['spongebob', 'patrick', 'sandy', 'squidward']
rank = ['admin', 'admin', 'moderator', 'user']
hujan = ('yes', 'no', 'yes', 'no')

user_rank = zip(username, rank,hujan)
for i in user_rank:
    print(i)