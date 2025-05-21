import re  
splice_comb = input("What is your splice_combination (GTAG, GCAG, ATAC):")  
file_path = "tata_genes.fa"  # Define the file path
donor = splice_comb[0:2]
acceptor = splice_comb[2:4]

def read_fasta(file_path):
    # Function to read a FASTA file and return a dictionary of gene sequences
    genes = {}  
    current_gene = None  
    
    with open(file_path, 'r') as file:  # Open
        for line in file:  # Iterate through each line in the file
            line = line.strip() 
            if line.startswith('>'):  
                if current_gene is not None:  
                    genes[current_gene] = ''.join(genes[current_gene]) 
                current_gene = line[1:] 
                genes[current_gene] = [] 
            else:  
                if current_gene is not None:  
                    genes[current_gene].append(line) 
    return genes  # Return the dictionary of gene sequences

def splice(seq):
    # Function to splice a sequence based on donor and acceptor sites
    global donor, acceptor 
    donor_matches = re.finditer(donor, seq) 
    acceptor_matches = re.finditer(acceptor, seq)  
    donor_positions = sorted([match.start() for match in donor_matches]) 
    acceptor_positions = sorted([match.start() for match in acceptor_matches]) 

    valid_donors = []  
    valid_acceptors = []  

    i, j = 0, 0  
    while i < len(donor_positions) and j < len(acceptor_positions):  
        if donor_positions[i] < acceptor_positions[j]: 
            if not valid_acceptors or donor_positions[i] > valid_acceptors[-1]: 
                valid_donors.append(donor_positions[i]) 
                valid_acceptors.append(acceptor_positions[j])  
            i += 1  
            j += 1  
        else:
            j += 1  

    if valid_acceptors and valid_donors:  # Check if valid donor and acceptor positions exist
        return True 
    else:
        return False  

def count_tata(seq):
    find_tata = re.findall(r"TATA[A,T]A[A,T]", seq)  #Find all TATA box
    count = len(find_tata) 
    return(count)  

genes = read_fasta(file_path)  
spliced_genes = {}  


with open(f"{splice_comb}_spliced_genes.fa", "w") as output:  
    for gene_name, sequence in genes.items():  
        sequence = ''.join(sequence)
        if splice(sequence):  
            spliced_genes[gene_name] = sequence  
            count = count_tata(sequence)  
            output.write(f">{gene_name}_TATAbox_number: {count}\n")  
            output.write(f"{sequence}\n")  