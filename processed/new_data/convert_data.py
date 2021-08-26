from Bio import SeqIO

my_file = open("/home/trunglx/Downloads/project_final_AI/processed/neg_training.txt")
i = 1
for i in range(2000):
    # read the contents

    my_file_content = my_file.read()
    my_dna = my_file_content.rstrip("\n")
    # calculate the length


    # print the output
    print(">neg_train[i]" "\n"+ my_dna)