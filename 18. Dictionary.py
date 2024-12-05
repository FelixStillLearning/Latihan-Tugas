#Dictionary in python = A changeable, unordered of unique key:Value Pairs
#                       Fast because they use hashing, allow us to access a value quickly

negara = {'Indonesia':'Jakarta','USA':
          'Washington DC',
           'Malaysia': 'Kuala Lumpur',
           'russia':'moscow'}

negara.update({'jawa barat':'bandung'})
negara.update({'jawa tengah':'Semarang'})
negara.pop('Malaysia')
negara.clear()
#print(negara['Indonesia'])
#print(negara.get('jawa barat'))
#print(negara.keys())
#print(negara.values())
#print(negara.items())

for key,value in negara.items():
    print(key,value)
