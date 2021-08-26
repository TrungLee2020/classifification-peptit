import numpy as np
from iFeature.codes.AAINDEX import *
from iFeature.codes.PSSM import *
from iFeature.codes.ASA import *
from iFeature.codes.AAC import *
from iFeature.codes.DPC import *
from iFeature.codes.TPC import *

def feature_generator(file_path, temp_file_path):
    f = open(file_path, 'r', encoding='utf8')
    fasta_list = np.array(f.readlines())
    aa_feature_list = []
    for flag in range(0, len(fasta_list), 2):
        fasta_str = [[fasta_list[flag].strip('\n').strip(), fasta_list[flag + 1].strip('\n').strip()]]
        aac_output = AAC(fasta_str)
        dpc_output = DPC(fasta_str)
        tpc_output = TPC(fasta_str)
        # zsl_output = ZSCALE(fasta_str)
        feature_id = aac_output[1][0].split('>')[1]
        aac_output[1].remove(aac_output[1][0])
        dpc_output[1].remove(dpc_output[1][0])
        tpc_output[1].remove(tpc_output[1][0])
        # zsl_output[1].remove(zsl_output[1][0])
        aac_feature = []
        dpc_feature = []
        tpc_feature = []
        # zsl_feature = []
        for i in range(0, len(aac_output[1]), 20):
            temp = aac_output[1][i:i + 20]
            aac_feature.append(temp)
        for i in range(0, len(dpc_output[1]), 531):
            temp = [float(i) for i in dpc_output[1][i:i + 531]]
            dpc_feature.append(temp)
        for i in range(0, len(tpc_output[1]), 20):
            temp = tpc_output[1][i:i + 20]
            tpc_feature.append(temp)
        # for i in range(0, len(zsl_output[1]), 5):
        #     temp = zsl_output[1][i:i + 5]
        #     zsl_feature.append(temp)
        aa_fea_matrx = np.hstack(
            [np.array(aac_feature), np.array(dpc_feature), np.array(tpc_feature)])
        aa_feature_list.append([feature_id, aa_fea_matrx])
    np.save(temp_file_path, aa_feature_list)
    return temp_file_path + '.npy'