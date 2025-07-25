from constant import MODEL_ENDPOINTS, HUGGINGFACE_API_KEY, COHERE_API_KEY
from langchain_community.llms import HuggingFaceEndpoint
from langchain_cohere.llms import Cohere
from langchain.llms.base import LLM
import requests


def initialize_llm_model(model_name: str):
    model_endpoint = MODEL_ENDPOINTS[model_name]
    return HuggingFaceEndpoint(
        endpoint_url=model_endpoint,
        huggingfacehub_api_token=HUGGINGFACE_API_KEY,
        temperature=0.1,
    )


def initialize_cohere_llm_model():
    return Cohere(cohere_api_key=COHERE_API_KEY)