from flask import Blueprint, request, render_template, redirect, url_for
from .model_files.inference import get_image_label

# initialize the main blueprint
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        print(request.files)
        if 'image_file' not in request.files:
            print('no file uploaded')

        file = request.files['image_file']
        image = file.read()
        label = get_image_label(image_bytes=image)
        
        return render_template('results.html', label=label)