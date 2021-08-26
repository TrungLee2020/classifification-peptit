from Bio import SeqIO

my_file = open("/home/trunglx/Downloads/project_final_AI/processed/neg_training.txt")

# read the contents
my_dna = my_file.read()

# calculate the length
dna_length = len(my_dna)

# print the output
print("sequence is " + my_dna +  " and length is " + str(dna_length))