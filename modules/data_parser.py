import pandas as pd
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders.csv_loader import CSVLoader

def load_url(url_webpage):
    loader = WebBaseLoader(url_webpage)
    doc = loader.load_and_split()
    return doc

def load_csv(csv_path):
    loader = CSVLoader(csv_path)
    doc = loader.load()
    return doc
