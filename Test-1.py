for element in [1, 4, 9, 16]:
    print (element)

G_content = []

my_seq = ('GGTTAACTCGTAGCGATTGACATCAGTAGTACGATGACAGTACGTACATATAGCTAGATCGATTCGACTTCGATCGATCACTTACGACAGTCACGTACGTATCAGATCTAGATCGATCTCGATCGACTAG')

for base in ('G','C'):
    number=my_seq.count(base)
    G_content.append(number)

print(G_content)

Perc_G = sum(G_content)*100/len(my_seq)
print("The precentage of G is :{}".format(Perc_G))

seq = [0, 1, 2, 3, 4, 5]
window_size = 2

for i in range(len(seq) - window_size + 1):
    print(seq[i: i + window_size])
    print(sum(seq[i: i +window_size]))

my_list = ('1,2,3,4,5,6,7,8,9')

def sliding_window(elements, window_size):
    if len(elements) &my_list;= window_size:
        return elements

    for i in range (len(elements) - window_size + 1):
        yield elements[i:i+window_size]
    
sw_gen = sliding_window(my_list,3)
print(next(sw_gen))
print(next(sw_gen))

[max(my_seq[i:i+3]) for i in range(len(my_seq) - (3-1))]

import rolling              # import library
roll = rolling.Max(my_seq, 3)  # iterator returning maximum of each window of size 5
list(roll)

b = [my_seq[i:i+3] for i in xrange(len(my_seq)-1)]
print(b)

import pandas
import rolling
seq = [3, 1, 4, 1, 5, 9, 2]
roll_list = rolling.Apply(seq, 3, operation=tuple, window_type='variable')
list(roll_list)

l = [1,2,3,4,4,7]
def f(l: list) -> int:
    


import sys
print(sys.path)