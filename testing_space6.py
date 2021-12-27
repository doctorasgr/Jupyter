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