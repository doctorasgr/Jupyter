a = []         
  
print("Values of a:", a)
print("Type of a:", type(a))
print("Size of a:", len(a)) 

b = ""         
  
print("Values of a:", b)
print("Type of a:", type(b))
print("Size of a:", len(b)) 

c = ''
print("Values of a:", c)
print("Type of a:", type(c))
print("Size of a:", len(c)) 


seq = ""
f = open("seq_file.txt","r")
for line in f:
    line = line.strip()
    if '>' not in line:
        seq += line
print(seq)

seq_head = ""
f = open("seq_file.txt", "r")
for line in f:
    line = line.strip()
    if '>' in line:
        seq_head += line
print(seq_head)
