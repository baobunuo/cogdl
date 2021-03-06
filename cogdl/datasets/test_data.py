import torch

from cogdl.datasets import register_dataset
from cogdl.data import Dataset, Data

@register_dataset("test_small")
class TestSmallDataset(Dataset):
    r"""small dataset for debug"""
    def __init__(self, args=None):
        x = torch.FloatTensor([[-2, -1], [-2, 1], [-1, 0], [0, 0], [0, 1], [1, 0], [2, 1], [3, 0], [2, -1], [4, 0], [4, 1], [5, 0]])
        edge_index = torch.LongTensor([[0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 9, 9 , 9 , 10, 10, 11, 11],
                                       [1, 2, 0, 2, 0, 1, 3, 2, 4, 5, 3, 3, 6, 7, 8, 5, 7, 5, 6, 8, 9, 5, 7, 7, 10, 11, 9 , 11, 9 , 10]])
        y = torch.LongTensor([0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3])
        self.data = Data(x, edge_index, None, y, None)
        self.data.train_mask = torch.tensor([True, False, False, True, False, True, False, False, False, True, False, False])
        self.data.val_mask = torch.tensor([False, True, False, False, False, False, True, False, False, False, False, True])
        self.data.test_mask = torch.tensor([False, False, True, False, True, False, False, True, True, False, True, False])
        self.num_classes = 4
        self.transform = None

    def get(self, idx):
        assert idx == 0
        return self.data