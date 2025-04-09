seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
max_intron_length = 0

# 从序列中查找所有的GT剪接供体的位置
for i in range(len(seq) - 1):
    if seq[i:i + 2] == 'GT':
        # 从GT之后开始查找AG剪接受体
        for j in range(i + 2, len(seq) - 1):
            if seq[j:j + 2] == 'AG':
                intron_length = j - i + 2
                if intron_length > max_intron_length:
                    max_intron_length = intron_length

print(max_intron_length)