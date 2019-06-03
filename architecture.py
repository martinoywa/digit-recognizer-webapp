"""Contains model architecture class and two helper functions.
    get_model(): Loads the trainded model
    get_tensor(): Persorms transforms on the input image
"""
import io
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

# architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # linear layer (784 -> 1 hidden node)
        self.fc1 = nn.Linear(28 * 28, 512)
        self.fc2 = nn.Linear(512, 512)
        self.fc3 = nn.Linear(512, 10)
        self.dropout = nn.Dropout(p=.5)

    def forward(self, x):
        # flatten image input
        x = x.view(-1, 28 * 28)
        # add hidden layer, with relu activation function
        x = self.dropout(F.relu(self.fc1(x)))
        x = self.dropout(F.relu(self.fc2(x)))
        x = F.log_softmax(self.fc3(x), dim=1)
        
        return x

def get_model():
    """Returns loaded model."""
    chechpoint = 'model.pt'
    model = Net()
    model.load_state_dict(torch.load(chechpoint, map_location='cpu'), strict=False)
    model.eval()
    
    return model

def get_tensor(image_bytes):
    """Returns transformed image."""
    return ''

