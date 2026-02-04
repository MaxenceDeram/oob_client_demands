# Ensure project root is on sys.path so tests can import local modules
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
