seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
max_intron_length = 0

# find all GTs in sequence
for i in range(len(seq) - 1):
    if seq[i:i + 2] == 'GT':
        # find all AGs after GT
        for j in range(i + 2, len(seq) - 1):
            if seq[j:j + 2] == 'AG':
                intron_length = j - i + 2
                #compare this length with the longest
                if intron_length > max_intron_length:
                    max_intron_length = intron_length

print(max_intron_length)#21