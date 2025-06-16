heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1. Length of list
print(f"The lengeth of list is: {len(heroes)}")

# 2. Add 'black panther' at the end
heroes.append('black panther')
print(heroes)

# 3. Remove 'black panther' and insert it after 'hulk'
heroes.remove('black panther')
# heroes.insert(3, 'black panther') # Easy way
heroes.insert(heroes.index('hulk') + 1, 'black panther') # Accurate way when index is unknown
print(heroes)

# 4. Replace 'thor' and 'hulk' with 'doctor strange'
heroes[heroes.index('thor'):heroes.index('hulk') + 1] = ['doctor strange']
print(heroes)

# 5. Sort the list alphabetically
heroes.sort()
print(heroes)

print(dir(heroes)) # This shows all the usable functions for your heroes list