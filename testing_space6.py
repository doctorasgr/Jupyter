acc_list = ''

f = open('multi_fasta.txt','r')

for line in f:
    line = line.strip()
    if '>' in line:
        acc_list += line + '\n'
print(acc_list)

start = 'sp|'
end = '|PROT'
tmp = acc_list.split(start)

substring = []
for substr in tmp:
    if end in substr:
        substring.append(substr.split(end)[0])
print(substring)

animal_q = 'PROT_CAT'
result = None
while result == None:
    for animal in f:
        if animal.startswith('>'):
            animal_name = animal.strip('|PROT_')[1]
            if animal_name == animal_q:
                result = line.strip()
                print(result) 