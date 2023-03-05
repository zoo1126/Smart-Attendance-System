import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms, datasets

class facenet(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size = 7, stride = 2)
        self.pool1 = nn.MaxPool2d(3, 2, padding = (1,1))
        self.bn1 = nn.BatchNorm2d(64)

        self.conv2a = nn.Conv2d(64, 64, kernel_size=1, stride= 1)
        self.conv2 = nn.Conv2d(64, 192, kernel_size=3, stride=1, padding = 1)
        self.bn2 = nn.BatchNorm2d(192)
        self.pool2 = nn.MaxPool2d(3, 2, padding=(1, 1))

        self.conv3a = nn.Conv2d(192, 192, kernel_size=1, stride=1)
        self.conv3 = nn.Conv2d(192, 384, kernel_size=3, stride=1, padding = 1)
        self.pool3 = nn.MaxPool2d(3, 2, padding=(1, 1))

        self.conv4a = nn.Conv2d(384, 384, kernel_size=1, stride=1)
        self.conv4 = nn.Conv2d(384, 256, kernel_size=3, stride=1, padding = 1)

        self.conv5a = nn.Conv2d(256, 256, kernel_size=1, stride=1)
        self.conv5 = nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1)

        self.conv6a = nn.Conv2d(256, 256, kernel_size=1, stride=1)
        self.conv6 = nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1)

        self.pool4 = nn.MaxPool2d(3, 2, padding=(1, 1))

        self.fc1 = nn.Linear(7 * 7 * 256, 1 * 32 * 128)
        self.fc2 = nn.Linear(1 * 32 * 128, 1 * 32 * 128)
        self.fc3 = nn.Linear(1 * 32 * 128, 1 * 1 * 128)

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool1(x)
        x = self.bn1(x)

        x = self.conv2a(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.pool2(x)

        x = self.conv3a(x)
        x = self.conv3(x)
        x = self.pool3(x)

        x = self.conv4a(x)
        x = self.conv4(x)

        x = self.conv5a(x)
        x = self.conv5(x)

        x = self.conv6a(x)
        x = self.conv6(x)
        x = self.pool4(x)
        x = x.view(-1)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        x = x.view(1,-1)
        normx = torch.norm(x, 2, dim=1)
        output = torch.div(x, normx)
        return output

cerition = torch.nn.MSELoss()
# loss = cerition(y1,y2) * 128 + torch.tensor([0.2])
