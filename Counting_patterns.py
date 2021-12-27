pattern="TT"
count=0
my_seq = 'GGTTAACTCGTAGCGATTGACATCAGTAGTACGATGACAGTACGTACATATAGCTAGATCGATTCGACTTCGATCGATCACTTACGACAGTCACGTACGTATCAGATCTAGATCGATCTCGATCGACTAG'
for i in range(len(my_seq)-len(pattern)+1):
    if my_seq[i:i+len(pattern)] == pattern:
        count=count + 1
print(count)