from flask import Flask

app = Flask(__name__)

from .views import main
app.register_blueprint(main)