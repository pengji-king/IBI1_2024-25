import re

tata_genes = []
with open('/Users/wangermi/Desktop/note/IBI1 8011/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as file:
    gene_name = ""
    gene_seq = ""
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if gene_seq and re.search('TATA[AT]{2}', gene_seq):
                tata_genes.append((gene_name, gene_seq))
            gene_name = line[1:].split(' ')[0]
            gene_seq = ""
        else:
            gene_seq += line
    # 处理最后一个基因
    if gene_seq and re.search('TATA[AT]{2}', gene_seq):
        tata_genes.append((gene_name, gene_seq))

with open('/Users/wangermi/Desktop/note/IBI1 8011/IBI1_2024-25/Practical7/tata_genes.fa', 'w') as out_file:
    for name, seq in tata_genes:
        out_file.write(f'>{name}\n{seq}\n')