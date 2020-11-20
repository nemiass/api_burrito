from app.config import app
from app.rutas import *

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    