from flask import Blueprint

# initialize the main blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Hello Digit Recognizer'