#!/usr/bin/python3
import sys
import os

# Add your project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from app import app as application

if __name__ == "__main__":
    application.run()