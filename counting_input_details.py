from typing import no_type_check


data = []

input_file = open("my_file.txt")
for line in input_file:
    count = int(line.strip())
    data.append(count)
data.sort()

n_items = len(data)
total = sum(data)
highest = max(data)
minimum = min(data)

input_file.close()

out_file = open("stats.txt", "w")

out_file.write ("Number of SNP IDs: {}\n".format(n_items))
out_file.write ("Total SNPs: {}\n".format(total))
out_file.write ("Highest frequency: {}\n".format(highest))
out_file.write ("Lowest frequency: {}\n".format(minimum))
out_file.close()