# Exercise #1

# Filter out all of the empty strings from the list below

# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

from re import A


places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

filtered = list(filter(lambda name: name >= "A", places))
print(filtered)


# Exercise #2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
author = list(map(lambda x:x.title(), author))
author.sort(key=lambda x: x.split()[-1][0])
print(author)



# #Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

def custom_map(places, map_f):
    result_list = []
    
    for (a,b) in places:
        new_num = (a,map_f(b))
        result_list.append(new_num)
        
    return result_list

print(custom_map(places, lambda b: (9/5)*b + 32))




def fib_seq(n):
    if n <= 1:
        return n
    else:

        return(fib_seq(n-1) + fib_seq(n-2))

fib = 5

for i in range(fib + 1):
       print(f"Iteration {i}: {fib_seq(i)}")