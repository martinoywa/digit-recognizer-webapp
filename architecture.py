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
        #convolutional layer
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.conv3 = nn.Conv2d(32, 64, 3, padding=1)
        # max pooling layer
        self.pool = nn.MaxPool2d(2, 2)
        # fully connected layers
        self.fc1 = nn.Linear(64 * 4 * 4, 512)
        self.fc2 = nn.Linear(512, 64)
        self.fc3 = nn.Linear(64, 10)
        # dropout
        self.dropout = nn.Dropout(p=.5)

    def forward(self, x):
        # add sequence of convolutional and max pooling layers
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        # flatten image input
        x = x.view(-1, 64 * 4 * 4)
        # add hidden layer, with relu activation function
        x = self.dropout(F.relu(self.fc1(x)))
        x = self.dropout(F.relu(self.fc2(x)))
        x = F.log_softmax(self.fc3(x), dim=1)
        
        return x


def get_model():
    """Returns loaded model."""
    chechpoint = '/home/martineliteai/flask/digit_recognizer_deployed/model.pt'
    model = Net()
    model.load_state_dict(torch.load(chechpoint, map_location='cpu'), strict=False)
    model.eval()

    return model

def get_tensor(image_bytes):
    """Returns transformed image."""
    transform = transforms.Compose([transforms.Resize((28,28)),
                                    transforms.ToTensor()])
    image = Image.open(io.BytesIO(image_bytes)) # image_bytes are what we get from web request
    
    return transform(image).unsqueeze(0) # sends a single image

