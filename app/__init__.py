from flask import Flask

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configura
app.config.from_pyfile("config.py")

from app import views