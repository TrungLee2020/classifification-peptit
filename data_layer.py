from torch.utils.data import Dataset
import numpy as np

class AIP_dataset(Dataset):
    def __init__(self, feature_list, target_list):
        self.feature = feature_list
        self.label = target_list
        self.set_length = len(self.label)
    def __getitem__(self, index):
        feat = self.feature[index]
        lab = self.label[index]
        return feat, lab
    def __len__(self):
        return len(self.feature)

def matrix_generator(data_file_path, pad_len=38):
    feat_data = np.load(data_file_path, allow_pickle=True)
    pad_feat_data = np.array([np.pad(data[1], ((0, pad_len - data[1].shape[0]), (0, 0)), mode='constant'), for data in feat_data])
    task_feat = pad_feat_data
    task_id = feat_data[:, 0]
    print('Output feature dimention: ', task_feat.shape)
    return task_feat, task_id
