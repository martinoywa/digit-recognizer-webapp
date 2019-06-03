from .architecture import get_tensor, get_model

model = get_model()

def get_image_label(image_bytes):
    tensor = get_tensor(image_bytes)
    output = model.forward(tensor)
    print(output)