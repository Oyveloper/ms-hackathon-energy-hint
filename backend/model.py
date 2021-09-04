import torch.nn.functional as F
from torch import nn
from torch.utils import data

from hdf5_dataloader import HDF5Dataset


class Autoencoder(nn.Module):
    def __init__(self, input_size):
        super(Autoencoder, self).__init__()
        conv1 = nn.Conv1d(input_size, (input_size - 3) * 8, kernel_size=4, stride=1, padding='same')
        linear1 = nn.Linear((input_size - 3) * 8, 128)
        linear2 = nn.Linear(128, (input_size - 3) * 8)
        linear3 = nn.Linear((input_size - 3) * 8, input_size)
        conv2 = nn.Conv1d(input_size, input_size, kernel_size=1, stride=1, padding='same')

    def forward(self, x):
        x = self.conv1(x)
        x = self.linear1(x)
        x = F.reLU(x)
        x = self.linear2(x)
        x = F.reLU(x)
        x = self.linear3(x)
        x = F.reLU(x)
        x = self.conv2(x)
        return x


my_nn = Autoencoder(40)
print(my_nn)

num_epochs = 50
loader_params = {'batch_size': 100, 'shuffle': False, 'num_workers': 1}

dataset = HDF5Dataset('path', recursive=True, load_data=False,
                      data_cache_size=4, transform=None)

data_loader = data.DataLoader(dataset, **loader_params)

for i in range(num_epochs):
    for x, y in data_loader:
        # here comes your training loop
        pass
