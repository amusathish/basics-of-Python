def codons_extract(dnasequence,frame):
    codons = []
    i = frame
    while i + 3 <= len(dnasequence):
        codons.append(dnasequence[i:i+3])
        i += 3
    '''for i in dnasequence:
        codons.append(dnasequence[i:i+3])
        i += 3
        if len(codons) == 3:
            codons.append(codons)'''
    return codons


def protein_extract(codons, startcodon, stopcodon):
    protein = []

    for i in range(len(codons)):
        if codons[i] in startcodon:
            for j in range(i, len(codons)):
                protein.append(codons[j])
                if codons[j] in stopcodon:
                    return protein
            return []
    return []


def aa_count(codons_list,genetic_code):
    aacountlist = {}
    for i in range(len(codons_list)):
        if codons_list[i] in genetic_code:
            getgeneticvalue = genetic_code[codons_list[i]]
            if getgeneticvalue in aacountlist:
                aacountlist[getgeneticvalue] += 1
            else:
                aacountlist[getgeneticvalue] = 1
    return aacountlist

ddef read_dna(seq,filepath):
    myfile = open(filepath,"r")
    #lines = myfile.readline()
    result = ""
    seqFound = False
    found = False
    
    for line in myfile:
        line = line.strip()
        
        if line.startswith('>'):
            if line[1:].strip() == seq:
                found = True 
                if (found == True and seqFound == True):
                    break
                else:
                    seqFound = True             
            else:
                found = False
                if (found == False and result != ""):
                    break
        elif found:
           result += line.strip().upper() 
        
    myfile.close()
    return result
        

genetic_code = {'GCT':'A','GCC':'A','GCA':'A','GCG':'A', 
               'CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R', 
               'AAT':'N','AAC':'N', 
               'GAT':'D','GAC':'D', 
               'TGT':'C','TGC':'C', 
               'CAA':'Q','CAG':'Q', 
               'GAA':'E','GAG':'E', 
               'GGT':'G','GGC':'G','GGA':'G','GGG':'G', 
               'CAT':'H','CAC':'H', 
               'ATT':'I','ATC':'I','ATA':'I', 
               'CTT':'L','CTC':'L','CTA':'L','CTG':'L','TTA':'L','TTG':'L', 
               'AAA':'K','AAG':'K', 
               'ATG':'M', 
               'TTT':'F','TTC':'F', 
               'CCT':'P','CCC':'P','CCA':'P','CCG':'P', 
               'TCT':'S','TCC':'S','TCA':'S','TCG':'S','AGT':'S','AGC':'S', 
               'ACT':'T','ACC':'T','ACA':'T','ACG':'T', 
               'TGG':'W', 
               'TAT':'Y','TAC':'Y', 
               'GTT':'V','GTC':'V','GTA':'V','GTG':'V'}



# composition('sequence1','examples/example1.fna',genetic_code,['ATG','GTG'],['TAG','TAA'])
def composition(seq,filepath,genetic_code,startcodon, stopcodon):
    frame = 0
    dna=read_dna(seq,filepath)
    if dna == "":
        print("Error: the sequence is not in the file")
        return
    for frame in range(3):
        
        protein = protein_extract(codons_extract(read_dna(seq,filepath),frame),startcodon,stopcodon)
        if protein == []:
             print(f"Frame {frame}: no valid protein")            
        else:
            aminoacidcount = str(aa_count(protein_extract(codons_extract(read_dna(seq,filepath),frame),startcodon,stopcodon),genetic_code))
            print(f"Frame {frame}:")
            print("protein:", protein)
            print("amino acid count:", aminoacidcount)


          

print(composition('sequence1','examples/example1.fna',genetic_code,['ATG','GTG'],['TAG','TAA']))

'''>>> composition('sequence1','examples/example1.fna',genetic_code,['ATG','GTG'],['TAG','TAA'])
Frame 0:
protein: ['ATG', 'ACA', 'TAG']
amino acid count: {'M': 1, 'T': 1}
Frame 1:
protein: ['GTG', 'AAT', 'GGG', 'ATT', 'GAA', 'TAA']
amino acid count: {'V': 1, 'N': 1, 'G': 1, 'I': 1, 'E': 1}
Frame 2: no valid protein
>>> composition('sequence3','examples/example1.fna',genetic_code,['ATG','GTG'],['TAG','TAA'])
Error: the sequence is not in the file
'''
