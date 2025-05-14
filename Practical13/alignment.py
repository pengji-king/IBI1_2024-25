#def read_fasta(file_path):
#   with open(file_path, 'r') as file:
#        lines = file.readlines()
#       name = lines[0].strip()[1:]
#        sequence = ''.join(line.strip() for line in lines[1:])
#   return sequence

#here is the sequence we will use
human_sod2_seq = "MLSRAVCGTSRQLAPVLGYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"#read_fasta("P04179.fasta")
mouse_sod2_seq = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"#read_fasta("P04179.fasta")
random_seq = "EKVYNSIFSGVINTWPIHGMYEYMEKAYEYEVIKHTSNGTDAMQFYRMVQGGYPPQSQIFVDQEIIEWAHLKNGFDDACAIMMCGIVQSKKLVHEILRGTTDGNPGLEVKRHSDPLWTCNVQWVMTNFESFNSEPDTRGDLGMMCCVFVIYPQEKNPLGAMEAEFQTQYVTHSRPHSEYKQYAPACWCTKWVHIMGKGFNPKPTSSSENCVSDEYASGTDQL"


def calculate_similarity_score(seq1, seq2):
    score = 0
    edit_distance = 0
    for i in range(len(seq1)): #compare each amino acid
        if seq1[i]!=seq2[i]:
            edit_distance += 1 #add a score 1 if amino acids are different
    print (edit_distance)
    score = 1 - edit_distance/len(seq1)
    return score

# calculate the similarity of human and mouse
human_mouse_score = calculate_similarity_score(human_sod2_seq, mouse_sod2_seq)
print("human_mouse_score is "+ str(human_mouse_score))

# calculate the similarity of human and random
human_random_score = calculate_similarity_score(human_sod2_seq, random_seq)
print("human_random_score is " + str(human_random_score))

# calculate the similarity of random and mouse
mouse_random_score = calculate_similarity_score(mouse_sod2_seq, random_seq)
print("mouse_random_score is " + str(mouse_random_score))