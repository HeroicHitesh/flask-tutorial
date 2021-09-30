from flask import Flask

app = Flask(__name__)

# Workaround for circular imports
from app import routes