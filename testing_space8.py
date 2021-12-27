f_in = open('Schistosoma_m.gb','r')
f_out = open('AF269252.fasta','w')

flag = 0

for line in f_in:
    if 'ACCESSION' in line:
        AC = line.split()[1].strip()
        f_out.write('>' + AC)
    elif line.startswith("ORIGIN"):
        flag = 1
    elif flag == 1:
        fields = line.split()
        if fields != []: 
            seq = ''.join(fields[1:])
            f_out.write('\n' + seq.upper())

f_in.close()
f_out.close()
print(f_out)