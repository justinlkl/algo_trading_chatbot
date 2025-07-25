import logging
import sys
from langchain_chroma import Chroma
from langchain_community.embeddings import CohereEmbeddings
from modules.splitter import data_splitter
from IPython.display import Markdown, display

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Get embedding model
def get_embedding_model(cohere_api_key):
    embed_model = CohereEmbeddings(
        cohere_api_key=cohere_api_key, model="embed-v4.0"
    )
    return embed_model

# Embed split to vector
def embed_splits_to_vector(chunks: list):
    for chunk in chunks:
        page_content = chunk.page_content
        return page_content

# Create vector store
def create_vectorstore(chunks: list, embed_model):
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embed_model)
    return vectorstore

def get_retriever(docs, cohere_api_key):
    chunks = data_splitter(docs)
    embed_model = get_embedding_model(cohere_api_key)
    vectorstore = create_vectorstore(chunks, embed_model)
    retriever = vectorstore.as_retriever()
    return retriever
