seq = 'ACGTTTCACGTTTTACGG'
k = 3

def FrequencyTable(seq, k):
    freqMap = {}
    n = |seq|
    for i = 0 to n - k:
        Pattern = Text(i, k)
        if freqMap[Pattern] doesn't exist
            freqMap[Pattern]← 1
        else
           freqMap[pattern] ←freqMap[pattern]+1 
    return freqMap