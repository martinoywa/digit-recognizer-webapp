from .architecture import get_tensor, get_model
import torch

model = get_model()

def get_image_label(image_bytes):
    tensor = get_tensor(image_bytes)
    output = model.forward(tensor)
    _, pred = torch.max(output, 1)
    
    return pred.item()