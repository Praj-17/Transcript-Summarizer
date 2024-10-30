from .constants import SummaryModel
from .modules import PDFtoText, GeminiRunner
import yaml
import os

# Load the configuration from config.yml
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)